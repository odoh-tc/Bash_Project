#!/usr/bin/python3

def print_multiplication_table(m):
    for i in range(1, 11):
        for j in range(1, m+1):
            print(i * j, end='\t')
        print()
mul = int(input("Enter the number you want: "))
print_multiplication_table(mul)
