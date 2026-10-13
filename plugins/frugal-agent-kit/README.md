# Frugal Agent Kit — OpenAI directory pilot

This directory is the **source** of a skills-only plugin for the universal ChatGPT/Codex Plugins Directory.

- No hosted MCP, account connection, paid credits, Python dependency, executable tool or telemetry is included in the submitted package.
- The plugin offers consultative context triage, low-cost route review and completion-evidence review.
- It is **not** the entire Frugal Skills catalog; outstanding third-party provenance items are excluded.

## Build

From the repository root:

```bash
python plugins/frugal-agent-kit/build_package.py
```

This verifies the manifest, skill headers, resource paths and SVG assets and creates `plugins/frugal-agent-kit/dist/frugal-agent-kit-openai-submission-v0.1.0.zip`, adding the repository root MIT LICENSE. It performs **local static validation only**, not OpenAI portal checks.

## Submit (human / portal action)

1. Open https://platform.openai.com/plugins and select the intended project.
2. Verify the publishing identity and organizational permissions.
3. Upload the generated ZIP as a new plugin draft.
4. Review automated **Metadata & Skills** findings and correct any issues before submitting.
5. Test each user prompt and keep the plugin read-only; verify what it actually does.
6. Submit the draft for OpenAI review; on approval, explicitly publish it.

More details: https://developers.openai.com/plugins/deploy/submission

This change does not submit, publish, merge, connect infrastructure, or incur costs.
