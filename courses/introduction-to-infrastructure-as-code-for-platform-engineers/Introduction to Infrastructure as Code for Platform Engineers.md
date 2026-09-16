# Introduction to Infrastructure as Code for Platform Engineers

## Module 1: Introduction

### Infrastructure as Code (IaC) emerged as a response to the chaos of manual provisioning, one-off scripts, and unmaintainable cloud configurations spread across AWS, Azure, and Google Cloud. Rather than running fragile scripts, IaC uses declarative tools like Terraform, OpenTofu, and Pulumi to define the desired end-state of infrastructure in version control, letting the tool handle the API calls. This is distinct from configuration management tools like Ansible or Chef, which operate inside already-provisioned machines. The key shift is from "autonomy" to "empowerment with guardrails": security policies are pre-vetted, audits become instantaneous, and cost-saving patterns are baked into standard templates.

A critical design question for platform teams is whether to expose raw IaC directly to developers or abstract it behind a cleaner interface. Raw IaC is highly flexible for subject matter experts but too complex for most developers, who would rather focus on delivering business value. VCS-backed modules serve as the ideal middle ground: developers invoke a pre-approved module with a handful of variables, while the platform team handles the underlying networking, security groups, and compliance configuration. This approach supports self-service without sacrificing guardrails.

AI can accelerate IaC in two areas: code generation and operations. As a pair programmer, AI generates high-quality configurations when given an organization's style guides and naming conventions. For operations, AI can assist with troubleshooting and self-healing workflows, but it must always operate through declarative IaC and version control rather than executing raw API commands directly. MCP servers that provide real-time provider documentation help prevent the hallucinated or deprecated resource schemas that LLMs are prone to generating.

## Module 2: Building the abstraction

When designing the developer-facing interface, platform teams choose between raw IaC, Configuration as Code (YAML/JSON), and graphical developer portals. Each suits a different audience, and most successful organizations support all three simultaneously, anchoring them in the same version-controlled modules to ensure consistency. VCS-backed modules strike the right balance: developers consume pre-approved configurations as code and adjust exposed parameters, while the platform team handles the heavy lifting. The portal should map complex cloud parameters to developer-friendly terms (for example, "Eastern US" instead of us-east-1) so that developers are never blocked by the platform.

The "Rule of Three" is a practical guide for when to build a module: if the same grouping of infrastructure is deployed more than three times across teams, it is time to standardize it. Modules should also enforce security and compliance by default, hardcoding attributes like encryption at rest and tagging policies so that developers cannot provision non-compliant resources even if they try. The anatomy of a module centers on a strict input-output contract: minimal, validated inputs and clean singular outputs that allow platform engineers to refactor internals without breaking downstream consumers. Avoid "super-modules" that bundle too many disparate resources; smaller, decoupled modules are far easier to evolve and debug.

Decoupling dependencies limits the blast radius of changes. Platform teams should follow three principles: keep inputs to a minimum, limit module nesting to two layers, and embed lifecycle protection rules on stateful resources like databases and storage buckets. For data passing between modules, a centralized key-value store is the most scalable pattern for large systems. AI can play a useful role here as a pair programmer, generating module scaffolding from style guides and mock validations, as long as teams account for LLM knowledge cutoffs and integrate MCP servers for up-to-date provider documentation.

## Module 3: Deploying infrastructure

Modularised IaC encapsulates complex architectural decisions, such as VPC peering, private database subnets, and routing table structures, into standardized templates that developers invoke with minimal input. The "opinionated by default" approach bakes secure, high-performance defaults into the module, exposing only essential parameters like environment tags or cluster sizing tiers. Once published, modules must respect backward compatibility: output types and validated inputs are a contract, and breaking changes require a major version increment with clear communication to consuming teams.

A rigorous testing pipeline is non-negotiable before publishing any module version. The three-tier pyramid covers unit testing (static configurations and conditional logic, no real resources), contract testing (verifying that output types from one module can be consumed by another), and integration testing (full sandbox deploys testing sad paths and minimum IAM permissions). Contributions from subject matter experts and application developers are encouraged but governed through a PR review workflow with automated linting, unit tests, and security scanning. A rotating "sustaining engineer" role prevents PR fatigue from stalling delivery.

Platform teams can expose modules through three interfaces: raw IaC primitives, Configuration as Code (YAML parsed by GitOps operators), and developer portals with form-based inputs. Many organizations support all three, allowing developers to start with a portal and "eject" to raw IaC if they need advanced customization. AI fits naturally into this pipeline as an automated PR reviewer, assessing blast radius, flagging compliance issues, and routing high-risk changes to a senior engineer. Avoid enabling it to be an unmonitored deployer of infrastructure until you have sufficient context and observability; all AI-generated changes must flow through version control and the standard testing pipeline.

### Style guide:

File organization
Code formatting
Naming conventions
Required attributes
Preferred functions or methods
Avoid referencing other modules
Other quirks

Note: Put these in documentation or validation tool!

### Testing modules

Separate account
Conditional or iterative logic - (if/for)
Sad paths for upgrades
Passing criteria - security/compliance
IAM permissions

### Pyramid of tests

Unit test
Contract
Integration

### Module ready for production

main --> branch/fork --> PR (trigger linting/formatting, tests, security/compliance) --> main

Note: Code review only if large change

Pull request fatigue?

Rotation - "Sustainin Engineer"

	Triage
	Stakeholder coordination

Automation

	Linting and formatting
	Testing

## Module 4: Practices for security and compliance

Secrets must never be hardcoded in IaC files or passed as plaintext variables. Platform teams should enforce centralized secrets managers such as AWS Secrets Manager, Azure Key Vault, or IBM Vault, with infrastructure code retrieving secrets dynamically at runtime. State files must be encrypted at rest, and ephemeral resources should be used where available to prevent secrets from being written to persistent state at all. Least privilege access is equally critical: CI/CD pipelines should hold only the minimum permissions required for a given module, with access analyzers used during development to tighten IAM policies from broad to constrained.

Consistent tagging is the backbone of platform auditing, cost tracking, and security. A standard tagging policy should include managed_by, owner, environment, repository, date_created, business_unit, and purpose, all embedded directly into core modules so that compliance is automatic rather than developer-dependent. Policy as Code (using OPA/Rego or Sentinel for Terraform) enforces organizational standards at three gating levels: Advisory (warning only), Soft Mandatory (requires a documented exception), and Hard Mandatory (hard stop). For cost management, time-to-live tags and automated decommissioning of idle environments are more reliable than rigid cost-threshold blocks, which tend to catch legitimate deployments in the crossfire.

AI accelerates policy development by translating natural language security requirements directly into Rego or Sentinel code. However, passing full IaC files and compliance runbooks to an LLM is expensive and can produce false positives. The pragmatic pattern is to shift-left to deterministic CLI tools (tfsec, Checkov, OPA) and use AI only for remediation: the scanner identifies the violation, passes the failing block to the AI agent, and the agent generates a corrected plan for human review.

### Secrets management

Use an official secrets manager
Temporary, write-only attribute
Encrypt before use

### Access management

"Just enough" to "least" privilege
Access analyzers are your friend
Offer self-service for access
Dev vs, stagin vs. prod

### Module supply chain security

Mirror public modules
Linting rules are your friend

Standardization != compliance

### Cost compliance

Policy as Code
Cost management

### Platform hygiene checklist

Required tags
TTL for resources
Least privilege access for IaC
Codify functional expections
Codify security exceptions

### AI as pair programmer

#### Generate custom policies

Establish style guide
Can use spec-driven development

### AI as compliance reviewer

Token Usage Per Security Review

For a comprehensive Terraform file (like aws_instance_comprehensive.tf with 352 lines):

Input Tokens: ~12,000–15,000

System prompt & instructions: ~8,000–10,000
Terraform file content: ~2,500–3,000
Policy files: ~1,200–1,500
Context & environment: ~500–1,000

Output Tokens: ~3,500–7,000

Security analysis: ~2,000–4,000
Issue findings: ~1,000–2,000
Recommendations: ~500–1,000

Total per review: ~15,500–22,000 tokens

Shifting left consumes tokens

Offload to an analysis tool

CLI
Remote server

Note: Token ranges are estimates based on usage with IBM Bob, which uses model switching.

### AI as a platform interface

Example: https://github.com/joatmon08/platform-infrastructure-skills

The policy: Build and scale like code.

The tags: Set one standard for cost, security, and auditing.

## Module 5: Practices for infrastructure lifecycle and operations

Platform teams typically frame the IaC lifecycle in three operational phases: Day 0 (greenfield provisioning and establishing golden paths), Day 1 (updates, drift reconciliation, and routine module upgrades), and Day 2 (incident response, hotfixes, and break glass procedures). In practice, most engineering time is spent on Day 1 and Day 2, constantly refactoring brownfield infrastructure and reconciling configurations that have drifted from version control. Self-service offerings must be designed with the full lifecycle in mind, giving developers clear, version-controlled paths to upgrade, modify, and decommission resources.

Before applying any change, a blast radius assessment is essential: what resources depend on the target, and how critical are they to the business? Low-impact changes like DNS metadata updates carry a small blast radius, while modifications to a VPC CIDR block can cascade across subnets, EKS clusters, databases, and load balancers. High-risk changes should use a blue-green approach, provisioning a parallel "green" stack and gradually shifting traffic before decommissioning the old one. Break-glass procedures allow engineers to intervene manually during active incidents, but any manual change must be back-ported into version-controlled IaC immediately to prevent silent overwrites on the next pipeline run. Rather than reverting, engineers should roll forward to a new declared state.

Brownfield migration follows a four-step workflow: analyze dependencies and lifecycles, separate concerns by provider and lifecycle into distinct modules, import resources and refactor hardcoded IDs into dynamic inputs, then execute a dry run targeting zero changes. AI agents can handle the repetitive parts of this work, parsing legacy configurations and generating moved or import blocks, provided they have clear runbooks and escalation paths for failures they cannot resolve deterministically. Backed by declarative IaC and version control, AI operators can scale Day 2 work such as drift reconciliation and bulk imports while platform engineers retain full review authority over every generated change.

### AI as an operator

Context really matters.

Logs
Error messages
Infrastructure state

Give it a runbook.

Provide escalation path.

Prioritize fixes through IaC.

### Example:

"""
User: The run failed to deploy the Helm release. Diagnostic logs are in logs/.

Agent: I see the error is that the Helm chart timed out. Let me check kubectl get pods -n bobs-book-agent to get the status of the release.

Agent: I see that the release is stuck on Pending. Let me check the Kubernetes logs for the release.

Agent: From kubectl describe pvc -n bobs-book-agent data-postgresql-0, the PVC failed with Warning ProvisioningFailed 4m21s (x122 over 34m) persistentvolume-controller storageclass.storage.k8s.io "gp3" not found.

This is a cluster-level issue — the gp3 StorageClass is not configured in the cluster.

This requires platform team intervention to:

Create the gp3 StorageClass
Configure the EBS CSI driver if not already installed
Verify IAM permissions for EBS volume provisioning

Would you like me to open a ticket with the platform team?
"""
