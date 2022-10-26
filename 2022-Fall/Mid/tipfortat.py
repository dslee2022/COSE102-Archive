bIsFirst = 1
last_input = ""

while (True):
  i_str = input()
  #print("last_input:", last_input)
  if (i_str == "END"):
    break
  if (bIsFirst == 1):
    print("C")
    bIsFirst = 0
  elif (last_input == "D"):
    print("D")
  elif (last_input == "C"):
    print("C")
  last_input = i_str