# Module 2: The operational realities of modernization

## Slide 1
**The operational realities of modernization**

- DEVOPS MODERNIZATION FOR PLATFORM ENGINEERS
- MODULE
- 02

> **Presenter notes:**
> Welcome to Module 2: The Operational Realities of Modernization. In Module 1, we talked about what modernization is — and isn't. Now we're getting into what it actually costs when it goes wrong. Financially, operationally, and humanly. Fair warning: some of this will feel familiar. That's not a coincidence.

## Slide 2
**The invoice arrives**

> **Presenter notes:**
> This section is called 'The Invoice Arrives.' Which is a polite way of saying: let's talk about what you're actually paying for — including the stuff that never made it into the original business case.

## Slide 3
**The sunk cost fallacy**

- Remember the “migration mirage”?
- The most dangerous cost is the budget burned on unfinished projects.
- 37% of organizations lost >25% of migration budget to abandoned initiatives.
- Average project runs 18% over budget ($315k wasted avg).
- In this course, you’ll learn how to avoid typical failure points and make the right decisions as a C-level, VP, or Director leader.

> **Presenter notes:**
> Here's where it gets psychologically uncomfortable. The sunk cost fallacy in migration looks like this: you've already spent $800K, the project is behind, and nobody wants to be the person who calls it. So you keep going — spending more to protect what you've already spent. According to a 2025 survey of DevOps and IT Leaders, 37% of organizations lost more than a quarter of their migration budget to abandoned initiatives. The iceberg diagram show the reality: license costs are the tip. What's underwater is abandoned layers, abandoned work, retraining costs, and dual-running environments where you're paying for both the old and new system simultaneously. Nobody budgets for that last one.

## Slide 4
**The innovation freeze**

- “While you focus on migration, you are not innovating. 61% of teams delay new initiatives for six months or more after a migration, creating an ‘innovation freeze’ where competitors keep shipping while you’re still fixing pipelines. The gap widens into real business consequences… missed revenue and delayed market entry.”

> **Presenter notes:**
> This chart is deceptively simple and genuinely alarming. Line A is your competitor, shipping features throughout your migration. Line B is you, in migration paralysis. 61% of teams delay new initiatives for six months or more after a migration. Six months. That's not a sprint delay — that's a market position problem. The feature gap isn't just an engineering metric; it's missed revenue and delayed market entry. Your competitors didn't pause their roadmap while you were fixing pipelines.

## Slide 5
**Cognitive load into**

- burnout…
- 'Migrations often dump complexity onto developers. - “You build it, you run it' often becomes 'You fix the platform'.
- Instead of abstracting complexity, migrations often just hand developers a new tool.
- Context switching kills flow and velocity. Debugging a migrated pipeline doesn’t just cost 15 minutes — it costs the 20+ minutes it takes to regain focus.

> **Presenter notes:**
> I love that this slide has a meme on it, because honestly it earns one. The dynamic it's capturing is real: migrations often promise to simplify things but instead just hand developers a new tool on top of everything else. 'You build it, you run it' becomes 'you build it, you run it, and you also debug why the migration broke it at 11pm.' Context switching is the silent killer here — debugging a broken pipeline doesn't cost 15 minutes, it costs the 20-plus minutes it takes your brain to get back into flow state afterward. Multiply that across a team, across months - that’s a lot of wasted time and effort.

## Slide 6
**Burnout is the mind killer**

- As cognitive load increases, and teams burnout - their pace of innovation, and overall productivity collapses.
- Struggling devs are less productive
- 70% reported increased developer burnout during migrations.
- Tired engineers cut corners and skip validation. The result? 40% of teams discovered new security blind spots post migration.
- Burnout is a security risk

> **Presenter notes:**
> 70% of engineers report increased burnout during migrations. And here's the thing that often gets missed in the business case: burnout isn't just a people problem, it's a security problem. Tired engineers cut corners and they skip validation steps. 40% of teams discovered new security blind spots after their migration. The cycle is high pressure → migration fatigue → skipped checks → security blind spots → more pressure. You can't security-audit your way out of a culture of exhaustion.

## Slide 7
**The myth of consolidation**

- Standardizing into a platform is the goal. But it does not work by default. Just “migrating” isn’t enough.
- 74% reported MORE tool sprawl after consolidation efforts.
- Why? Different teams have different needs.
- The shadow IT paradox: Engineers route around damage and blockers. If the "Standard Tool" blocks them, they spin up "Shadow Tools".
- Result? You not only lose visibility, but governance too

> **Presenter notes:**
> This one stings a little. The whole premise of most migrations is 'fewer tools, less chaos.' Makes sense in theory. In practice, 74% of organizations reported more tool sprawl after consolidation efforts. Why? Because the standard tool doesn't actually serve everyone's needs, so teams route around it. They spin up shadow tools. And now you have the official tool and the unofficial ones, and you have zero visibility into the unofficial ones. You haven't consolidated — you've just lost governance over the parts you can't see.

## Slide 8
**The pivot: Evolutionary modernization**

> **Presenter notes:**
> Okay — enough doom. Let's talk about what actually works. This next section is the pivot to evolutionary modernization, which is a fundamentally different mental model than what most migration plans are built on.

## Slide 9
**The pivot: Evolutionary modernization**

- Stop trying to reach a 'Final State'.
- Build for constant evolution and change.
- Strategy: Interoperability over Uniformity.
- Migration (finite project)
- Modernization (Infinite Capability)

> **Presenter notes:**
> The pyramids versus the tree. Migrations are treated like construction projects — there's a blueprint, a deadline, a 'final state.' But software systems don't work that way. They need to adapt. They need to live. The three principles here are worth writing down: stop chasing a final state, build for constant evolution, and choose interoperability over uniformity. That last one is the hardest cultural shift — especially for teams that have been told standardization is the goal. Interoperability is the new standardization.

## Slide 10
**Strategy 1: The Strangler Fig Pattern**

- Don't kill the legacy system right away. Wrap it.
- Isolate legacy components.
- Route traffic and logic to a new control plane around it.
- Embrace progressive migratio and replace piece-by-piece only when value is demonstrated. This way you incrementally replace the legacy system.
- Use the Strangler Fig pattern to modernize without a rip-and-replace keeping teams shipping, avoiding rewrites, and reducing burnout during the transition.

> **Presenter notes:**
> Now on to our strategies. The Strangler Fig is one of my favorite patterns — both for the name and for what it actually solves. The idea: don't kill the legacy system. Wrap it. Build a control plane around it, route traffic through the new layer, and replace pieces incrementally only when you've proven the value. The legacy core keeps running while you're modernizing around it. Teams keep shipping. No big bang cutover. No 'all hands on deck migration weekend.' Just steady, measurable progress that you can actually defend in a budget review.

## Slide 11
**Strategy 2: The Control Plane**

- Rather than replace… integrate and abstract!
- Air traffic control: A control plane standardizes “rules of flight” across tools (Jenkins/GitHub Actions/GitLab) without forcing one tool for everyone.
- Interface over tools: Manage the shared interface and policies (e.g., “no prod without a security scan”) consistently across teams and toolchains.
- Visibility first: Instrument everything to see bottlenecks/usage/abandonment, then refactor incrementally with data (avoiding migrating blind).
- This process allows you to achieve the goals of a migration (standardization, security, visibility) without the pain of a migration (burnout, downtime, budget overruns).

> **Presenter notes:**
> For our second strategy, the air traffic control analogy is the right one here. The control plane doesn't dictate which aircraft — or which CI/CD tool — everyone has to use. It sets the rules of flight. 'No prod without a security scan' becomes a policy enforced at the control plane level, not something you hope each team remembers. Visibility first means you instrument everything before you start refactoring — so you're making decisions based on data, not gut feel. This is how you get the outcomes of a migration — standardization, security, visibility — without the pain of one.

## Slide 12
**Take a few minutes to reflect on your own organization.**

- Identify one "Shadow IT" tool your team uses.
- Why do they use it?
- What deficiency in your platform does it solve?
- ?

> **Presenter notes:**
> Take a genuine pause here. Think about your own organization: what's one shadow IT tool your team is using right now? Not theoretically — actually using. And ask yourself why. What gap in the official platform did someone get frustrated enough to work around? The answer to that question is your highest-priority platform engineering backlog item. That's your user research, right there.

## Slide 13
**In conclusion**

- Modernization isn’t migration
- Migration drains budgets, freezes innovation, increases cognitive load and burnout, creates tool sprawl and shadow IT
- The solution for organizations is to
- Evolve, not rip-and-replace, focusing on continuous modernization over “final states”. Measure flow and momentum, not migration percentage. Utilize control plane and platform engineering best practices

> **Presenter notes:**
> And in summary for Module 2: migrations drain budgets, freeze innovation, burn out your best engineers, create tool sprawl, and generate shadow IT. The answer isn't a better migration plan — it's a different approach entirely. Evolve, don't rip-and-replace. Measure flow and momentum, not migration percentage. That last metric shift matters: 'what percentage of teams are migrated' is the wrong question. 'Are teams shipping faster and more safely' is the right one.

## Slide 14
**Quick recap + agenda**

- Financial and operational realities: sunk costs, abandoned migrations, and wasted budget
- Human impact like developer burnout, cognitive overload, and innovation freezes
- The myth of consolidation: why standardizing on fewer tools often increases complexity
- Evolutionary modernization: incremental change that preserves momentum and reduces risk
- What we covered in Module 2
- Platform-as-a-Product: user-centric roadmaps, pilots, and continuous feedback
- Incremental rollout strategies: parallel systems, phased adoption, and minimizing blast radius
- Security continuity: avoiding blind spots and maintaining posture during transitions
- Measuring success: developer velocity, adoption, satisfaction, and business value
- What we will cover in Module 3

> **Presenter notes:**
> Next, Module 3 is where we get hands-on with the roadmap. Platform-as-a-Product, incremental rollout strategies, how to maintain security posture during a transition, and how to measure success in ways that actually land with the business. See you there.
