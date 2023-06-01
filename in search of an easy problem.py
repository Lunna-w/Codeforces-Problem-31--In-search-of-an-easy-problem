m = int(input())

n = list(map(int, input().split())) 

ez = 0
hard = 0

for i in n: 
    if i == 1:
        hard += 1

if hard > ez:
    print("HARD")
else:
    print("EASY")