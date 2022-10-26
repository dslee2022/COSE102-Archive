#피로도

key_first_line = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
key_second_line = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
key_third_line = ["z", "x", "c", "v", "b", "n", "m"]

final_key = dict()
for key in key_first_line:
  final_key[key] = 1
for key in key_second_line:
  final_key[key] = 2
for key in key_third_line:
  final_key[key] = 3 
final_key[" "] = 4

str_input = input()
str_len = len(str_input)
i = 0

result = 0

while (i < str_len - 1):
  tmp = final_key[str_input[i + 1]] - final_key[str_input[i]]
  if (tmp < 0):
    tmp *= -1
  result += tmp
  i += 1

print(result)