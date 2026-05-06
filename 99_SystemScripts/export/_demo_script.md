# CcVault 导师演示视频 · 分镜脚本（8-10 分钟完整版）

> **目标**：让导师在 9 分钟内理解这个知识库的**规模、结构、自动化能力、检索深度**，并建立对下一步工作的信心。
> **生成日期**：2026-04-23
> **适用版本**：Phase 2（MinerU 升级 Day 2 暂停点）

---

## 0. 录制工具推荐（按推荐度排序）

| 工具 | 优点 | 缺点 | 链接 |
|---|---|---|---|
| **OBS Studio** | 免费专业、录屏+摄像头+音频分轨、场景切换 | 学习成本 10 分钟 | [obsproject.com](https://obsproject.com/) |
| **Xbox Game Bar（Win+G）** | Windows 11 自带、零安装、快捷 | 只能单窗口、不能切换场景 | Win+G 快捷键 |
| **ShareX** | 轻量、含截图 GIF 一条龙 | 视频功能基础 | [getsharex.com](https://getsharex.com/) |
| **腾讯会议** | 自己开会录自己、会后自动生成 mp4 | 水印 | — |

**录制参数建议**：1080p / 30fps / mp4 / 录系统音。如果用 OBS 首次录，5 分钟照 [官方 YouTube 入门视频](https://www.youtube.com/watch?v=DTk99mHDX_I) 设好即可。

---

## 1. 录前准备清单（20 分钟完成）

### 1.1 桌面整洁
- [ ] 关掉所有不相关窗口（特别是微信、邮箱、浏览器其他标签）
- [ ] 桌面壁纸换成纯色（或默认 Windows 壁纸）
- [ ] 任务栏只留必要图标（右键隐藏时钟通知不建议，但可以关闭「显示桌面切换动画」）
- [ ] 屏幕分辨率调到 1920x1080（和最终视频分辨率一致，避免模糊）

### 1.2 预加载窗口（建议用**虚拟桌面** `Win+Ctrl+D` 分组）

**桌面 1 · Obsidian（核心）**
- [ ] 打开 `D:\CcVault` 为 vault
- [ ] 确认 Dataview / Graph / Copilot 等插件已启用
- [ ] 关掉左右侧边栏（Ctrl+Alt+Z / Ctrl+Alt+B），只留正文 —— 展示时更专注
- [ ] 字号调大：Ctrl+= 按 2-3 次（录屏里小字看不清）
- [ ] 提前打开以下 tabs（从左到右）：
  1. `_INDEX.md`
  2. `ECE R0 Rev4 Am2.md`（未升级对比样本，体积小一屏看完）
  3. `ECE R46 Rev4.md`（已升级样本，含表格/公式/图）
  4. `00_Dashboards/_MinerU_Upgrades.md`（Dashboard 量化）
  5. `04_Topics/communities/community_005.md`（GraphRAG 社区示例）
  6. `_CHANGELOG.md`（时间线）

**桌面 2 · 文件资源管理器**
- [ ] 打开 `D:\CcVault\00_Raw\标准库\`（展示原始 PDF 杂乱起点）
- [ ] 视图切换为**大图标**（演示 PDF 密密麻麻的视觉冲击）

**桌面 3 · PowerShell / MCP 演示**
- [ ] PowerShell 窗口一个，cwd = `D:\CcVault`
- [ ] 字号调到 18（`Ctrl+滚轮` 或设置→字体）
- [ ] 背景色建议黑底白字（默认）

### 1.3 常用快捷键备忘

| 场景 | 快捷键 |
|---|---|
| Obsidian 切换标签 | `Ctrl+Tab` / `Ctrl+Shift+Tab` |
| Obsidian 打开 Graph View | `Ctrl+G` |
| Obsidian 搜索 | `Ctrl+O`（快速跳转）/ `Ctrl+Shift+F`（全文搜索）|
| 放大光标附近（Windows 放大镜）| `Win++`（增大）/ `Win+-`（缩小）/ `Win+Esc`（关闭）|
| 录屏暂停/恢复（OBS 默认）| `Ctrl+Shift+P`（自行配置）|
| 切虚拟桌面 | `Ctrl+Win+←/→` |

### 1.4 预跑一次（15 秒）

录一段 15 秒测试视频：切一次虚拟桌面 → 打开一个 note → 关掉。回放确认：
- [ ] 画面清晰（字可读）
- [ ] 鼠标光标可见
- [ ] 系统音是否录上（点击声、通知声）
- [ ] 麦克风音量（如要配音）

---

## 2. 分镜脚本（9 段 / 共 ~9 分钟）

> 旁白**不是逐字稿**，是关键词。按自己节奏讲，更自然。每段结尾有「过渡句」衔接下一段。

---

### 段 1 · 起点痛点（0:00 → 0:40 · 40 秒）

**画面**：切到桌面 2（资源管理器），展示 `D:\CcVault\00_Raw\标准库\` 里 1444 个 PDF 文件。

**操作**：
1. 鼠标快速滚动窗口，滚到底（制造"数量多"的视觉）
2. 右键任一 PDF → 打开方式 → PDF 阅读器，展示原始 PDF 内容（含表格 / 图）3 秒
3. 关掉 PDF 阅读器，回到资源管理器

**旁白要点**：
- "这是整个项目的起点：**1444 份汽车法规 PDF**"
- "涵盖 ECE / GB / EU / 日韩 / 美澳 等 17 个区域"
- "原始状态：只是一堆文件名，没有统一命名、没有元数据、没有关联"
- "人工翻读每份要 20-30 分钟，全部看完需要 **600+ 小时**"

**过渡**："为了让这堆资料**可检索、可追溯、可交叉引用**，我设计了一套自动化 pipeline ——"

---

### 段 2 · 整体产物与规模（0:40 → 1:30 · 50 秒）

**画面**：切到桌面 1（Obsidian），打开 `_INDEX.md`。

**操作**：
1. 展示 `_INDEX.md` 顶部的"核心指标"
2. 滚动到"按区域 / 按主题"分布表
3. 按 `Ctrl+G` 打开 Graph View，让 1414 个节点自动排布 10 秒
4. `Ctrl+G` 关闭 Graph View

**旁白要点**：
- "经过两周迭代，现在有 **1414 条结构化 note**"
- "每条 note 是一份**汽车法规**，含 YAML 元数据 + 中文摘要 + 原文参考段"
- "按区域：ECE 951 条、国标 443 条、其他 20 条"
- "按主题：37 个自动聚类的细分主题（制动 / 照明 / 碰撞 / 电池 ...）"
- "Graph View 里每个点是一条 note，连线代表**跨区域等价**或**版本演化**关系"

**过渡**："先看一条典型 note 长什么样 ——"

---

### 段 3 · 单条 note 深入（1:30 → 3:00 · 1 分 30 秒）

**画面**：切到 `ECE R46 Rev4.md` 标签（视野 / 间接视野装置，升级过，含丰富结构化元素）。

**操作**：
1. 从**顶部 YAML FrontMatter** 开始滚动
   - 圈出 `reg_id`、`region`、`topic`、`status`、`publication_date`
   - 圈出 `equivalent_to`、`supersedes`、`cross_check`
   - **重点**圈出 `_ocr_upgraded: mineru` 和 `_mineru_blocks: tables 5 / formulas 15 / images 8`
2. 滚到**正文**：LLM 生成的中文摘要 / 适用范围
3. 滚到**原文参考段**："## 原文参考（MinerU 云解析 · 2026-04-22）"
   - 展示真实的**表格**（HTML 渲染）
   - 展示**LaTeX 公式**（如 `r_m = ...`）
   - 展示**原 PDF 截取的图**

**旁白要点**：
- "FrontMatter 有 **25+ 个字段**，每个字段由 LLM 从原 PDF 自动抽取"
- "`equivalent_to` 自动建立**跨区域等价**，`supersedes` 记录**版本演化链**"
- "`cross_check` 字段由第二个 LLM 独立复核，置信度 high/medium/low"
- "`_mineru_blocks` 是这次 Phase 2 升级新增：表格 5 个 / 公式 15 个 / 图 8 张，**全部**来自原 PDF 精确还原"
- "正文结构：LLM 生成中文摘要（**快速检索入口**）→ 原文参考段（**技术细节备查**）"

**过渡**："这是升级过的形态。对比一下**升级前**的 note 有什么差别 ——"

---

### 段 4 · 升级前后对比（3:00 → 4:00 · 60 秒）

**画面**：切到 `ECE R0 Rev4 Am2.md`（未升级对比样本）。

**操作**：
1. 展示这条 note：FM 字段完整，但**没有** `_ocr_upgraded: mineru` 标记
2. 滚到正文底部 —— **没有** "## 原文参考" 段
3. 切回 `ECE R46 Rev4.md`
4. `Ctrl+F` 搜 "原文参考"，跳到该段
5. 展示该段里的**表格 + 公式 + 图**

**旁白要点**：
- "原 pipeline 基于百度 OCR，以文本提取为主"
- "结果是：**表格结构丢失**（只剩一堆数字）、**数学公式变乱码**、**图被抛弃**"
- "MinerU 云 OCR 解决这个：结构化识别 → 输出结构化 Markdown"
- "这一轮升级已经处理 **845 / 1444 份 PDF（58%）**，补回：**2,036 个表格 + 1,353 个公式 + 2,284 张图**"
- "全部**增量合并**，不破坏原摘要"

**过渡**："这些数字是怎么追踪的？看 Dashboard ——"

---

### 段 5 · Dashboard 量化（4:00 → 5:00 · 60 秒）

**画面**：切到 `00_Dashboards/_MinerU_Upgrades.md`。

**操作**：
1. 展示顶部 Dataview 统计块（升级数 / 比例）
2. 滚到"富信息 notes 排行"（表格 ≥5 的 note 列表）
3. 展示"按主题覆盖率"（哪些主题升级最全）
4. 展示"按日期追踪"（2026-04-22 vs 2026-04-23 分组）

**旁白要点**：
- "所有 Dashboard 都是 **Dataview 实时查询**"
- "数字永远与 FrontMatter 同步，不用手工维护"
- "Vault 一共 10+ 个 Dashboard：按区域 / 按主题 / 置信度 / 等价映射 ..."
- "每做一次迭代，Dashboard 自动反映变化"

**过渡**："Dashboard 是浏览视角。如果我想**检索**，比如'前照灯配光性能'有哪些法规？——"

---

### 段 6 · MCP 检索能力（5:00 → 6:30 · 1 分 30 秒）

**画面**：切到桌面 3（PowerShell）。**或者**（如果你装了 Claude Desktop / Obsidian Copilot）在 LLM 里直接问。

**选项 A · 用 Obsidian Copilot（推荐，视觉最直观）**：
1. 打开 Copilot 侧栏
2. 输入："`@ccvault 用 BM25 搜一下前照灯 配光性能 相关的法规`"
3. 展示返回的 top 5 结果，含 reg_id / region / topic / score
4. 再问："`@ccvault GB 12676-2014 对应的 ECE 法规是什么？它被哪条新标准替代了？`"
5. 展示工具调用过程 + 结果

**选项 B · PowerShell 直接跑检索脚本**（推荐给第一次录的人，零依赖最稳）：

提前进入 venv（如果你 auto_reg_index 装了 venv），然后依次跑：

```powershell
# BM25 语义检索（1 秒返回）
python D:\CcVault\99_SystemScripts\auto_reg_index\_semantic_search.py "前照灯 配光性能" --limit 5

# GraphRAG 社区检索（3 秒返回，含社区综述）
python D:\CcVault\99_SystemScripts\auto_reg_index\_graphrag_search.py "制动系统 ABS 防抱死" --topk-communities 2 --topk-notes 5

# 版本演化链
python D:\CcVault\99_SystemScripts\auto_reg_index\_semantic_search.py "GB 12676" --limit 3
```

**录制节奏**：每个命令敲完按回车前停 1 秒（让观众看清命令），结果出来后**用鼠标从上往下滑过**（制造信息流视觉）。

**旁白要点**：
- "整个 vault 暴露给 LLM 的**工具层**叫 `ccvault` MCP Server"
- "共 19 个工具：`search_regulations_bm25`、`search_communities_graphrag`、`get_equivalence`、`get_supersession_chain` ..."
- "LLM 可以在一个自然语言对话里**组合调用**"
- "比如'前照灯配光性能'返回 top 5 GB 标准，score 按 BM25 排序（jieba 分词支持中英混合）"
- "如果是 '整个制动系统领域格局' 这类**全景**问题，会走 GraphRAG 社区检索"

**过渡**："GraphRAG 社区是什么？来看一个真实例子 ——"

---

### 段 7 · GraphRAG 社区综述（6:30 → 7:30 · 60 秒）

**画面**：切到 `04_Topics/communities/community_005.md`。

**操作**：
1. 展示标题："照明信号装置 / 安装规定 / 配光性能 / 中国标准 / ECE法规"
2. 展示 FM：member_count 16、edge_count 18、top_region cn、top_topic lighting_signaling
3. 滚到正文"成员总览"：ECE 法规 3 项 + 国标 13 项
4. 滚到"核心技术脉络"（LLM 生成的综述段）
5. 滚到"与其他社区的关系"

**旁白要点**：
- "33 个 GraphRAG 社区是基于 **`supersedes` / `equivalent_to` / `references` 关系图**的 Louvain 聚类"
- "每个社区的综述由 LLM 生成：**成员总览 → 技术脉络 → 与其他社区的关系**"
- "这个社区把 **ECE R48 和 GB 4785 系列**聚在一起 —— 正好反映了'中国安装规定采标 ECE'的客观现实"
- "给导师回答'某个领域格局'类问题，直接查社区综述比读 1414 条 note 快数百倍"

**过渡**："最后看整个项目的迭代速度 ——"

---

### 段 8 · 迭代时间线（7:30 → 8:30 · 60 秒）

**画面**：切到 `_CHANGELOG.md`。

**操作**：
1. 展示最顶部的 "2026-04-22~23 · MinerU 云 OCR 升级 Day 1-2" 条目
2. 滚过成果数据表（表格 / 公式 / 图 全绿）
3. 滚过"新增基础设施"列表
4. 滚过"修复 Bug"列表（5 个已修 bug）
5. 往下滚展示之前的历史条目（给导师**速度感**）

**旁白要点**：
- "这是人读版变更日志，最新条目在最上方"
- "Phase 2（MinerU 升级）从昨天早上 7 点开始，到今早 7 点暂停，**30 小时内处理 845 个 PDF / 合并 595 条 note / 修 5 个 bug**"
- "全部在 MinerU **免费额度**内，直接花费 ¥0"
- "新增了 6 个运维脚本（watchdog / QC / 修复三件套）"
- "对比往下滚 —— 整个项目从零到现在才两周"

**过渡**："这就是当前状态。下一步——"

---

### 段 9 · 收尾与下一步（8:30 → 9:00 · 30 秒）

**画面**：回到 `_INDEX.md` 或显示一张自制的总结图（可选）。

**旁白要点**：
- "已完成：1414 条结构化 note / 37 主题 / 33 社区 / 168 等价映射 / 58% PDF 升级"
- "本周剩余工作：剩余 599 个 PDF 继续升级、低置信度 35 条复核、GraphRAG 社区综述在升级后重建"
- "下一个 Phase：文献 Zettelkasten（50 篇学术 PDF 已设计好目录与模板）"
- "**所有这些内容已经打包发给您了**（指 `CcVault_导师版_2026-04-23.zip`）—— 可用 Obsidian 直接打开浏览"
- "感谢老师时间"

**结束**：静止画面 2 秒再停录。

---

## 3. 后期与常见翻车点

### 3.1 翻车点 · 录音杂音
- 背景有风扇/空调 → 剪辑软件（如 **剪映 / Davinci Resolve** 免费版）的"AI 降噪"一键处理
- 麦口水音 → 尽量离麦 20cm，录前喝口水

### 3.2 翻车点 · 鼠标光标看不清
- Windows 设置 → 鼠标 → 调大指针、换成**深色**指针（浅色桌面时）
- OBS 可加光标**高亮滤镜**

### 3.3 翻车点 · Obsidian 渲染慢
- 关掉 Graph View 窗口后再录 —— Graph 插件常年吃 CPU
- 预加载所有 tabs 在录前就打开过一次，让图片/Dataview 缓存好

### 3.4 后期建议
- 加**字幕**（每段一个大标题覆盖，B 站/YouTube 常见做法）：**剪映**自动识别中文字幕，5 分钟搞定
- 开头加 5 秒**封面字幕**："CcVault · 汽车法规结构化知识库 · 阶段性汇报"
- 结尾加 3 秒**联系方式**
- 背景音乐**可选**，如果加选节奏平缓的纯音乐，音量 -20dB 以下（别盖过人声）

### 3.5 输出参数
- 分辨率：1080p（1920x1080）
- 帧率：30fps（录屏不需要 60，浪费体积）
- 编码：H.264 / mp4
- 码率：CRF 22-23（平衡质量与体积）
- **预期体积**：9 分钟视频约 **200-400 MB**

---

## 4. 最小可交付（MVP）· 如果时间紧

如果今天只能录一次无后期，按以下取舍：

1. 跳过段 6（MCP 演示需要额外准备）—— 用段 5 Dashboard 带过
2. 跳过段 8 详细内容 —— 只放 CHANGELOG 顶部一眼
3. 总时长压到 **5-6 分钟**

最核心不可砍：
- ✅ 段 3 单条 note 深入（展示结构）
- ✅ 段 4 升级前后对比（展示价值）
- ✅ 段 5 Dashboard（展示自动化）

---

## 5. 参考素材位置

| 用途 | 路径 |
|---|---|
| 未升级对比样本 | `@D:\CcVault\01_Wiki\regulations\ece\ECE R0 Rev4 Am2.md` |
| 已升级丰富样本 | `@D:\CcVault\01_Wiki\regulations\ece\ECE R46 Rev4.md` |
| GraphRAG 社区样本 | `@D:\CcVault\04_Topics\communities\community_005.md` |
| MinerU 升级 Dashboard | `@D:\CcVault\00_Dashboards\_MinerU_Upgrades.md` |
| 总索引 | `@D:\CcVault\_INDEX.md` |
| 变更日志 | `@D:\CcVault\_CHANGELOG.md` |
| 原始 PDF 目录 | `D:\CcVault\00_Raw\标准库\` |

---

> **祝录制顺利**。录完后发给导师前，自己先看一遍 —— 90% 的小瑕疵这样能发现。
