board=[
    [0,0,0,0,6,8,0,3,0],
    [1,9,0,0,0,0,0,0,0],
    [8,0,3,1,0,0,2,0,0],
    [4,0,0,0,5,1,0,6,0],
    [7,0,0,0,2,0,0,0,4],
    [0,0,0,0,7,0,8,0,0],
    [0,1,0,0,0,5,0,0,7],
    [0,0,4,0,0,0,0,0,0],
    [0,5,0,0,3,0,1,0,0]
]

def bprint(boa):

    for i in range(len(boa)):
        if(i%3==0 and i!=0):
            print("--------------------")
        for j in range (len(boa[0])):
            if(j%3==0 and j!=0):
                print("|",end="")
            if(j==8):
                print(boa[i][j])
            else:
                print(str(boa[i][j])+" ",end="")

def search_empty(boa):
    for i in range(len(boa)):
        for j in range(len(boa[0])):
            if(boa[i][j]==0):
                return(i,j)
    return False

def validity(boa,num,pos):
    for j in range(len(boa[0])):
        if (boa[pos[0]][j]==num and pos[1]!=j):
            return False
    for i in range(len(boa)):
        if(boa[i][pos[1]]==num and pos[0]!=i):
            return False

    xsq= pos[1]//3
    ysq= pos[0]//3

    for i in range(ysq*3, ysq*3+3):
        for j in range(xsq*3, xsq*3+3):
            if(boa[i][j]==num and (i,j)!=pos):
                return False
    return True

def solution(boa):
    search=search_empty(boa)
    if (search==False):
        return True
    else:
        r,c=search
    for i in range(1,10):
        if validity(boa,i,(r,c))==True:
            boa[r][c]=i

            if solution(boa):
                return True
            boa[r][c]=0
    return False

bprint(board)
print("\n0's denoting empty blocks")
solution(board)
print("\n")
print("Solved: ")
bprint(board)








