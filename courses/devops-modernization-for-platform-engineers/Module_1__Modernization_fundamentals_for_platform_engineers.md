# Module 1: Modernization fundamentals for platform engineers

## Slide 1
**Modernization fundamentals for platform engineers**

- DEVOPS MODERNIZATION FOR PLATFORM ENGINEERS
- MODULE
- 01

> **Notas do apresentador:**
> Welcome to Module 1 of DevOps Modernization for Platform Engineers. If you're here, you've probably already survived at least one migration project — which means you probably already have a great war story or two. Let's make sure your next one goes better with guidance from this course.

## Slide 2
**Who am I?**

- Liz Ryan

> **Notas do apresentador:**
> I’m Liz Ryan and I'll be your guide through this module. The goal isn't to sell you on any particular tool or approach. It's to give you the mental models and the data to make better decisions — because, as you're about to see, the industry has been making some expensive ones.

## Slide 3
**Our focus inthis course**

- Together, we’ll unpack sustainable modernization for platform engineers from the “migration mirage” to CI/CD control planes, DevEx, and AI governance.
- Migration myths, and the crucial difference between migration and modernization.
- How to approach modernization as an evolutionary, product-driven change, balancing platform, security, and delivery without disrupting teams or increasing risk.
- How to design a practical modernization roadmap through platform engineering best practice

> **Notas do apresentador:**
> This module tackles something we call the 'migration mirage' — the gap between what modernization promises and what it actually delivers. We'll also get into CI/CD control planes, developer experience, and AI governance. Yes, AI is already in the room, and it has opinions about your pipelines.

## Slide 4
**By the end of this course**

- You’ll know everything you need to:
- Spot blockers behind stalled modernization and respond before they turn into delays and possible demise.
- Choose an approach that scales in your org
- Understand best practice for building a roadmap you can run, with pilots, phased adoption, governance for emerging tech (including AI), and metrics that prove progress to the business.
- In this course, you’ll learn how to avoid typical failure points and make the right decisions when modernizing your CI/CD and DevOps organization.

> **Notas do apresentador:**
> By the end of this course you’ll have three outcomes. You'll be able to spot a stalled modernization before it becomes a career-defining disaster. You'll know how to choose an approach that actually scales. And you'll have a roadmap framework that can survive contact with real organizational politics.

## Slide 5
**The migration mirage**

- The reality
- Though 85% of enterprises migrated in the last 2 years…
- Only 25% achieved expected value within 1 year
- 38% delivered less ROI than promised
- "Migrate to a modern platform. Consolidate your toolchain. Watch complexity disappear."
- The pitch
- Simply, “migrating”is not enough

> **Notas do apresentador:**
> Let’s get started - based on a 2025 survey of IT and DevOps Leaders, 85% of enterprises conducted a migration in the last two years. Sounds great. But only 25% hit their expected value within a year, and 38% delivered less ROI than promised. So roughly a third of these organizations spent a lot of money, disrupted their teams, and got... less than they paid for. The pitch sounds amazing. The reality is more complicated.

## Slide 6
**The $315K Surprise**

- Average cost overrun per enterprise.
- $1.75M + 18% = $315,000Avg migration
- cost
- Avg budget overrun
- Wasted capital

> **Notas do apresentador:**
> Here's the math nobody puts in the business case: an average migration runs at about $1.75 million, and typically overshoots budget by 18%, which works out to $315,000 in wasted capital per enterprise. That's not a rounding error. That's a small engineering team. Or a very nice offsite. Point being — this isn't theoretical money.

## Slide 7
**Where budgets go to die**

- It isn't just about paying more; it's about paying for nothing. Budget is consumed by dead-end approaches and abandoned integrations.
- of organizations lost >25% of their
- migration budget to failed initiatives.

> **Notas do apresentador:**
> 37% of organizations lost more than a quarter of their migration budget to failed initiatives. Not overruns — failed initiatives. Work that got abandoned. Tools that never got integrated. Approaches that hit dead ends. The money didn't disappear; it just bought nothing.

## Slide 8
**Where does the money go?**

- Tool sprawl
- Teams add tools to patch local gaps, missing shared context, and inconsistent policy, increasing fragmentation, negatively impacting work and slowing delivery.
- Visibility gap
- Productivity tax
- This doesn’t only cost time in wasted effort, or budget, but massively impacts the rate of innovation in your organization due to increased cognitive load, and time wasted for your most expensive engineers.
- 02
- 03
- Build and delivery logic running outside governance, unmonitored AI-generated configs, orphaned runners/scripts, and manual changes that increase risk and reduce visibility.
- When systems aren’t connected, people are forced to be the glue themselves, context-switching across dashboards, brittle scripts, and manual handoffs/ evidence gathering.
- 01

> **Notas do apresentador:**
> There are three culprits to this problem. First, Tool sprawl — teams adding tools to patch local problems, which just creates more fragmentation. Second, Visibility gaps — AI-generated configs and orphaned scripts running outside governance, which is as scary as it sounds. And third, what I love calling the 'productivity tax' — when your systems aren't connected, your engineers become the connective tissue. They're context-switching across dashboards, babysitting brittle scripts, doing manual handoffs. Your most expensive people are doing your least valuable work.

## Slide 9
**Modernization ≠ Migration.Modernization is an outcome, not a tool purchase.**

- True modernization changes the workflow, not the vendor.
- While a migration might focus on simply replacing one tool with another, a modernization looks at improving the entire system itself.
- I.e changing the URL of your Cl server doesn't fix the flow of value. If you move a messy, fragmented process to a new unified platform, you simply inherit a messy, unified platform.
- New tool + old process = expensive old process

> **Notas do apresentador:**
> This is the most important slide in the module, so I'll say it plainly: changing the URL of your CI server is not modernization. If you take a fragmented, messy process and move it to a shiny new platform, you now have a fragmented, messy process on a shiny new platform. New tool plus old process equals expensive old process. Modernization is about the workflow, not the vendor.

## Slide 10
**The alternative: Platform engineering + control plane approach**

- Bring a user-centric approach to roadmap and clear success metrics, so modernization becomes incremental, measurable and less risky.
- Platform engineering impact
- Ensure visibility, organizational change and product thinking for your modernization effort.
- Unify delivery workflows across tools, reducing sprawl, improving visibility, and enabling safer, measurable modernization without vendor lock-in.
- Control plane

> **Notas do apresentador:**
> The alternative is a platform engineering approach paired with what's called a control plane. The key words here are incremental, measurable, and less risky. This isn't a big-bang migration. It's an evolutionary change with visibility built in — and crucially, no vendor lock-in.

## Slide 11
**What is a control plane?**

> **Notas do apresentador:**
> Think of the control plane as the layer that sits between your existing toolchain — GitHub, Snyk, Argo, Jira, whatever you're running — and the enterprise visibility layer above it. It handles orchestration, policy, and data normalization. It doesn't replace your tools; it connects them and governs them. The stuff below the control plane can change without blowing up everything above it.

## Slide 12
**What does the control do?**

> **Notas do apresentador:**
> What does the control do? It has three functions: Guardrails — security that enables teams rather than blocking them, which is a distinction security teams and developers will both appreciate. Visibility — actually knowing what's running where, which sounds basic until you've been in an incident at 2am trying to answer that question. And Flow — frictionless movement of code to production. That's the whole goal.

## Slide 13
**Treat your modernization like a product**

- Mindset shift
- Move away from viewing migration solely as a technical, political, or "lift-and-shift" challenge, focus instead on creating a seamless, valuable, and sustainable transition.
- A key pillar of platform engineering
- You need to think about those impacted by the modernization efforts as customers of your “product”. Understand their pain, fears, and their desires.
- Impacted users as customers
- User research, user centric design, product roadmap, feedback loops, product marketing, etc.
- Product management basics
- For members of your team that are highly technical, making this shift in mindset can be hard. Lead by example!

> **Notas do apresentador:**
> This is where the mindset shift happens. If you're highly technical, this might feel uncomfortable — because it means thinking about your internal developers as customers, doing user research, running feedback loops, thinking about adoption. But here's the reality: a modernization no one uses is just an expensive side project. Lead by example on this one.

## Slide 14
**In conclusion**

- Migrations:
- Cost organizations millions
- Waste huge amounts of time and productivity
- The solution for teams is to:
- Modernize, not migrate, focusing on organization change, and workflow improvement - not simply tool replacement
- Utilize control plane and platform engineering best practices

> **Notas do apresentador:**
> In summary: migrations cost more than planned, waste time and productivity, and often deliver less than promised. The fix isn't a better tool — it's a better approach. Modernize the workflow, not just the vendor. Use platform engineering best practices and a control plane to make it incremental and measurable. That's the difference between a transformation and a very expensive detour.

## Slide 15
**Quick recap + agenda**

- What modernization is (and isn’t) and how it differs from a simple migration
- The true costs of migration
- How to best approach effective modernization: Platform engineering + control plane
- What a control plane is and why it matters for guardrails, consistency, and visibility
- What we covered in Module 1
- Financial and operational realities: sunk costs, abandoned migrations, and wasted budget
- Human impact like developer burnout, cognitive overload, and innovation freezes
- The myth of consolidation: why standardizing on fewer tools often increases complexity
- Evolutionary modernization: incremental change that preserves momentum and reduces risk
- What we will cover in Module 2

> **Notas do apresentador:**
> In Module 2 we go deeper into the financial and human costs — developer burnout, cognitive overload, the myth that consolidating tools reduces complexity. Spoiler: it often doesn't. But we'll also get into evolutionary modernization — how to make incremental changes that preserve momentum and reduce risk. See you there.
