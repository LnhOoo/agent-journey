# agent-journey

从零开始学 Agent / 智能体开发的学习日志与代码。

**起点**：2026-10-20，此前没写过一行代码
**目标**：用 24 周（每天约 1.5 小时）从零走到能独立交付一个生产可用的 Agent 系统
**方法**：串行 + 复刻 —— 先用 Python 把完整链路打通，再用 Java 把同样的东西重写一遍，最后用 MCP 把两侧连起来

---

## 为什么是 Python + Java

- **Python 是试验场**：新框架、新范式、模型 SDK 都先出 Python 版
- **Java 是落地场**：真实企业里的订单、权限、事务、微服务都在 Java 侧
- **真正的价值点在 MCP**：Python 写的工具挂成 MCP Server，Java 侧的 Agent 直接调用。不是两门语言各学一遍，是让它们协作

---

## 路线与进度

| 阶段 | 周次 | 内容 | 状态 |
|---|---|---|---|
| 第 0 周 | W0 | 环境搭建（uv / Python / JDK / Git） | ✅ 已完成 |
| 第一轮 | W1-W10 | Python 打通完整链路 | 🚧 进行中 |
| 第二轮 | W11-W18 | Java 复刻同样内容 | ⬜ 未开始 |
| 第三轮 | W19-W24 | MCP 打通两侧 + 工程化部署 | ⬜ 未开始 |

每周的验收清单没全打勾，就不进下一周。

---

## 本机环境

| 项目 | 版本 / 路径 |
|---|---|
| 系统 | Windows 11 |
| Python | 3.13.12（`C:\Users\13698\AppData\Local\Programs\Python\Python313`） |
| 包管理 | uv 0.13.3（`C:\Users\13698\.local\bin`） |
| JDK | 21（Week 11 开始用到） |
| 模型 API | DeepSeek（OpenAI 兼容格式） |

环境自检：

```powershell
uv --version
uv python list --only-installed
java -version
git --version
```

---

## 目录结构

```
agent-journey/
├── README.md          本文件
├── .gitignore         忽略密钥、虚拟环境、编译产物
├── .env               密钥（已被 git 忽略，不会上传）
├── notes/             每日学习笔记，一天一个文件
└── rounds/
    ├── round1-python/ 第一轮：Python 打通链路
    ├── round2-java/   第二轮：Java 复刻
    └── round3-bridge/ 第三轮：MCP 打通 + 工程化
```

每个 week 目录下放一个 README，写清楚：这周学了什么、代码怎么跑、踩了什么坑。

---

## 每日约定

1. **每天必须有能跑起来的东西** —— 哪怕只多打印一行
2. **当天写笔记**（学了什么 / 卡在哪 / 明天做什么），放进 `notes/`
3. **每天 commit 一次**，让提交记录连起来
4. **卡超过 30 分钟就求助**，别死磕

---

## 安全红线

- API 密钥只放 `.env`，**永不写进代码、永不提交**
- 每次 commit 前用 `git status` 扫一眼，确认列表里没有 `.env`
- 万一误提交：立刻去平台后台**作废该密钥重新生成**。历史记录删不干净，改密钥才是唯一解法

---

## 参考

- [LangGraph 官方文档](https://docs.langchain.com)
- [Spring AI Reference](https://docs.spring.io/spring-ai/reference/)
- [LangChain4j](https://docs.langchain4j.dev)
- [MCP 协议规范](https://modelcontextprotocol.io)
- Anthropic《Building effective agents》—— Agent 设计模式，必读短文
