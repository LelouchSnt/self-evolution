import random
import matplotlib.pyplot as plt

# 累计频率追踪 Cumulative frequency tracking
n_total = 10000
six_count = 0
frequencies = []

for i in range(1, n_total + 1):
    if random.randint(1, 6) == 6:
        six_count += 1
    frequencies.append(six_count / i)

plt.figure(figsize=(10, 5))
plt.plot(frequencies, label='Observed frequency')
plt.axhline(y=1/6, color='r', linestyle='--', label='Theoretical P(6) = 1/6')
plt.xlabel('Number of rolls')
plt.ylabel('Frequency of 6')
plt.title('Law of Large Numbers: Frequency → Probability')
plt.legend()
plt.savefig('frequency_convergence.png')
plt.show()