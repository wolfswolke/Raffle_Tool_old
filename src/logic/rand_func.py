import random


def get_numbers(number_of_winners, number_of_devices):
    number_of_winners = int(number_of_winners)
    winners = random.sample(range(number_of_winners), number_of_devices)
    return winners
