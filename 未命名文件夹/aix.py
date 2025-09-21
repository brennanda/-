import random
import streamlit as st
import matplotlib.pyplot as plt

# 判断是否有重复生日
def has_duplicate_birthdays(n_people):
    birthdays = [random.randint(1, 365) for _ in range(n_people)]
    return len(birthdays) != len(set(birthdays))

# 模拟函数
def simulate(n_people, trials=10000):
    count = 0
    for _ in range(trials):
        if has_duplicate_birthdays(n_people):
            count += 1
    return count / trials

# ---- Streamlit 页面 ----
st.title("🎂 生日问题模拟器")
st.markdown("模拟生日悖论：在一群人中，至少两人生日相同的概率。")

# 输入框
n = st.slider("选择人数", 2, 100, 23)
trials = st.number_input("实验次数", min_value=1000, max_value=100000, value=10000, step=1000)

# 计算概率
prob = simulate(n, trials)
st.write(f"**结果：** 在 {n} 个人中，至少两人生日相同的概率 ≈ **{prob:.3f}**")

# 曲线图
x = range(1, 51)
y = [simulate(i, trials) for i in x]

fig, ax = plt.subplots()
ax.plot(x, y, marker='o')
ax.set_xlabel("人数")
ax.set_ylabel("至少两人生日相同的概率")
ax.set_title("生日悖论模拟结果")
ax.grid(True)

st.pyplot(fig)