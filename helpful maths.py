#Codeforces problems 339 A 
nums = input()
nums = nums.split("+")
nums.sort()
nums = "+".join(nums)
print(nums)