MyUni = "AUPP"
for i in range(len(MyUni)-1):
    for j in range(len(MyUni)-3):
        print(i,j) 

n = 3

for i in range(1,n+1):
    print(' '*(n-i), end='')
    for j in range(1, i+1):
        print(j, end='')
    for j in range(i-1, 0,-1):
        print(j, end='')
    print()

for i in range(1,3):
    for j in range(1,3):
        print(i * j, end=' ')
    print()

for i in range(1,4):
    for j in range(3):# or range(1,4)
        print(i, end=" ")
    print()
x = 5
while x >= 0: # while needs ":"
    print(x)
    x = x - 1


for i in range(3):
    for j in range(3):
        print((i+j)%2, end=' ')
    print()