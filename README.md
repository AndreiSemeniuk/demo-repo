# agent-platform-demo

A demo of a **GitHub Actions–driven agent platform**. Everything is placeholder — no workflow
deploys anything real. Steps are `echo` + short `sleep`, so each run finishes in under a minute
and produces realistic logs and a polished job summary.

## The two-click flow

1. **Actions → Create Agent Project → Run workflow**
   Pick a department, name the agent, choose `prompt` or `hosted`. The run scaffolds the project
   files and (unless `dry_run`) "opens" a pull request — see the link in the job summary.
2. **Actions → Deploy / Destroy Agent → Run workflow**
   Pick the agent and environment. The run validates config, builds and pushes an image,
   deploys, assigns roles and polls until the agent is active — then gives you an
   **Open in Playground** link.

Shared tools (MCP servers) are shipped separately with **Deploy / Destroy Utils**.

## Workflows

| Workflow | File | Inputs |
|---|---|---|
| Create Agent Project | `.github/workflows/create-agent-project.yml` | department, agent_name, agent_kind, sharepoint_site_url, dry_run |
| Deploy / Destroy Agent | `.github/workflows/deploy-agent.yml` | action, agent_name, environment, provision_toolbox, dry_run |
| Deploy / Destroy Utils | `.github/workflows/deploy-utils.yml` | action, util_name, environment, dry_run |

All workflows succeed with their default inputs.

## Repository layout

```
projects/
  logistics/
    config.yaml                      # department config: environments, defaults
    agents/
      logistic-agent/
        agent.yaml                   # model, tools, knowledge
        agent.manifest.yaml          # environments, roles, toolbox, evaluation
        system_prompt.md             # agent instructions
    shared/
      utils/
        shipping-mcp/                  # shared MCP server (container app)
          main.py
          Dockerfile
          requirements.txt
```

> All IDs, URLs and resource names are placeholders (`00000000-…`, `*.example.com`).
