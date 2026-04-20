#codeforces problem 791 A
a = int(input())
b = int(input())
year = 0
while( a <= b):
    a = a*3
    b = b*2
    year += 1
    continue
print(year)