import random
from collections import Counter

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

def advantage(dice, num_rolls):
    rolls = [dice.roll() for _ in range(num_rolls)]
    return max(rolls)

def disadvantage(dice, num_rolls):
    rolls = [dice.roll() for _ in range(num_rolls)]
    return min(rolls)

def calculate_probabilities(dice, num_simulations, num_rolls):
    advs = [advantage(dice, num_rolls) for _ in range(num_simulations)]
    disadvs = [disadvantage(dice, num_rolls) for _ in range(num_simulations)]

    print('\nProbability of getting a roll equal to or higher than the k value.')
    print(f'{"k":2s}  {"disadv":6s}  {"normal":6s}  {"advant":6s}')

    cumulative_disadv = 0
    cumulative_norm = 0
    cumulative_adv = 0

    disadv_counts = Counter(disadvs)
    adv_counts = Counter(advs)

    for k in range(dice.sides, 0, -1):
        cumulative_disadv += disadv_counts[k] / num_simulations
        cumulative_norm += 1 / dice.sides # Probability for normal roll
        cumulative_adv += adv_counts[k] / num_simulations
        print(f'{k:2d}  {cumulative_disadv:6.3f}  {cumulative_norm:6.3f}  {cumulative_adv:6.3f}')

def calculate_probabilities_from_lists(dice, disadvs, advs):
    print('\nProbability of getting a roll equal to or higher than the k value.')
    print(f'{"k":2s}  {"disadv":6s}  {"normal":6s}  {"advant":6s}')

    cumulative_disadv = 0
    cumulative_norm = 0
    cumulative_adv = 0

    disadv_counts = Counter(disadvs)
    adv_counts = Counter(advs)

    for k in range(dice.sides, 0, -1):
        cumulative_disadv += disadv_counts[k] / len(disadvs)
        cumulative_norm += 1 / dice.sides # Probability for normal roll
        cumulative_adv += adv_counts[k] / len(advs)
        print(f'{k:2d}  {cumulative_disadv:6.3f}  {cumulative_norm:6.3f}  {cumulative_adv:6.3f}')

def average_value(dice, num_simulations=100000, num_rolls=2, roll_function=None):
    total_sum = 0
    if roll_function is None:
        total_sum = sum(dice.roll() for _ in range(num_simulations))
    else:
        total_sum = sum(roll_function(dice, num_rolls) for _ in range(num_simulations))
    
    average = total_sum / num_simulations
    
    return average

def average_value_from_list(rolls):
    total_sum = sum(rolls)
    average = total_sum / len(rolls)
    return average



NUM_SIMS = 100000
NUM_ROLLS = 2

d = Dice(20)

advs = [advantage(d, NUM_ROLLS) for _ in range(NUM_SIMS)]
normal = [d.roll() for _ in range(NUM_SIMS)]
disadvs = [disadvantage(d, NUM_ROLLS) for _ in range(NUM_SIMS)]

#calculate_probabilities(d, NUM_SIMS, NUM_ROLLS)

calculate_probabilities_from_lists(d, disadvs, advs)

#disadv_avg = average_value(d, NUM_SIMS, NUM_ROLLS, roll_function=disadvantage)
#normal_avg = average_value(d, NUM_SIMS)
#adv_avg = average_value(d, NUM_SIMS, NUM_ROLLS, roll_function=advantage)

adv_avg = average_value_from_list(advs)
normal_avg = average_value_from_list(normal)
disadv_avg = average_value_from_list(disadvs)

print(f'Average value of disadvantage rolls: {disadv_avg:6.3f}')
print(f'Average value of normal rolls: {normal_avg:6.3f}')
print(f'Average value of advantage rolls: {adv_avg:6.3f}')
