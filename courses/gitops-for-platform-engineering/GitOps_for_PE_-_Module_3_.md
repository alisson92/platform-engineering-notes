# GitOps for PE Module 3

## Página 1

GitOps Architecture, Patterns 
and Anti-Patterns
 
GITOPS FOR PLATFORM ENGINEERING
MODULE 03

## Página 2

GitOps Architecture
2

## Página 3

Remember this.
Declarative Versioned and 
Immutable
Pull-Based
Just four simple principles—no more, no less. 
3
Continuously 
Reconciled
GitOps Architecture
Feedback Loop

## Página 4

Internal vs External Reconciler
4
Workload Clusters

## Página 5

Internal vs External Reconciler
5

## Página 6

Declarative
6
Declarative means deﬁning the desired "what" (the 
end state) and letting the system handle the "how" 
(the steps to get there).
Imperative is a list of commands; Declarative is a 
description of the destination
 kubectl scale deployment my-app --replicas=3 
Definition (YAML): replicas: 3 
Imperative is like giving a driver turn-by-turn directions; 
Declarative is giving the driver an address and letting 
them ﬁnd the best route

## Página 7

7
Versioned and Immutable
Versioned and immutable means every change is 
identiﬁed by a unique, permanent tag (like a Git 
hash or Docker digest) so that once a version is 
deployed, it can never be altered—only replaced by 
a newer version.
❌
 The Bad Way (Mutable)
✅
 The Good Way (Versioned & 
Immutable)
Tags are for humans (versioned); Hashes are for machines (immutable); Never use 
'latest' in production.

## Página 8

8
In a Pull-based system, an agent inside the cluster 
continuously monitors Git and 'pulls' changes to 
synchronize the state, ensuring the cluster always 
matches the source of truth.
❌
 The Push Model (Traditional CI/CD)
- Code: git push  -> CI/CD Server runs 
kubectl apply -f deployment.yaml 
- Risk: You have to store sensitive Kuberentes 
credentials (Kubeconfig) inside your CI tool.
✅
 The Pull Model (GitOps)
- Code: git push  -> Argo CD (inside the 
cluster) detects the change and pulls it.
- Benefit: No cluster credentials leave the 
cluster. Even if someone manually deletes a 
pod, the Pull-based agent will "pull" the correct 
state back.
Push-based is 'Fire and Forget' from the outside; Pull-based is 'Watch and Sync' 
from the inside.
Pull-Based

## Página 9

9
Continuously Reconciled means the system 
constantly compares the observed state of the 
cluster with the desired state in Git and 
automatically ﬁxes any discrepancies (drift) 
without human intervention.
Continuous Reconciliation turns 'I hope it's running' into 'I know it's running' by 
constantly killing the drift.
Continuous Reconciled
The "Loop" Logic
◆ Observe: Argo CD looks at the running Pods in your 
webapp namespace.
◆ Diff: Argo CD looks at the YAML in your Git repo.
◆ Act: If a Pod was manually deleted or a replica count 
was changed via kubectl, Argo CD "reconciles" it by 
re-applying the Git state.

## Página 10

*(sem texto extraível nesta página)*

## Página 11

Progressive Delivery
11

## Página 12

Rolling Update 
Progressive Delivery
Is the umbrella term. It’s the overarching philosophy or discipline of modern software releases.
Replaces pods one by 
one (incrementally).
Standard availability with 
minimal resource 
overhead.
Shadow/Mirrorin
g
Mirrors live trafﬁc to the 
new version without the 
user seeing the result.
Performance & Load 
testing under real 
conditions.
A/B Testing 
Distributes trafﬁc based 
on user attributes 
(region, browser, ID).
Business metrics (Which 
version converts 
better?).
Blue/Green 
Two identical 
environments; switches 
100% trafﬁc from Blue 
(old) to Green (new).
Zero Downtime and 
instant rollbacks.
12
Canary
Routes a small 
percentage of trafﬁc 
(e.g., 5%) to the new 
version to test it.
Risk mitigation by 
testing on real users.
While "Continuous Delivery" focuses on moving code from the developer to production as fast as 
possible, Progressive Delivery focuses on how that code is exposed to users to minimize risk

## Página 13

Rolling Update 
Progressive Delivery
Is the umbrella term. It’s the overarching philosophy or discipline of modern software releases.
Replaces pods one by 
one (incrementally).
Standard availability with 
minimal resource 
overhead.
Shadow/Mirrorin
g
Mirrors live trafﬁc to the 
new version without the 
user seeing the result.
Performance & Load 
testing under real 
conditions.
A/B Testing 
Distributes trafﬁc based 
on user attributes 
(region, browser, ID).
Business metrics (Which 
version converts 
better?).
Blue/Green 
Two identical 
environments; switches 
100% trafﬁc from Blue 
(old) to Green (new).
Zero Downtime and 
instant rollbacks.
13
Canary
Routes a small 
percentage of trafﬁc 
(e.g., 5%) to the new 
version to test it.
Risk mitigation by 
testing on real users.
While "Continuous Delivery" focuses on moving code from the developer to production as fast as 
possible, Progressive Delivery focuses on how that code is exposed to users to minimize risk

## Página 14

Trunk-Based vs 
Branch-Based Development
14

## Página 15

Trunk-Based vs Branch-Based Development
15
Branch-Based Development (Env per Branch): 
In this model, different Git branches represent different 
environments (e.g., a staging branch and a production 
branch).
◆ How it works in GitOps: Argo CD has multiple 
"Applications." The Staging App tracks the staging 
branch, and the Production App tracks the 
production branch. To deploy to production, you 
perform a Pull Request (PR) from staging to 
production.
◆ Focus: Control, manual gates, and clear separation 
between environment states.
◆ Best for: Regulated industries or teams that require 
manual sign-offs before a production release.
Trunk-Based Development
In this model, developers collaborate on a single branch (usually 
main or master). Short-lived feature branches are merged as 
quickly as possible.
◆ How it works in GitOps: Argo CD tracks the main branch. As 
soon as a commit is pushed or merged into main, Argo CD 
automatically syncs those changes to the cluster.
◆ Focus: Speed, Continuous Integration, and avoiding "merge 
hell."
◆ Best for: Teams with high automation, automated testing, and 
a "fail forward" mentality.
 
 Trunk-based is about Continuous Deployment, while Branch-based is about Release Control

## Página 16

Promotions between Stages: Trunk-Based
16
◆ No Branch Merges: We don't merge staging into production. 
Both environments track main.
◆ Environment-Speciﬁc Values: We use separate values.yaml
◆ Promotion = Tag Update: Promoting a version means updating 
the image.tag in the production conﬁguration ﬁles.
◆ Decoupled: Code is integrated into main immediately (CI), but 
deployed to production only when the conﬁguration is updated 
(CD).
In Trunk-Based GitOps, we promote 'Artifact 
Versions,' not 'Git Branches.

## Página 17

Promotions between Stages: Branch-Based
17
◆ Environment = Branch: The state of the staging branch is 
exactly what is running in the Staging cluster.
◆ Promotion via Merge: Moving code from Dev to Staging requires 
a Git Merge/Pull Request.
◆ Visibility: You can use git diff dev..staging  to see exactly 
what is about to be deployed.
◆ Permissions: Git branch protection rules (e.g., "Only Artem can 
merge to main") act as deployment gates.
This architecture is categorized as a GitOps 
anti-pattern and is not recommended for 
production-scale environments.

## Página 18

Before Kargo: You write a custom bash 
script in GitHub Actions to sed  an image 
tag in a YAML ﬁle and commit it to 
another branch. (Fragile & complex).
With Kargo: You deﬁne a Warehouse and 
Stages. You click "Promote" in a UI (or via 
CLI). Kargo handles the GitOps-compliant 
state change automatically.
18
◆ Continuous Promotion: Instead of manually editing YAML tags for every environment, Kargo 
orchestrates the "Promotion" of Freight (a bundle of Git commits, Images, and Helm charts) 
across stages.
◆ Trunk-Based but Controlled: It allows you to keep a single branch (Trunk-based) while 
providing the visual Promotion Gates (Dev → Staging → Prod) that teams usually try to solve 
with messy branch-based GitFlow.
◆  Decoupled from CI: Kargo stops the "CI-as-CD" anti-pattern. You don't need GitHub 
Actions or Jenkins to "push" changes; Kargo manages the lifecycle natively within 
Kubernetes.
Promotions between Stages: Kargo as Bridge

## Página 19

The PR Generator is a feature of the Argo CD ApplicationSet controller.
Normally, Argo CD needs a folder in Git to create an application. The PR Generator 
changes this: It treats an open Pull Request as a trigger to create a temporary Argo 
CD Application automatically.
1. The Trigger: A developer creates a new branch (e.g., feat-login) 
and opens a Pull Request against the main branch.
2. The Discovery: The PR Generator constantly polls your Git provider 
(GitHub/GitLab). It "sees" the new PR.
3. The Templating: The Generator uses a template to create a new 
Argo CD Application on the ﬂy. It can use variables from the PR, 
such as:
a. {{.branch}}: The branch name (e.g., feat-login).
4. The Deployment: Argo CD creates a temporary namespace (e.g., 
preview-pr-123) and deploys the app there.
 19
Argo CD: Pull-Request Generator (I)

## Página 20

20
Argo CD: Pull-Request Generator (II)

## Página 21

21
Argo CD: Pull-Request Generator (III)

## Página 22

Repository Strategies
22

## Página 23

Repository Strategies: Mono vs Multi Repo(s)
23
Multi Repo (The "One per Service")
Each service or team has its own dedicated Git 
repository for its code and manifests.
◆ How it works in GitOps: Argo CD has many 
"Application" objects, each pointing to a different 
repository.
◆ Focus: Autonomy, isolation, and granular access 
control (RBAC).
◆ Best for: Large organizations with many 
independent teams where Team A should not be 
able to touch Team B’s code or conﬁguration.
Mono Repo (The "One for All")
All code, Helm charts, and Kubernetes manifests for all 
services/teams are kept in a single, large Git repository.
◆ How it works in GitOps: Argo CD points to different folders 
within the same repo
◆ Focus: Visibility, cross-service consistency, and simpliﬁed 
dependency management.
◆ Best for: Smaller teams or organizations that want to share 
code/templates easily and maintain a global overview.
 
Mono Repo prioritizes shared consistency and visibility; Multi Repo prioritizes team autonomy 
and security boundaries.

## Página 24

Folder per Environment (I)
24
The Core Philosophy
Instead of using Git branches (which lead to 
"Merge Hell"), we use folders within a single 
branch (usually main).
➔ Single Source of Truth: One branch to 
rule them all.
➔ Promotion via Copy: Moving a release 
is a simple cp (copy) command 
between folders.
➔ Clarity: A quick look at the /envs 
folder shows exactly what is deployed 
where.
 
Simple (Stage-Based)
Best for small teams or single-region applications. It 
follows the software lifecycle.
Best for: Projects where "Prod" is a single cluster.
Note: staging and prod should inherit from the same 
variants/stable folder to ensure they remain 
identical in conﬁguration.

## Página 25

Folder per Environment (II)
25
The Specialized Hardware/Feature Pattern
Used when environments differ by technical 
capabilities (e.g., AI/ML workloads).
Best for: Performance testing, GPU-heavy workloads, or 
cost-optimization (using smaller clusters for QA).
The Geographic Matrix (Region/Country-Based)
Required for global applications with data residency 
(GDPR) or latency requirements.
Best for: Large scale apps where "Prod" is not one place, 
but many.
Note: This structure allows you to use Kustomize 
Components to apply "EU-only" settings (like speciﬁc 
database endpoints) to all folders under the /eu tree.

## Página 26

Folder per Environment (III)
26
Pattern Complexity Best Use Case
Stage-only Low Start-ups, single apps.
Stage + Region Medium SaaS companies with global users.
Stage + Variant High Specialized tech (Edge computing, AI, Finance).

## Página 27

Folder per Environment (IV)
27
Selection Criteria Recommended Grouping Example Structure
Low Complexity Stages envs/dev, envs/prod
High Compliance Countries envs/germany, envs/usa
Multi-Cloud Setup Cloud Providers envs/aws-eu, envs/azure-us
Speciﬁc Hardware Variants envs/gpu-cluster, envs/cpu-cluster
Global Scaling Regional Matrix envs/prod-eu, envs/prod-us

## Página 28

State Store
28

## Página 29

State Store: Git, OCI or  
ConﬁgHub (I)
29
The State Store is the "Source of Truth" for your desired Kubernetes 
state. While Git is the default, modern GitOps architectures often use 
OCI or ConﬁgHub.
Git (The Standard)
OCI - Open Container Initiative (The Modern Way)
ConﬁgHub (The New Solution on the Market)
Don't confuse the Development Source (Git) with the Distribution Source 
(State Store). You can write code in Git, but use a CI pipeline to push it 
to OCI for the actual deployment.
Using OCI as a State Store is becoming the gold standard for enterprises 
because it treats YAML exactly like code—versioned, packaged, and 
signed

## Página 30

30
Git
Mechanism: Direct sync from a Git 
repository (GitHub, GitLab, Bitbucket).
Best For: Most teams; provides full 
history, Pull Request workﬂows, etc.
Challenge: Large repositories with 
thousands of ﬁles can cause 
performance bottlenecks 
(slow polling) for the GitOps 
controller.
State Store: Git, OCI or  ConﬁgHub (II)
OCI
Mechanism: Packaging Kubernetes 
manifests into an OCI Artifact (the same 
format as Docker images) and pushing 
them to a Registry (GHCR, Harbor, ECR).
Best For: Scaling GitOps. Decouples the 
"Source" (Git) from the "Release" (Registry).
Advantages: * Faster Sync: Argo CD/Flux 
pulls a single compressed artifact instead of 
cloning a whole Git history.
● Immutable Releases: Every version is 
a signed, immutable "Logical 
Container" of YAMLs
ConﬁgHub
Mechanism: Moves away from "File-based" 
Git to "Data-based" storage. It stores fully 
rendered, literal YAML manifests in a 
structured database (Source of Record) 
instead of managing complex templates in 
Git.
Best For: Platform Engineering teams 
managing hundreds of clusters or apps 
who want to eliminate "Conﬁg Sprawl" and 
template errors.
● WYSIWYG (What You See Is What 
You Get): No more hidden logic. 
Every manifest is stored in its ﬁnal, 
"WET" (Write Every Time) form, 
making it instantly readable and 
validatable.

## Página 31

31
Recap: GitOps Architecture, Patterns…
❏ GitOps Architecture: 4 principles + internal vs. external reconcilers 
(single cluster vs. ﬂeet).
❏ Progressive Delivery: strategies, risks, and beneﬁts
❏ Trunk vs. Branch: trunk reduces complexity; combine approaches 
when needed
❏ Repository Strategies: choose a promotion model that scales
❏ State Store: Git is common, but not the only option—consider OCI and 
ConﬁgHub
GitOps is based on the four principles.
But if you want to get the most out of it, you also need to understand the 
other building block!

## Página 32

Demo
32
