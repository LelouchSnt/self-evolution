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
    print(f"N = {num}:{" ":<6}P(6) = {prob[6]:.4f}")