# A solution to Project Euler problem 16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

num = 2 ** 15 # 2^15
sum = 0

while num != 0: 
  # adds up while taking the last digit simultaneously
  sum += (num%10)
  
  # removes the last digit
  num //=10
  
print(sum)
