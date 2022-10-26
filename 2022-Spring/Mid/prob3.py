#쌍둥이

list1 = sorted(input().split())
list2 = sorted(input().split())
bSame = 1

len_list1 = len(list1)
len_list2 = len(list2)

if (len_list1 != len_list2):
  bSame = 0

i = 0
if (bSame == 1):
  while (i < len_list1):
    if (list1[i] != list2[i]):
      bSame = 0
      break
    i += 1

if (bSame == 0):
  print("NO")
else:
  print("YES")