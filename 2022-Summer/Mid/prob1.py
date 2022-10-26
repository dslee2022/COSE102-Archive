#2022학년도 여름계절학기 중간고사
#이벤트

#drink 3 coke, get one free

coke_cnt = int(input())
coke_tmp = -1
result = coke_cnt

while (True):
  result += int(coke_cnt / 3)
  coke_tmp = int(coke_cnt % 3)
  coke_cnt = int(coke_cnt / 3) + coke_tmp
  if (coke_tmp == coke_cnt):
    break

print(result)