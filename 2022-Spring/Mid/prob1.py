#2022학년도 제 1학기 컴퓨터프로그래밍2 중간고사
#부정 사용


def getavg(exclude_index, input_list):
  i = 0
  new_list = list()
  for tmp in input_list:
    if (exclude_index != i):
      new_list.append(tmp)
    i += 1
  
  total_count = len(new_list)
  total_sum = sum(new_list)
  return (int)(total_sum) / (int)(total_count)

electricity_use_str = input().split()
electricity_use = list()

for e_str in electricity_use_str:
  electricity_use.append(int(e_str))

result = 0
i = 0
for tmp in electricity_use:
  t_avg = getavg(i, electricity_use)
  if ((tmp / t_avg) >= 1.5):
    result = tmp
    break
  i += 1
if (result != 0):
  print(result)
else:
  print("Not Found")