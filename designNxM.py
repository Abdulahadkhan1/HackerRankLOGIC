N, M = map(int, input().split())
from itertools import count
from stringprep import in_table_a1

design =  '.|.'

count = 1

for i in range(N):
        if(N//2 == i):
            print(("WELCOME").center(M, '-'))
        elif(i < N//2):
            print((design * count).center(M, '-'))
            count += 2
        else:
            count -= 2
            print((design * count).center(M, '-'))