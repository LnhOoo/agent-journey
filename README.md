# agent-journey

我的 AI Agent 开发学习日志。

**目标：**用 12 周（约 150 小时）从零走到能独立做出一个生产可用的 Agent —— Python 出原型与工具，Java 出生产服务，两侧用 MCP 打通。

**开始日期：**2026-09-30
**计划总览：**见本仓库根目录 `学习计划.md`（或桌面上的 12 周计划手册）

---

## 为什么是 Java + Python 两条腿

- **Python 是主战场**：新框架、新论文、模型 SDK 都先出 Python 版（LangGraph、LlamaIndex）。
- **Java 是落地战场**：企业里已有的订单、权限、事务、微服务都在 Java 侧（Spring AI、LangChain4j、AgentScope Java）。
- **真正的价值点在 MCP**：Python 里写的工具挂成 MCP Server，Java 侧 Agent 直接调用。不是两门语言各学一遍，是让它们协作。

---

## 进度

| 周 | 主题 | 状态 |
|---|---|---|
| Week 0 | 环境准备 + 申请 API Key | 进行中 |
| Week 1 | Python 突击（异步 / pydantic / 装饰器） | 未开始 |
| Week 2 | Java 突击（record / HttpClient / Jackson / Maven） | 未开始 |
| Week 3 | 裸调模型 API，Python + Java 各一遍 | 未开始 |
| Week 4 | 提示词工程与上下文管理 | 未开始 |
| Week 5 | **手写工具调用循环（Python）** | 未开始 |
| Week 6 | **手写工具调用循环（Java）** | 未开始 |
| Week 7 | RAG 检索增强（Python） | 未开始 |
| Week 8 | Java 侧 RAG + 记忆系统 | 未开始 |
| Week 9 | 上框架：LangGraph | 未开始 |
| Week 10 | 上框架：Spring AI / LangChain4j | 未开始 |
| Week 11 | MCP：把两侧打通 | 未开始 |
| Week 12 | 工程化与毕业项目 | 未开始 |

状态用「未开始 / 进行中 / 已完成」三种。**每周的验收清单没全打勾就不进下一周。**

---

## 本机环境（以后重装系统照着这个配）

| 项目 | 版本 / 路径 |
|---|---|
| 操作系统 | Windows 11 |
| JDK | 21.0.1（`JAVA_HOME=C:\Program Files\Java\jdk-21.0.1`） |
| Python | 3.13.14 |
| Git | 2.55.0.windows.3 |
| IDE | IntelliJ IDEA 2024.1.4 / PyCharm 2024.2.1 / VS Code |

**模型 API：**DeepSeek（`https://api.deepseek.com`，模型 `deepseek-chat`），完全兼容 OpenAI 格式。

环境自检命令：

```bash
java -version
javac -version
python --version
git --version
```

---

## 目录结构

```
agent-journey/
├── README.md            本文件：目标、进度、环境
├── .gitignore           忽略密钥、虚拟环境、编译产物
├── .env.example         密钥模板（复制成 .env 后填自己的）
├── notes/               每日学习笔记，一天一个文件
│   ├── README.md        笔记怎么写
│   └── 2026-09-30.md
├── week01-python/       Week 1 的练习代码（学到再建）
├── week02-java/         Week 2 的练习代码
├── week03-hello-llm/    Week 3：第一段真正调用模型的代码
└── ...
```

每个 week 目录下都放一个 `README.md`，写清楚：这周学了什么、代码怎么跑、踩了什么坑。

---

## 每日约定

1. **每天必须有能跑起来的东西。** 哪怕只多打印了一行，也比读 50 页文档强。
2. **当天写笔记**（三行法：学了什么 / 卡在哪 / 明天做什么），提交到 `notes/`。
3. **每天推一次 Git**，让提交格子连起来。
4. **卡超过 30 分钟就求助**，别死磕。死磕是新手最大的时间黑洞。

---

## 安全红线

- API 密钥只放 `.env`，**永远不写进代码、永远不提交**。
- 每次 `git commit` 前用 `git status` 扫一眼，确认列表里没有 `.env`。
- 万一不小心提交了：立刻去平台后台**作废该密钥重新生成**，然后改代码。历史记录里的密钥删不干净，改密钥才是唯一解法。

---

## 参考资源

- LangGraph 官方文档
- Spring AI Reference（官方）
- DeepSeek / 阿里云百炼 API 文档
- Anthropic《Building effective agents》（Agent 设计模式，必读短文）
- ReAct 论文（工具调用循环的思想来源，读摘要和示例图即可）

> 这个领域三个月换一茬，**优先看官方文档和源码，别依赖视频课**。
