def square_root(x):
    return x**0.5

def get_dist(x1, x2, y1, y2):
  x1 = (x2 - x1) * (x2 - x1)
  y1 = (y2 - y1) * (y2 - y1) 
  return square_root(x1+y1)

x1_input = input().split()
y2_input = input().split()

x = list()
y = list()

for x_tmp in x1_input:
  x.append(int(x_tmp))
for y_tmp in y2_input:
  y.append(int(y_tmp))

x_len = len(x)
y_len = x_len

i = 0
j = 0
bFound = 0

while i < x_len:
  while j < y_len:
    real_dist = get_dist(x[i], x[j], y[i], y[j])
    if real_dist < 50 and (i != j):
      bFound = 1
    j += 1
  i += 1

if (bFound == 1):
  print("YES")
else:
  print("NO")