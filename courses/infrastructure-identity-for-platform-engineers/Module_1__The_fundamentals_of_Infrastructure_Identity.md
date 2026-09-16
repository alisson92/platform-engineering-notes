# Module 1: The fundamentals of Infrastructure Identity

## Slide 1
**The fundamentals of Infrastructure Identity**

- INFRASTRUCTURE IDENTITY FOR PLATFORM ENGINEERS
- MODULE
- 01

> **Notas do apresentador:**
> This module is about reframing how we think about access — not as configuration, but as identity.
> 
> Infrastructure identity is emerging as a foundational layer in platform engineering, not just a security concern.
> 
> The goal is to give you a mental model you can actually apply in your platform design.

## Slide 2
**Chris De La Garza**

- Who we are?

> **Notas do apresentador:**
> My name is Michele Mancioppi, and I have spent most of my career monitoring distributed systems and building observability tooling.

## Slide 3
**Our focus inthis course**

- Together, we will break down how the realm of Infrastructure Identify fits into the platform engineering story - it’s importance, it’s challenges, and how to approach doing it right as a platform engineer.
- What is infrastructure identify and why does it matter?
- How platform engineering can drive Infrastructure Identity as a new paradigm, shifting security toward a model where every entity from hardware to AI is authenticated and authorized based on real-time needs.
- How Infrastructure Identity intersects with platform engineering

> **Notas do apresentador:**
> Infrastructure identity sits right at the intersection of developer experience and security.
> 
> The shift we’re talking about is from static, predefined access to dynamic, identity-driven access.
> 
> This is becoming unavoidable as systems scale and automation increases.

## Slide 4
**By the end of this course**

- You’ll have everything you need to:
- Understand why identity compromise and secret sprawl are the root causes of modern infrastructure breaches.
- Design and implement a unified Infrastructure Identity model that covers humans, machines, workloads, and AI agents.
- Use platform engineering to eliminate static credentials by applying cryptographic identities, zero-trust principles, and short-lived, just-in-time access at scale.
- A single data breach now costs organizations on average more than $4.4 million globally. A secret anywhere in the environment is a vulnerability.

> **Notas do apresentador:**
> The key takeaway is that secrets and credentials are the root of most infrastructure risk.
> 
> This isn’t just about improving security — it’s about enabling safer automation at scale.
> 
> Platform teams are uniquely positioned to solve this because they own the developer interface.

## Slide 5
**Introduction to Infrastructure Identity**

> **Notas do apresentador:**
> So, time to dive in. What is this “Observability” that we hear so much about?

## Slide 6
**We scaled our infrastructure,**

- but not our access.
- Compute evolved from static servers to dynamic, autoscaling clusters.Access controls remain stuck on 1990s primitives: passwords and static SSH keys.Manual provisioning cannot keep pace with automated workflows.

> **Notas do apresentador:**
> We’ve modernized compute, but access models are still stuck in the past.
> 
> This mismatch is one of the biggest hidden sources of friction in modern engineering.
> 
> It’s also why security controls often feel like they slow teams down instead of helping them

## Slide 7
**The reality of the engineers daily grind**

- Fragmented access across the stack with different access paths for everything.
- Imagine how many different access paths across a standard setup of AWS, Kubernetes, Postgres etc
- At the same time, context switching destroys engineering flow.
- While "It works on my machine, but I can't connect to staging.” hits everyone
- Engineers are juggling too many tools just to do their jobs. The cognitive load & friction grow increasingly, with parallel growth in security risks from bad actors.

> **Notas do apresentador:**
> Engineers don’t think in terms of “access systems” — they just feel the friction.
> 
> Every additional tool or access path increases both cognitive load and risk.
> 
> This is where platform engineering should step in: simplifying, not adding complexity.

## Slide 8
**Friction breeds shadow IT**

- Increasingly complicated setups (and load on developers) has massively increased the chance of data breaches.
- Security mandates without thought around usability results in bypassed controls.
- As friction increase,  shared team keys and backdoors grow more and more frequently.

> **Notas do apresentador:**
> When systems are hard to use, people don’t follow them — they work around them.
> 
> Shadow IT is not a failure of people, it’s a failure of system design.
> 
> Good platform design reduces the need for workarounds instead of policing them.

## Slide 9
**What is Infrastructure Identity?**

- Identity is the new kingdom key
- 68% of security incidents involve human factors like social engineering and phishing
- 71% increase in stolen credential usage year-over-year,
- 95% of breached assets are servers
- “Infrastructure identity is a modern, Zero Trust security approach that assigns, manages, and cryptographically verifies unique identities for every entity, including humans, machines, software, and AI workloads, within a computing environment.”

> **Notas do apresentador:**
> Identity is becoming the primary control surface for modern infrastructure.
> 
> This extends beyond users — everything becomes an identity: services, workloads, AI.
> 
> The key shift is from “who can access what” to “what identity is verified and trusted.”

## Slide 10
**Zooming in**

- Instead of granting access based on:
- IP addresses
- VPN access
- Network location
- You grant access based on:
- Who you are (human identity)
- What the service is (machine identity)
- Short-lived cryptographic credentials
- Strong authentication + authorization policies

> **Notas do apresentador:**
> Traditional access is location-based — identity-based access is context-aware.
> 
> This is a fundamental shift from perimeter security to zero trust.
> 
> It allows access decisions to be made dynamically, not preconfigured.

## Slide 11
**Why does Infrastructure Identity matter?**

- Infrastructure Identity extends trust beyond user login, bringing cryptographic trust to the basement, not just the front door.
- It bridges the gap between Identity Providers and the infrastructure layer (compute, clusters, databases, and internal services).
- Instead of relying on static credentials or standing privileges, it enables verified, short-lived, identity-based access to infrastructure resources.
- Every static secret in your environment is a live vulnerability that rotating or encrypting only delays.
- It’s a platform engineers’ job to ensure Infrastructure Identity is a first-class part of the platform.

> **Notas do apresentador:**
> Infrastructure identity brings trust deeper into the system — not just at login.
> 
> It closes the gap between identity providers and actual infrastructure resources.
> 
> Most importantly, it replaces static risk with dynamic, verifiable access.

## Slide 12
**The danger of standing privileges**

- Long-lived API keys, SSH keys, and tokens sit idle but active.
- Compromised credentials drive the majority of infrastructure breaches.
- If a secret exists, it can be leaked, stolen, or misconfigured.
- The mere existence of a secret is a risk.

> **Notas do apresentador:**
> The biggest risk isn’t active attackers — it’s dormant credentials waiting to be abused.
> 
> Long-lived access creates invisible risk that accumulates over time.
> 
> Eliminating standing privileges is one of the highest-leverage security improvements.

## Slide 13
**Why should platform engineers own this?**

> **Notas do apresentador:**
> Platform engineers define how developers interact with infrastructure.
> 
> That means they implicitly define how access works across the organization.
> 
> This makes identity a platform concern, not just a security one.

## Slide 14
**What is security platform engineering?**

- Security platform engineering is the branch of platform engineering that focuses on embedding security directly into the Internal Developer Platform (IDP).
- Rather than shifting security left onto developers, security platform engineering focuses on shifting security policies, guardrails, and best practices down into the platform itself.
- Security is increasingly the domain of the platform engineer. Infrastructure identity is no different.
- Identity now underpins access to infrastructure, workloads, and automation. It directly shapes developer experience, security, and self-service. Security defines policy, but platform operationalizes identity as part of the internal developer platform.
- Infrastructure identify is a platform engineers domain

> **Notas do apresentador:**
> Instead of shifting security responsibility to developers, we embed it into the platform.
> 
> This is about making the secure path the default path.
> 
> Identity becomes a core part of that platform abstraction layer.

## Slide 15
**7 reasons platform teams needto own Infra Identity**

- Infrastructure identity is no longer “just security”
- 1
- Platform Engineering owns the developer contract
- 2
- Identity is one of the highest cognitive load creators  in orgs
- 3
- Identity affects workload design
- 4
- AI and automation make all this unavoidable!
- 5
- Aligns security with velocity
- 6
- Key driver of a secure-by-design system!
- 7

> **Notas do apresentador:**
> Identity is one of the biggest contributors to cognitive load in engineering teams.
> 
> As automation and AI increase, identity complexity becomes unavoidable.
> 
> Owning identity is how platform teams align security with velocity.

## Slide 16
**In conclusion**

- The old security operating model isn’t good enough.
- Static credentials, VPNs, and network-based controls drain budgets, slow teams down, increase cognitive load, and create access sprawl and shadow admin which means RISK.
- The solution for organizations is to:
- Evolve toward infrastructure identity continuously modernizing how humans, workloads, and automation authenticate.
- Embrace security by design.

> **Notas do apresentador:**
> The traditional model fails because it relies on static, manual controls.
> 
> Infrastructure identity enables continuous, dynamic access instead.
> 
> This is ultimately about moving toward secure-by-design systems.

## Slide 17
**Take a few minutes to reflect on your**

- own organization.
- Where does access friction show up most in your tear team's daily workflows?
- What "shadow workarounds" have people created to bypass it?
- ?

## Slide 18
**Quick recap + agenda**

- What is Infrastructure Identity?
- Why does it matter?
- Why platform engineers, not just security teams, own the access experience.
- The evolution of access control: from SSH keys and VPNs to cryptographic identity.
- What we covered in Module 1
- Hidden costs of traditional access models: operational overhead, breach risk, and compliance friction.
- The silo effect: how disparate IAM, PAM, and secret managers slow engineering teams
- How reactive access models create audit and compliance burdens.
- Quantifying the impact: mean time to access (MTTA) and its effect on velocity.
- What we will cover in Module 2

> **Notas do apresentador:**
> We’ve established the problem: fragmented access, secrets, and risk.
> 
> We’ve introduced the solution: identity as the foundation of access.
> 
> Next, we’ll go deeper into implementation and practical patterns.
