#codeforce problem 158 A
n, k = (map(int , input().split()))
score = list(map(int, input().split()))
next_round = 0
for s in score:
    threshold = score[k-1]
    if s >= threshold and s > 0 :
        next_round += 1
print(next_round)