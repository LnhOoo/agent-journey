# GitHub CLI（gh）使用指南

已安装：**gh 2.101.0**（2026-09-15 发布），安装路径 `C:\Program Files\GitHub CLI\gh.exe`。

`gh` 是 GitHub 官方的命令行工具。装了它之后，建仓库、推送、看 Issue、开 PR 都不用打开网页。

---

## 第一步：登录（只做一次）

打开一个**新的**终端（重要，见下方"坑"），执行：

```bash
gh auth login
```

然后跟着提示一步步走，每个问题选什么：

| 终端问你 | 你选 |
|---|---|
| Where do you use GitHub? | **GitHub.com**（直接回车） |
| What is your preferred protocol for Git operations? | **HTTPS**（直接回车） |
| Authenticate Git with your GitHub credentials? | **Y**（回车） |
| How would you like to authenticate GitHub CLI? | **Login with a web browser**（直接回车） |

接着屏幕上会显示一行类似这样的东西：

```
! First copy your one-time code: A1B2-C3D4
Press Enter to open github.com in your browser...
```

1. **先记住那个一次性码**（`A1B2-C3D4` 这样的）
2. **按回车**，会自动打开浏览器
3. 浏览器里把那个码输进去 → 点 **Authorize github**
4. 回到终端，看到 `Authentication complete` 就成功了

验证一下：

```bash
gh auth status
```

看到 `Logged in to github.com as 你的用户名` 就是好了。

---

## 第二步：一键建仓库并推送（省掉网页那一堆操作）

登录成功后，在 `agent-journey` 目录下执行**一条**命令：

```bash
gh repo create agent-journey --public --source=. --push
```

参数说明：

- `agent-journey` —— 仓库名
- `--public` —— 公开（想私有就换成 `--private`）
- `--source=.` —— 用当前目录作为仓库内容
- `--push` —— 自动设置远程地址并推上去

这一条命令等价于：网页建仓库 + `git remote add` + `git push -u origin main` 三件事。

跑完它会给你一个仓库网址，打开就能看到你的 README 了。

> 如果提示仓库名已存在（比如你之前在网页上建过），换个名字，或者先 `gh repo delete 用户名/agent-journey` 删掉旧的。

---

## 常用命令速查

### 仓库

```bash
gh repo list                      # 列出你所有的仓库
gh repo view                      # 在终端看当前仓库信息
gh repo view --web                # 用浏览器打开当前仓库
gh repo clone 用户名/仓库名         # 克隆别人的仓库
gh repo create 名字 --public --source=. --push    # 建仓库并推送
```

### 日常同步（还是用 git，gh 不替代它）

```bash
git add .
git commit -m "notes: 今天学了 async/await"
git push
```

### Issue（可以当学习任务清单用）

```bash
gh issue list                     # 看当前仓库的 issue
gh issue create --title "搞懂 tool_call_id" --body "为什么必须原样回传"
gh issue close 3                  # 关闭第 3 号 issue
```

> 学习小技巧：把每周的验收清单建成本仓库的 Issue，做完一个关一个，GitHub 上会有完整的完成记录——这本身就是一份很漂亮的成长轨迹。

### 其他可能用得上的

```bash
gh auth status                    # 看当前登录状态
gh auth refresh                   # 刷新凭证（权限不够时试试）
gh repo fork 别人的仓库            # fork 别人的项目
gh pr list / gh pr create         # 管理 Pull Request（以后协作再用）
gh browse                         # 浏览器打开当前仓库
```

---

## 一定会遇到的一个坑

**装完 gh 后，在原来的终端里敲 `gh`，会提示 `command not found`。**

原因：终端启动时才读取系统的 PATH 环境变量，新装的软件路径还没进来。

解决办法（任选一个）：

1. **关掉终端重新打开**（最简单）
2. 或者用完整路径调用：`"C:\Program Files\GitHub CLI\gh.exe" auth login`
3. 或者刷新当前终端的环境：`export PATH="$PATH:/c/Program Files/GitHub CLI"`

---

## 顺带一提：浏览器登录的好处

用 `gh auth login` 走浏览器授权之后，**Git 的推送认证也一并解决了**。

以后 `git push` 不用再输用户名密码，也不用折腾 Personal Access Token —— 这就是推荐装 gh 的主要原因。

如果哪天想退出：

```bash
gh auth logout
```

---

## 相关文档

- 同目录下 `github上手指南.md` —— 不用 gh、纯网页 + git 命令的做法，以及常见报错对照表
- 仓库根目录 `README.md` —— 学习目标和 12 周进度
