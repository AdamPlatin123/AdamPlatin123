# AdamPlatin123

**Agent Harness · Developer Tools · Open Source** 
   

大连理工大学生物信息学本科（2023–2027，2027 届）。技术主线：构建 Agent 运行环境、插件验证管线与开发者工具

**可靠性、安全边界与可验证执行**。

> 🔍 **求职中**：中国大陆 Agent / Harness 研发、技术型 DevRel 实习 · 2027 届校招
> *Open to Agent/Harness R&D & tech-DevRel internships · Class of 2027.*
> 📧 [AdamPlatin123@outlook.com](mailto:AdamPlatin123@outlook.com)

---

## 精选工程

### [dsh-plugin-radar](https://github.com/AdamPlatin123/dsh-plugin-radar) · ★1,448 Owner · Python/Shell

独立构建的 **DeepSeek Harness 插件生态验证管线**：多源发现（GitHub/npm，18,000+ 候选仓库）→ 仓库身份归一去重 → **Kubernetes 隔离执行（一插件一 pod，累计 13,000+ 次运行级测试，覆盖 9,200+ 已定位仓库）** → 结果分类与 15 分钟快照发布。GitHub 上的插件目录由管线自动生成，非人工清单；判定数据经 schema 稳定接口（`dsh-radar/v1`）供插件市场与社区清单直接消费。曾登 GitHub Trending 日榜 #22。

→ [引擎源码 engine/](https://github.com/AdamPlatin123/dsh-plugin-radar/tree/main/engine) · [架构文档](https://github.com/AdamPlatin123/dsh-plugin-radar/blob/main/docs/radar/architecture.md) · [数据契约](https://github.com/AdamPlatin123/dsh-plugin-radar/blob/main/docs/radar/data-contracts.md) · [数据接口 docs/api.md](https://github.com/AdamPlatin123/dsh-plugin-radar/blob/main/docs/api.md)
（发现/聚合/渲染/分发引擎已开源；测试引擎在开源计划中，仓库含 CI 冒烟自证可运行）

### [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) · ★2,847 Owner / 主要协作者 · Python/React

**已合并 PR ×20**，覆盖终端安全、便携包更新完整性、安装恢复与渲染回归。日常职责包括代码审查、问题分诊与兼容性维护。代表修复见下方「代表性上游贡献」，曾登 GitHub Trending React 日榜 #7。

### [BioHermes](https://github.com/AdamPlatin123/BioHermes) · Python / React

面向单服务器-多用户的计算生物学科研 Agent：**Judge → Select → Execute → Verify 四层执行闭环**——任务可执行性判定、98 项技能选择、Podman 沙箱执行、带溯源的输出验证与二级自愈恢复，配套 React SPA 前端；PBMC3k 场景无人值守验收。源码整理中，可按需提供架构说明、演示与验收记录。

### [Open-Deep-Research-workflow-on-Dify](https://github.com/AdamPlatin123/Open-Deep-Research-workflow-on-Dify) · ★320 Owner · Yaml

Dify 深度研究工作流：多源检索 → 大纲 → 带引用的研究报告。被 [Awesome-Dify-Workflow（10.8k★）](https://github.com/svcvit/Awesome-Dify-Workflow)收录并署名：[收录提交](https://github.com/svcvit/Awesome-Dify-Workflow/commit/565ad61a6dcb564a158ddb420a47e058af9468a0)。

---

## 代表性上游贡献

| 能力 | 修复 |
|---|---|
| 安全边界 | [#584 终端 OSC 注入防护](https://github.com/ccch1mneyyy/dsh-TUI/pull/584)：出口净化 / scheme 门禁 |
| 发布与更新可靠性 | [#585 便携包更新链完整性](https://github.com/ccch1mneyyy/dsh-TUI/pull/585)：SHA256 校验 / 流式限额 / 解压树校验 |
| 故障定位与回归验证 | [#361 首次安装错误流识别](https://github.com/ccch1mneyyy/dsh-TUI/pull/361)：ERR_PNPM_ADDING_TO_ROOT 与假成功检测 |
| 终端渲染工程 | [#405 选中标记换行/浮层错位修复](https://github.com/ccch1mneyyy/dsh-TUI/pull/405) |

→ [dsh-TUI 全部 20 个已合并 PR](https://github.com/ccch1mneyyy/dsh-TUI/pulls?q=is%3Apr+author%3AAdamPlatin123+is%3Amerged)

**其他项目**

| 项目 | 修复 |
|---|---|
| [hermes-agent](https://github.com/NousResearch/hermes-agent)（NousResearch） | [#9151](https://github.com/NousResearch/hermes-agent/pull/9151)：内存内容扫描模式对齐——安全扫描覆盖面修复 |
| [dsh-desktop](https://github.com/dataelement/dsh-desktop)（dataelement） | [#191](https://github.com/dataelement/dsh-desktop/pull/191)：手机连接面加固（mobile connection surface hardening） |
| [dsh-plugin-upgrade-skill](https://github.com/oh-my-dsh/dsh-plugin-upgrade-skill)（生态官方） | [#38](https://github.com/oh-my-dsh/dsh-plugin-upgrade-skill/pull/38)：升级运行时验证 runner（签名校验）· [#33](https://github.com/oh-my-dsh/dsh-plugin-upgrade-skill/pull/33)：迁移前 baseline 归因 + boot race 有界重试 |
| [unsloth](https://github.com/unslothai/unsloth)（unslothai） | [#4987](https://github.com/unslothai/unsloth/pull/4987)：AnimatePresence 路由切换 DOM 重复修复 · [#4764](https://github.com/unslothai/unsloth/pull/4764)：缓存模型推理 loading 文案纠正 |
| [easy-dataset](https://github.com/ConardLi/easy-dataset)（ConardLi） | [#678](https://github.com/ConardLi/easy-dataset/pull/678)：provider 选择 UI 与资源改进 · [#680](https://github.com/ConardLi/easy-dataset/pull/680)：交互逻辑优化 |

→ [全部已合并上游 PR 检索](https://github.com/pulls?q=is%3Apr+author%3AAdamPlatin123+is%3Amerged+-user%3AAdamPlatin123+-user%3Adsh-external)

---

## 教育与经历

- **大连理工大学** 生物信息学 本科（2023–2027）· 校人工智能社团技术负责人（2024–2026）
- **高校课题组**：LLM 数据算法优化与 AI 教育应用 · 软件著作权 2 项
- **Genexis 研究团队**（跨校合作）：多组学数据预训练模型微调 · 产出发明专利 2 项（第一发明人，已受理并通过初审）
- **企业合作项目**：AI 应用开发——本地大模型长文本处理工具与服务器基础设施优化

## 主要荣誉

- 科大讯飞医疗咨询问答优化算法挑战赛 **冠军**（队长）
- 中国高校计算机大赛（CCCC）AIGC 创新赛 **全国三等奖**（队长）
- 信通院「光华杯」智慧教育专题赛 **全国二等奖**
- 国家级大创 **2 项**（其中 1 项任队长）· 软著 2 项 · 发明专利 2 项（第一发明人）

完整清单见 [AWARDS.md](AWARDS.md)。

## 技能

`LLM 微调` `RAG` `Agent Workflow→Loop→Harness 开发` `Python` `TypeScript / Node.js` `React` `Shell` `Linux` `容器 / Kubernetes` 

---

<details>
<summary><b>更多项目与时间线</b></summary>

**生态工具链**：[dsh-zcf](https://github.com/AdamPlatin123/dsh-zcf)（DSH 一键零配置安装向导，npm 发版）· [dsh-tonghuashun](https://github.com/AdamPlatin123/dsh-tonghuashun)（同花顺风格客户端皮肤，按官方 cordis.patch.yml 流程开发）

**实验与兴趣**：[gomoku_rl_demo](https://github.com/AdamPlatin123/gomoku_rl_demo)（AlphaZero 五子棋：残差策略价值网络 + MCTS + 自我对弈可视化）· [Legacycode-win3.2](https://github.com/AdamPlatin123/Legacycode-win3.2)（QEMU 虚拟串口 + Python Bridge，让 Claude 住进 1994 年的中文 Windows 3.2）· [Docling-webui](https://github.com/AdamPlatin123/Docling-webui) / [Faster-Whisper-WebUI](https://github.com/AdamPlatin123/Faster-Whisper-WebUI)（文档解析与语音转写开箱即用界面）

**小工具**：[claude-code-print-skill](https://github.com/AdamPlatin123/claude-code-print-skill) · [claude-code-installer](https://github.com/AdamPlatin123/claude-code-installer) · [Fish-AI-Handbook](https://github.com/AdamPlatin123/Fish-AI-Handbook)（与朋友合写）

**时间线**

- 2023-12 注册 GitHub · 2024 Dify / FastGPT 生态工作流
- 2025-02 Open-Deep-Research-workflow-on-Dify（320★）
- 2026 BioHermes · gomoku_rl_demo · Legacycode-win3.2
- 2026-08 dsh-plugin-radar（1,463★）· dsh-TUI · （★2,938） dsh-zcf （first month download：8000+） / dsh-tonghuashun

</details>

---

## Contact

- Email：[AdamPlatin123@outlook.com](mailto:AdamPlatin123@outlook.com)
- GitHub：[AdamPlatin123](https://github.com/AdamPlatin123)
- 欢迎就 Agent 工程、开发者工具、开源协作交流

