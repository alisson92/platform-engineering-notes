# Intro to AI in Platform Engineering

## Module 1: The AI and platform engineering landscape

### The AI and platform engineering landscape

In this module, we explore the fundamental concepts of platform engineering and how Artificial Intelligence (AI) is influencing and being influenced by this practice. We will focus on the bi-directional relationship between AI and platform engineering and discuss key concepts, challenges, and emerging trends in this rapidly evolving field.

### Key definitions for platform engineering

Platform engineering is a specific discipline focused on building and maintaining Internal Developer Platforms (IDPs). These platforms are designed to offer self-service capabilities, standardisation, and an overall better developer experience.

The Platform-as-a-Product Cycle: Platform teams act as product owners, treating their IDP as the product itself. The customers of this product are typically developers. A constant feedback loop between developers and the platform team ensures the product continually improves.
Core Goals of Platform Engineering: The practice aims for specific outcomes, including faster time to market, improved developer experience, increased reliability, standardisation, and security. Critically, a key goal is the reduction in cognitive load for development teams.
Internal Developer Platform (IDP): An IDP is the sum of golden paths. It acts as a layer that glues together different technologies and tools, abstracting away complexity to lower cognitive load. By implementing standardisation and a layer of self-service, IDPs drive compliance and security by design.

### The growing impact of AI on software delivery

AI is no longer a side project in the software industry; it is rapidly redefining how software is built, shipped, and run. Platform engineering is positioned to both shape and be shaped by this shift.

The transformation of software delivery is seen through:

Code generation and developer tooling: Tools such as GitHub Copilot help developers become more productive.
Agentic integration: AI is increasingly integrated across the entire Software Development Lifecycle (SDLC).
Automation and detection: This includes automated testing, monitoring, predictive scaling, and intelligent incident detection.

Industry adoption is strong:

73.5% of surveyed organisations view AI as playing a large role in achieving their goals.
89% of platform engineers surveyed reported using AI daily, whether for coding, documentation, or parsing logs.
70% of respondents believe AI will fundamentally reshape platforms within 12 months.

### The two pathways: Differentiating AI for PE and PE for AI

The relationship between AI and platform engineering is seen through two distinct pathways, often referred to as a "fork in the road":

The ultimate goal is the convergence of these two pathways into a holistic platform layer.

### Current state analysis and emerging trends

The current intersection of AI and platform engineering is centred on distinguishing hype from reality.

Proliferation of buzzwords: There is a continued stream of ambiguous or overlapping terms like AIOps, MLOps, GenAI, DataOps, ChatOps, and LLMOps. The main risk is becoming distracted by terminology rather than focusing on achieving measurable outcomes.
Growing expectations on platform teams: Platform teams are now expected to host and support both traditional applications and AI workloads. This requires managing complex infrastructure, such as GPU scheduling, distributed training, and large data pipelines. The customer base is expanding to include new stakeholders like data scientists, who require curated environments and specific data access.
AI regulatory environment evolution: Platform engineers are tasked with building adaptable yet secure systems that meet evolving regulations. Platforms must increasingly ensure compliance for AI workloads in areas such as data privacy, explainability, and auditability.
Future hosting of AI applications: While 25.1% of platform teams currently do not host agents or AI-infused applications, a significant majority (39.2%) report that they anticipate this becoming a requirement soon.

### Next steps

Before moving to the next module, consider the following points:

How could AI enhance the platform you currently have or the one you plan to build?
How might your platform need to evolve to support the AI workloads you are being asked to run?
What are the technical and product considerations for supporting these AI initiatives, ensuring the product you build is secure and compliant?

## Module 2: AI for platform engineering: Enhancing productivity and automation

### AI for platform engineering: Enhancing productivity and automation

This module focuses on the first directional relationship between AI and platform engineering: AI for Platform Engineering. This pathway centres on leveraging Artificial Intelligence to enhance the operational aspects, automation, and overall developer experience of an Internal Developer Platform (IDP). Using AI within platforms is a key driver for advancing platform engineering goals such as improving developer productivity, enhancing standardisation and compliance, and boosting security. AI is already widely integrated into daily workflows, with 89% of surveyed platform engineers reporting daily use. Common use cases include generating code (74.9%), producing documentation (69.7%), and creating infrastructure files (42.2%). By implementing AI, platform teams can also achieve significant benefits such as boosting Platform Return on Investment (ROI), meeting organizational goals to implement AI, and reducing operational toil.

### Intelligent use cases: From proactive observability to self-optimization

AI significantly advances platform capabilities across several critical areas, moving systems from reactive monitoring to proactive, intelligent insights. AI-driven observability uses tools like automated log analysis to parse vast quantities of data quickly, detecting trends such as memory leaks long before they cause an outage. Similarly, LLM-powered anomaly detection can summarise a week's worth of alert data into a brief readout for Site Reliability Engineers (SREs), drastically reducing alert fatigue and accelerating the Mean Time to Detection (MTTD). Furthermore, intelligent automation helps platforms self-optimize, reducing manual toil. Examples include AI forecasting traffic surges and recommending pre-scaling Kubernetes nodes to handle potential load, or using an incident bot to detect database CPU spikes, identify the problematic query, and suggest a pre-tested fix for engineering review. These automations lead to a lower Mean Time to Resolution (MTTR) and greater consistency in performance. Finally, Natural Language Interfaces and LLMs act as copilots, supporting developers, SREs, and platform engineers in generating Infrastructure as Code (IaC), configuration files, and security policies. LLMs thrive in the structured data environments provided by platform engineering, making complex concepts like infrastructure resources and logs accessible to both technical and non-technical users.

### Best practises: Mitigating risks and adopting AI responsibly

Integrating AI into platform operations is not without challenges, and platform teams must proactively understand these risks to avoid problems. Key risks include hallucinations, where models produce information that appears correct but is factually wrong or invented, posing a danger when dealing with security and infrastructure configurations. The reliability of LLM-generated code is also a concern, as it tends to be fragile and unreliable in production edge cases, potentially leading to misconfigurations or outages. Moreover, the non-deterministic nature of LLMs means the same prompt can produce different outputs on various runs, undermining automation that relies on repeatable results. To mitigate these issues, platform adoption must balance innovation with caution, focusing on safety and reliability. Best practices include implementing a human in the loop approach, treating AI as an assistant or "junior engineer" making suggestions rather than an autonomous decision maker, and requiring human review and approval for all AI-generated changes, especially before deployment. Teams should enforce strict deterministic interactions by constraining AI inputs and outputs to repeatable formats like JSON or YAML, often using low 'temperature' settings to reduce randomness. Finally, it is crucial to implement guardrails and observability for AI Agents from the start, applying Role-Based Access Control (RBAC) to AI systems, limiting data scope, logging all agent actions, and tracking AI-related metrics such as model drift and MTTR improvements to ensure measurable business impact and build trust.

## Module 3: Platform engineering for AI: Building the backbone

### Platform engineering for AI: Building the backbone

This module shifts the focus to platform engineering for AI, defined as building platforms specifically to provide a stable backbone for AI and machine learning (ML) workloads. If AI is viewed as the "rocket ship," the platform acts as the "launch pad" and "Mission Control Center," enabling AI/ML workloads from end-to-end. Platforms built for AI/ML differ from traditional Internal Developer Platforms (IDPs) as they must support unique core requirements. These include providing high-performance hardware such as GPUs, TPUs, and MPUs, along with the necessary orchestration. Key functionalities also involve dynamic resource management for training and inference processes, specialised data infrastructure for real-time streams, and providing secure, scalable serving for models in production. Critically, these platforms must enable new personas - such as data scientists and ML engineers—to efficiently develop, train, and deploy their models.

### Architectural planes of an AI-focused IDP

The architectural design of an IDP tailored for Data/AI/ML workloads is distinct, leveraging six planes of responsibility. The Observability Plane is essential for overseeing the entire system and includes unique components like Model Observability and Hallucination Detection, alongside traditional monitoring and cost tracking. 

The Data and Model Management Plane is central to AI support, containing tools and systems for Model Training, Feature Stores, Model Registry, and Model Serving. Meanwhile, the Platform Interfaces Plane must include specialized interfaces like Notebook Workspaces to accommodate data engineers and scientists, while the Integration and Delivery Plane manages complex Data/ML Pipelines which differ significantly from standard CI/CD. The Security Plane extends traditional security practices by incorporating Model Scanning to ensure compliance and understand the model's underlying data set.

### Streamlining delivery and scaling AI workloads

A core function of the platform is establishing golden paths - opinionated, standardized, and automated workflows that minimize cognitive load and provide the "path of least resistance" to achieve an outcome. For instance, a golden path allows a data scientist to request a notebook workspace, triggering complex provisioning, resource attachment, and isolation under the hood without manual intervention. 

Scaling AI applications, however, presents unique difficulties, such as dealing with bursty GPU-intensive workloads that challenge traditional scaling rules, operational unpredictability due to model drift or degradation, and the complexity of managing the entire model lifecycle. Platforms mitigate these difficulties by providing automated operational resilience (e.g., auto scaling for GPUs and automated rollbacks) and through the implementation of concepts like MLOps (automating ML workflows) and ModelOps (extending DevOps principles with emphasis on governance, monitoring, and compliance for models). This holistic approach allows the platform to reduce pain points by abstracting complexity (such as GPU orchestration) and ensuring governance is baked in by design.

## Module 4: Implementing and scaling AI platforms: Best practices and future outlook

### Implementing and scaling AI platforms: Best practices and future outlook

The last module of our course focuses on implementing and scaling AI platforms, bringing together the two main perspectives explored in the course: AI for platform engineering (enhancing platform operations) and platform engineering for AI (providing a reliable backbone for AI/ML workloads). The long-term vision is that the future is not about platforms or AI alone, but the symbiosis of both, with platforms evolving into AI-native operating environments. Many Platform Engineering teams will eventually be responsible for supporting both traditional and AI/ML workloads under a unified platform layer, making a holistic approach crucial rather than a siloed one. This convergence is logical because both pathways share core concerns such as security, observability, automation, standardization, and governance. However, merging these pathways presents distinct challenges, including security risks (like unauthorized data access or model poisoning), managing the infrastructure strain from high GPU/TPU costs, dealing with pipeline complexity (reconciling DevOps and MLOps), addressing cultural friction among different personas, and demonstrating measurable business impact (ROI).

### Best practices for responsible AI adoption

For successful adoption of AI in platform engineering, whether building smarter platforms or platforms for AI, organisations must balance innovation with caution. A critical starting point is to define your direction by matching the effort to organisational priorities: choose AI for platform engineering if the goal is efficiency and productivity, or choose platform engineering for AI if the mandate is to scale ML/GenAI capabilities. Once a direction is chosen, teams should start small, piloting safely with a Minimum Viable Platform (MVP), selecting a low-risk but high-value use case, such as GPU provisioning pipelines for PE for AI or log summarization for AI for PE. Above all, the foundation must build guardrails early using a human-in-the-loop approach, ensuring no unsupervised automation happens in production. This involves being security-first (e.g., implementing RBAC for AI agents and sanitizing data feeds) and establishing observability from day zero (logging prompts, outputs, and agent actions). Success is ultimately defined by measurable business impact and building trust in the AI-powered or AI-backing platform.

### Key future trends in platform engineering and AI

Looking ahead, the direction is clearly toward convergence. Several key trends are expected to define the future of software delivery and operations. We anticipate the rise of Self-optimizing platforms, which embed AI agents to dynamically allocate resources, tune policies, and optimize performance and cost in real-time without continuous human intervention. This leads naturally to the development of AI-native IDPs, where AI copilots, automated security agents, and observability assistants are built directly into the control plane rather than being mere add-ons. Furthermore, the divide between DevOps and MLOps pipelines will dissolve into Unified workflows, offering a single platform experience for all users (app developers, ML engineers, data scientists). Finally, increasing regulation (such as the EU AI Act) will drive a Governance-first design, forcing platforms to embed compliance and ethical guardrails by default. Future platforms will also begin to treat AI agents as a proper platform persona, complete with assigned permissions, quotas, and policies, just like their human engineering counterparts.
