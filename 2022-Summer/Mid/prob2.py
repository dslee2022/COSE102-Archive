#스타벅스

str_list = list()

while (True):
  str_input = input()
  if (str_input == "END"):
    break
  else:
    str_input.split()
  new_str = str_input[0][0] + str_input[1][0]
  str_list.append(new_str)

i = 0
list_len = len(str_list)

bFlag = 0
while (i < list_len - 1):
  if (str_list[i] == str_list[i + 1]):
    bFlag = 1
  i += 1

if (bFlag == 1):
  print("YES")
else:
  print("NO")