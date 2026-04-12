#codeforce problem 2009B
t = int(input())
for i in range(t):
    y = int(input())
    ans =[]
    for i in range(y):
        arr = input()
        ans.append(arr.index("#") + 1)
    ans = ans[::-1]
    print(*ans )    
