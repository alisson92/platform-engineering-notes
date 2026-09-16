# GitOps for PE Module 2

## Page 1

![Page 1](images/module-2/page-1.png)

GitOps Fundamentals and 
Core Principles
 
GITOPS FOR PLATFORM ENGINEERING
MODULE 02

## Page 2

![Page 2](images/module-2/page-2.png)

History and Origin
2

## Page 3

![Page 3](images/module-2/page-3.png)

History and Origin
1. Desired state: deﬁned in cookbooks (recipes)
2. Chef client: runs at intervals on each target node 
(server / VM)
3. Drift detection: the client compares actual state 
with the cookbooks
4. Remediation: If drift is detected, the client 
reconciles the node to the desired state
GitOps—and the ideas behind it—are 
older than you might think
Configuration Management (CM)
Chef, a conﬁguration management tool, was announced in 2009 (formerly Opscode)
3

## Page 4

![Page 4](images/module-2/page-4.png)

History and Origin - Today
In 2017, GitOps was deﬁned based on 
four principles
Just four principles—no more, no less.
Declarative, Versioned and Immutable, 
Pull-based and Continuously reconciled!   
You name it, you own it!
Alexis Richardson introduced the term GitOps in 2017 while he was at Weaveworks. 
Today, he is the CEO of ConﬁgHub.
4

## Page 5

![Page 5](images/module-2/page-5.png)

Terminology
5

## Page 6

![Page 6](images/module-2/page-6.png)

6
◆ Current State
◆ Desired State
◆ State Store
◆ Drift
◆ Reconciliation
◆ Code
◆ Infrastructure as Code (IaC)
◆ Infrastructure as Data (IaD)
◆ Conﬁguration as Code (CaC)
◆ Conﬁguration as Data (CaD)
◆ Declarative
◆ Feedback Loop
◆ Rollback
◆ Continuous Delivery
◆ Continuous Deployment
Terminology

## Page 7

![Page 7](images/module-2/page-7.png)

7
Terminology- Part 1/3
Current State is what is actually 
running right now.
People often treat Current State as 
“the truth”.
Desired State is the normative 
deﬁnition of what the system 
should be.
It is also the intent, not a runtime 
artifact.
State Store is the place where 
the authoritative representation 
of intent lives. 
Git is typically the primary state 
store.
Drift is the difference between 
Desired State and Current State.
Drift is not “failure” by default — 
it’s a signal that the system is out 
of alignment.
Reconciliation is the heart of 
GitOps: converging Current State 
toward Desired State.
Reconciliation ≠ “deployment”.
Deployment is just one kind of 
reconciliation action.

## Page 8

![Page 8](images/module-2/page-8.png)

8
Declarative describe what you 
want, not how to do it.
Declarative ≠ simple.
Feedback Loop is the process 
where a cluster-resident reconciler 
continuously compares the desired 
state (deﬁned in Git) with the current 
state of the cluster and automatically 
corrects any detected drift to enforce 
consistency.
Rollback is usually not a special 
operational procedure. 
Rollback = revert a commit or move a 
tag.  Reconciliation applies the 
previous Desired State again.
Continuous Delivery means, 
that code is always ready for 
production but requires a manual 
approval step before 
deployment.
Continuous Deployment 
means, that code is 
automatically deployed to 
production without human 
intervention once all tests pass.
Terminology - Part 2/3

## Page 9

![Page 9](images/module-2/page-9.png)

9
Terminology - Part 3/3
Code means executable or 
evaluatable deﬁnitions that 
transform inputs into a resulting 
state.
Infrastructure as Code (IaC) 
means, that the infrastructure is 
created and changed by 
executing code that contains 
provisioning logic.
Infrastructure as Data (IaD) 
means, that the Infrastructure is 
described as plain declarative 
state data that controllers 
continuously reconcile.
Conﬁguration as Code (CaC) 
is generated through templates 
and logic rather than expressed 
directly.
Conﬁguration as Data (CaD) 
is stored as plain, declarative 
data without execution logic 
(code).

## Page 10

![Page 10](images/module-2/page-10.png)

10
Terminology - Part 3/3
Code means executable or 
evaluatable deﬁnitions that 
transform inputs into a resulting 
state.
Infrastructure as Code (IaC) 
means, that the infrastructure is 
created and changed by 
executing code that contains 
provisioning logic.
Infrastructure as Data (IaD) 
means, that the Infrastructure is 
described as plain declarative 
state data that controllers 
continuously reconcile.
Conﬁguration as Code (CaC) 
is generated through templates 
and logic rather than expressed 
directly.
Conﬁguration as Data (CaD) 
is stored as plain, declarative 
data without execution logic 
(code).
GitOps prefers Data in Git 
and Code in controllers!

## Page 11

![Page 11](images/module-2/page-11.png)

11
Terminology - Example 3/3 (I)
- Infrastructure 
as Code (IaC)
- Infrastructure 
as Data (IaD) 
- Conﬁguration 
as Code (CaC)
- Conﬁguration  
as Data (CaD) 
templates/ci.yaml
values.yaml

## Page 12

![Page 12](images/module-2/page-12.png)

12
Terminology - Example 3/3 (II)
- Infrastructure 
as Code (IaC)
- Infrastructure 
as Data (IaD) 
- Conﬁguration 
as Code (CaC)
- Conﬁguration  
as Data (CaD) 
templates/ci.yaml
values.yaml

## Page 13

![Page 13](images/module-2/page-13.png)

13
Terminology - Example 3/3 (III)
- Infrastructure 
as Code (IaC)
- Infrastructure 
as Data (IaD) 
- Conﬁguration 
as Code (CaC)
- Conﬁguration  
as Data (CaD) 
templates/ci.yaml
values.yaml
There is no 100% ﬁxed deﬁnition of CaD and 
IaD. The meaning depends on context and can 
change over time.
In general, you can say that IaD is a subset of 
CaD (a semantic specialization).
● IaD = platform scope
● CaD = workload scope

## Page 14

![Page 14](images/module-2/page-14.png)

The Four Principals 
(What is GitOps)
14

## Page 15

![Page 15](images/module-2/page-15.png)

Remember this.
Declarative Versioned and 
Immutable
Pull-Based
Just four simple principles—no more, no less. 
15
Continuously 
Reconciled
The Four Principles (What is GitOps)
Feedback Loop

## Page 16

![Page 16](images/module-2/page-16.png)

What is GitOps Not
ClickOps or ad-hoc kubectl changes
A replacement for IaC tools
Manual, Git-based deployments
CI/CD with Git slapped on top
Scripting IaC from Git
Just a developer-only approach at first
A replacement for DevOps! 
A replacement for CI/CD (maybe for CD, but 
not CI)
A replacement for Platform Engineering!
16
GitOps is not

## Page 17

![Page 17](images/module-2/page-17.png)

17
CI/CD vs GitOps CD (I)

## Page 18

![Page 18](images/module-2/page-18.png)

18
CI/CD vs GitOps CD (II)

## Page 19

![Page 19](images/module-2/page-19.png)

Context: How GitOps Fits In
19

## Page 20

![Page 20](images/module-2/page-20.png)

Context: How GitOps Fits In
20
GitOps is not a tool, but an operating model
that accelerates DevOps, secures DevSecOps,
and scales Platform Engineering.
Evolution, Not Replacement: GitOps is seen as an 
advanced implementation of DevOps principles
◆ Devops
◆ DevSecOps
◆ Platform Engineering

## Page 21

![Page 21](images/module-2/page-21.png)

21
And by the way: DevOps is dead!

## Page 22

![Page 22](images/module-2/page-22.png)

DevOps Platform 
Engineering

## Page 23

![Page 23](images/module-2/page-23.png)

*(no extractable text on this page)*

## Page 24

![Page 24](images/module-2/page-24.png)

24
Recap: GitOps Fundamentals and Core 
Principles
❏ GitOps is not new—but in 2017, Alexis Richardson gave it a name
❏ Terms can be tricky. Understanding them well will help you now and 
in the future.
❏ GitOps is based on just four principles: 
❏ Declarative 
❏ Versioned and Immutable 
❏ Pull Based 
❏ Continuous Reconciliation
❏ GitOps is not a replacement for DevOps or Platform Engineering.
❏ GitOps is the glue for platform engineering. It allows you to:
❏ Deﬁne declarative policies, infrastructure, budgets, dashboards, and more
❏ Scale your platform by offering self-service
