# Observability for Platform Engineering

## Module 1: Observability foundations for platform engineers

### The origins of observability

The concept of observability grew out of the need to address what traditional monitoring, application performance management (APM), and log analytics couldn't handle. It represents a conceptual evolution driven by technological advancements and the specific requirements of cloud-native applications.

Originally, observability was defined as a property of a system: if you can deduce its internal state by querying it from the outside, then it is observable. This system aimed to provide understanding into why an issue occurred, rather than merely identifying that an issue exists.

The term gained popularity in the tech world around 2016, spearheaded by Charity Majors and Ben Sigelman, who drew insights from the effective monitoring and troubleshooting strategies employed at companies like Facebook and Google. Observability is seen as a bringing together of previous practices, including APM, log analytics, infrastructure monitoring, real user monitoring (RUM), synthetic monitoring, and profiling, combined into a unified approach.

Despite its well-intentioned original meaning, the term has regrettably lost much of its precision due to marketing and is often used interchangeably with monitoring. Nonetheless, for platform engineers, observability remains crucial for comprehending system behavior, efficiently diagnosing incidents, and ensuring a superior developer and end-user experience.

### Observability or monitoring?

Observability is fundamentally a property of a system, allowing you to deduce its internal state by querying it from the outside. It signifies a conceptual evolution designed to overcome the limitations of traditional monitoring, Application Performance Management (APM), and log analytics, especially crucial for cloud-native applications.

Conversely, monitoring is the practice of collecting and processing telemetry - such as metrics, logs, and traces - with the aim of achieving observability. While often confused due to marketing, monitoring typically indicates what is happening, whereas observability delves into why it is happening.

If monitoring tells you something is wrong, observability tells you why. 

### The different types of telemetry

Telemetry, often referred to as signals, represents the data collected and processed to achieve observability. Traditionally, telemetry was conceptualized around the "three pillars": logs, metrics, and traces. However, modern observability now treats these, and other types, as signals that must seamlessly work together, rather than standalone silos.

Types of telemetry (signals):

Logs: Descriptions of events at a specific point in time, providing detail and error context. They can be structured and linked to a trace.
Metrics: Quantitative measurements collected as time series (e.g., counters, gauges, histograms), which are effective for showing trends, anomalies, and alerting.
Traces: Represent a single user transaction's journey through a distributed system, composed of multiple spans (individual units of work). They show how requests flow across services, highlighting latencies and dependencies.
Profiles: Reveal CPU or memory consumption at runtime to pinpoint bottlenecks.
Real User Monitoring (RUM): Collects information on how end-users interact with applications, providing full visibility into feature behaviour in the wild.

Important to consider: Telemetry without context is just data.

### Why semantic conventions matter

Semantic conventions are standardized naming rules for telemetry metadata, defining a common vocabulary for logs, metrics, and traces. They are crucial for ensuring consistency, portability, composability, and actionable data across services, teams, and platforms.

Without these conventions, different teams naming things inconsistently leads to conflicting analyses, broken dashboards, and chaotic troubleshooting during incidents. This consistency is vital for effective correlation across diverse telemetry signals, especially in complex, multi-team environments. OpenTelemetry provides and advances these conventions, forming a foundation for interoperability and predictable observability.

### Why should platform engineers care about observability?

Platform engineers must care about observability because it is fundamental to their success in managing today's increasingly complex, cloud-native systems. Their role involves taking care of the increasing levels of complexity underpinning applications, which feature many moving parts and failure modes.

Observability empowers platform engineers to:

Deliver a good developer experience through their platform.
Detect and troubleshoot issues fast, ensuring that fixes are truly effective.
Provide confidence to deploy faster and resolve incidents quicker.
Help developers deliver a good user experience to their end-users.

### Observability and Platform-as-a-Product

Platform engineers treat their platform as a product, with developers as their customers. In this "platform as a product" mindset, observability is a core feature rather than a mere checklist.

By viewing observability as a core product feature of the platform, they can abstract complexity, enforce standards, and provide paved paths for developers, ultimately reducing toil and scaling their impact. Key elements include:

Auto-instrumentation: Often via the OpenTelemetry Operator, it provides telemetry without requiring code changes, reducing developer toil.
Enforced Semantic Conventions: Ensures consistent, queryable, and portable telemetry metadata across teams.
Default dashboards and alert rules: Offers ready-to-use analysis tools, sometimes managed as code (e.g., Perses).
Correlation: Logs, metrics, and traces are pre-wired and correlated, simplifying troubleshooting.
Ultimately, this reduces friction for developers, allowing them to focus on business logic while ensuring reliable and consistent insights.

## Module 2: The platform engineer's dual role in observability

### The two roles of a platform engineer in observability

Platform engineers hold a dual responsibility when it comes to observability: they must both observe the platform itself (e.g., Kubernetes clusters, CI/CD pipelines) and enable product teams to observe their own applications.

Observing the platform: When we talk about observability for platform engineers, it’s not just about our applications - it’s about an entire, interconnected ecosystem.

Platform engineers must monitor the platform infrastructure itself.
Key activities include tracking system health, resource usage, and errors, as well as detecting degraded nodes, analyzing autoscaler behavior, and validating rollout health. This builds confidence for safe deployments and provides understanding of the platform's behavior.

Enabling developers:

Platform engineers are also tasked with providing observability as a service to application teams. This means ensuring developers receive essential telemetry like metrics, traces, and logs by default.
This involves offering pre-configured auto-instrumentation (often through tools like the OpenTelemetry Operator and annotations), access to ready-to-use dashboards, and ensuring all telemetry signals are correlated out of the box.

### The main challenges in platform observability

Platform engineers face major observability challenges because of the growing complexity of modern, cloud-native systems. A key problem is telemetry without context, where data lacks clear definition, origin, or relationships, leading to quick and wrong conclusions during outages.

Lack of telemetry consistency across applications and environments is another big obstacle. Without standardized semantic conventions, different teams define and name telemetry differently, resulting in conflicting analyses, broken dashboards, and messy troubleshooting. This gets worse with tool fragmentation, vendor lock-in, and proprietary query languages, making it tough to get unified insights.

On top of that, manual instrumentation doesn't scale, causing bottlenecks, errors, and repeated work. Platform engineers also deal with tooling drift, where custom dashboards no longer match reality, and lack of impact analysis, making it hard to connect platform issues to user-facing problems. These challenges get in the way of effective incident response and deployment confidence.

### A day in the life: Incident flow

This would be a smooth troubleshooting process made possible by connected observability signals. It usually happens like this:

An alert fires from ingress metrics, indicating a latency spike on checkout.
A trace then shows a slow downstream service in a specific region, pinpointing the source of the slowdown.
Logs attached to that trace reveal a new feature rollout missing cache headers, identifying the root cause.
A rollback is triggered, and its successful validation is confirmed by RED metrics.

This efficient incident response only works when telemetry is consistent and correlated across all layers. 

### The superpower of correlation

Correlation is key in observability, directly addressing many of the previously mentioned challenges.

When metrics, logs, traces - and increasingly profiling data and real user monitoring - all share the same context, we can connect events from the client all the way through the backend.

Imagine spotting a frontend slowdown in RUM, linking it directly to a backend trace, and then using profiling data to pinpoint the CPU bottleneck in the service. That kind of end-to-end correlation shortens troubleshooting dramatically and gives a much clearer picture of real user impact.

## Module 3: The open source observability tool landscape

### The OSS observability puzzle

The OSS (Open-Source Software) observability tool ecosystem is broad and still evolving. Part of our role as platform engineers is to understand enough about these tools to make informed decisions about what to include in our stack.

This is the CNCF Observability tool landscape: 

<this-is-the-cncf-observability-tool-landscape-page>

A way to approach it is to understand which open-source observability tools can fit together to form a working stack. Putting together a puzzle helps platform engineers understand how to build a flexible, vendor-neutral, and future-proof observability system.

We will discuss the following puzzle.

<puzzle-image-example-for-the-tehcnologies-below>

Prometheus for storing metrics.
OpenSearch for storing logs.
Jaeger for storing traces.
Perses for dashboards.
OpenTelemetry acts as the "glue", collecting, processing, and exporting telemetry to these different backends, enabling correlation.

While OpenTelemetry connects these systems at the ingestion and processing layer, it is important to note that each backend still operates independently, possessing its own UI, query language (e.g., PromQL for Prometheus, Piped Processing Language for OpenSearch), and data model. This flexibility allows for choosing "best of breed" components but introduces complexity, as teams must learn multiple tools and platform engineers must ensure they work seamlessly together.

### Introducing OpenTelemetry

OpenTelemetry (OTel) is a vendor-neutral, open-source project within the Cloud Native Computing Foundation (CNCF) that provides a comprehensive set of APIs, SDKs, and tools to instrument, generate, collect, and export telemetry data. It defines data models and a wire format (OTLP) for transmitting telemetry, as well as semantic conventions to ensure consistent metadata across systems.

OTel is not a proprietary all-in-one observability tool or a query language; instead, it acts as "the glue" that standardizes how telemetry (logs, metrics, traces, profiles, and real user monitoring) is collected, structured, and transmitted to various backends. Its core components include APIs, SDKs, and the OpenTelemetry Collector, a versatile tool for processing, filtering, and routing telemetry.

By adopting OTel, organisations can instrument once and export anywhere, removing vendor lock-in and allowing them to choose best-of-breed backend tools like Prometheus, Jaeger, and OpenSearch. This approach ensures portability, consistency, and future-proofs observability practices, making it a foundation for modern observability pipelines.

OTel is notably the second largest CNCF project by official metrics and by contributors.

### Prometheus, Jaeger, OpenSearch, Perses: Metrics for modern systems

As mentioned, the OSS observability “puzzle" proposes a way that Prometheus, Jaeger, OpenSearch, and Perses combine to form a comprehensive open-source observability stack for modern systems.

Prometheus serves as the de facto standard for metrics in cloud-native environments, known for its pull-based model and powerful PromQL query language, ideal for detecting infrastructure anomalies.
Jaeger is an open-source distributed tracing system, visualizing requests as they traverse multiple services, highlighting performance bottlenecks, latencies, and errors.
OpenSearch provides scalable log storage and search capabilities, derived from Elasticsearch, and is a popular choice for centralized logging.
Perses focuses on dashboards-as-code, allowing dashboards to be defined in YAML, versioned in Git, and deployed via CI/CD, aiming for vendor-neutral and portable visualizations.

OpenTelemetry acts as the "glue", collecting, processing, and exporting telemetry (metrics, logs, traces) to these different backends, enabling correlation. While this stack offers flexibility and "best-of-breed" components, it also presents challenges due to each tool having its own UI, query language (e.g., PromQL, Piped Processing Language), and data model.

### Demo: Observability tools in action

In this lesson we have seen a quick demo of how Prometheus, Jaeger, OpenSearch, Perses and OpenTelemetry all work in action. You can also try it out for yourself in the “Observability for Platform Engineering” repository here: https://github.com/dash0hq/observability-for-platform-engineering-course

### PromQL: the platform engineer’s language

PromQL is often called the "lingua franca" of the cloud-native observability world, serving as the shared query language for platform engineers. It is expressive, composable, and battle-tested, with years of production use. Its widespread familiarity means most engineers (and all LLMs) already know how to write it, simplifying onboarding and analysis.

Platform engineers rely on PromQL for their day-to-day work, particularly for metrics-based monitoring and detecting infrastructure anomalies like high CPU usage. Some observability platforms even extend PromQL to query other signals like logs and traces, reducing cognitive load and context switching for developers. This fluency is crucial for faster incident response and building consistent, reusable query patterns.

### OSS Tools: 3 signals, 3 interfaces

One of the realities of today’s OSS observability stack is that you don’t just have different tools: you also have different query languages and interfaces for each signal.

For example:
• Prometheus uses PromQL for metrics.
• OpenSearch uses Piped Processing Language (PPL) for logs.
• Jaeger relies on UI-driven filtering for traces.

This means platform engineers, and often developers, have to context-switch between different mental models when working with telemetry. The lack of a standard query language across all signals is a big barrier to a unified observability experience.

### OSS vs. Open Core: choose the right model

When selecting observability tools, platform engineers must understand the distinction between truly Open Source Software (OSS) and Open Core models.

Open Core tools often appear open but reserve many key features behind a commercial paywall. This can lead to vendor lock-in for critical functionalities.
Truly open tools, such as Prometheus and Perses, are typically governed by organisations like the CNCF, with their entire feature set being community-driven, portable, and extensible.

It is crucial to evaluate governance, community activity, and licensing terms, not just the project's superficial "open-source" label. Choosing the right model directly impacts your ability to maintain portability, extendibility, and adapt your observability stack long-term without commercial constraints.

## Module 4: Demystifying OpenTelemetry

### OpenTelemetry as the standard

OpenTelemetry (OTel) has emerged as the standard for collecting telemetry in modern systems, becoming the second largest CNCF project by many metrics, after Kubernetes, see below the CNCF open source tooling ecosystem, also here.

<imagem-for-cncf-velocity>

Its widespread adoption is driven by several key factors:

Vendor-Neutrality: OTel provides a non-proprietary approach to telemetry collection, eliminating vendor lock-in by standardizing how data is generated and transmitted. This allows organisations to instrument once and export anywhere, choosing best-of-breed backend tools.
Comprehensive Signal Support: It supports metrics, logs, traces, and is expanding to profiling and real user monitoring (RUM), offering a unified API for all telemetry types.
Semantic Conventions: OTel defines standard naming rules and attributes for telemetry metadata, ensuring consistency, portability, and composability across teams and systems.
OpenTelemetry Collector: This "Swiss army knife" centrally collects, processes, filters, and routes telemetry, providing a powerful policy enforcement layer for data hygiene and cost control.

By standardizing telemetry collection and structuring, OTel future-proofs observability practices and empowers platform engineers with control and flexibility.

### Why OpenTelemetry?

Before OTel, every vendor had their own SDK and format: logs, traces, and metrics lived in silos; some vendors still use proprietary formats, and you should think long and hard about whether to accept it. This created duplication, inconsistent data, and vendor lock-in.

The "why" behind OTel's design is to eliminate vendor lock-in and promote an open ecosystem. Historically, proprietary SDKs and formats created data silos and made changing vendors a massive undertaking. OTel replaces this with a vendor-neutral, shared model, allowing organizations to instrument once and export anywhere.

It supports metrics, logs, traces, profiles, and real user monitoring (RUM) through consistent APIs and the Collector. By enforcing semantic conventions, OTel ensures telemetry metadata is consistent, portable, and composable. This decouples instrumentation from backend tools, offering flexibility to choose best-of-breed solutions and future-proof observability practices.

### Spans and traces

In OpenTelemetry, traces represent a single user transaction or workflow as it travels through a distributed system, providing a complete map of its journey. They consist of multiple spans, each an individual unit of work (e.g., an HTTP request or database query). Spans have a hierarchy in terms of “which happened first”, which are called parent-child relations.

Spans include operation names, timestamps, duration, and metadata, linking hierarchically to show cause and effect. This concept originated in Google's Dapper paper. Trace context propagation is crucial, linking logs and metrics (via exemplars) to traces, enabling automatic correlation and comprehensive system visibility.

<image-span-and-traces>

### Logs in OpenTelemetry

OpenTelemetry (OTel) considers logs a core telemetry signal, representing an event description at a specific point in time. OTel primarily handles logs as structured data, though raw strings are also supported. A crucial feature is their ability to link to a span in a trace by including its trace ID and span ID. This enables automatic cross-signal correlation, ensuring logs become part of the same story as the request that generated them, contributing to full cross-signal observability when combined with context.

### Metrics in OpenTelemetry

OpenTelemetry (OTel) treats metrics as a core telemetry signal, collecting time series data.

OTel metrics are structured, correlated, and flexible, similar to Prometheus. They are meant to collect time series:

Counter: accumulates over time, e.g., number of requests
UpDownCounter: increases or decreases, e.g., concurrent sessions
Gauge: snapshot of a value, read at the time of export
Histogram: aggregates value distributions, e.g., request latency
Asynchronous instruments: for when you don’t control the increment, e.g., reading memory usage directly

<image-metrics-in-otel>

### Resources

In OpenTelemetry, resources are metadata that describe the origin of telemetry, such as a process, container, or Kubernetes pod. They are defined by attributes like service.name, cloud.region, or k8s.pod.name.

These resources apply to all telemetry signals (logs, metrics, traces). OpenTelemetry uses semantic conventions to standardise these attributes, ensuring consistency across systems. This enables meaningful grouping, filtering, and joining of telemetry, which is crucial for multi-team, multi-tenant, and multi-cluster environments.

### Semantic conventions = consistency

Semantic conventions are OpenTelemetry's standardised way of describing telemetry metadata, defining a common set of attributes for consistency across services and teams. They ensure telemetry is portable, composable, and actionable, enabling meaningful grouping, filtering, and cross-signal correlation.

Without them, teams invent custom labels, leading to conflicting analyses, broken dashboards, and hindered observability. Examples include service.name and http.response.status_code.

### The OpenTelemetry Collector: Your pipeline engine

The OpenTelemetry (OTel) Collector functions as the central router and policy enforcement layer in an observability architecture, often described as a "Swiss army knife" or the "pipeline engine" for telemetry. Its architecture is built around Receivers, Processors, and Exporters.

Receivers enable it to ingest telemetry in various formats, such as OTLP or Prometheus. Processors allow for filtering, batching, transforming (e.g., redacting sensitive data with OTLP, enriching with attributes), and sampling telemetry. Finally, Exporters forward the processed data to one or multiple destinations, like Prometheus, Jaeger, OpenSearch, or various observability backends.

<image-otel-collector-pipeline>

This modular design empowers platform engineers to build robust and flexible telemetry pipelines. It enables cost control through filtering and sampling, ensures data compliance via redaction, and promotes metadata consistency without requiring application code changes.

The Collector decouples instrumentation from backend tools, centralizes control, and allows organizations to easily experiment with different observability solutions.

### OpenTelemetry Operator and auto-instrumentation

The OpenTelemetry (OTel) Operator is crucial for managing OTel Collectors at scale on Kubernetes, effectively running fleets of collectors. Its primary function is to enable auto-instrumentation (also known as automatic injection or no-touch instrumentation), which is key to rapidly adopting OTel by injecting OTel SDKs or agents into application pods at runtime.

This process often uses Kubernetes pod annotations, allowing platform engineers to deploy observability without developers needing to modify source code. It works effectively for languages such as Java, Python, and .NET, automatically capturing telemetry from frameworks and libraries. For compiled languages like Go, eBPF can be considered, though it has security implications.

Auto-instrumentation removes friction for developers, ensuring consistent telemetry coverage and providing a healthy baseline of observability by default. This approach allows platform engineers to scale observability across an organisation, making it an invisible, effortless platform capability.

## Module 5: Simplifying observability with automation and standards

### How to scale observability

To scale observability effectively, it must be treated as a platform capability, baked into the infrastructure with automation, standards, and defaults. Manual instrumentation is time-consuming and prone to errors, leading to inconsistencies and duplication.

Platform engineers reduce toil by automating instrumentation, routing, and processing telemetry, ideally making observability invisible and effortless for developers. Key strategies include:

Auto-instrumentation via the OpenTelemetry Operator, which injects OTel agents into applications using Kubernetes annotations, providing a consistent baseline without code changes.
Treating dashboards and alerts as code (e.g., with Perses) by defining them in YAML, versioning in Git, and deploying via CI/CD for reproducibility.
Enforcing semantic conventions to standardize telemetry metadata, ensuring consistency, queryability, and portability across teams and services.
Utilizing the OpenTelemetry Collector as a central pipeline engine for receiving, processing, filtering, redacting, and routing telemetry, enabling cost control and data compliance at the platform layer.

By providing paved paths and sensible defaults, platform teams empower developers with reliable insights, shifting their focus from observability setup to building features.

### GitOps for dashboards and alerts

One of the most ignored parts of observability is how we handle dashboards and alerts.

Too often, these exist only in someone's browser or in a monitoring tool's interface, making them difficult to track, review, or get back if they disappear. When we treat dashboards and alerts as code, we can use the same organized workflow we already use for infrastructure and application code. This means defining dashboards and alerts in declarative formats, typically YAML, then storing them in Git, allowing for version control, review via pull requests, and deployment through CI/CD pipelines.

Projects like Perses enable "Dashboards-as-Code", where dashboard definitions can live in Git, be reviewed, and even reused across vendors supporting its specification. Similarly, the Prometheus operator facilitates alerts-as-code through Prometheus rules. This approach ensures changes are reproducible, transparent, and recoverable, eliminating manual UI edits that can easily be lost or untracked. It reduces toil and promotes consistency across teams and environments.

### Auto-instrumentation with OpenTelemetry

Auto-instrumentation with OpenTelemetry is a crucial method for scaling observability by collecting telemetry without developers modifying application code. It leverages language-specific agents (e.g., Java, Python, .NET) to automatically capture telemetry from frameworks, libraries, and runtimes.

When combined with the OpenTelemetry Operator on Kubernetes, these agents can be automatically injected into application pods via annotations. This approach removes friction for developers, ensuring consistent telemetry coverage and a healthy baseline of observability by default. Platform engineers can deploy observability across an entire workload fleet effortlessly, allowing developers to focus on business logic.

### Data control for platform engineers

The OpenTelemetry (OTel) Collector functions as the central policy enforcement layer for telemetry, enabling platform engineers to exert data control over the flow and quality of observability data. It empowers them to implement crucial policies before data reaches backends. It covers:

Dropping or filtering debug logs in production to reduce noise and control costs.
Redacting sensitive fields (e.g., user.email) to ensure data compliance with privacy regulations.
Enriching telemetry by adding attributes like deployment.environment.name for better context.
Sampling traces to manage data volume without losing critical insights.

This centralization allows for telemetry hygiene and consistency at the platform layer, without requiring application code changes, offering a robust and flexible approach to observability management.

### Provide defaults, allow overrides

When scaling observability across an organization, finding the right balance between control and flexibility matters a lot. As platform engineers, we can offer paved paths, like auto-instrumentation, default dashboards, and shared alert templates. These ensure teams get value out-of-the-box without having to figure everything out from scratch.

But flexibility matters too. Teams should be able to change these defaults when their specific needs require it. The key is making the defaults strong enough that most teams won't need to modify them. This approach reduces friction, creates more consistency, and still gives developers the freedom to customize when they need to.

### Observability becomes infrastructure

Platform engineers don't just keep observability systems running; they deliver observability as infrastructure. This means teams can use telemetry the same way they use compute, storage, or networking: when they need it, without asking anyone, and in a consistent way.

The features mentioned here - self-service telemetry, standardized collection, reliable dashboards, and guardrails for compliance - are what make observability part of the platform's core foundation, not something added later. And when it's done well, it’s invisible to developers: they focus on building, not babysitting dashboards or wrangling data pipelines.

### Build the platform, not the dashboard!

Platform engineers should build the platform, not the dashboards!. Their role is to establish the foundational capabilities that make observability effortless and scalable for development teams. This includes automating instrumentation (e.g., via the OpenTelemetry Operator), managing data pipelines through the OTel Collector, and enforcing semantic conventions for consistent telemetry.

By providing default dashboards (e.g., with Perses), platform engineers empower teams with out-of-the-box insights, allowing developers to focus on building features rather than wrestling with observability setup.

### Final demo

In this lesson we have seen a quick demo, try it out for yourself in the “Observability for Platform Engineering” repository created for you here: https://github.com/dash0hq/observability-for-platform-engineering-course
