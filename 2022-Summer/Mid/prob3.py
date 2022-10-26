#여행

last_input = ""
last_input_dict = dict()

while (True):
  last_input = input()
  if " " in last_input:
    last_input = last_input.split()
  else:
    break
  
  if last_input[0] in last_input_dict:
    if last_input[1] < last_input_dict[last_input[0]]:
      last_input_dict[last_input[0]] = last_input[1]
  else:
    last_input_dict[last_input[0]] = last_input[1]

print(last_input_dict[last_input])