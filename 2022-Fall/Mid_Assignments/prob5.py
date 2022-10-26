#Problem 5 유니크

s_input = input()
s_len = len(s_input)
not_unique = 0
i = 0
j = 0
while (i < s_len):
  s_char = s_input[i]
  while (j < s_len):
    if ((s_char == s_input[j]) and (j != i)): #j != i로 원래 같은게 같다고 뜨는걸 방지, s_char와 s_input 비교함
      not_unique = 1 # 같을경우 not_unique 플래그 올려줌
      break
    j += 1
  j = 0
  i += 1
  if (not_unique == 1): #not_unique 플래그 켜지는 순간 브레이크
    break
if (not_unique == 0): #not_unique 가 0이므로 유니크함
  print("YES")
else:
  print("NO")