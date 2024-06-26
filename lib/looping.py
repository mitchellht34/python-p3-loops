#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    num = 10
    while num > 0:
        print(num)
        num -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    int_list = [num * num for num in int_list]
    return int_list

def fizzbuzz():
    # code goes here!
    for i in range(100):
        i += 1
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
