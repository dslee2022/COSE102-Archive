#호랑이 수

def TigerNumber(n): #get int
  n_str = str(n)
  n_str_len = len(n_str)
  str_list_int = list()
  bFlag = 0
  i = 0
  while (i < n_str_len):
    tmp = int(n_str[i])
    if (n % tmp != 0):
      bFlag = 1
    i += 1
  if (bFlag == 0):
    return True
  else:
    return False

n_input = int(input())
print(TigerNumber(n_input))