last_input = input()
result = dict()
total_word_count = 0

while (last_input != "END"):
  names = last_input.split("]")
  names = names[:1]
  names = names[0].split("&")

  names.append(names[0][1:])
  del(names[0])
  lyrics = last_input.split()
  lyrics = lyrics[1:]
  
  word_count = 0
  for j in lyrics:
    word_count += len(j)
  for i in names:
    if i in result:
      result[i] = result[i] + word_count
      total_word_count += word_count    
    else: 
      total_word_count += word_count
      result[i] = word_count

  last_input = input()

max_value = max(result.values())  # maximum value
max_keys = [k for k, v in result.items() if v == max_value] # getting all keys containing the `maximum`

min_value = min(result.values())  # maximum value
min_keys = [k for k, v in result.items() if v == min_value] # getting all keys containing the `maximum`

max_value_pct = (max_value / total_word_count) * 100
min_value_pct = (min_value / total_word_count) * 100
print(max_keys[0], " {:.2f}".format(max_value_pct), "%", sep="")
print(min_keys[0], " {:.2f}".format(min_value_pct), "%", sep="")