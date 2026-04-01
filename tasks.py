# task 1
# n = int(input())

# for i in range(1, n + 1):
#     if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 or i % 5 == 0):
#         print(i, end="")

# task 2
# num = int(input())
# original = num
# digits = len(str(num))
# total = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     total += digit ** digits
#     temp //= 10

# print(total == original)

# task 3
# s = input()

# compressed = ""
# count = 1

# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         count += 1
#     else:
#         compressed += s[i - 1] + str(count)
#         count = 1

# compressed += s[-1] + str(count)

# print(compressed)

# task 4
s = input()

cleaned = s.replace(" ", "").lower()
is_palindrome = cleaned == cleaned[::-1]

print(is_palindrome)

# task 5


