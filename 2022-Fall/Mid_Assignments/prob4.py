#Problem 4 개교 기념
name = input().split()
result = 0
for i in name:
  n_len = len(i) #길이를 구해옴
  last_char = i[n_len - 1] #len - 1 = 마지막 문자
  if (last_char == "고" or last_char == "려" or last_char == "대"):
    result+=1 #결과++
print(result)