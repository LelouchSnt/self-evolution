"""
# Day 01 Python 复习
name = "Saint"
age = 25
subjects = ["CS", "Statistics", "English"]

for subject in subjects:
    print(f"{name} is learning {subject}")

if len(subjects) == 3:
    print("三科并进，交叉赋能！")
print("Hello, Self-Evolution")

import random
dic_1 = {}
for _ in range(1000):
    a=random.randint(1,6)
    if a in dic_1:
        dic_1[a] += 1
    else:
        dic_1[a] = 1

print(dic_1)
"""

import random
def simulate_dice(num:int) -> dict:
    """
    docstring:
    Simulate rolling a die 'num' times.

        Args:
            num: Number of times to roll the die.

        Returns:
            A dictionary mapping each face (1-6) to its frequency.
    """
    counts = { i:0 for i in range(1,7)}
    for _ in range(num):
        result = random.randint(1,6) #原变量名为a， 要注意细节，有良好的编程习惯！
        assert 1 <= result <= 6, f"非法骰子结果: {result}" #此处加上一个assert，用于判断输出内容的合法性
        counts[result] += 1
        # print(f"Roll{_}:{result}")
    ratio = {face : count / num for face, count in counts.items()}
    return ratio

for n in [10,100,1000,10000,100000]:
    freq = simulate_dice(n)
    for f, p in freq.items(): # for i in dict 等价 for i in dict.keys()
        print(f"N={n:>6} : P({f}):{p:.4f}", end="\t") # 使用dict.items可以有效避免二次查询字典内容
    print()




