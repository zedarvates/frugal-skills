---
name: tool-route-review
description: "Plan a bounded, cheaper and safer tool route using stated capabilities, constraints and evidence. Use for consultative tool selection, not automatic routing or execution."
---
# Tool route review (advisory only)

1. Identify the requested operation, required accuracy, privacy boundary, side effects, and verification criteria.
2. List eligible mechanisms: existing verified result, deterministic calculation, local script, local small model, external API, human review.
3. Eliminate mechanisms without the needed capability, permission, security or evidence. An alleged cheap route is not automatically safe.
4. Compare surviving routes using **provided** cost, latency, quality and availability observations. If costs are unknown, write `unknown` and abstain from ranking by price.
5. Propose one route and fallback, with exact verification that would determine success or escalation.
6. Do not call tools, buy credits, change permission boundaries, publish code, merge, or access a machine without explicit authorization.

Distinguish observed evidence from an estimate. No savings or accuracy benchmark is implied by this skill.
