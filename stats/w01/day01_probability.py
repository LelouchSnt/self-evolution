import random
def roll_dice(n_rolls:int)->dict:
    """
    This is a function to simulate rolling a fair dice for n_rolls times
    :param n_rolls: the number of dice rolling times
    :return: a dict mapping all faces of dice to  its relative appeared frequency.
    """
    face_num = {i:0 for i in range(1,7)}
    for j in range(n_rolls):
        face = random.randint(1,6)
        assert 1<=face<=6, "Invalid Value"
        face_num[face] += 1
    face_freq = {faces: counts/n_rolls for faces,counts in face_num.items()}
    return face_freq

for num in [10,100,1000]:
    prob = roll_dice(num)
    print(f"N = {num}: {"P(6)":>10} = {prob[6]:<6.4f}")

def coin_flip(n_flip:int)->dict:
    """
    This is a function to simulate flip a coin for n_flips, and calculate its frequency.
    :param n_flip: the amount of coin flip times
    :return: a dict mapping all faces of the coin and its relative appeared frequency.
    """
    face_n = {a:0 for a in range(2)}
    for i in range (n_flip):
        face = random.randint(0,1)
        assert face==0 or face == 1,"Invalid Value"
        face_n[face] += 1
    return {faces:counts/n_flip for faces,counts in face_n.items()}
for num in [1000,10000,100000]:
    prob = coin_flip(num)
    label = f"N = {num}:"
    print(f"{label:<15} P(0)={prob[0]:>10}\t {"P(1)":<5}={prob[1]:>10}")
