# Find index of an element in an array

a = int(input())
n = int(input())
arr = map(int,raw_input().strip().split(' '))

for index, i in enumerate(arr):
    if i == a:
        print index
