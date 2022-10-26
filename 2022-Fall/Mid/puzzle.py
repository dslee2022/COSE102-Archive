def puzzle(a, b):
  result = ""
  i = 0
  while (i < len(a)):
    if (a[i] == b[i]):
      result= result + "O"
    elif b[i] in a:
      result = result + "?"
    else:
      result = result + "X"
    i += 1
  return result

a = input()
b = input()
print(puzzle(a, b))