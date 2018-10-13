# A solution to Project Euler problem 16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

num = 2 ** 15 # 2^15
mod = 0
sum = 0

while num != 0:
  # gets the last digit
  mod = num%10 
  
  # adds up
  sum += mod
  
  # removes the last digit
  num = num/10
  
print(sum)