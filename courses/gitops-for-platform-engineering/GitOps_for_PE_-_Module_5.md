# GitOps for PE Module 5

## Página 1

GitOps in Enterprise - Scaling and 
Security
 
GITOPS FOR PLATFORM ENGINEERING
MODULE 05

## Página 2

Gitops at Scale - Reference 
Architecture(s)
2

## Página 3

3
One central instance manages deployments for many 
remote clusters via their Kubernetes API.
Pros:
● Centralized Visibility: A single "Single Pane of Glass" 
for all clusters and applications.
● Ease of Management: SSO, RBAC, and repository 
credentials are conﬁgured only once.
● Efﬁciency: Perfect for using ApplicationSets with the 
cluster generator  or ClusterProﬁles to push 
add-ons across the ﬂeet.
Cons:
● Blast Radius: A failure in the hub affects all connected 
clusters.
● High Security Risk: Central cluster stores admin 
credentials (kubeconﬁgs) for all target clusters.
● Networking: Requires the Hub to have direct network 
access to the target clusters' APIs.
Hub & Spoke

## Página 4

4
Instance is co-located with the workloads it manages.
Pros:
● High Reliability: Clusters are fully autonomous. An 
outage in Cluster A has no impact on Cluster B.
● Strict Isolation: No cluster-wide admin credentials 
stored centrally; security boundaries match cluster 
boundaries.
● Edge/Air-Gapped Ready: Best for Edge deployments 
or clusters behind strict ﬁrewalls.
Cons:
● Management Overhead: Every instance must be 
individually patched, updated, and conﬁgured.
● Fragmented Visibility: Developers must switch 
between multiple URLs/clusters to check application 
health.
● Consistency Risk: Harder to ensure all Argo/ 
instances stay synchronized in their conﬁguration.
Instance per Cluster

## Página 5

5
Hub & Spoke x 
Instance per Cluster
A central Hub orchestrates the ﬂeet, while each target cluster runs 
its own Dedicated Instance of to execute reconciliations locally.
Pros
● Decentralized Reliability: If the central Hub goes down, local 
instances continue to sync and maintain the desired state 
independently.
● Scalability: Heavy lifting (manifest rendering and API 
watching) is distributed across clusters, preventing the 
central Hub from becoming a performance bottleneck.
Cons
● Resource Overhead: Running a full set of controllers in every 
single cluster signiﬁcantly increases total CPU/RAM 
consumption.
● Management Burden: Operators must maintain, patch, and 
update two layers (the central Hub and all dedicated local 
instances) simultaneously.

## Página 6

6
The Management Cluster acts as the active driver, directly 
"pushing" conﬁgurations to the target API servers.
Registration: A SveltosCluster resource is created and 
labeled in the management cluster.
Security: The managed cluster’s Kubeconﬁg is stored as a 
Secret within the management cluster.
Deployment Flow:
● Sveltos fetches the Kubeconﬁg Secret.
● It creates a Kubernetes client to access the managed 
cluster's API server.
● Resources are deployed directly from the hub to the 
spoke.
Requirement: The management cluster must have direct, 
immediate access to every managed cluster's API endpoint 
(Inbound connectivity).
Hub & Spoke Agent 
based - Push

## Página 7

7
The Managed Cluster "pulls" its own desired state from the 
management hub, allowing for operation behind ﬁrewalls.
Registration: A SveltosCluster resource is created in the 
hub and explicitly marked for Pull Mode.
Security: A highly-permissioned ServiceAccount is created 
within the managed cluster for a local agent.
Deployment Flow:
● Sveltos prepares and stores resources in the 
management cluster.
● The Agent (running on the spoke) fetches the 
resources from the hub.
● The Agent applies the resources locally.
Advantage: Ideal for clusters in private networks; as long as 
the agent can reach the management hub (Outbound).
Hub & Spoke Agent 
based - Pull

## Página 8

8

## Página 9

9
Logical Grouping 
Separate instances for "Production" vs. "Non-Prod," or by 
geolocation units (e.g., "EU" vs. "US").
Pros:
● Controlled Blast Radius: Production issues are isolated 
from Dev/Staging.
● Better Scaling: Distributes the load (Repo 
Server/Controller) across multiple instances.
● Reduced Friction: Provides a single view for speciﬁc 
teams while maintaining critical boundaries.
Cons:
● Middle Security Risk: Central cluster(s) stores admin 
credentials (kubeconﬁgs) for all target clusters.
● Fragmented Visibility: No "Global Single Pane of 
Glass"; users must switch between different 
URLs/contexts depending on the group.
● Resource Inefﬁciency: Higher total CPU/RAM 
consumption as core controllers (API, Repo-server) 
are duplicated for every logical group.

## Página 10

10
Sharding
Sharding is a horizontal scaling strategy used to manage tens of 
thousands of applications by distributing the controller 
workload.
Pros:
● Massive Scalability: Distributes CPU/RAM load across 
multiple controller pods to handle huge ﬂeets.
● Fault Isolation: Performance issues in one shard (e.g., a 
massive Git repo) do not affect other shards.
● Tenant Dedication: Allows assigning speciﬁc shards to 
high-trafﬁc tenants or critical environments.
● s high activity doesn't interfere with others.
Cons:
● Management Complexity: Requires manual setup of 
directories and Kustomize patches for every shard.
● Resource Overhead: Higher total footprint as core 
controllers are duplicated for each shard.
● Labeling Discipline: All linked resources (Repo, 
Kustomization, Chart) must have consistent shard labels 
or they will be ignored.

## Página 11

11
Sharding
Sharding is a horizontal scaling strategy used to manage tens of 
thousands of applications by distributing the controller 
workload.
Pros:
● Massive Scalability: Distributes CPU/RAM load across 
multiple controller pods to handle huge ﬂeets.
● Fault Isolation: Performance issues in one shard (e.g., a 
massive Git repo) do not affect other shards.
● Tenant Dedication: Allows assigning speciﬁc shards to 
high-trafﬁc tenants or critical environments.
● s high activity doesn't interfere with others.
Cons:
● Management Complexity: Requires manual setup of 
directories and Kustomize patches for every shard.
● Resource Overhead: Higher total footprint as core 
controllers are duplicated for each shard.
● Labeling Discipline: All linked resources (Repo, 
Kustomization, Chart) must have consistent shard labels 
or they will be ignored.

## Página 12

GitOps and Security - Secrets 
Management and Compliance
12

## Página 13

Compliance - Kyverno
13
Key Capabilities
◆ Validation: Enforces best practices (e.g., "Disallow 
Root User," "Require Resource Limits") by blocking 
non-compliant deployments.
◆ Mutation: Automatically patches incoming 
resources to meet organizational standards (e.g., 
adding mandatory labels).
◆ Generation: Creates new resources based on 
triggers (e.g., when a Namespace is created, 
generate a default Deny-All NetworkPolicy).
◆ Reporting: Provides cluster-wide compliance 
reports to identify existing resources that violate 
new security policies.
Kyverno is a Kubernetes-native policy engine that manages 
Compliance and Best Practices using declarative resources 
(CRDs). It eliminates the need for complex programming 
languages (like Rego) by using familiar YAML-based policies.
◆ Declarative Compliance: Policies are stored in Git, versioned, 
and synced to the cluster just like any other application or 
infrastructure component.
◆ Shift-Left Security: Validates manifests during the CI/CD 
pipeline or at the Pull Request stage before they ever reach 
the cluster.
◆ Automated Remediation: Beyond just "blocking" bad conﬁgs, 
it can mutate (ﬁx) or generate (create) missing resources 
(e.g., auto-injecting NetworkPolicies or Sidecars).
 
Kyverno is the 'GitOps-native Guardrail': If Git deﬁnes what should run, Kyverno ensures 
only what is allowed can run

## Página 14

Guardrails that's Scales!
14

## Página 15

Guardrails that's Scales! (II)
15

## Página 16

16
Sealed Secrets Operator 
Uses asymmetric encryption. You encrypt a secret locally 
using a public key; only the controller in the cluster holds the 
private key to decrypt it
Pros:
● Git-Centric: The encrypted "SealedSecret" is safe to 
store in Git.
● Simple Setup: No external infrastructure (like a Vault) 
required.
Cons:
● Key Management: If you lose the cluster's private key, 
you cannot decrypt your Git-stored secrets anymore.
● Rotation: Manual re-encryption is usually required 
when secrets change.
Secrets Management with GitOps
External Secrets Operator (ESO)
Acts as an API bridge. It fetches the actual secret values from 
an external provider (AWS Secret Manager, HashiCorp Vault, 
Azure Key Vault) at runtime.
Pros:
● Security Best Practices: Sensitive data never even enters 
your GitOps repository—only a reference 
(ExternalSecret) is stored.
● Auto-Sync: Changes in the external provider are 
automatically synced to the cluster.
Cons:
● Dependency: Requires an external Secret Store 
(Vault/Cloud Provider) to be available and managed.
● Complexity: More conﬁguration needed (SecretStores, 
authentication, IAM roles).

## Página 17

External Secrets Operator (ESO) - Kubara
17

## Página 18

External Secrets Operator (ESO) - Kubara
18

## Página 19

External Secrets Operator (ESO) - Kubara
19

## Página 20

External Secrets Operator (ESO) - Kubara
20

## Página 21

Culture Shift
21

## Página 22

GitOps in - GitOps out
22
Why is it hard to internalize at ﬁrst?
◆ Relinquishing Control: The hardest part is 
"letting go" of direct cluster access; developers 
and admins often feel restricted.
◆ Steep Learning Curve: Teams must master trunk 
based workﬂows for progressive delivery.
◆ The "Lag" Factor: Changes are no longer instant 
(seconds via CLI) but take time to ﬂow through 
Git and the reconciler, which requires a shift in 
mindset regarding feedback loops.
◆ Strict Discipline: GitOps punishes "quick and 
dirty" ﬁxes
Why GitOps Requires a Cultural Shift
◆ From Manual to Declarative: Teams must stop "ﬁxing" things 
directly in the cluster (kubectl edit ) and trust the 
automated process via Git.
◆ Shared Responsibility: Operations and Development merge 
closer; the Git repository becomes the "Single Source of 
Truth" for everyone, requiring high levels of collaboration.
◆ Transparency & Accountability: Every change is visible 
through Pull Requests, which requires a culture that 
embraces open peer reviews and auditability.
GitOps is 20% Tooling and 80% Discipline. The challenge isn't the technology, but the habit of 
never touching the cluster manually again

## Página 23

Everything as Code
Our vision: A uniﬁed environment where 
Security and FinOps deﬁne policies or 
budgets as code. Whether via Git or an 
interface, every rule is declarative, 
versioned, and automatically enforced 
across clusters.
23

## Página 24

Everything as Code (II)
24

## Página 25

Everything as Code (III)
25

## Página 26

Everything as Code (IV)
26
Moving beyond 'ClickOps' forced a mindset shift: Service 
Owners embraced Dashboards-as-Code. By taking 
ownership through YAML and Helm, they stopped being 
passive users and became active creators. While the start 
was difﬁcult, it ultimately transformed infrastructure into a 
shared, engaging responsibility.

## Página 27

27
Recap: GitOps Architecture, Patterns…
❏ You can choose between Hub & Spoke, Standalone or … topologies. Every 
environment is different, so feel free to combine these patterns to get the best 
of both worlds. The most popular are Hub & Spoke and Standalone.
❏ Kubernetes is not secure by default. As a platform provider, you must enforce 
critical policies like "RunAsNonRoot" through guardrails to keep the cluster safe.
❏ Secrets management should be as easy as the rest of your code. Use Sealed 
Secrets for a simple Git-native setup, or switch to External Secrets Operator 
(ESO) if you already have a Vault. 
❏ The tools are nice, but never forget that developers are the end-users. No 
matter how you build it, the focus must stay on providing a great self-service 
experience. Culture matter.

## Página 28

Demo
28
