# Third-party notices

Botte Secrète adopts ideas, interfaces, interoperability contracts and independently
written tests from other projects. This file records every external source the
skills draw on, what was taken, and what still has to be verified before any part
of this catalog is redistributed.

## Policy

This restates the standing boundary (internal register MEM-018):

- Adopting **ideas, interfaces, contracts and independently written tests** is
  permitted.
- Any **copied source** requires a provenance review and retention of the
  applicable licence and notices.
- **Copyleft and permissive code must not be silently relicensed.** Apache-2.0
  material must never be presented as if it were MIT-only, and vice versa.
- **Prefer clean, independently written implementations** of an identified
  contract over importing someone else's code.

## Status legend

| Status | Meaning |
|---|---|
| VERIFIED | Licence confirmed against the upstream repository, and the use is compatible. |
| TO CHECK | Upstream identified, licence not yet confirmed. |
| BLOCKED | Upstream not even identified, or the use is a text adaptation. Must be resolved before publication. |
| LOW | Concept or paper only, or an external dependency that is never redistributed. |

## Summary

| Source | Used by | Form of use | Licence | Status |
|---|---|---|---|---|
| DietrichGebert/ponytail | decision_ladder, harvest | ladder ordering, benchmark corrections | MIT | VERIFIED |
| rtk-ai/rtk | rtk, harvest | external CLI plus interoperability contract | Apache-2.0 | VERIFIED |
| Caveman (project not identified) | caveman | output-style levels | unknown | **BLOCKED** |
| multica-ai/andrej-karpathy-skills | karpathy-guidelines | adapted text | unknown | **BLOCKED** |
| MITRE CWE | cwe_kb | CWE catalogue entries | MITRE terms | **TO CHECK** |
| RepoAudit / DeepAudit | fallow_like, cwe_kb | analyzer set and CWE pairing | unknown | **TO CHECK** |
| Headroom | botte_proxy, universal_compressor | proxy mode, multi-type compression | unknown | TO CHECK |
| shadcn/improve | directives_audit | the "recon" step | unknown | TO CHECK |
| Omnigent | meta_harness | governed multi-agent pipeline concept | unknown | TO CHECK |
| Stanford AutoMem | auto_memory | memory-as-capability concept | unknown | TO CHECK |
| fallow-cli | fallow | external analyser | unknown | LOW |
| oculix-org/Oculix, SikuliX | app_test | external jar, downloaded by the user | upstream | LOW |
| Microsoft FastContext | fast_context | concept only, model not used | upstream | LOW |
| Google Co-Scientist, Red Teaming LLM, adversarial multi-agent literature | cardinal | red-team concepts | papers | LOW |
| Mark Kashef and Anthropic, "A Harness for Every Task" | dynamic-workflows | orchestration patterns | upstream | LOW |
| Google OR-Tools | context_budget, decision_ladder | 0/1 knapsack idea, no code | Apache-2.0 | LOW |

## Verified sources

### DietrichGebert/ponytail — MIT

- Upstream: https://github.com/DietrichGebert/ponytail
- Reviewed snapshot: main at 16f29800fd2681bdf24f3eb4ccffe38be3baec6b
- What is used: the ordering of the "does this need to exist at all" ladder, and
  corrections to benchmark methodology and adapter drift.
- What is deliberately **not** taken: the upstream persona, and any arrangement
  where a prompt itself acts as an execution gate. Botte keeps deterministic
  policy authority.
- Obligation: MIT attribution and licence retention apply if any upstream text is
  reproduced. The current use is ideas and contracts, not copied text.

### rtk-ai/rtk — Apache-2.0

- Upstream: https://github.com/rtk-ai/rtk
- Reviewed release: v0.44.2. Snapshot commits are recorded for master and develop
  in the internal register.
- What is used: an external command wrapper, plus an interoperability contract.
  Botte integrates the tool externally and implements its own wrapper.
- Obligation: Apache-2.0 notices and licence retention apply to any copied
  source. Nothing from this project is redistributed here.

## Blocked — resolve before publication

### Caveman

The caveman skill states that it was inspired by a project referred to only as
"Caveman (69k stars on GitHub)". No repository URL is recorded. Under the policy
above this cannot ship until the exact upstream is identified and its licence
read. If the upstream is not permissively licensed, the skill text needs to be
rewritten as an independent implementation of the idea.

### multica-ai/andrej-karpathy-skills

- Upstream: https://github.com/multica-ai/andrej-karpathy-skills
- What is used: the four principles in karpathy-guidelines, described as
  **adapted**, which is closer to a derivative work than to an adopted idea.
- Obligation: confirm the upstream licence and attribution wording, or rewrite
  the file as an independent statement of the same practices.

## To check

For each entry below: open the upstream, read the licence file, record the licence
identifier here, and state whether the use is compatible.

- **MITRE CWE** — cwe_kb ships a small CWE catalogue. Confirm what text is
  redistributed and under which MITRE terms, as opposed to referencing CWE
  identifiers only.
- **RepoAudit / DeepAudit** — cited as the inspiration for the analyzer set and
  the taint-plus-explanation pairing. Identify the exact repositories.
- **Headroom** — cited for the proxy mode and for multi-type compression.
  Identify the exact project.
- **shadcn/improve** — cited for the "recon" step in directives_audit. Identify
  the exact repository.
- **Omnigent** — cited as the inspiration for meta_harness, whose implementation
  is described as entirely its own. Identify the exact project and confirm that
  no code was copied.
- **Stanford AutoMem** — cited as the inspiration for memory-as-capability.
  Identify whether this is a paper or a repository, and its terms.

## Low risk

- **fallow-cli**, **OculiX / SikuliX**, **Microsoft FastContext** and the
  **red-team literature** are either external tools the user installs themselves
  or concepts described in papers. Nothing from them is bundled here. Keep them
  in this file for completeness and re-check if any of their code is ever copied.
- **Google OR-Tools** informs the knapsack approach in context_budget. Only the
  algorithmic idea is used; no OR-Tools code is present.

## How to keep this file current

1. Any new skill that states an external inspiration gets an entry here in the
   same change.
2. Status moves from TO CHECK to VERIFIED only with the licence identifier and
   the repository URL recorded.
3. A BLOCKED entry blocks publication of the affected skill, not of the whole
   catalog: the skill can be held back from the published set.
