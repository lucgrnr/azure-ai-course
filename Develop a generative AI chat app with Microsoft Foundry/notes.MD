# Choosing between the Foundry SDK and OpenAI SDK
Microsoft Foundry supports two approaches for building AI applications. Each serves different purposes, and understanding when to use each one helps you build the right solution.

## When to use the Foundry SDK
Use the Foundry SDK when your application needs Foundry-specific capabilities:
* Foundry Agent Service for building and managing AI agents
* Tool invocation and approval workflows
* Cloud evaluations for testing and validating AI responses
* Tracing and observability for monitoring application behavior
* Foundry direct models (non-Azure OpenAI models available through the model catalog)
* Project metadata, connections, and governance features

Microsoft recommends the Foundry SDK when building apps with agents, evaluations, or Foundry-specific features.

## When to use the OpenAI SDK
Use the OpenAI SDK when you need maximum compatibility with the OpenAI API:
* Full OpenAI API compatibility for existing code and tooling
* Portability between OpenAI and Azure OpenAI deployments
* Chat Completions, Responses, and Images APIs
* Minimal dependency on Foundry-specific concepts

The OpenAI SDK is ideal for model inference workloads where you want existing OpenAI code to work with minimal changes. However, this approach doesn't provide Foundry-specific features like agents or evaluations.

Microsoft Foundry gives you flexibility in how you build AI applications. Use the Foundry SDK with AIProjectClient when you need project-level features like agents, evaluations, tracing, and connections. Use the OpenAI SDK when you need straightforward model inference with maximum OpenAI compatibility. Both SDKs work with your Foundry project endpoint, so you can combine them as needed in your applications. You can also use both SDKs together in the same application—the Foundry SDK for project features and the OpenAI SDK for model inference.