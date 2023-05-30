# A = int(input())
# num = 11
# ans = 0
# if num % 3 == 0 and num % 5 == 0 :
#   while (num >= 5):
#     num -= 5
#     ans += 1
#   while (num >= 3):
#     num -= 3 
#     ans += 1 
# else:
#     while (num >= 3):
#       num -= 3
#       ans += 1 

# if num == 0:
#   print(ans)
# else:
#   print(-1)

# if num // 5 > 0:
#     ans += num // 5
#     num = num - ans*5

# print(num)
# print(ans)

# num = int(input())
# ans = 0
# temp = num

# if num % 5 !=0 and num % 3 != 0 and num > 5:
#     while(num%3!=0 and num>=0):
#         num -= 5
#         ans += 1
#     print(ans)
#     print(num)
#     while(num>0):
#         num -= 3
#         ans += 1

# elif num > 5 and num % 5 != 0:
#     while(num>=3):
        
#         num -= 3
#         ans += 1
#     print(ans)
#     print(num)

# else:
#     while(num>=5):
#         num -= 5
#         ans += 1
#     print(ans)
#     print(num)
#     while(num>=3):
#         num -= 3
#         ans += 1


# if num==0:
#     print(ans)
# else:
#     print(-1)

# num = int(input())
# ans = 0
# temp = num

# while num >= 5 and num % 5 == 0 or num % 5 != 0 and num % 3 != 0:
#     num -= 5
#     ans += 1

# while num >= 3 :
#     num -= 3
#     ans += 1

# if num == 0:
#     print(ans)
# else:
#     print(-1)

num = int(input())
ans = 0

while num >= 3 :
    if num % 5 == 0:
        ans += num // 5
        num = 0
        break
    num -= 3
    ans += 1

if num == 0:
    print(ans)
else:
    print(-1)