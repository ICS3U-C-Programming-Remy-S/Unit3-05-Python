#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Oct 19, 2023
# This program will ask the user
# for a number and it will tell them
# what month corresponds to it.


def main():
    # Get the user guess and display message
    print("This program will ask the user for a number from 1 to 12")
    print("then it will tell them what month corresponds to it.")
    user_month = int(input("Please enter a integer: "))

    # Check what month corresponds to user month
    match user_month:
        case 1:
            print("1 represents January.")

        case 2:
            print("2 represents February.")

        case 3:
            print("3 represents March.")

        case 4:
            print("4 represents May.")

        case 5:
            print("5 represents May.")

        case 6:
            print("6 represents June.")

        case 7:
            print("7 represents July.")

        case 8:
            print("8 represents August.")

        case 9:
            print("9 represents September.")

        case 10:
            print("10 represents October.")

        case 11:
            print("11 represents November.")

        case 12:
            print("12 represents December.")

        case _:
            print("{} is not a valid number.".format(user_month))


if __name__ == "__main__":
    main()
