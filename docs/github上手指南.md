# GitHub 上手指南（零基础版）

本地仓库 `agent-journey` 已经建好并且有第一次提交了。这份文件教你怎么把它放到 GitHub 上，以及以后每天怎么同步。

全程大约 10 分钟，只需要做一次；之后每天只用 3 条命令。

---

## 第一部分：在 GitHub 网站上建一个空仓库

### 第 1 步 · 注册 / 登录

浏览器打开 <https://github.com> ，右上角 **Sign up** 注册（用你的邮箱，学生建议顺手申请 GitHub Student Pack，能白嫖一堆工具），已有账号就 **Sign in**。

### 第 2 步 · 新建仓库

登录后，看页面右上角，有个 **+** 号按钮，点它 → 选 **New repository**（新建仓库）。

### 第 3 步 · 填写信息

页面上要填这几项：

| 项目 | 填什么 |
|---|---|
| Repository name（仓库名） | `agent-journey` |
| Description（描述，可选） | `我的 AI Agent 开发学习日志` |
| Public / Private | **建议选 Public**（公开）。学习记录公开更利于以后当作品集展示；如果你介意，选 Private 也完全没问题 |
| Add a README file | **不要勾！** ⚠ |
| Add .gitignore | **不要勾！** ⚠ |
| Choose a license | 先不选 |

> ### 为什么那两个框不能勾
> 本地仓库里已经有 README 和 .gitignore 了。如果网站上又生成一个，两边内容对不上，推送时 Git 会报 `unrelated histories` 或 `rejected`，新手到这一步很容易懵。
> **我们已经有了，所以让它保持空白。**

### 第 4 步 · 创建

点绿色的 **Create repository** 按钮。

### 第 5 步 · 复制仓库地址

创建成功后会跳到一个 "Quick setup" 页面。找到 HTTPS 那一项，地址长这样：

```
https://github.com/你的用户名/agent-journey.git
```

点地址右边的小复制按钮复制它。**你的用户名**就是下一步要用的东西。

> 如果页面上写的是 `--initial-commit` 之类的提示不用管，那是给空仓库用的，我们本地已经有提交了。

---

## 第二部分：把本地仓库推上去

### 第 6 步 · 打开 Git Bash

在 `agent-journey` 文件夹里，**右键空白处** → 选 **Open Git Bash here**（在资源管理器地址栏直接输入 `bash` 回车也行）。

弹出来的黑框框就是终端。先确认你在正确的目录：

```bash
pwd          # 应该显示 .../agent-journey
git log --oneline    # 应该能看到一行 "chore: init agent-journey learning repo"
```

### 第 7 步 · 连接远程仓库

把下面命令里的 `你的用户名` 换成你自己的 GitHub 用户名（比如 `Lin` 之类），然后回车：

```bash
git remote add origin https://github.com/你的用户名/agent-journey.git
```

这条命令没有任何输出就是成功了。可以用这条确认：

```bash
git remote -v
```

会显示两行 `origin https://github.com/你的用户名/agent-journey.git`。

### 第 8 步 · 推送

```bash
git branch -M main
git push -u origin main
```

### 第 9 步 · 登录（这一步最容易卡）

执行 push 后，通常会自动弹出一个 **GitHub 登录窗口**：

- **情况 A：弹出了浏览器或窗口让你登录** → 直接点 "Sign in with browser"，用你的 GitHub 账号授权即可。成功后回到终端等它跑完。这是最省事的情况，Windows 的 Git 自带凭证管理器，之后都不用再登录。
- **情况 B：终端里让你输入 Username 和 Password** → ⚠ **密码那里不能填你的 GitHub 登录密码**（GitHub 从 2021 年起就不接受账号密码了），必须填 **Personal Access Token**。生成方法见下面的"如果卡在登录"。

### 第 10 步 · 验证

终端出现 `branch 'main' set up to track 'origin/main'` 之类的字样就是成功了。

回到浏览器刷新你的仓库页面，应该能看到 README.md、notes/ 这些文件。

---

## 如果卡在登录：生成 Personal Access Token（PAT）

1. GitHub 网页右上角点头像 → **Settings**
2. 左侧最下面 → **Developer settings**
3. → **Personal access tokens** → **Tokens (classic)**
4. 点 **Generate new token (classic)**
5. Note 随便填，比如 `my-laptop`
6. Expiration 选 90 days 或更长
7. **勾选 `repo`**（这一个就够了，它包含了仓库读写权限）
8. 拉到最下面点 **Generate token**
9. **立刻复制那串 `ghp_xxxxx`**（只显示这一次，关掉就没了，重新生成即可）

回到终端，`git push` 时：

- Username：填你的 GitHub **用户名**
- Password：粘贴刚才那串 **ghp_** 开头的 token（粘贴时终端不显示内容，这是正常的，回车就行）

---

## 第三部分：以后每天怎么同步

每天写完笔记后，在 `agent-journey` 目录下执行三条：

```bash
git add .
git commit -m "notes: 2026-10-01 学了 async/await"
git push
```

说明：

- `git add .` 把改动放进暂存区
- `git commit -m "..."` 记录一次提交，**引号里的话写清楚今天做了什么**（以后翻记录全靠它）
- `git push` 推到 GitHub

**提交前养成一个习惯：**

```bash
git status
```

看一眼列表里**有没有 `.env`**。如果有，说明密钥要泄露了，立刻停手检查 `.gitignore`。

---

## 常见问题

| 报错 | 原因 | 怎么解决 |
|---|---|---|
| `remote: Support for password authentication was removed` | 用了登录密码当密码 | 改用 Personal Access Token |
| `failed to push some refs` / `! [rejected]` | 建仓库时勾了 README 或 LICENSE | 最省事的办法：删掉这个仓库重建一个空的，重来第 2–8 步 |
| `src refspec main does not match any` | 本地还没有任何提交 | 先 `git add .` 和 `git commit`，再 push |
| `fatal: remote origin already exists` | 已经加过远程地址了 | 先 `git remote remove origin`，再重新 add |
| `403 Permission denied` | token 权限不够或用户名填错 | 重新生成 token 并确认勾了 `repo` |

---

## 万一不小心把密钥推上去了

1. **第一件事：去平台后台作废那个 API Key，重新生成一个。** 这是唯一有效的止损方式。
2. GitHub 历史记录里的东西删不干净（可以被爬到），所以不要指望"删掉文件再提交一次"能解决。
3. 以后提交前一定 `git status` 扫一眼。
