#!/usr/bin/env python3

# Created by: Nicolas Riscalas
# Created on: April 25 2022
# Game for random number


import random
import colorama
from colorama import Fore, Back, Style


def main():

    # input
    biggest_num_str = input("Enter the largest number to be generated\n")
    try:
        biggest_num = int(biggest_num_str)
    except:
        print(Fore.WHITE + "that is not a valid number")
        main()
    random_num = random.randint(1, biggest_num)
    while True:
        users_num_str = input(
            Fore.WHITE + "Guess a number between 1 and {} \n".format(biggest_num)
        )
        try:
            users_num = int(users_num_str)
        except:
            print("You have to input an integer")
            main()
        if users_num > random_num:
            print(Fore.RED + "The number is lower")
        elif users_num < random_num:
            print(Fore.RED + "The number is higher")
        else:
            print(Fore.GREEN + "You guessed the right number!")
            break


if __name__ == "__main__":
    main()
