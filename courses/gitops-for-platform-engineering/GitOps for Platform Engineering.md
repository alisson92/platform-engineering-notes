# GitOps for Platform Engineering

## Module 1: Introduction and motivation

### This course, led by Artem Lajko, explores GitOps as the essential "glue" that ties platform engineering components together. Over the course of six modules, you will move from the core fundamentals and architecture patterns to mastering industry-standard tools like Argo CD, Flux CD, and Sveltos,. You will learn how to scale these practices for enterprise environments managing thousands of clusters, how to address security and governance, and understand the necessary cultural shifts required to adopt GitOps successfully.

### Why GitOps

GitOps offers "1000 reasons plus one" for adoption, primarily enabling infrastructure to become reliable and self-healing because Git dictates exactly what the system must look like. Real-world data demonstrates that adopting GitOps can reduce infrastructure costs by 50%, cut incident response times to under five minutes, and eliminate release downtime entirely,,. It effectively transforms Git into your deployment API, providing fully versioned infrastructure, perfect reproducibility, and a bulletproof audit trail where every change is reviewable and transparent.

Why Do We Want GitOps?

We want GitOps because it establishes a binding contract between humans and agents: humans define the desired state in Git, and agents continuously reconcile the live system to match it, ensuring the pipeline does not need privileged cluster access. This model acts as the glue for continuous delivery, ensuring disaster recovery, automated drift correction, and enhanced security through strong audit trails. Furthermore, by keeping everything in Git, the system becomes AI-ready, allowing intelligent tools to analyze the repository and explain exactly what happened and why.

### The Wild West …before DevOps …before GitOps

Before modern practices, operations resembled the "Wild West," where engineers manually accessed servers via RDP or SSH to install patches and deploy applications. Managing complex setups, such as high-availability enterprise environments, often meant juggling multiple terminal windows and relying on manual configuration updates that simply did not scale. This era was plagued by maintenance challenges, such as keeping a Configuration Management Database (CMDB) updated manually, which rarely reflected the actual state of the system.

### Lead to Infrastructure as Code

These manual inefficiencies led to the birth of Infrastructure as Code (IaC), introducing tools such as Chef, Puppet, Ansible, and Terraform. This shift allowed engineers to move away from executing manual steps to describing what they wanted in a declarative manner, essentially letting the machine fulfil the request based on code.

### New tooling…similar challenge…running on my machine

However, new tools brought similar challenges; often, code was still "running on my machine," meaning simultaneous changes by different engineers (e.g., Alex and Alice) could overwrite each other due to a lack of shared state. While teams eventually moved to "Pipeline Ops," executing changes through CI/CD, this often resulted in "drift"—a discrepancy between the configuration in Git and the actual state of the target system that might persist, unnoticed, until the next deployment event.

In summary, this module sets the stage by explaining the motivation behind GitOps and how its pull-based reconciliation differs fundamentally from traditional push-based delivery. By the end of this course, you will understand how to build a platform distribution, manage a fleet of clusters, and navigate the cultural changes required to stop manual fixes and trust the automated process.

## Module 2: GitOps fundamentals and core principles

### While the idea of a pull-based model for configuration management traces back to tools like Chef (announced in 2009), the specific concept of GitOps is more recent. The term "GitOps" was coined in 2017 by Alexis Richardson, the then-CEO of Weaveworks,. Richardson gave this operational model its name and defined it strictly through four core principles, effectively establishing the framework used today.

### The four principles:

Alexis Richardson defined GitOps through four non-negotiable principles: declarative, versioned and immutable, pull-based, and continuously reconciled. The declarative principle means you describe what you want (the desired state) rather than scripting how to get there. The system must be versioned and immutable, meaning every change is stored in a history log (like Git) and treated as a unique version. The pull-based approach utilizes an agent that watches the repository to fetch changes, while continuous reconciliation ensures this agent constantly compares the live system against the desired state to automatically correct any drift.

It is crucial to clarify that GitOps is not a replacement for DevOps, Platform Engineering, or Continuous Integration (CI); rather, it is an operational model that replaces traditional push-based delivery. GitOps is not "ClickOps," where users manually adjust settings in a UI, nor is it ad-hoc kubectl commands run manually against a cluster. Furthermore, simply slapping Git on top of a standard CI/CD pipeline does not constitute GitOps; if the pipeline pushes changes without continuous synchronization and drift detection, it misses the core requirement of the reconciliation loop.

### Terminology

Understanding GitOps requires mastering specific terms. The Desired State is the normative definition of what should be running, while the Current State is what is actually running on the target system. Drift occurs when there is a discrepancy between these two states, triggering Reconciliation, the process where an engine converges the current state toward the desired state. The State Store (usually Git) serves as the single source of truth. The Feedback Loop describes the continuous cycle of observing and correcting this state, and a Rollback is simply a git revert operation, which the reconciler then applies to the system. Additionally, GitOps distinguishes between Infrastructure/Configuration as Code (logic-based) and Infrastructure/Configuration as Data (plain declarative state without execution logic).

Comparison: Traditional CI/CD vs. GitOps. In traditional CI/CD, often called the Push-based model, a pipeline executes commands (like kubectl apply) from the outside to deploy changes, which requires the pipeline to hold privileged cluster credentials. This is often described as a "fire and forget" method. In contrast, GitOps uses a Pull-based model where an agent inside the cluster (like Argo CD) watches the Git repository and pulls changes in. This "watch and sync" approach is more secure because no cluster credentials ever leave the environment.

### Contextualization: GitOps within DevOps, DevSecOps, and Platform Engineering

GitOps fits into the broader landscape not as a replacement, but as an advanced implementation of DevOps principles. It enables DevSecOps by allowing teams to define security policies and compliance as code, which are then enforced by the GitOps agent. In the context of Platform Engineering, GitOps acts as the "glue" that ties platform components together, enabling scalable self-service platforms where infrastructure, dashboards, and budgets are all managed declaratively.

And by the way: DevOps is dead / DevOps -> Platform Engineering You may hear the provocative statement that "DevOps is dead." This refers to the evolution of the role rather than the culture; defining a role merely by a collection of tools was never sustainable. The industry is shifting from the ambiguous "DevOps Engineer" title toward Platform Engineering, organizing responsibilities into planes (e.g., observability, security),. In this evolution, GitOps serves as the operational engine that allows platform engineers to move away from manual "ticket-based" ops to building automated, self-healing platforms.

## Module 3: GitOps architecture, patterns, and anti-patterns

### GitOps Architecture: Declarative

GitOps architecture relies on four core principles: it must be declarative, versioned and immutable, pull-based, and continuously reconciled. Unlike imperative systems, where you define a recipe of steps to execute, a declarative architecture requires you to define the desired "what"—the final state declared in YAML—and lets the system figure out the "how" to achieve it. This architecture ensures that the system always knows what it should look like based on the single source of truth.

### In-cluster vs. external reconciler

The reconciler is the engine that applies GitOps, and it can run either inside or outside the cluster. An internal (in-cluster) reconciler runs as a pod within the target cluster, having direct access to the Kubernetes API server to watch Git and apply changes, effectively allowing the system to manage itself. Conversely, an external reconciler (like a central Argo CD instance) operates from the outside to manage resources on external clusters, a pattern often used when managing a fleet of clusters to provide a central control plane.

### Progressive delivery: Blue/Green, Canary, rolling updates

Progressive delivery is an advanced strategy that allows you to release new features to a subset of users or environments gradually, minimizing risk and enabling rapid feedback. While continuous delivery focuses on speed, progressive delivery focuses on safety by using strategies like Rolling Updates (replacing pods incrementally), Blue/Green (switching traffic between identical environments), or Canary deployments. This approach aims to guarantee continuous delivery with zero downtime by validating changes on a smaller scale before a full rollout.

### Trunk-based development vs. branch-based approaches

Your choice between trunk-based and branch-based development significantly influences your GitOps architecture. In trunk-based development, developers collaborate on a single main branch, promoting immutable artifact versions rather than merging git branches between environments. In contrast, branch-based development maps every environment to a specific branch (e.g., dev, staging, prod) where promotion happens via pull requests, offering strict release control suitable for highly regulated industries where manual sign-offs are required. Learn why branch-based development is considered an anti-pattern in GitOps. 

### Architecture patterns: Single source of truth, repository separation

When structuring repositories, you can choose between mono and multi-repository strategies. A mono repository offers a single pane of glass with high visibility and consistency, making it easy to share code and manage global configurations, while multi-repository setups provide better autonomy, isolation, and granular access control for independent teams. Experience suggests a hybrid pattern often works best: centralizing common platform configurations in one repository while keeping workload specifications in separate team repositories to balance control and autonomy.

Anti-patterns: Environment-per-branch & Mixing infrastructure and applications. Using a branch-based approach where every environment is a distinct branch is often considered a GitOps anti-pattern. This is because Git starts managing environment differences through merges, leading to conflicts, "merge hell," and eventual environment drift that becomes difficult to track. Another common challenge is the "sprawl of configs," where mixing infrastructure logic across various layers (provider charts, umbrella charts, and overlays) reduces visibility, making it difficult to understand exactly what changed and why when errors occur.

### State store alternatives (Git, OCI, ConfigHub)

While Git is the default state store for most teams, it is not the only solution; modern architectures are increasingly adopting OCI or ConfigHub. Using OCI allows you to package manifests as immutable artifacts, decoupling the development source in Git from the distribution source and enabling faster synchronization. Alternatively, ConfigHub creates a "Source of Record" database that stores fully rendered manifests (configuration as data), eliminating the complexity of templating errors and ensuring "what you see is what you get".

## Module 4: GitOps tooling 101: Argo CD, Flux CD and Sveltos

### GitOps tooling 101: Argo CD, Flux CD and Sveltos

The GitOps landscape is dominated by three primary tools, each serving distinct platform needs. Argo CD, released in 2019, is an application-centric controller known for its robust User Interface (UI), effectively offering a "Single Pane of Glass" for developers to visualize and manage application lifecycles. Flux CD, the project that originally coined the term "GitOps," operates as a modular set of controllers (the "Unix philosophy") without a native UI, making it a lightweight, Kubernetes-native engine ideal for invisible background automation and security. The newest entrant, Sveltos, is designed specifically for fleet management, using label-based ClusterProfiles to distribute platform add-ons across large numbers of clusters.

### Comparison of architectures, operation, and use cases

These tools differ significantly in how they process changes. Argo CD typically renders manifests by executing template commands (like helm template) and applying the result, providing a strong visualization of the resource hierarchy. Flux CD relies on dedicated controllers (Source, Helm, Kustomize) to continuously reconcile the cluster state against Git or OCI artifacts, focusing on deep Kubernetes role-based access control (RBAC) integration. Sveltos takes a different approach by deploying real Helm releases directly into managed clusters based on defined profiles, making it highly effective for creating uniform environments across a Hub-and-Spoke topology,.

When to use which tool Choosing the right tool depends on your specific platform requirements. If your priority is developer self-service, visibility, and a rich ecosystem, Argo CD is the industry standard. If you require a low-footprint solution for edge computing or prefer a tool that integrates invisibly with native Kubernetes workflows, Flux CD is the ideal choice. For managing massive fleets of clusters with requirements for strong multi-tenancy and event-driven add-on distribution, Sveltos is the strongest candidate. However, you are not limited to one; a powerful "Kubara way" pattern involves combining tools - for instance, using Flux or Argo CD to manage the control plane while Sveltos manages the fleet.

### Helm vs. Kustomize – differences, strengths, and combinations

GitOps relies heavily on how manifests are generated, leading to the choice between Helm and Kustomize. Helm acts as a package manager with a templating engine, allowing you to abstract complexity and inject logic (loops, if/else) into your deployments, making it perfect for reusable products. Kustomize uses an overlay approach, maintaining the original YAML transparency while patching specific fields (like replica counts) for different environments. In practice, these tools are often combined: a Helm chart defines the base application "product," while Kustomize applies the final environment-specific configuration patches.

### Building a GitOps service catalog with Helm

To scale GitOps effectively, you should build a Service Catalog using the "Wrapper Chart" (or Umbrella Chart) pattern. This involves wrapping third-party charts (like cert-manager) with your own templates to add missing resources, such as ClusterIssuers or security policies, ensuring that every installation is production-ready by default. This approach enforces Governance and the DRY (Don't Repeat Yourself) principle by centralizing configurations in one catalog while allowing flexibility through value overrides per cluster. By using a catalog, you enable GitOps at scale, managing a fleet of clusters consistently through a central control plane.

## Module 5: GitOps for Enterprises – Scaling and security

### GitOps at Scale – Reference architectures

When scaling GitOps for the enterprise, there is no single "best" topology; rather, teams must choose between patterns like Hub-and-Spoke, Dedicated Instances, or hybrid models based on their specific requirements. The Hub-and-Spoke model uses a central management cluster (the Hub) to control deployments across many remote clusters (Spokes), offering a "Single Pane of Glass" for centralized visibility and efficient fleet management using tools like Argo CD ApplicationSets or Sveltos ClusterProfiles,. However, this model introduces a large "blast radius" - if the Hub fails, fleet management is affected - and poses a security risk because the Hub must store admin credentials for every target cluster. Conversely, the Dedicated Instance per Cluster (or Standalone) model runs a GitOps controller on every single cluster, ensuring high reliability and strict isolation, perfect for edge or air-gapped environments, though it results in fragmented visibility and higher management overhead.

To balance these trade-offs, enterprises often adopt Hybrid Topologies or advanced Agent-based models. For instance, a "Hub and Spoke Agent Pull" model allows the managed cluster to pull its desired state from the Hub using an outbound connection, removing the need for the Hub to store privileged ingress credentials for the spokes. For extremely large environments, teams might employ Sharding, splitting the GitOps workload across multiple controller instances to distribute CPU/RAM load, or Logical Grouping, where separate hubs manage specific regions (e.g., EU vs. US) or environments (Prod vs. Non-Prod) to control the blast radius and align with organizational boundaries.

### Secrets management in GitOps

A fundamental challenge in GitOps is that while Git serves as the single source of truth (in theory) for configuration, you must never store plain-text secrets in the repository. The best practice is to store only references to secrets or encrypted artifacts in Git, ensuring that the actual sensitive values remain secure either in an external vault or strictly inside the cluster. This approach ensures that your security and compliance teams can audit changes without exposing sensitive data.

To solve this, tools like Sealed Secrets and the External Secrets Operator (ESO) have become industry standards. Sealed Secrets uses asymmetric encryption, allowing developers to encrypt secrets locally (which are safe to commit to Git) that can only be decrypted by the controller inside the cluster; however, if the private key is lost, the data is unrecoverable. Alternatively, External Secrets Operator acts as an API bridge, fetching secrets at runtime from enterprise-grade providers like AWS Secrets Manager, Azure Key Vault, or HashiCorp Vault. This method is considered state-of-the-art for enterprises as it ensures secrets never enter Git, only the ExternalSecret reference does, keeping the setup compliant and secure.

### Cultural shifts through GitOps – GitOps in, GitOps out

Adopting GitOps at an enterprise level requires a significant cultural shift, often summarized as "GitOps is 20% tooling and 80% discipline",. Teams must transition from manual "ClickOps" or ad-hoc kubectl fixes to a strict "Everything via Git" principle, where the Git repository acts as the unchangeable contract between humans and agents. This means relinquishing direct access to production clusters and trusting the automated reconciliation loop, a change that can initially feel restrictive to developers used to instant manual fixes.

By establishing Git as the Single Source of Truth, organizations create a transparent environment where every change—whether it's code, infrastructure, or policy—is versioned, reviewable, and auditable through Pull Requests. This shift enables "GitOps In, GitOps Out," where different stakeholders (including Security and Finance) provide inputs like rules and budgets into Git, and the GitOps platform ensures the output matches those declarations automatically. Ultimately, this culture of shared responsibility and transparency is what allows platforms to scale, making the system resilient and self-healing without constant human intervention.

## Module 6: Outlook and trends – GitOps is a sprawl of configs...

### Sprawl of configs: A major challenge in scaling GitOps is the "sprawl of configs," where configuration logic is fragmented across multiple layers such as third-party provider charts, internal umbrella charts, and environment-specific overlays. This setup often works until it breaks; when the GitOps engine executes this complex chain of code, errors may point to locations that do not reflect the root cause, leading to a significant loss of visibility. Troubleshooting becomes difficult as engineers must jump between different repositories and folders to mentally construct the final state and understand exactly what changed.

Current developments. To address this complexity, the industry is shifting toward "Source Hydration," a process where templates are rendered into their final plain YAML form (Configuration as Data) before being stored and applied. This trend is championed by figures like Alexis Richardson, the founder of Weaveworks, who coined the term "GitOps" and is now CEO of ConfigHub Inc., a company focusing on storing fully rendered manifests in a structured database to eliminate template errors and ensure "What You See Is What You Get".

Simultaneously, we are seeing the rise of "Gitless GitOps," where OCI artifacts replace Git as the distribution source. By packaging manifests and images together into immutable, signed OCI artifacts, teams can achieve faster synchronization and enforce stricter security policies, such as "only signed runs" using tools like Kyverno. New tools like Kargo are also emerging to handle the promotion of these changes across stages, managing the underlying branching logic so developers can focus on a trunk-based approach.

### The future of GitOps in combination with AI and Platform Engineering

The future of platform engineering involves integrating AI as the "brain" of the platform, with GitOps providing the necessary reliable foundation. Because GitOps acts as the single source of truth for the desired state and Kubernetes orchestrates the actual state, AI tools can analyze this data to explain not just what is happening, but why it is happening. By running agents (such as Kagent) on workload clusters and connecting them to CustomGPTs via secure APIs, platforms can offer chat interfaces where users can ask questions like "Why is my app white?" and receive accurate answers based on real-time logs and configuration history.
