# AdamPlatin123

**Agent Harness · Developer Tools · Open Source**

Undergraduate in Bioinformatics at DUT (2023–2027, class of 2027). My technical throughline: building agent runtimes, plugin verification pipelines, and developer tooling around **reliability, security boundaries, and verifiable execution**.

> 🔍 **Open to work**: Agent / Harness R&D and tech-DevRel internships in mainland China · class-of-2027 campus hiring
> 📧 [AdamPlatin123@outlook.com](mailto:AdamPlatin123@outlook.com)

---

## Featured Engineering

### [dsh-plugin-radar](https://github.com/AdamPlatin123/dsh-plugin-radar) · ★1,468 · Owner · Python/Shell

Independently built **verification pipeline for the DeepSeek Harness plugin ecosystem**: multi-source discovery (GitHub/npm, 18,000+ candidate repos) → identity normalization & deduplication → **Kubernetes-isolated execution (one pod per plugin; 13,000+ cumulative runtime-level tests across 9,200+ located repos)** → result classification with 15-minute snapshot publishing. The plugin directory on GitHub is pipeline-generated, not a hand-curated list; verdicts are exposed through a schema-stable interface (`dsh-radar/v1`) that plugin marketplaces and community lists consume directly. Reached GitHub Trending daily #22.

→ [Engine source engine/](https://github.com/AdamPlatin123/dsh-plugin-radar/tree/main/engine) · [Architecture doc](https://github.com/AdamPlatin123/dsh-plugin-radar/blob/main/docs/radar/architecture.md) · [Data contracts](https://github.com/AdamPlatin123/dsh-plugin-radar/blob/main/docs/radar/data-contracts.md) · [Data API docs/api.md](https://github.com/AdamPlatin123/dsh-plugin-radar/blob/main/docs/api.md)
(Discovery/aggregation/rendering/distribution engines are open-sourced; the test engine is on the open-sourcing roadmap — the repo ships CI smoke tests as runnable self-evidence.)

### [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) · ★3,054 · Admin / Core Maintainer · Python/React

**21 merged PRs** spanning terminal security, portable-package update integrity, install recovery, and rendering regressions. Day-to-day responsibilities include code review, issue triage, and compatibility maintenance. Representative fixes are listed under *Representative Upstream Contributions* below. Reached GitHub Trending (React) daily #7.


### [Open-Deep-Research-workflow-on-Dify](https://github.com/AdamPlatin123/Open-Deep-Research-workflow-on-Dify) · ★322 · Owner · YAML

Deep-research workflow on Dify: multi-source retrieval → outline → cited research report. Included with attribution in [Awesome-Dify-Workflow (10.8k★)](https://github.com/svcvit/Awesome-Dify-Workflow): [inclusion commit](https://github.com/svcvit/Awesome-Dify-Workflow/commit/565ad61a6dcb564a158ddb420a47e058af9468a0).


### [BioHermes](https://github.com/AdamPlatin123/BioHermes) · Python / React

Research agent for computational biology on single-server, multi-user setups: a **Judge → Select → Execute → Verify four-stage execution loop** — task feasibility judging, 98-skill selection, Podman-sandboxed execution, provenance-carrying output verification, and second-level self-recovery, with a React SPA frontend; passed unattended acceptance on the PBMC3k scenario. Source being tidied for release; architecture notes, demos, and acceptance records available on request.


---

## Representative Upstream Contributions

| Capability | Fix |
|---|---|
| Security boundary | [#584 terminal OSC injection hardening](https://github.com/ccch1mneyyy/dsh-TUI/pull/584): output sanitization / scheme gating |
| Release & update reliability | [#585 portable-package update-chain integrity](https://github.com/ccch1mneyyy/dsh-TUI/pull/585): SHA256 verification / streaming limits / extraction-tree checks |
| Failure diagnosis & regression | [#361 first-install error-stream detection](https://github.com/ccch1mneyyy/dsh-TUI/pull/361): ERR_PNPM_ADDING_TO_ROOT & false-success detection |
| Terminal rendering | [#405 selection-marker wrapping / overlay misalignment fix](https://github.com/ccch1mneyyy/dsh-TUI/pull/405) |

→ [All 21 merged dsh-TUI PRs](https://github.com/ccch1mneyyy/dsh-TUI/pulls?q=is%3Apr+author%3AAdamPlatin123+is%3Amerged)

**Other projects**

| Project | Contribution |
|---|---|
| [dsh-plugin-upgrade-skill](https://github.com/oh-my-dsh/dsh-plugin-upgrade-skill) (ecosystem-official, **Collaborator**; repo featured in the official DSH v0.1.2-rc.1 release notes) | [#38](https://github.com/oh-my-dsh/dsh-plugin-upgrade-skill/pull/38): upgrade-runtime verification runner (signature checks) · [#33](https://github.com/oh-my-dsh/dsh-plugin-upgrade-skill/pull/33): pre-migration baseline attribution + bounded retry on boot race — 7 merged PRs in total |
| [hermes-agent](https://github.com/NousResearch/hermes-agent) (NousResearch) | [#9151](https://github.com/NousResearch/hermes-agent/pull/9151): memory-content scanning pattern alignment — security-scan coverage fix |
| [dsh-desktop](https://github.com/dataelement/dsh-desktop) (dataelement) | [#191](https://github.com/dataelement/dsh-desktop/pull/191): mobile connection surface hardening |
| [unsloth](https://github.com/unslothai/unsloth) (unslothai) | [#4987](https://github.com/unslothai/unsloth/pull/4987): AnimatePresence route-transition DOM duplication fix · [#4764](https://github.com/unslothai/unsloth/pull/4764): cached-model inference loading copy fix |
| [easy-dataset](https://github.com/ConardLi/easy-dataset) (ConardLi) | [#678](https://github.com/ConardLi/easy-dataset/pull/678): provider-selection UI & asset improvements · [#680](https://github.com/ConardLi/easy-dataset/pull/680): interaction-logic optimization |

→ [Search all merged upstream PRs](https://github.com/pulls?q=is%3Apr+author%3AAdamPlatin123+is%3Amerged+-user%3AAdamPlatin123+-user%3Adsh-external)

---

## Education & Experience

- **DUT**, B.Eng.-track Bioinformatics (2023–2027) · tech lead of the campus AI society (2024–2026)
- **University research group**: LLM data-algorithm optimization and AI-in-education applications · 2 registered software copyrights
- **Genexis research team** (cross-university): multi-omics pretrained-model fine-tuning · 2 invention patents filed as **first inventor** (accepted, preliminary examination passed)
- **Industry collaboration**: AI application development — long-document processing tools on locally deployed models, plus server-infrastructure optimization

## Selected Honors

- iFLYTEK Medical Consultation QA Optimization Algorithm Challenge — **Champion** (team lead)
- China Collegiate Computing Contest (CCCC), AIGC Innovation Track — **National 3rd Prize** (team lead)
- CAICT "Guanghua Cup" Smart Education Track — **National 2nd Prize**
- 2 national-level Innovation & Entrepreneurship Training projects (1 as team lead) · 2 software copyrights · 2 invention patents (first inventor)

Full list in [AWARDS.md](AWARDS.md).

## Skills

`LLM fine-tuning` `RAG` `Agent Workflow→Loop→Harness development` `Python` `TypeScript / Node.js` `React` `Shell` `Linux` `Containers / Kubernetes`

---

<details>
<summary><b>More projects & timeline</b></summary>

**Ecosystem tooling**: [dsh-zcf](https://github.com/AdamPlatin123/dsh-zcf) (one-command zero-config DSH setup wizard, published on npm — 7,800+ cumulative downloads) · [dsh-tonghuashun](https://github.com/AdamPlatin123/dsh-tonghuashun) (Tonghuashun-terminal-style client skin built on the official cordis.patch.yml mechanism)

**Experiments & fun**: [gomoku_rl_demo](https://github.com/AdamPlatin123/gomoku_rl_demo) (AlphaZero Gomoku: residual policy-value net + MCTS + live self-play visualization) · [Legacycode-win3.2](https://github.com/AdamPlatin123/Legacycode-win3.2) (QEMU virtual serial + Python bridge, letting Claude live inside Chinese Windows 3.2 from 1994) · [Docling-webui](https://github.com/AdamPlatin123/Docling-webui) / [Faster-Whisper-WebUI](https://github.com/AdamPlatin123/Faster-Whisper-WebUI) (out-of-the-box document-parsing & speech-to-text web UIs)

**Small utilities**: [claude-code-print-skill](https://github.com/AdamPlatin123/claude-code-print-skill) · [claude-code-installer](https://github.com/AdamPlatin123/claude-code-installer) · [Fish-AI-Handbook](https://github.com/AdamPlatin123/Fish-AI-Handbook) (co-written with friends)

**Timeline**

- 2023-12 Joined GitHub · 2024 Dify / FastGPT ecosystem workflows
- 2025-02 Open-Deep-Research-workflow-on-Dify (322★)
- 2026 BioHermes · gomoku_rl_demo · Legacycode-win3.2
- 2026-08 dsh-plugin-radar (1,468★) · dsh-TUI (3,054★, 21 merged PRs, Admin) · dsh-zcf (7,800+ downloads) · dsh-tonghuashun

</details>

---

## Contact

- Email: [AdamPlatin123@outlook.com](mailto:AdamPlatin123@outlook.com)
- GitHub: [AdamPlatin123](https://github.com/AdamPlatin123)
- Always happy to talk agent engineering, developer tools, and open-source collaboration
