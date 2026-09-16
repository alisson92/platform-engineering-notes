# Module 3: What does sustainable modernization look like?

## Slide 1
**What does sustainable modernization look like?**

- DEVOPS MODERNIZATION FOR PLATFORM ENGINEERS
- MODULE
- 03

> **Presenter notes:**
> Welcome to Module 3: What does sustainable modernization actually look like? We've spent two modules on the problem — the costs, the failures, the patterns that don't work. This module is where we flip it. We're going to talk about the operating model, the strategies, and the metrics that make modernization actually stick. Let's get into it."

## Slide 2
**The mindset shift**

> **Presenter notes:**
> Before we get into tactics, we need to address something more fundamental — a mindset shift that has to happen before any of the strategies we'll cover will stick. Because you can have the right tools and the wrong mental model, and you'll still end up with the same expensive mess we covered in Modules 1 and 2. The good news is this shift isn't complicated. It just requires letting go of something most engineering organizations have been doing for a long time."

## Slide 3
**The project vs. product trap**

- Migrations fail when they are treated as finite projects with arbitrary end dates. Sustainable modernization needs to be habit, not deadline.
- This doesn’t mean not adding target dates… products have targets, and sprints. It means not saying “This all ends on XYZ date, and then move on”

> **Presenter notes:**
> Here's the core problem. Most modernization initiatives are set up as projects — there's a blueprint, a budget, a deadline, and a definition of 'done.' Finish migration by Q4. And the moment Q4 arrives, whether you're actually done or not, the attention moves on.
> The team disperses. The budget closes. And whatever state the platform is in at that moment becomes the new legacy system you'll be modernizing in three years.
> The infinity loop on the right is the alternative: reduce friction continuously. That's not a vague aspiration — it's a fundamentally different operating model with different incentives, different team structures, and different success metrics.
> To be clear, this doesn't mean no deadlines. Products have sprints and target dates. It means you don't declare victory and walk away. Modernization isn't a destination — it's a practice.

## Slide 4
**Platform-as-a-Product (PaaP) defined**

- A key pillar of platform engineering
- Ownership: Instead of working on a “project” that is finished at a certain time, a platform team treats the platform (in this case the modernization initiative) as their product across the entire product life cycle
- New perspective: Developers using the platform are treated like customers
- Product management basics: User research, user centric design, product roadmap, feedback loops, product marketing, etc.
- This same operating model works for how you think about your modernization plans!

> **Presenter notes:**
> Platform-as-a-Product is the operating model that makes continuous modernization work. Three things shift when you adopt it.
> First, ownership. The platform team owns the modernization initiative the way a product team owns a product — across its full lifecycle, not just to a handoff date. There's no 'we built it, now operations runs it.' The team stays with it.
> Second, perspective. The developers using your platform are your customers. Not your ticket queue, not your internal stakeholders — your customers. That means their experience matters, their friction matters, and their feedback is product input, not noise.
> Third, practice. You apply actual product management disciplines: user research, roadmapping, feedback loops, adoption metrics. For teams that are deeply technical, this can feel foreign. But it's also what separates platforms people actually use from platforms people route around.

## Slide 5
**Platform as a Product**

- Value proposition: Your platform must be as easy to use as developers' preferred tools (Otherwise you get Shadow IT)
- MVP strategy: Build the skateboard, not the cruise ship
- Feedback: Complaints are bug reports, not annoyances to be pushed through or ignored.
- The platform as a product approach is based on defining your mission, doing user research, starting small to allocate internal resources efficiently, then iterating, proving value and marketing your platform internally to secure buy-in.
- Luca GalanteCore Contributor to Platform Engineering Community

> **Presenter notes:**
> Luca Galante, a core contributor to the Platform Engineering community, breaks it down well. You start by defining your mission and doing real user research — not assumptions about what developers need, actual conversations. Then you start small. Build the skateboard before the cruise ship. Prove value with something lightweight before scaling.
> The feedback point is the one I'd really emphasize: complaints are bug reports, not annoyances. When a developer tells you something is painful or confusing, that's the most valuable signal you can get. It tells you exactly where your platform is creating friction instead of removing it. The teams that treat that feedback as product data are the ones that build platforms people voluntarily adopt. And voluntary adoption, as we'll see, is one of the most important metrics you can track.

## Slide 6
**So what does PaaP in modernization entail?**

- You are thinking about your modernization like it’s a product. And the impacted developers are your customers.
- Speak to your developers and understand exactly what their needs, desires and challenges are
- User research
- Build a product roadmap for your modernization with your objective dates, must haves, and future ideas.
- Roadmapping
- Identify your golden paths. The supported, opinionated workflow that create the safe paths of least resistance.
- Golden paths
- The Control Plane connects diverse, messy tools to a unified developer experience giving you breathing room.
- Control plane
- You need to quantify and validate your efforts. Are you moving faster and breaking viewer things?
- Measurement
- By approaching modernization in this way you take a more sustainable, lower risk, and overall faster approach to modernization your CI/CD tooling

> **Presenter notes:**
> Applied to modernization specifically, platform as a product gives you five disciplines working in concert.
> User research — talk to your developers before you build. Understand what's actually slowing them down, what they're working around, and what they wish existed.
> Roadmapping — a living product roadmap with objective dates, must-haves, and future ideas. Not a migration checklist, a product plan.
> Golden paths — opinionated, supported workflows that create the path of least resistance. We'll go deep on these shortly.
> Control plane — the technical layer that connects your tools and gives you visibility and governance without forcing everyone onto a single tool.
> Measurement — quantifying your progress in ways that connect to business outcomes, not just migration completion.
> Remove any one of these and the others weaken. They're designed to work together.

## Slide 7
**Modernization in action**

> **Presenter notes:**
> Okay — let's get practical. This next section is about execution: how you build the roadmap, how you roll things out, how you design golden paths, and how you know it's working. This is the part you can take back to your team on Monday.

## Slide 8
**Building your roadmap: The feedback loop**

> **Presenter notes:**
> This cycle — ship capability, measure usage, gather feedback, refine capability — looks like standard product thinking. And it is. But there's a reason it matters more right now than it ever has before.
> Traditional product development was built on assumptions that no longer hold: requirements fully defined upfront, roadmaps stable across quarters, PM defines and engineering executes. AI breaks all three of those assumptions simultaneously. The solution space isn't fully known when you start. Model behavior is non-deterministic. And the best user experience only emerges through real usage — you can't prototype your way to it in a conference room.
> The shift teams need to make is from 'define, build, validate' to 'define just enough, build, learn, adjust, repeat.' In practice that means aligning on four things: the outcome — why it matters; the context — what the system needs to know; the constraints — what must not be violated; and the feedback loops — how you improve. Everything else becomes lighter weight.
> The biggest risk in the AI era isn't building the wrong thing. It's moving too slowly to learn and adapt. This loop isn't a nice-to-have process improvement. It's the operating model your modernization needs to survive contact with reality.

## Slide 9
**Incremental rollout strategy**

- Avoid the "Big Bang" of a rip and replace. Expand through circles of trust to limit blast radius iterating as you go.
- MVP: 1 Friendly team (high-touch support)
- Beta: 3-5 teams (focus on self-service).
- General availability: Scale (open to all).

> **Presenter notes:**
> This concentric circle model is how you avoid the big bang. You start with one friendly team — people who will give you honest feedback, tolerate rough edges, and won't escalate to your CTO the moment something breaks. You give them high-touch support. That's your pilot.
> Then you expand to 3-5 teams with a focus on self-service, because you can't hold everyone's hand at scale. You're testing whether the platform can stand on its own. That's beta.
> Then you open to everyone. General availability.
> The key concept at every stage is blast radius. If something breaks at pilot, one team is affected and you fix it quietly. Find the same problem post-GA and you're dealing with an org-wide incident. The circles exist to protect you from scaling mistakes.
> In the AI era there's an additional reason to move through these stages deliberately: each ring is a learning loop, not just a risk gate. The pilot gives you real usage data before you bake assumptions into a platform that hundreds of teams will depend on. Don't rush through it.

## Slide 10
**Identify the golden paths for your modernization**

- Definition: An opinionated, supported workflow (e.g., Spring Boot to AWS).
- The Incentive: Use this path, and we handle security, ops, and networking.
- The Freedom: Devs can go off-road, but then they need to bring their own support.

> **Presenter notes:**
> A golden path is an opinionated, supported workflow — the route your platform team has paved, secured, and will maintain. The image here captures it perfectly: a clean road through chaos.
> The incentive structure is what makes it work. Use the golden path, and security, ops, and networking are handled for you. The platform takes care of the things developers don't want to think about. Go off-road, and you can — but you're bringing your own support. That's not a punishment, it's an honest division of responsibility.
> The practical result is that most developers, given a genuine choice between fast-and-supported and custom-and-unsupported, will choose the golden path. And when they do, you get voluntary adoption — which compounds. Teams that adopt early become advocates. Advocates bring other teams. That gravitational pull is far more powerful than mandates.

## Slide 11
**Golden path examples:**

> **Presenter notes:**
> These are three concrete examples that illustrate the range of what golden paths can do.
> The frontend freedom path modernizes the pipeline — security, audit, deployment speed — without touching the application architecture. Developers don't have to rewrite anything. This is evolutionary modernization in its purest form: the platform improves around the team without disrupting their work.
> The serverless API path reduces time-to-hello-world from two days to ten minutes. Write that number down. That is the kind of concrete, defensible outcome that keeps modernization budgets funded.
> The AI-assisted delivery path might be the most important one going forward. Developers are using AI to write code faster than security teams can review it. This path closes that gap by automatically generating tests and performing semantic security review on every commit — before a human ever looks at it. It turns AI from a governance risk into a force multiplier. That's a compelling story for any c-level conversation.

## Slide 12
**Utilize the Control Plane**

- It gives you the technical breathing room you to make long term cultural change.
- Unify your delivery workflows across tools, and reduce sprawl and gain immediate visibility
- Use visibility to guide roadmap, user research creation, and golden paths
- Execute feedback loop
- Measure improvement
- The hardest part of modernization is the necessary cultural change (& the politics) utilising a Control Plane approach connects diverse, messy tools to a unified developer experience immediately, giving you a clear launch point.

> **Presenter notes:**
> Here's the honest framing: the hardest part of modernization isn't the technology — it's the culture and the politics. Getting teams to change how they work, getting leadership to stay patient, getting everyone aligned on a direction that will take longer than one quarter to prove out.
> The control plane gives you a technical quick win to work with while you're doing that harder work. Unify your delivery workflows, gain immediate visibility, reduce sprawl. Those are things you can demonstrate in weeks, not quarters. And demonstrated results are the most effective organizational change tool available.
> Think of the control plane as buying you breathing room. Use it wisely.

## Slide 13
**Release Orchestration as the gateway**

- Decouple the workflow from the tool.
- Swap underlying tools (e.g., Jenkins to GitHub Actions) without breaking the developer experience.
- The Developer just sees the symphony, not the instruments.

> **Presenter notes:**
> The developer experience shouldn't change every time you swap an underlying tool. That sounds obvious, but most organizations are structured in a way where it does — every platform change ripples through to developers, creating retraining costs, friction, and resistance.
> Release orchestration solves this by sitting between developers and the underlying toolchain. The developer sees the symphony — a coherent, consistent workflow. They don't see the instruments. Jenkins, Argo, Snyk, AWS — the orchestrator coordinates all of it and presents a single interface.
> The strategic implication: when you eventually need to move from Jenkins to GitHub Actions, or from Argo to something new, you make that change at the orchestration layer. Developer experience stays intact. No disruption, no retraining, no resistance. That's how you keep modernization moving without burning out the people it's supposed to help

## Slide 14
**Continuous security: Guardrails, not gates**

- Philosophy: Security is the pavement, and not a toll booth.
- Automated triage: Block builds only on critical risks, just warns with others.
- Implementation: "No root access" is a code check, not a slow manual review.

> **Presenter notes:**
> Security is the pavement, not a toll booth. That's the philosophy in one line.
> The traditional model — security review at the end, manual, blocking, slow — doesn't scale. It creates a queue, the queue creates pressure, pressure creates shortcuts, and shortcuts create the blind spots we talked about in Module 2. The 40% of teams that discovered new security issues post-migration? That's what gate-based security produces under stress.
> Automated triage that blocks only on critical risks and warns on everything else keeps developers moving while catching what genuinely matters. 'No root access' as a code check rather than a slow manual review is the implementation of that philosophy. Security that integrates into the workflow doesn't get worked around. Security that blocks the workflow does.

## Slide 15
**Momentum metrics**

- Measure FLOW, not "migration percentage". And prove value incrementally to keep funding.
- How you think about your metrics and goals in modernization is crucial to optimising for actual success.% of apps migrated isn’t the wrong thing to measure if it’s all you can - but your goal is to aim for taking it to the next step, and having a metric that can connect to the objectives of the wider organization.

> **Presenter notes:**
> This slide makes a simple but important distinction. Percentage of apps migrated is an output metric — it tells you how much work you've completed. Time to onboard and deployment frequency are outcome metrics — they tell you whether that work is actually delivering value.
> The distinction matters more in the AI era than it ever has. Teams optimizing for outputs can look busy and make no real progress. Optimizing for outcomes forces you to ask the harder question: is the platform actually making developers faster and more capable?
> Report migration percentage if it's the only thing you have. But make it your goal to connect your metrics to outcomes the business cares about — speed, reliability, developer productivity. That's the conversation that sustains long-term investment.

## Slide 16
**Metrics examples:**

> **Presenter notes:**
> Five metrics that actually capture momentum.
> Time-to-hello-world is your proof metric — if a new developer or migrating team can deploy a standard application to production in two hours instead of two weeks, you have a compelling result even if only 5% of your portfolio has migrated. That number alone can change a budget conversation.
> Deployment frequency is your flow metric. If teams using the modernized platform are shipping significantly faster than teams on legacy, that creates gravitational pull — other teams notice and want in.
> Golden path adoption rate measures voluntary usage. Unlike migration percentage, which can be forced, voluntary adoption proves the platform is genuinely useful. It's your product-market fit signal.
> Developer NPS is your leading indicator for burnout risk. If scores are declining, teams are struggling before it shows up in productivity data. Fix it early.
> Change failure rate is your trust-builder with nervous stakeholders. Show that the new platform breaks less than the old one. That's how you keep the political capital to keep going."

## Slide 17
**Take a few minutes to reflect on your own organization**

- Describe your 'Ideal Golden Path' in 3 sentences.
- What is the single biggest hurdle preventing you from building it today?
- ?

> **Presenter notes:**
> Two questions worth sitting with genuinely, not just rhetorically.
> First: describe your ideal golden path in three sentences. Not the one you have, the one you want — the workflow that, if you could build it, would make the biggest difference to your developers tomorrow.
> Second: what is the single biggest hurdle preventing you from building it today? Is it a technical constraint? An organizational one? A funding conversation you haven't had yet?
> The gap between those two answers is your modernization roadmap. Everything else is detail

## Slide 18
**In conclusion**

- Modernization isn’t a one-time migration
- Treat modernization as a product, not a deadline-driven project: keep improving the developer experience continuously.
- Evolve vs. rip-and-replace with incremental rollouts (pilot → beta → GA)
- Design golden paths so the safest path is the easiest path
- Use a control plane to decouple workflows from tools and avoid tool sprawl
- Prove momentum by measuring flow

> **Presenter notes:**
> The through-line for Module 3: the safest path should be the easiest path. That's the design principle behind golden paths, behind incremental rollouts, behind guardrails over gates. Make the right thing easy and the wrong thing harder, and you don't have to mandate anything.
> Treat modernization as a product with a continuous lifecycle. Roll out in circles to limit blast radius and maximize learning. Use the control plane to decouple your workflows from your tools. And measure flow — not migration percentage — to prove you're making progress that matters to the business.
> One final thought: if you get the operating model right, you're not just building for today's AI capabilities. You're building a system that can evolve as those capabilities change. And given how fast that's happening right now, that adaptability isn't a nice-to-have. It's the whole point.

## Slide 19
**Quick recap + agenda**

- Platform-as-a-Product: user-centric roadmaps, pilots, and continuous feedback
- Incremental rollout strategies: parallel systems, phased adoption, and minimizing blast radius
- Security continuity: avoiding blind spots and maintaining posture during transitions
- Measuring success: developer velocity, adoption, satisfaction, and business value
- What we covered in Module 3
- How you should be thinking about your own modernization
- Integration architectures: connecting CI/CD, security, and infrastructure tools into a cohesive ecosystem
- AI governance challenges: managing AI adoption, compliance gaps, and review bottlenecks
- What next?
- What we will cover in Module 4
- With security platform engineering, vulnerability management goes from manuel toil to automated breeze.

> **Presenter notes:**
> In Module 4 we get into the specifics: how to think about your own modernization, integration architectures for connecting CI/CD, security, and infrastructure into a cohesive ecosystem, AI governance and compliance challenges, and what's next. A lot of teams find Module 4 is where things click into place — see you there.
