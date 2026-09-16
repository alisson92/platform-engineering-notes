# Module 4: Building your AI-ready modernization roadmap

## Slide 1
**Building your AI-ready modernization roadmap**

- DEVOPS MODERNIZATION FOR PLATFORM ENGINEERS
- MODULE
- 04

> **Presenter notes:**
> Welcome to Module 4: Building your AI-ready modernization roadmap. This is the final module, and it's where everything we've covered comes together into something you can actually use. We've talked about why migrations fail, what they really cost, how to think about modernization as a product, and what sustainable execution looks like. Now we're going to get specific — your roadmap, your architecture, your metrics, and how AI changes all of it. Let's finish strong.

## Slide 2
**Thinking about your own modernization**

> **Presenter notes:**
> Before we get into frameworks and timelines, I want to take a step back and ask a more fundamental question: how are you actually thinking about your own modernization? Not your organization's official position — what's your mental model? Because the lens you bring to this shapes every decision that follows. Let's start there.

## Slide 3
**Questions you need to answer**

- (Before doing anything else)
- Why are we embarking on a modernization journey? You need to understand what the goals are across stakeholders, is it due to an exec mandate?
- Most likely your goal is something like:
- Reduce cost, improve productivity, reduce cognitive load
- NOT
- Move from tool A to tool B
- This same operating model works for how you think about your modernization plans!

> **Presenter notes:**
> There's one question you need to answer before you do anything else. Before you evaluate tools, before you build a business case, before you schedule the first architecture meeting. The question is: why are we doing this?
> It sounds obvious. It almost never gets answered clearly. Most modernization efforts start with a tool decision — 'we're moving to GitHub Actions' or 'we're consolidating onto this platform' — and the why gets retrofitted after the fact. That's backwards, and it's one of the primary reasons modernization efforts stall or get defunded mid-flight.
> Your actual goal is almost certainly something like: reduce cost, improve productivity, reduce cognitive load on engineering teams. It is not 'move from tool A to tool B.' That's a method, not a goal. And if you can't clearly articulate the difference to a skeptical executive in two sentences, you're not ready to start.
> The good news is that once you're clear on the why, everything else — the roadmap, the metrics, the success criteria — becomes much easier to define. The operating model we've been building throughout this course exists to serve that outcome. Keep coming back to it.

## Slide 4
**Potential of a unified roadmap**

- Visibility (Day 1-10): See the shadow factory
- Governance (Day 11-20): Navigate the politics, standardise policy
- Automation (Day 21-30): Accelerate delivery and prove value
- (this is ambitious. But very possible)

> **Presenter notes:**
> This staircase diagram is one of my favorite ways to explain modernization sequencing, because it makes the logic obvious. You can't govern what you can't see. You can't automate what you haven't governed. The sequence isn't arbitrary — each step creates the foundation for the next.
> Days 1 through 10 are about visibility. Before you change anything, see everything. Connect your tools to the control plane and get a clear picture of what's actually running, where the gaps are, and where the quick wins live. This is also where you do your first user research — talk to developers, run surveys, understand what's actually painful. You're building a map before you start driving.
> Days 11 through 20 are governance. Now that you can see the landscape, you start standardizing. Replace ad-hoc checks with codified policy. Navigate the organizational politics — and yes, there will be politics. This is where alignment work happens, where you start defining your golden paths, and where you begin automating compliance evidence so you're not manually assembling audit reports at the end of every quarter.
> Days 21 through 30 are automation. Deploy your first real use case, measure what happens, gather feedback, and iterate. You're not done at day 30 — you're launched. There's a difference.
> Yes, this is ambitious. But it's also very possible if you stay disciplined about the sequence.

## Slide 5
**The 30-Day modernisation sprint**

- Modernisation must yield results in weeks, not quarters.
- Week 1: Baseline
- Connect the Control Plane, get visibility over currently tooling situation. Do first user researches (Surveys and dev interviews). Assess the situation and identify quick wins.
- Week 2-3: Governance
- Week 4: Launch MVP
- The hardest part of a modernization is understanding where to start both effectively and productively. My optimizing for visualisation and setting the baseline first - you set yourself up for future success! (And massively de-risk)
- 02
- 03
- Start replacing ad-hoc checks with codified policies. Automate compliance evidence and define standards using your Golden Paths.
- Deploy first use case, measure success, gather feedback, iterate, and continue.
- 01

> **Presenter notes:**
> Let's make the timeline concrete. Three phases, four weeks.
> Week one is about baseline. Connect the control plane and get visibility over your actual tooling situation — not the architecture diagram from two years ago, but what's actually running today. Do your first round of user research: surveys and developer interviews. You're trying to understand the real landscape, not the idealized one. And you're identifying quick wins — things you can improve fast that will demonstrate momentum and build credibility for the harder work ahead. The hardest part of any modernization is knowing where to start productively. Optimizing for visibility first massively de-risks everything that follows.
> Weeks two and three are governance. You're replacing manual, ad-hoc checks with codified policies. You're automating compliance evidence collection. You're defining the standards that will become your golden paths. This is often where the organizational work gets real — getting alignment on standards across teams that have been doing things their own way for years takes patience and, frankly, some politics. Lead with data from week one. 'Here's what we found' is a much better conversation opener than 'here's what we think you should do.'
> Week four: launch your MVP. Deploy the first use case to your pilot team, measure success against the baseline you established in week one, gather feedback, and iterate. You're not trying to boil the ocean in week four — you're proving the model works. One team, one golden path, measurable results. That's your proof point for everything that comes next.

## Slide 6
**Remember: Think architecture of outcomes!**

- Modernization is not about the tools you buy; it is about the friction you remove.
- Manual ticketing and long wait times during handoffs, combined with fragile, unmaintained glue code and visibility gaps that create blind spots across the lifecycle, ultimately lead to a critical fractures in your initiative.

> **Presenter notes:**
> This is a principle worth tattooing somewhere visible: modernization is not about the tools you buy. It's about the friction you remove.
> The diagram here shows a typical delivery pipeline with three failure points called out: manual handoffs, fragile scripts, and visibility leaks. These are the things that actually slow teams down. Manual ticketing and long wait times during handoffs. Glue code that nobody owns, nobody understands, and breaks at the worst possible moment. Visibility gaps that create blind spots across the lifecycle — so when something goes wrong, you're doing forensics instead of fixing it.
> When you approach modernization as an architecture of outcomes, you ask different questions. Instead of 'what tool should we replace?' you ask 'where is the most friction in this pipeline?' Instead of 'how do we consolidate our toolchain?' you ask 'what would it take to remove that manual handoff?' Those questions lead to different — better — decisions. And they lead to modernization that developers actually experience as an improvement, rather than just a different set of tools to learn.

## Slide 7
**Remember: Be careful with whatyou measure!**

- Simple way to think about ROI?
- ROI = Value generated - Integration cost
- Think back to why you are embarking on a modernization journey, what you measure should be based on that goal.
- If that goal is productivity,
- Don’t measure “number of users using new tool”
- Measure “how quickly and efficiently development teams can deliver high-quality software.”

> **Presenter notes:**
> There's a trap that's easy to fall into, especially when you're under pressure to show progress: measuring what's easy to measure rather than what actually matters.
> Go back to your why. If your goal is productivity, then the metric that matters is how quickly and efficiently development teams can deliver high-quality software. Not how many users are on the new tool. Not what percentage of pipelines have been migrated. Those are activity metrics, not outcome metrics.
> The ROI formula here is simple and worth keeping front of mind: value generated minus integration cost. If the integration cost is high and the value generated is low, you have a negative ROI modernization — and those happen more often than anyone likes to admit, precisely because teams measure the wrong things and don't notice until the budget is gone.
> Define your outcome metric before you start. Measure it at baseline in week one. And report against it throughout. It sounds like basic discipline — it is — but it's also surprisingly rare. Teams that do it have a much easier time maintaining executive support when things take longer than planned, which they will.

## Slide 8
**How does AI change modernization?**

> **Presenter notes:**
> Okay. We've talked about roadmaps, timelines, and metrics. Now I want to address the elephant in the room that has been sitting in the corner of every conversation for the last two years.
> How does AI change modernization? The honest answer is: substantially. Not in ways that make everything we've covered irrelevant — quite the opposite, the fundamentals matter more than ever. But AI introduces new challenges and new opportunities that your modernization roadmap needs to account for. Let's get into it.

## Slide 9
**The shift to Agentic AI in software development**

- By 2028, 70% of development teams will use agentic coding assistants (Gartner prediction).
- AI will generate exponentially more code, but human capacity to review and manage it grows only linearly.
- This creates a new challenge: teams must manage a massive amount of AI-generated development at scale.

> **Presenter notes:**
> Here's the trajectory. By 2028, according to Gartner, 70% of development teams will be using agentic coding assistants. Not just autocomplete — agents that can plan, execute, and iterate across the development lifecycle.
> The math problem this creates is worth sitting with. AI will generate exponentially more code. Human capacity to review and manage that code grows only linearly. That gap doesn't close on its own. If anything, it widens as the tools get more capable.
> What this means in practice: the volume of code flowing through your pipelines is going to increase dramatically, and the code won't have a human author in the traditional sense. It'll have a human who prompted it, but that's different. Your platform needs to be able to handle that — at scale, with governance, without creating a review bottleneck that eliminates all the velocity gains AI was supposed to deliver.
> This is not a future problem. Teams are already running into it. The modernization work we've been talking about throughout this course is what positions you to handle it well instead of scrambling to catch up.

## Slide 10
**The current developer productivity problem**

- Developers spend most of their time on non-coding tasks:
- 89% of developer time is spent on tasks like answering questions, context switching, or fixing small issues.
- Only 11% of time is spent on innovation.
- Frequent interruptions (Slack questions, small bugs, documentation) can cause 30–60 minutes of lost focus.

> **Presenter notes:**
> Before we talk about AI as a solution, let's be honest about the problem it's solving — and the problem it could make worse if you're not careful.
> 89% of developer time is spent on non-coding tasks: answering questions, context switching, fixing small issues, chasing down approvals. Only 11% is spent on actual innovation. Read that again. The most expensive people in your organization are spending 89% of their time not doing the thing you hired them to do.
> And context switching is particularly brutal. A Slack notification, a small bug, a documentation question — each interruption can cost 30 to 60 minutes of lost focus time. Not 30 to 60 seconds. Minutes. The cognitive cost of re-establishing deep focus after an interruption is enormous, and it compounds across a team over weeks and months.
> AI coding assistants have the potential to reclaim some of that 89%. But only if the underlying platform is set up to support them — with the right guardrails, the right governance, the right golden paths. Otherwise you're adding a fast car to a congested road. You need to fix the road too.

## Slide 11
**Moving beyond AI coding assistants**

- The goal is not just AI helping individuals write code. With the principles explored in this course, enabling, AI can become a trusted team member that:
- Builds features
- Suggests architecture
- Coordinates tasks across the development lifecycle
- Works alongside teams rather than just assisting individuals

> **Presenter notes:**
> The vision most people have of AI in development is an autocomplete tool that helps individuals write code faster. That's the starting point, not the destination.
> The more interesting — and more achievable — version is AI as a trusted team member that operates at the team level, not just the individual level. One that can build features end-to-end, suggest architecture based on your specific platform context, coordinate tasks across the development lifecycle, and work alongside teams rather than just assisting individuals one prompt at a time.
> This isn't science fiction. It's happening in early-adopter organizations right now. But it requires the same foundation we've been building throughout this course: visibility into what's running, governance of what's allowed, golden paths that define the safe routes, and a control plane that can coordinate everything.
> The teams that have done the modernization work are the ones positioned to deploy AI at this level. The teams that haven't are the ones who will spend the next two years trying to use AI to patch a platform that was never designed to support it. That's an expensive way to learn the lesson.

## Slide 12
**/Remember the Control Plane**

- The same principles apply. Integrate, abstract, and coordinate AI agents!
- Agent orchestration
- Interface over tools
- Simplify the AI landscape
- Just as the control plane let you integrate and manage a diverse toolset, the control plane can do the same for AI. Coordinate agents, simplify workflows, and embed AI directly into the developer experience.

> **Presenter notes:**
> Here's where the course comes full circle. We introduced the control plane in Module 1 as the way to unify a diverse toolchain without forcing everyone onto a single tool. Everything since then has built on that foundation.
> Now apply the same logic to AI. You're going to have multiple AI agents, multiple models, multiple tools operating across your development lifecycle. Without coordination, that becomes another form of tool sprawl — but faster-moving and harder to govern than the toolchain sprawl we talked about in Module 2.
> The control plane solves the same problem it always has: agent orchestration, interface over tools, simplifying the landscape. It coordinates your AI agents the way it coordinates your CI/CD tools — with consistent policy, visibility, and governance. You're not managing individual AI interactions; you're managing a platform that AI operates within.
> If you've been wondering how to govern AI adoption without slowing it down, this is the answer. Same principles. Same architecture. New application.

## Slide 13
**A simple interaction model for**

- agents & modernization
- Plan
- Respond
- Execute
- Understand intent: Agents interpret developer requests and analyze platform context (code, pipelines, policies).
- Coordinate the platform: Through the control plane, agents gather information and orchestrate actions across CI/CD, security, and infrastructure.
- Execute safely: Agents automate fixes, tests, and deployments while respecting platform guardrails and golden paths.

> **Presenter notes:**
> Let's make the AI interaction model concrete. Three steps: plan, respond, execute.
> In the plan phase, agents interpret developer requests and analyze platform context — your code, your pipelines, your policies. They're not operating in a vacuum; they're operating with full awareness of the platform's state and constraints. This is only possible if your platform has the visibility and data structure to support it. Another reason the baseline work in week one is so important.
> In the respond phase, agents coordinate through the control plane, gathering information and orchestrating actions across CI/CD, security, and infrastructure. They're not bypassing your governance layer — they're working within it. That's the key distinction between AI that accelerates your platform and AI that creates chaos in it.
> In the execute phase, agents automate fixes, tests, and deployments while respecting platform guardrails and golden paths. They stay on the road. They don't go off-road unless a human has explicitly decided that's appropriate.
> The simplicity of this model is intentional. Plan, respond, execute. The complexity lives inside each step — but the framework itself is something your whole team can reason about and build toward.

## Slide 14
**In conclusion**

- Building your modernization roadmap
- Start with outcomes, not tools: Define the goals of modernization before changing technology.
- Create a clear roadmap: Progress through visibility → governance → automation.
- Deliver value quickly: Use short cycles to baseline, launch, and iterate.
- Prepare for AI-driven delivery: Coordinate agents across the platform using a control plane.

> **Presenter notes:**
> Four principles to carry out of this course.
> Start with outcomes, not tools. Define what success looks like for your organization before you touch a single technology decision. Write it down. Get alignment on it. Keep coming back to it when decisions get hard.
> Create a clear roadmap. Visibility first, then governance, then automation. Don't skip steps. Each one creates the foundation for the next, and skipping them is how you end up with automation that automates the wrong things at scale.
> Deliver value quickly. Use the 30-day sprint structure to get real results in front of real users fast. Early wins create organizational momentum that's very hard to build any other way. Protect your pilot team, learn from them, and use what you learn to make the next rollout better.
> Prepare for AI-driven delivery. The shift to agentic AI is happening whether your platform is ready or not. The modernization work you do today is what determines whether AI becomes a force multiplier for your teams or a governance nightmare for your organization. Build the platform that AI can operate within safely. That's the most future-proof investment you can make right now.

## Slide 15
**Next steps?**

> **Presenter notes:**
> So — what do you actually do on Monday? This section is about moving from frameworks to action. We're going to get specific about your integration architecture and what the journey forward looks like in practice. No more theory. Let's talk about what you go build.

## Slide 16
**Map the connective tissue.**

- [ Existing CI Trigger ]
- [ Unified Security Context ]
- [ Policy-as-Code Check ]
- Design your integration architecture
- Identify one high-friction delivery pipeline (e.g., a messy Jenkins-to-production deployment).
- Design the flow: How will your existing CI/CD, and security tools be orchestrated without migrating them?
- Define the automated guardrails (Policy-as-Code) and evidence collection points.
- [ Governed Deployment ]
- If you can't trace a release through your existing tools, you are just managing tool sprawl, not modernizing. Visibility must precede automation.

> **Presenter notes:**
> Map the connective tissue. That phrase is doing a lot of work, and it's worth unpacking.
> Most organizations have delivery pipelines — but they're not really pipelines in the clean, diagrammatic sense. They're a series of handoffs held together by tribal knowledge, manual steps, and scripts that one person wrote three years ago and nobody has touched since. That's the connective tissue. And it's usually where the most friction lives.
> Start by identifying one high-friction delivery pipeline. Not your whole estate — one. Pick the one that causes the most pain, the most delays, the most late-night Slack messages. Your messy Jenkins-to-production deployment, your compliance evidence collection process, whatever it is.
> Then design the flow: how will your existing CI/CD and security tools be orchestrated without migrating them? You're not replacing the tools. You're building a layer above them that coordinates their execution and gives you visibility into the whole chain.
> Then define your automated guardrails — policy-as-code — and your evidence collection points. Where in the pipeline should compliance checks happen? What gets recorded, and where does that data live?
> And here's the most important test: if you can't trace a release through your existing tools from commit to deployment, you are not modernizing. You are managing tool sprawl. Visibility must come before automation, every time.

## Slide 17
**The journey forward**

- You now have the blueprint for sustainable, integration-first DevOps modernization.
- Make your modernization evolutionary, not disruptive.
- Start Small: Target one high-impact pipeline and connect it to a unified control plane to gain immediate visibility without forcing a migration.
- Remember to measure flow and establish your baseline. Use momentum metrics like time-to-onboard, deployment frequency, and developer eNPS to prove your value and justify continued investment!
- Never forget that Modernization is an organizational change, not just a tooling swap. Build a unified control plane, reduce cognitive load with Golden Paths, and treat your platform as a product to ensure continuous, sustainable evolution.

> **Presenter notes:**
> You now have the blueprint. I want to be specific about what that means, because 'you have the blueprint' can feel abstract.
> You have a framework for thinking about modernization as an organizational change, not a tooling swap. You have a sequenced roadmap — visibility, governance, automation — that de-risks the process and creates early wins. You have a product model for how to build and maintain a platform your developers will actually want to use. You have a metrics framework that connects to business outcomes rather than just activity. And you have an architecture — the control plane — that positions you to absorb AI-driven change without losing governance or visibility.
> The practical starting point: pick one high-impact pipeline and connect it to a unified control plane. Gain immediate visibility without forcing a migration. Establish your baseline metrics. Start your first pilot with a friendly team.
> That's not a massive undertaking. It's a focused, time-boxed sprint with a concrete deliverable. And it creates the momentum that makes everything else possible.
> Remember: modernization is an organizational change. The technology is the easy part. Changing how teams think about their platform, how they measure success, how they engage with the users of that platform — that's the real work. The good news is you don't have to do it all at once. You iterate your way there, just like the product model says.

## Slide 18
**What we learned**

- Modernization is an outcome, not a tooling swap
- Rip-and-replace migrations drive developer burnout
- A control plane unifies workflows without lock-in
- Integrating tools outperforms replacing them
- Treat your internal platform like a product
- Evolutionary change preserves team momentum
- Security must be continuous, not a manual gate
- Golden Paths reduce cognitive load and drive adoption
- AI governance requires a unified control plane

> **Presenter notes:**
> Let's close the loop on the whole course.
> Modernization is an outcome, not a tooling swap. We said that in Module 1 and it's been the spine of everything since. Rip-and-replace migrations drive developer burnout — the data on that is uncomfortable but clear. A control plane unifies workflows without lock-in. Integrating tools outperforms replacing them. Treat your internal platform like a product.
> On the right side: evolutionary change preserves team momentum — you don't have to blow everything up to move forward. Security must be continuous, not a manual gate. Golden paths reduce cognitive load and drive adoption. And AI governance requires a unified control plane.
> Nine principles. Four modules. One through-line: the teams that modernize successfully are the ones that treat it as a continuous, human-centered, outcome-driven practice — not a project with a finish line.
> Thank you for going through this course. Now go fix something.
