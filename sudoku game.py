import os
import pygame
#from Sudoku Game Solver import find_empty, validity check, solver

pygame.font.init()
pygame.display.set_caption("SUDOKU")
WIDTH, HEIGHT=500, 500
GAME=pygame.display.set_mode((WIDTH, HEIGHT))
WHITE=(255,255,255)
GREEN=(0,255,0)
BLACK=(0,0,0)
GREY=(100,100,100)
RED=(255,0,0)
NUMBER_FONT=pygame.font.SysFont('comicsans',55)
FPS=60
GRID=pygame.transform.scale(pygame.image.load(os.path.join('files used','grid.png')),(WIDTH, HEIGHT))

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

def solver(q,input_squares):
    pos=find_empty(q)
    if pos==None:
        return True
    for i in range(1,10):
        if validity_check(q,i,pos)==True:
            q[pos[0]][pos[1]]=i
            if solver(q,input_squares)==True:
                #draw_window(q,input_squares)
                return True
            q[pos[0]][pos[1]]=0
    return False

def input_squares_finder(grid):
    input_squares=[]
    start_x, start_y=35, 28
    temp_x=start_x
    temp_y=start_y
    for row in range(len(grid)):
        temp_x=start_x
        for col in range(len(grid[row])):
            if grid[row][col]==0:
                temp=[]
                square=pygame.Rect(temp_x-15,temp_y-10,53,53)
                temp.append(square)
                temp.append(False)
                temp.append([row,col])
                temp.append(0)
                input_squares.append(temp)
            temp_x+=51
        temp_y+=51
    return input_squares    

def draw_window(grid,input_squares):
    start_x, start_y=35, 28
    GAME.blit(GRID,(0,0))
    temp_x=start_x
    temp_y=start_y
    for row in grid:
        temp_x=start_x
        for col in row:
            if col!=0:
                GAME.blit(NUMBER_FONT.render(str(col),1,BLACK),(temp_x, temp_y))
            temp_x+=51
        temp_y+=51
    count=0
    for i in input_squares:
        if i[3]==1:
            pygame.draw.rect(GRID,GREEN,i[0],2)
        elif i[3]==2:
            pygame.draw.rect(GRID,RED,i[0],2)
        else:
            pygame.draw.rect(GRID,BLACK,i[0],2)
    pygame.display.update()

def main():
    grid=[
    [0,3,0,0,1,0,0,6,0],
    [7,5,0,0,3,0,0,4,8],
    [0,0,6,9,8,4,3,0,0],
    [0,0,3,0,0,0,8,0,0],
    [9,1,2,0,0,0,6,7,4],
    [0,0,4,0,0,0,5,0,0],
    [0,0,1,6,7,5,2,0,0],
    [6,8,0,0,9,0,0,1,5],
    [0,9,0,0,4,0,0,3,0]
    ]
    original_grid=[
    [0,3,0,0,1,0,0,6,0],
    [7,5,0,0,3,0,0,4,8],
    [0,0,6,9,8,4,3,0,0],
    [0,0,3,0,0,0,8,0,0],
    [9,1,2,0,0,0,6,7,4],
    [0,0,4,0,0,0,5,0,0],
    [0,0,1,6,7,5,2,0,0],
    [6,8,0,0,9,0,0,1,5],
    [0,9,0,0,4,0,0,3,0]
    ]
    input_squares=input_squares_finder(grid)
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                for i in input_squares:
                    if i[0].collidepoint(event.pos):
                        i[1]=True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solver(original_grid,input_squares)
                    for i in input_squares:
                        i[3]=1
                else:
                    for i in input_squares:
                        if i[1]==True:
                            if event.key==pygame.K_BACKSPACE or event.key==pygame.K_DELETE:
                                grid[i[2][0]][i[2][1]]=0
                                i[3]=False
                            if event.key == pygame.K_1:
                                check=validity_check(grid,1,[i[2][0],i[2][1]])
                                if check==True:
                                    grid[i[2][0]][i[2][1]]=1
                                    i[3]=1
                                else:
                                    i[3]=2
                            if event.key == pygame.K_2:
                                check=validity_check(grid,2,[i[2][0],i[2][1]])
                                if check==True:
                                    grid[i[2][0]][i[2][1]]=2
                                    i[3]=1
                                else:
                                    i[3]=2
                            if event.key == pygame.K_3:
                                check=validity_check(grid,3,[i[2][0],i[2][1]])
                                if check==True:
                                    grid[i[2][0]][i[2][1]]=3
                                    i[3]=1
                                else:
                                    i[3]=2
                            if event.key == pygame.K_4:
                                check=validity_check(grid,4,[i[2][0],i[2][1]])
                                if check==True:
                                    grid[i[2][0]][i[2][1]]=4
                                    i[3]=1
                                else:
                                    i[3]=2
                            if event.key == pygame.K_5:
                                check=validity_check(grid,5,[i[2][0],i[2][1]])
                                if check==True:
                                    grid[i[2][0]][i[2][1]]=5
                                    i[3]=1
                                else:
                                    i[3]=2
                            if event.key == pygame.K_6:
                                check=validity_check(grid,6,[i[2][0],i[2][1]])
                                if check==True:
                                    grid[i[2][0]][i[2][1]]=6
                                    i[3]=1
                                else:
                                    i[3]=2
                            if event.key == pygame.K_7:
                                check=validity_check(grid,7,[i[2][0],i[2][1]])
                                if check==True:
                                    grid[i[2][0]][i[2][1]]=7
                                    i[3]=1
                                else:
                                    i[3]=2
                            if event.key == pygame.K_8:
                                check=validity_check(grid,8,[i[2][0],i[2][1]])
                                if check==True:
                                    grid[i[2][0]][i[2][1]]=8
                                    i[3]=1
                                else:
                                    i[3]=2
                            if event.key == pygame.K_9:
                                check=validity_check(grid,9,[i[2][0],i[2][1]])
                                if check==True:
                                    grid[i[2][0]][i[2][1]]=9
                                    i[3]=1
                                else:
                                    i[3]=2
                            i[1]=False
        draw_window(grid,input_squares)
    pygame.quit()

if __name__=="__main__":
    main()
