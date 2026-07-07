#codeforces problem 1A theater square 
n, m, a = map(int, input().split())
rows = (n + a - 1) // a
cols = (m + a - 1) // a
print(rows * cols)
