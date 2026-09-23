# ADK Harness Optimization Samples

These samples showcase various ways to optimize your harnesses - I believe they are all self-explanatory!

## How to Run

First, you need to add a .env to each agent directory. It should contain:
````
GOOGLE_GENAI_USE_ENTERPRISE=1
GOOGLE_CLOUD_PROJECT=your-gcp-project
GOOGLE_CLOUD_LOCATION=global
````
Then you can easily run the samples via the ADK Web UI (Dev UI).

```bash
uv sync
uv run adk web --allow_origins "*"
```

Just pick your sample from the dropdown at the top.