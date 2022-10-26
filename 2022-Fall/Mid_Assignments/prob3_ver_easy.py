#Problem 3 게임

name1 = input().split()
name2 = input().split()
name3 = input()

cnt = int(input())
game_players = dict(zip(name1, name2))
last_player = name3

i = 0

while (True):
 if (i == cnt):
 break
 last_player = game_players[last_player]
  i += 1

print(last_player)