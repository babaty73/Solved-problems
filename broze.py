code = input()

result = ""
i = 0

while i < len(code):

    if code[i] == ".":
        result += "0"
        i += 1

    elif code[i:i+2] == "-.":
        result += "1"
        i += 2

    else:
        result += "2"
        i += 2

print(result)
"""
horse shoe
s1, s2, s3, s4 = map(int, input().split())

buy = 0

if s2 == s1:
    buy += 1

if s3 == s1 or s3 == s2:
    buy += 1

if s4 == s1 or s4 == s2 or s4 == s3:
    buy += 1

print(buy)

vanye and fence

n, h = map(int, input().split())
heights = list(map(int, input().split()))

width = 0

for person in heights:
    if person > h:
        width += 2
    else:
        width += 1

print(width)


word cap

n = int(input())

for _ in range(n):
    word = input()

    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(word)
"""