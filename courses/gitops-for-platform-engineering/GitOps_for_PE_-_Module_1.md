# GitOps for PE Module 1

## Página 1

Introduction and Motivation 
GITOPS FOR PLATFORM ENGINEERING
MODULE 01

## Página 2

Artem Lajko
● Head of Platform Engineering at iits
● Ambassador for Platform Engineering 
● CNCF Kubestronaut
● Published Author
2
Book: Implementing GitOps with Kubernetes

## Página 3

3
What is this course about?
GitOps Fundamentals and 
Core Principles 
GitOps Architecture, 
Patterns, and Anti-Patterns
GitOps Tooling 101 - Argo 
CD, Flux CD and Sveltos
GitOps for Enterprises – 
Scaling and Security
Outlook and Trends – GitOps 
is a Sprawl of Configs
01 02 03
04 05 06
Introduction and Motivation

## Página 4

Why GitOps
4

## Página 5

Why GitOps?
1000 Reasons + 1 
◆ Git becomes your deployment API
◆ Fully versioned infrastructure
◆ Perfect reproducibility
◆ Bulletproof auditability
◆ Developer-friendly, Ops-safe
◆ Lower risk, higher velocity
5
GitOps is a contract between Agents and Humans!

## Página 6

6
Why GitOps? Let’s look at the numbers (I)
https://octopus.com/publications/state-of-gitops-report
https://platformengineering.org/reports/state-of-platform-engineering-vol-3

## Página 7

7iits-consulting: Migration from VMS and Rancher (RKE) to GitOps with Argo CD (KumoOps Stack)
Why GitOps? Let’s look at the numbers (II)

## Página 8

The Wild West Era - Before 
DevOps and GitOps 
8

## Página 9

The Wild West Era — Before DevOps and 
GitOps (I)
9

## Página 10

10
The Wild West Era — Before DevOps and 
GitOps (II)

## Página 11

11
2000s - 2010s
Enterprise HA Setup
The Wild West Era — Before DevOps and 
GitOps (III)

## Página 12

12
2000s - 2010s
Enterprise HA Setup
httpd.conf
httpd.conf
Doesn’t scale! 
The Wild West Era — Before DevOps and 
GitOps (IV)

## Página 13

The Birth of Infrastructure as 
Code
13

## Página 14

The Birth of Infrastructure as Code (IaC) - I
14

## Página 15

15
Everything becomes declarative! 
The Birth of Infrastructure as Code (IaC) - II

## Página 16

New Tooling…Similar Challenge… 
Still Running on My Machine
16

## Página 17

Conﬁg and Ops Still Run on My Machine
We now use “X as Code” (let’s call it conﬁg), 
but it still runs on engineers’ machines.
If Alex changes the VM ﬁrst, there is no 
shared state—because not every tool supports 
state.
Then Alice may apply her change, but it can 
overwrite Alex’s change and likely break the 
system.
Conﬁg and ops still run on the local machine.
17
Local Ops!

## Página 18

Ops still running on my Machine!
We have now split conﬁg and ops. Conﬁg lives 
in a central Git repo, but operations still 
happen on engineers’ machines.
Alex makes a change on the VM and commits 
the conﬁg to Git. Alice pulls the change, 
merges it with her own, and runs the change 
on the VM.
- Conﬁg is in Git 
- Ops still run on the local machine
18
Distributed Ops!

## Página 19

Pipeline Ops: Code still running on my Machine!
We have now split conﬁg and ops. Conﬁg lives 
in a central Git repo, and operations are 
executed through a pipeline.
Alex pulls the conﬁg, makes a change, and 
commits it. This triggers an event that runs the 
pipeline. The pipeline applies the changes to 
the VM.
- Conﬁg is in Git 
- Ops are through pipelines
19
Pipeline Ops!

## Página 20

Pipeline Ops: Code still running on my Machine!
We have now split conﬁg and ops. Conﬁg lives 
in a central Git repo, and operations are 
executed through a pipeline.
Alex pulls the conﬁg, makes a change, and 
commits it. This triggers an event that runs the 
pipeline. The pipeline applies the changes to 
the VM.
- Conﬁg is in Git 
- Ops are through pipelines
20
Event? 1 Day, 1 Week, 1 Month…? 
Drift…

## Página 21

Agent Ops: Code still running on my Machine!
We have now split conﬁg and ops. Conﬁg lives 
in a central Git repo. An agent watches the 
repo’s desired state for changes. If it detects 
drift, it pulls the conﬁg and reconciles the 
target environment to match the actual state.
- Conﬁg is in Git 
- Ops are running  through an Agent 
(Machine)!
21
Execute Ops through Git as a declarative 
contract!

## Página 22

You Have a Contract with the Agent
Agent: I fulﬁll the contract by continuously 
reconciling the desired state in Git with the 
actual state of the target environment.
User: I put everything in Git. Git becomes the 
single source of truth for the contract.
22
The user has a contract with the agent. The agent promises to keep the 
target environment in sync.

## Página 23

Why Do We Want GitOps?
23

## Página 24

24
Why Do We Want GitOps? 
❏ If you build a platform, GitOps is the glue for continuous delivery
❏ Single source of truth (visibility, history, …)
❏ Git as a common tool to store conﬁg as data, with one shared 
language
❏ Git as a contract between humans and agents 
❏ Disaster recovery and backups built in
❏ Security-friendly: strong audit trail
❏ AI-ready: it can explain what happened, why, when, and how

## Página 25

Recap and Learning Objectives
- What is GitOps
- How to manage a ﬂeet of 1,000 clusters
- How to build your own platform distribution
- Which GitOps topologies exist
- A comparison of GitOps tools
- Why GitOps is more than just tooling
…and more! 
What YOU will learn
- Understand the core ideas of GitOps
- See a real enterprise example
- Hands-on exercises with examples based 
on Kubara
- Learn how to choose the right solution
- Deep dive into the most popular GitOps 
tools
- Understand the culture behind GitOps
Let’s not spoil too much yet.
How YOU will learn
25
A quick look at what’s coming next.
