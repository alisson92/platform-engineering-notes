# Module 4: Implementing Unified Identity in Infrastructure

## Slide 1
**Implementing Unified Identity in Infrastructure**

- INFRASTRUCTURE IDENTITY FOR PLATFORM ENGINEERS
- MODULE
- 04

## Slide 2
**Zero Trust for infrastructure**

- + platform engineering

> **Presenter notes:**
> Clarify: Zero Trust isn’t new—but applying it to infrastructure is still immature in most orgs.
> 
> Tie to platform engineering: platforms are now the enforcement layer for Zero Trust.
> 
> Key idea: developers shouldn’t feel security friction—platform should abstract it.

## Slide 3
**The three pillars in practice**

- Non-negotiables for infrastructure Zero Trust
- Identity: Cryptographically verifying who or what is requesting access
- Authorisation: Evaluating context (device, health, on-call status) before granting
- Audit: Recording every action tied back to the verified identity
- Identity
- Authorisation
- Audit

> **Presenter notes:**
> Anchor this: these are non-negotiables, not best practices.
> 
> Identity: stress cryptographic identity → no more “network = trust.”
> 
> Authorization: highlight dynamic context (on-call, device posture, etc.)—this is where most orgs fail.
> 
> Audit: make it clear—if you can’t tie actions to identity, you don’t have Zero Trust.
> 
> Connect the three: identity without audit = blind; authorization without identity = meaningless.

## Slide 4
**Just-in-Time (JIT) Access in practice**

- Automated
- validation.
- Request
- Context check
- Auto
- expiration
- Just-in-Time Access
- Developer asks for
- specific access.
- Cert issued
- Access revoked
- instantly.
- Short-lived
- credential.
- Repeat
- (This applies wherever it’s humans or machines asking for access)

> **Presenter notes:**
> Walk through the flow like a story: request → validation → access → automatic removal.
> 
> Emphasize: access is temporary by design, not manually revoked.
> 
> Key mindset shift: access is granted per action, not pre-provisioned.
> 
> Call out: this applies equally to humans and machines—this is often overlooked.

## Slide 5
**Secure workflows, not ChatOps**

- Let devs initiate access from the tools they already use, but ensure that approval and enforcement happens in a controlled, identity-centric system governed by policy and short-lived credentials.Result: Prevents accidental 'emoji approvals' and maintains audit integrity.

> **Presenter notes:**
> This is a subtle but important point: convenience vs control.
> 
> Developers can initiate in Slack—but decisions shouldn’t happen there.
> 
> Highlight real-world failure mode: “someone approved prod access with an emoji.”
> 
> Core idea: separate UX from enforcement.
> 
> Reinforce: identity-centric systems preserve audit and policy integrity.

## Slide 6
**Infra Identity via developer portal**

- Access as a seamless self-service feature
- Click 'Debug Prod DB'
- API checks PagerDuty for on-call status.
- 1-hour cryptographic
- certificate issued in
- background.
- Secure terminal
- opens in browser.

> **Presenter notes:**
> This is the “golden path” experience.
> 
> Frame it as: security becomes invisible when done right.
> 
> Walk through the example:
> 
> Dev clicks → system checks context → cert issued → access granted.
> 
> Highlight: no tickets, no waiting, no manual approval loops.
> 
> This is how you scale secure access without slowing developers down.

## Slide 7
**Infrastructure-as-Code (laC) for Identity**

- When a new microservice is spun up, the platform automatically provisions the workload identity and access rules.
- Access policies are defined as code (e.g., role, TTL, permissions) and version-controlled alongside application code.
- Changes are committed to Git and validated through CI/CD, just like any other infrastructure change.
- Once approved and deployed, the platform enforces time-bound, policy-driven access automatically at the resource level.

> **Presenter notes:**
> Make the connection: identity should follow the same lifecycle as infrastructure.
> 
> Policies are not configs—they are code artifacts.
> 
> Emphasize benefits:
> 
> Version control = auditability
> 
> CI/CD = validation
> 
> Automation = consistency
> 
> Key takeaway: access is no longer “granted”—it’s declared and enforced.

## Slide 8
**The ultimate**

- audit trail
- We don't just log IPs. We log people (& machines) and actions.
- The "flight recorder" for platform ops.
- From…
- Legacy Log: IP 10.0.0.5 executed a command ❌To…
- Modern Log: Jane Doe (prod-db-admin, 1h TTL), verified via Okta on trusted Mac, ran DROP TABLE ✅

> **Presenter notes:**
> This is where Zero Trust proves its value.
> 
> Contrast old vs new:
> 
> Old: IP-based logs → useless for accountability
> 
> New: identity-rich logs → full traceability
> 
> Call it the “flight recorder” for infrastructure.
> 
> Important: audit is not just for compliance—it’s for debugging and trust.

## Slide 9
**Take a few minutes to reflect on your**

- own organization.
- What would it take to implement a 'zero standing privileges' rule for your production clusters by year-end?
- How could you embed access requests directly into your current developer portal?
- ?

> **Presenter notes:**
> Pause intentionally—this is where the audience internalizes.
> 
> Encourage them to think practically:
> 
> What would break if we removed standing access?
> 
> Where would friction show up?
> 
> Push them to connect this to their current platform maturity.

## Slide 10
**In conclusion**

- Infrastructure access isn’t a tooling decision, it’s an operating model shift.
- Make identity the control plane of your platform
- Default to verification and expiration, not static trust and manual approvals.
- Move from fragmented access layers into one unified, policy-driven identity layer.
- Turn secure access into a product experience… fast, observable, and measurable

> **Presenter notes:**
> Reinforce the big idea: this is not a tooling problem—it’s an operating model shift.
> 
> Highlight the transformation:
> 
> From static → dynamic
> 
> From fragmented → unified
> 
> Emphasize “identity as control plane”—this is the core mental model.
> 
> Close with: secure access should feel like a product experience, not a gate.

## Slide 11
**Next steps?**

## Slide 12
**Map the automation**

- [Portal UI Trigger ]
- [Platform API Context Check]
- [Cert Issued + TTL]
- Design your platform workflow
- Identify one highly sensitive resource (e.g., Prod Customer DB).
- Design the flow: How is it triggered? Who validates context?
- Define the Time-to-Live (TTL).
- [Audit Destination ]
- If you can’t draw this workflow, you don’t control your access model.

> **Presenter notes:**
> This is the most practical slide—slow down here.
> 
> Encourage them to actually map this after the session.
> 
> Stress: if you can’t draw your access flow, you don’t understand it.
> 
> Highlight each component:
> 
> Trigger → context → credential → audit
> 
> This is essentially designing your access supply chain.

## Slide 13
**The journey forward**

- You now have the blueprint for modern infrastructure identity.
- Make your computing trustworthy.
- Start Small: Target one legacy VPN or standing privilege and replace it via your IDP.
- Remember to measure (MTTA, eNPS, velocity) and establish your baseline. Use the improvement data to prove your value and expand your journey!
- Remember! Modern infrastructure identity isn’t a security upgrade, it’s a platform evolution. Start small, replace standing trust with expiring identity, measure the impact, and turn secure access into a core capability of your IDP

> **Presenter notes:**
> Reduce overwhelm: you don’t need to transform everything at once.
> 
> Suggest a starting point: replace one risky pattern (VPN, long-lived creds).
> 
> Emphasize measurement:
> 
> MTTA (Mean Time to Access)
> 
> Dev satisfaction
> 
> Delivery speed
> 
> Key idea: prove value → expand adoption.

## Slide 14
**What we learned**

- Infrastructure identity is a platform capability, not just security
- Legacy access models create friction, toil, and hidden risk
- Static secrets and standing privilege are the real vulnerabilities
- Identity must cover humans and machines equally
- Just-in-Time, short-lived credentials reduce blast radius
- Mean Time to Access (MTTA) is the metric that matters
- IAM, ZTNA, PAM, and Infra Identity must be unified
- The unified access plane becomes the control tower of the IDP
- Zero Trust succeeds when secure access becomes the golden path

> **Presenter notes:**
> Don’t read the list—summarize themes:
> 
> Identity is the foundation of modern platforms
> 
> Standing access is the core risk
> 
> Short-lived access is the solution
> 
> Highlight MTTA as a business metric, not just technical.
> 
> Close with a strong line:
> 
> “Zero Trust works when the secure path is the easiest path.”
