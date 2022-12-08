#!/usr/bin/env python
# coding: utf-8

import string
from time import sleep
import datetime

def func1():
    alphabet = list(string.ascii_lowercase)
    for i in alphabet:
        a=alphabet.index(i)
        print(i*(a+1))
        sleep(0.15)
        if i==alphabet[-1]:
            for i in alphabet[::-1]:
                print(i*(alphabet.index(i)+1))
                sleep(0.15)

def func2():
    l= datetime.datetime.now()
    while True:
        func1()
        n=datetime.datetime.now()
        print('Thank you for wasting {} seconds of your life'.format((n-l).total_seconds()))
        again = input("Again? ('yes','No') ")
        if 'yes' in again:
            continue
        else:
            m= datetime.datetime.now()
            print("Good Bye")
            print('Total time wasted {} seconds'.format((m-l).total_seconds()))
            break
func2()


