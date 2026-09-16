# Module 2: The cost of legacy access

## Slide 1
**The cost of legacy access**

- INFRASTRUCTURE IDENTITY FOR PLATFORM ENGINEERS
- MODULE
- 02

## Slide 2
**Why outdated architectures kill velocity and increase risk.**

> **Presenter notes:**
> Most teams think their bottlenecks are in CI/CD or infra — but it’s actually access.
> 
> Legacy access models weren’t designed for cloud-native, distributed systems.
> 
> This mismatch is what creates both friction and risk at the same time.

## Slide 3
**Access is the ultimate bottleneck.**

- Engineering teams optimize for deployment speed.
- Access requests still rely on IT tickets and manual approvals.
- The flow state breaks the moment an engineer hits a "permission denied" error.
- Teams overwhelming build fast, but are forced to wait to deploy.

> **Presenter notes:**
> We’ve optimized everything in the pipeline — except the moment access is required.
> 
> That “permission denied” moment is where modern systems fall back to legacy processes.
> 
> This is why fast teams still feel slow when it matters most.

## Slide 4
**The perimeter is a myth**

- VPNs grant broad networks, not specific resources.
- VPNs connect users to entire networks, ignoring the principle of least privilege.
- Legacy VPNs do not scale with distributed architectures.
- Once inside the perimeter, lateral movement is extremely easy. Massively increasing the negative impact of a increasingly common breaches.
- Perimeter-based security is outdated! Broad VPN access increases risk and limits scale, while Identity-based access enforces least privilege, reduces lateral movement, and fits modern distributed systems far more effectively.

> **Presenter notes:**
> The idea of a trusted internal network no longer holds in distributed systems.
> 
> VPNs solve connectivity, not security — they expand access instead of narrowing it.
> 
> Once inside, the system assumes trust, which is exactly the problem.

## Slide 5
**At the same time…**

- Teams are managing too many fragmented access planes. E.g.
- AWS has IAM
- Kubernetes has RBAC
- Postgres has local users
- And many many more examples
- Platform teams must maintain multiple, disconnected control planes.
- This fragmentation guarantees inconsistent security policies.

> **Presenter notes:**
> Every system reinvented access control — and now we have to manage all of them.
> 
> This fragmentation isn’t just annoying — it guarantees inconsistency.
> 
> Platform teams end up stitching together policies that were never meant to align.

## Slide 6
**Standing privileges = maximum risk.**

- What happens when 'always on' goes wrong?
- Static secrets dramatically increase the blast radius of a breach.
- If a developer is compromised, everything they have access to is compromised.
- You need just-in-time access, not just-in-case access.

> **Presenter notes:**
> The real danger isn’t access — it’s persistent access.
> 
> Long-lived credentials silently accumulate risk over time.
> 
> The longer something exists, the more likely it is to be misused or leaked

## Slide 7
**Remember this?**

- When official processes are too slow, teams create backdoors. Shared service accounts and locally stored keys proliferate and shadow access completely bypasses zero-trust governance.

> **Presenter notes:**
> When systems slow people down, people route around them — always.
> 
> Shadow access isn’t malicious, it’s a response to bad UX.
> 
> This is where security completely loses visibility and control.

## Slide 8
**Calculating the true cost**

- Productivity lost
- Engineering hours spent waiting, rather than actually delivering value - worse, their flow state is continually interrupted driving unproductive work.
- Ops toil
- Risk exposure
- It’s crucial to understand that the “cost” of your security practice is not just the salaries of your engineers, and your software license bill. It’s increasingly the cost of wasted time, and increased risk exposure!
- 02
- 03
- Platform or Ops team spend hours provisioning manually. These are often some of your most expensive employees spending time on manual toil!
- The financial (and reputation) impact of an easily preventable breach is massive, and growing more massive every year.
- 01

> **Presenter notes:**
> The biggest cost isn’t tools — it’s wasted engineering time.
> 
> Highly paid engineers end up waiting or doing manual access work.
> 
> And at the same time, risk is increasing in the background.

## Slide 9
**How it should be**

> **Presenter notes:**
> As our systems grow, so does the complexity of keeping them observable.
> Manual instrumentation — where every developer has to add their own telemetry code — simply doesn’t scale. Not only is it labor-intensive, but when every team defines telemetry differently, you end up with blind spots, noisy data, and duplication.
> This is why observability has to be treated as a platform capability, not an afterthought. We need automation to reduce toil, standards to ensure consistency, and sensible defaults so teams get a working baseline without any extra setup. This approach is what allows observability to grow with your platform — not become a bottleneck.

## Slide 10
**Quantify the wait:**

- Mean Time to Access (MTTA)
- MTTA measures the time from request to active session.
- High MTTA frustrates engineers and delays incident response.
- Every minute spent waiting is a minute not shipping.

## Slide 11
**Trust that expires by default: Just-In-Time Access**

- Neutralising credential theft:
- Certificates are issued just-in-time.
- Expiry in minutes or hours, not months.
- No static secrets to rotate or commit to GitHub.
- Stolen expired certificates are useless.

> **Presenter notes:**
> The goal is not to remove access, but to make it temporary and contextual.
> 
> Access should exist only when needed — and disappear automatically.
> 
> This dramatically reduces the window of opportunity for attackers.

## Slide 12
**From "what you hold" to “who you are”**

- Replacing secrets with cryptographic verification.
- Legacy: What secret do you hold?
- Modern: Who are you?
- AI makes this even more important! You in this context can be humans, or machines.
- Identity cannot be easily exfiltrated like a password could, modern access is tied to SSO and cryptographic verification.

> **Presenter notes:**
> Secrets are transferable — identity is not.
> 
> This is the fundamental shift: from possession-based to identity-based access.
> 
> It’s also what makes modern systems more resilient to leaks and breaches.

## Slide 13
**Machines are users too.**

- The silent majority.
- Scale: Microservices and scripts outnumber human engineers.
- The Risk: Shared root credentials among workloads are massive vulnerabilities.
- The Fix: Machine workloads require dynamic, verifiable cryptographic identities.
- “Machine identities (services, containers, automation) now outnumber human identities by up to 100:1 in modern enterprises.” (Gartner estimate on machine identity growth)

> **Presenter notes:**
> Most access today is not human — it’s workloads talking to each other.
> 
> But we still treat machine identity as an afterthought.
> 
> This creates massive blind spots in security and governance.

## Slide 14
**How does all this come together?**

- Platform engineers define a unified identity layer built directly into the platform, used by developers, services, machines, and AI.
- This replaces static secrets and fragmented trust models with dynamic, identity-based access across the stack.
- The result is a platform that is secure by design, with consistent access control for both humans and non-human identities.
- Infrastructure Identity is not just a security upgrade, but a technical and cultural upgrade as well.

> **Presenter notes:**
> This is where platform engineering becomes critical.
> 
> Identity isn’t a tool — it’s something you embed into the platform itself.
> 
> When done right, security becomes invisible and automatic.

## Slide 15
**These changes will improve your MTTA!**

- Short-lived, just-in-time credentials removes manual approvals & static key provisioning, reducing time from request to active session massively!
- Identity-based access replaces fragmented control planes with unified, policy-driven authentication, eliminating ticket queues and access drift
- Treating humans and machines as first-class identities enables automated, self-service access — accelerating incident response and restoring developer flow

> **Presenter notes:**
> Auto-instrumentation is one of the fastest ways to achieve coverage across your services without asking developers to modify their code. With OpenTelemetry, you can deploy language-specific agents — for example, Java, Python, Node.js — that automatically capture telemetry from frameworks, libraries, and runtimes.
> In Kubernetes, the OpenTelemetry Operator takes this further by allowing us to inject these agents automatically via annotations. That means platform engineers can turn on observability for an entire workload fleet just by updating deployment manifests — no code changes required.
> This approach is perfect for quickly onboarding teams to a consistent telemetry setup, ensuring data starts flowing early, and then layering in manual instrumentation later for more business context.

## Slide 16
**Infra Identity as a platform ROI driver!**

- Measure MTTA
- Gauge your current access setup and establish your baseline. Understand the time wasted, then calculate:
- Time wasted x avg dev cost = $$$
- Adopt Infra Identity
- Measure MTTA again!
- You could also measure deployment velocity, or eNPS as part of this “simple” 3 step approach to proving the value of your platform initiative via Infra identity!
- 02
- 03
- Implement just-in-time access, policy-as-code enforcement, and a unified identity control plane across your infrastructure (for both people, and machines!).
- Gauge your new access setup, and compare the new numbers to your baseline.
- How much time has been saved?
- 01

> **Presenter notes:**
> This gives you a way to justify platform investments in business terms.
> 
> Time saved translates directly into money saved.
> 
> And reduced risk is often even more valuable, even if harder to quantify.

## Slide 17
**In conclusion**

- The legacy access model is the real bottleneck. The solution for modern platform teams is to:
- Replace static secrets and network trust with short-lived, identity-based access for both humans and machines.
- Build infrastructure identity directly into the platform, making secure, just-in-time access the default, not the exception.
- Measure what matters. Reduce MTTA, restore developer flow, and prove platform ROI through saved time and reduced risk.

> **Presenter notes:**
> To wrap up this module: common vulnerabilities and exposures cost organizations millions in direct impact and in engineering time. 
> The naive approach, which is endless manual remediation, doesn’t scale and it burns out some of your most experienced engineers.
> What we want instead is to shift vulnerability management down into the platform and build systems that are secure by design.
> In the next modules, we’ll dig into what that looks like in practice and how you, as a platform engineer, can help drive that change.

## Slide 18
**Take a few minutes to reflect on your**

- own organization.
- If you mapped out the steps required for a new engineer to get production database access today... How many handoffs and tools are involved?
- ?

## Slide 19
**Quick recap + agenda**

- Hidden costs of traditional access models: operational overhead, breach risk, and compliance friction.
- How reactive legacy access models create audit and compliance burdens.
- Quantifying the impact: mean time to access (MTTA) and its effect on velocity.
- What platform engineers need to do to improve things
- What we covered in Module 2
- Comparing access control paradigms: IAM, PAM, ZTNA, and Infrastructure Identity.
- Identity-centric authentication: short-lived certificates vs. static credentials.
- Unifying access across cloud, Kubernetes, databases, and internal services.
- Role of machine and service identities in zero-trust ecosystems.
- What we will cover in Module 3
