# Problem 1 재테크


#A의 경우
#n이 홀수일 경우 누적 금액 + 10000
#n이 짝수일 경우 누적 금액 * 1.07

a = int(input())
b = int(input())
n = 0
while (True):
  n += 1
  if (n % 2 == 0): #짝수일 경우
    a *= 1.07
  else:
    a += 10000
  b *= 1.02
  if (a > b):
    break
print(n)