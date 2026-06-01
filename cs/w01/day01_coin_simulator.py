import random
def coin_simulator(n_flips):
    heads = 0
    result = random.choice(["heads","tails"])
    for i in range(n_flips):
        assert result=="heads" or result=="tails","INPUT ERROR"
        if result == "heads":
            heads += 1
    tails = n_flips - heads
    heads_ratio = heads / n_flips
    tails_ratio = tails / n_flips
    print(f"抛了{n_flips}次硬币。")
    print(f"抛出了正面{heads}次，{heads_ratio=:.2f}")
    print(f"抛出了反面{tails}次，{tails_ratio=:2f}")
    