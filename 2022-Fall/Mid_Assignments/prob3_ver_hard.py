#Problem 3 게임

#n1에 참가자 배열1
#n2에 1대1 매칭 시키기 위한 배열2
#n3에 첫 지목자를 담음
#N을 입력 받음

n1 = input().split() #이서 원영 유진
n2 = input().split() #원영 유진 이서 1대1 매칭
n3 = input() #이서
n4 = int(input()) #2

first_person_idx = 0

while (True):
  if (n1[first_person_idx] == n3): #첫번째 지목자의 인덱스를 가져옴
    break
  first_person_idx += 1

idx = first_person_idx #첫 지목자(=인덱스)를 첫 번째 지목자로 지정
j = 0

while (j <= n4):
  j += 1
  q = 0
  if (j % 2 != 0): #n1과 n2 서로 담고 있는 것이 다르므로 몫으로 어느쪽을 출력할지 구분하기 위하여 if문 사용
    while (n2[idx] != n1[q]):
      q += 1
    idx = q 
    if (j == n4):
        print(n1[idx]) 
  else:
      while (n2[idx] != n1[q]):
        q += 1
      idx = q
      if (j == n4):
        print(n1[idx])