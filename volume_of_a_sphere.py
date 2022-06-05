#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: Jun 2022
# This program finds the volume of a sphere

import math


def volume(radius):
    # this function calculates volume

    result = 4 / 3 * math.pi * radius**3
    result = round(result, 2)

    return result


def main():
    # this function checks the input

    while True:
        radius_as_string = input("Please enter radius of sphere (cm): ")
        try:
            print("")
            radius = float(radius_as_string)
            if radius < 0:
                print("invalid input. Please try again.")
                print("")
            else:
                answer = volume(radius)
                print(
                    "The volume of a sphere with radius {0} cm is: {1} cm³".format(
                        radius, answer
                    )
                )
                break
        except Exception:
            print("invalid input. Please try again")
            print("")


if __name__ == "__main__":
    main()
