import random
n = input (' Give n:')
m = input (' Give m:')
plh=0
pld=0
plv=0
AvVer=0
AvHor=0
AvDiag=0
print('\n')
a = [[i * j for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if i < j:
            a[i][j] = 'O'
        elif i >= j:
            a[i][j] = 'S'

for i in range(3):
    random.shuffle(a)
    pl1=0
    pl2=0
    pl3=0
    for row in a:
        print(' '.join([str(elem) for elem in row]))
    for y in range(len(a)): 
        for x in range(len(a[y])): 
            if a[y][x] == 'S':

                
                if not x >= len(a[y])-3:
                    if a[y][x+1] == 'O' and a[y][x+2] == 'S':
                        
                        pl1=pl1+1

                
                if (not x >= len(a[y])-3) and (not y >= len(a)-3):
                    if a[y+1][x+1] == 'O' and a[y+2][x+2] == 'S':
                        
                        pl2=pl2+1

                
                if not y >= len(a)-3:
                    if a[y+1][x] == 'O' and a[y+2][x] == 'S':
                       
                        pl3=pl3+1
    print( 'Horizontal:' , pl1)
    print( 'Diagonal:' , pl2)
    print( 'Vertical:' , pl3)
    print('\n')
    plh=plh+pl1
    pld=pld+pl2
    plv=plv+pl3
AvHor=plh/3
AvDiag=pld/3
AvVer=plv/3
print('\n')
print('AvHor:' , AvHor)
print('AvDiag:' , AvDiag)
print('AvVer:' , AvVer)

