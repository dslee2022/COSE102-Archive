def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2,n):
            if n % x == 0:
                return False
        return True
        

def find_prime(a, b):
  i = 1
  while (True):
    if (is_prime(i)):
      i_str = str(i)
      a_str = str(a)
      b_str = str(b)
      if a_str in i_str and b_str in i_str:
        return i
        break
    i += 1

a = int(input())
b = int(input())
print(find_prime(a, b))