# Day 01 练习：自我介绍生成器
# 规则：把每个地方的 "TODO" 换成你自己的内容，然后跑起来
# 跑法：uv run day01.py


# ---------- 任务 1：字符串变量 ----------
# 建一个变量 my_name，装你的名字
# 注意：文字要用引号包起来，中英文引号都行
my_name = "派大星"


# ---------- 任务 2：数字变量 ----------
# my_age 是整数（不加引号）
# my_height 是小数（比如 1.75）
my_age = 18
my_height = 1.88


# ---------- 任务 3：用 input 收集信息 ----------
# 用 input() 问三个问题，把答案存进 hobby、city、dream
# 写法：hobby = input("你平时喜欢干什么？")
hobby = input("你的爱好")
city = input("你的家乡")
dream = input("你的梦想")


# ---------- 任务 4：输出 ----------
# 用 f-string 打印一段自我介绍，要把上面所有变量都用上
# 写法：print(f"我叫{my_name}，今年{my_age}岁")
print(f"我叫{my_name},我的年龄{my_age}岁，我的身高{my_height}，我的爱好{hobby},我的家乡{city},我的{dream}")


# ---------- 挑战（做完上面再说） ----------
# input() 拿到的年龄是字符串，不是数字。
# 用 int() 转成整数，算一下你大概哪一年出生（今年按 2026 算）。
# 提示：birth_year = 2026 - int(输入的东西)
year = 2026-my_age
print(f"我出生于{year}")