question=[
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,7,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
    ]

def print_board(q):
    for i in range(9):
        if i%3==0:
            print("-------------------------")
        for j in range(9):
            if j%3==0:
                print("|",end=' ')
            print(q[i][j],end=' ')
        print('|')
    print("-------------------------")
def find_empty(q):
    for i in range(9):
        for j in range(9):
            if q[i][j]==0:
                return [i,j]
    return None

def validity_check(q,value,pos):
    #for row
    if value in q[pos[0]]:
        return False
    #for column
    for i in range(9):
        if q[i][pos[1]]==value:
            return False
    #for square
    row=pos[0]//3
    col=pos[1]//3
    for i in range(row*3,(row+1)*3):
        for j in range(col*3,(col+1)*3):
            if q[i][j]==value:
                return False
    return True

def solver(q):
    pos=find_empty(q)
    if pos==None:
        return True
    for i in range(1,10):
        if validity_check(q,i,pos)==True:
            q[pos[0]][pos[1]]=i
            if solver(q)==True:
                return True
            q[pos[0]][pos[1]]=0
    return False

print_board(question)
answer=solver(question)
if answer==False:
    print("Invalid Question")
else:
    print_board(question)








    
