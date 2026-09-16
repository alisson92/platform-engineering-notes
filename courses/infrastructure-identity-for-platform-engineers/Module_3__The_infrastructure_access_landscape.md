# Module 3: The infrastructure access and identity landscape

## Slide 1
**The infrastructure access and identity landscape**

- INFRASTRUCTURE IDENTITY FOR PLATFORM ENGINEERS
- MODULE
- 03

## Slide 2
**Navigating the landscape**

> **Notas do apresentador:**
> The access landscape is fragmented because each tool solved a different problem.
> 
> But those solutions were never designed to work as a cohesive system.
> 
> Platform engineers now have to make sense of that fragmentation.

## Slide 3
**Where we left off**

- From legacy drag to modern mapping
- Legacy friction: We identified the massive risk legacy systems like VPNs and fragmented access.
- Ticking time bombs: We saw how standing privileges create permanent vulnerabilities.
- Legacy systems and approaches to infrastructure access are dragging us down. What does this wide world look like?

> **Notas do apresentador:**
> Previously, we saw that legacy access creates both friction and risk at the same time.
> 
> The key issue is not just bad tools — it’s a broken model.
> 
> Now we zoom out and map the ecosystem that evolved from that model.

## Slide 4
**Decoding the alphabet soup:Where does it all fit?**

> **Notas do apresentador:**
> This is the first key insight: these tools operate at different layers, not the same one.
> 
> Most confusion comes from trying to compare tools that solve different problems.
> 
> The real question is not “which one is best?” but “what does each one actually secure?”

## Slide 5
**IAM (Identity and Access Management)**

- Authenticates users via SSO and identity providers
- Manages roles, groups, and permission policies
- Controls application access at login time
- Secures application login… but not infrastructure sessions.

> **Notas do apresentador:**
> IAM is where identity typically starts — but also where many teams stop.
> 
> It’s designed around applications, not infrastructure.
> 
> That’s why it leaves a gap between login and actual resource access.

## Slide 6
**ZTNA (Zero Trust Network Access)**

- Brokers secure connections to internal networks
- Verifies identity and device posture before access
- Replaces traditional VPN-based perimeter models
- Secures the network edge… but not the resource itself.

> **Notas do apresentador:**
> ZTNA improves on VPNs, but it still focuses on connectivity, not control.
> 
> It decides whether you can reach something — not what you can do once there.
> 
> This is why network-layer security alone is insufficient.

## Slide 7
**PAM (Privileged Access Management)**

- Stores and manages high-privilege credentials
- Enforces approval workflows for sensitive access
- Records and audits privileged sessions
- Secures and manages credentials… but still relies on them.

> **Notas do apresentador:**
> PAM tries to fix risk by controlling and auditing credentials.
> 
> But it still assumes credentials are the right abstraction.
> 
> So it manages the problem, rather than eliminating it.

## Slide 8
**Infrastructure Identity**

- Issues short-lived, cryptographic identities to resources
- Enforces policy at the server, cluster, and database layer
- Unifies identity for humans, machines, workloads, and agents
- Secures the resource itself… without relying on credentials.

> **Notas do apresentador:**
> This is the shift: move control to the resource layer itself.
> 
> Instead of protecting credentials or networks, we verify identity at access time.
> 
> This is what enables true least privilege and dynamic access.

## Slide 9
**Let’s break it down**

## Slide 10
**What’s the problem with SSO?**

- SSO authenticates users, but doesn’t control infrastructure access or enforce just-in-time, least-privilege permissions
- SSO secures applications, not servers, Kubernetes, databases, or machine-to-machine communication
- SSO is built for humans only but modern infrastructure also requires identity for services, automation, and AI agents
- SSO might successfully verify who you are at login… but most modern security incidents don’t happen because someone bypassed login.

> **Notas do apresentador:**
> SSO gives a false sense of security because it solves only the first step.
> 
> Most real-world incidents happen after authentication, not before.
> 
> This is why login-based security is not enough.

## Slide 11
**The solution to the SSO gap:**

- Remember trust that expires by default?
- How Identity-centric authentication solves the SSO gap
- Eliminate Vaults: Stop managing, rotating, and sharing static secrets.
- Ephemeral Access: Use short-lived X.509 and SSH certificates.
- Just-in-time: Certificates are issued on demand by the platform as needed, and expire automatically.
- When every session is identity-bound, time-bound, and policy-enforced by default, Access becomes automatic, scoped, and expiring, reducing your MTTA (our key metric!) and blast radius at the same time.

> **Notas do apresentador:**
> The key idea here is making access ephemeral and identity-bound.
> 
> Instead of granting access once, we continuously verify it.
> 
> This reduces both friction and risk at the same time.

## Slide 12
**How does embracing machine identity work?**

- Scripts, microservices, and CI/CD pipelines need access.
- They shouldn't share static credentials either.
- Workloads require dynamic, verifiable cryptographic identities (e.g., SPIFFE or Secure Production Identity Framework for Everyone).

> **Notas do apresentador:**
> Machines are now the dominant actors in infrastructure systems.
> 
> Yet most access models were designed only for humans.
> 
> This mismatch creates one of the biggest blind spots in security today.

## Slide 13
**CI pipeline stores a long-lived Kubernetes admin tokenThe token is shared across environments.It’s stored in a vault or as a GitHub secret.If leaked, the attacker gets broad, persistent cluster access.Rotation is manual and painful.**

- The CI job authenticates using platform-issued identity.The platform issues a short-lived X.509 certificate scoped to specific cluster, specific namespace, or specific roleWhen the job finishes, access disappears automatically as the certificate expires in minutes.
- No standing privilege, no secret rotation overhead, blast radius limited to a single job session, and improved MTTA through automatic, policy-driven access.
- Legacy model:
- Machine identity model:
- How does embracing machine identity work?

> **Notas do apresentador:**
> This comparison shows how deeply flawed the legacy model is for automation.
> 
> Long-lived tokens are essentially permanent access keys.
> 
> The modern model removes that risk by making access temporary and scoped.

## Slide 14
**What is the alternative?**

> **Notas do apresentador:**
> At this point, we’ve identified gaps across all existing approaches.
> 
> The question becomes: what would a unified model look like?
> 
> This sets up the concept of the unified identity layer.

## Slide 15
**The unified identity layer**

- One identity layer for everything.
- A single identity system for humans, machines, services, and AI
- Access is defined and enforced through identity, not credentials or network boundaries
- Acts as the foundation for consistent access across cloud, Kubernetes, and on-prem

> **Notas do apresentador:**
> The key idea is consolidation — one system instead of many disconnected ones.
> 
> Identity becomes the single source of truth for access decisions.
> 
> This simplifies both security and developer experience.

## Slide 16
**From fragmented access to unified identity**

- A key pillar of security platform engineering
- Policy translation layer: Define access once, and the platform maps it across IAM, RBAC, and databases automatically
- One workflow everywhere: Developers authenticate once, and access is consistently handled across AWS, Kubernetes, and on-prem
- No more credential sprawl: Identity dynamically provisions short-lived access instead of distributing secrets
- The unified identity layer becomes a control plane of your Internal Developer Platform, embedding secure-by-design access into platform engineering so every interaction is governed by default.

> **Notas do apresentador:**
> This is where platform engineering becomes the enabler.
> 
> The platform translates intent into enforcement across systems.
> 
> Developers don’t think about access anymore — it just works.

## Slide 17
**With a unified identity layer:**

- Separate IAM, RBAC, and database users → One identity layer
- Static credentials and secrets → Short-lived, identity-based access
- Different workflows per system → One consistent access model
- Human vs machine access → One unified identity system

> **Notas do apresentador:**
> This slide shows the practical impact of that shift.
> 
> Complexity is removed not by adding tools, but by abstracting them.
> 
> The result is consistency across environments and identity types.

## Slide 18
**Take a few minutes to reflect on your**

- own organization.
- How do you currently handle identities for automated systems?
- Do your machines share static credentials or possess verifiable identities?
- ?

## Slide 19
**In conclusion**

- Infrastructure access isn’t a single tool problem
- Treat identity as a platform capability, and design it into your Internal Developer Platform from day one.
- Move from standing privileges to trust that expires by default.
- Unify IAM, network, privilege, and resource access behind a single access plane.
- Design golden paths so secure access is automatic and seamless for humans and machines.

> **Notas do apresentador:**
> The key takeaway is that access is not a single-tool problem.
> 
> It’s a system design problem that needs a platform-level solution.
> 
> Identity becomes the unifying layer across all access controls.

## Slide 20
**Quick recap + agenda**

- Comparing access control paradigms: IAM, PAM, ZTNA, and Infrastructure Identity.
- Identity-centric authentication: short-lived certificates vs. static credentials.
- Unifying access across cloud, Kubernetes, databases, and internal services.
- Role of machine and service identities in zero-trust ecosystems.
- What we covered in Module 3
- Core components of zero trust for infrastructure: identity, authorization, audit.
- Implementing least privilege and just-in-time access in practice.
- Integrating access workflows into IDPs, CI/CD, and developer self-service portals.
- Automating policy enforcement and audit through code and APIs.
- What we will cover in Module 4
- With security platform engineering, vulnerability management goes from manuel toil to automated breeze.
