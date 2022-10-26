# Problem 2 완전수

divisor = list()
n = int(input())
i = 1 #avoid zero divison
while (i < n):
  if (n % i == 0):
    divisor.append(i)
  i += 1
cmp = 0
for j in divisor:
  cmp += j #cmp에다 j를 계속하여 누적시킴
if (cmp == n): #일치할 경우 YES 출력
  print("YES")
else:
  print("NO")