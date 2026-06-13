"""dic = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,  
    }
s = input()
if s in dic:
    print(dic[s])
else:
    if s == "IIII" :
        print("4")
    elif s == "IX":
        print("9")
    elif s == "XL":
        print("40")
    elif s == "XC":
        print("90")
    elif s == ("CD"):
        print("400")
    elif s == ("CM"):
        print("900")
"""
"""
    "IV" : 4,
    "IX" : 9,
    "XL" : 40, 
    "XC" : 90,
    "CD" : 400,
    "CM" : 900,
"""
roman = ["1"]
ch = list(map(int, roman))
print(ch)