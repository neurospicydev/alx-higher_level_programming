#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i < 100:
            end_char = " "
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz", end=end_char)
        elif i % 5 == 0:
            print("Buzz", end=end_char)
        elif i % 3 == 0:
            print("Fizz", end=end_char)
        else:
            print(i, end=end_char)
