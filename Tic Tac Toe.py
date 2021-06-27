import pygame,sys ,random,time,os
from pygame.locals import*

pygame.init()

GAMEWINDOW=pygame.display.set_mode((500,500),0,32)
pygame.display.set_caption('TIC TAC TOE')

obj=pygame.font.Font('freesansbold.ttf',35)
black=( 0, 0, 0)
green=( 0, 128, 0)
red=(255, 0, 0)                                      
white = (255, 255, 255)
your_score=0
computer_score=0
x= pygame.image.load('x.png')
o= pygame.image.load('o.png')
end= pygame.image.load('score board.png')
list=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
occupied=[]
player='X'
computer='O'

def intro_screen():
    i=pygame.mouse.get_pos()
    xpos=i[0]
    if xpos>250:
        GAMEWINDOW.blit(o,(0,0))
    else:
        GAMEWINDOW.blit(x,(0,0))
    event = pygame.event.wait()    
    if event.type == pygame.QUIT:
        terminate()    
    if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
        xpos,ypos = event.pos
        
        if xpos>445 and ypos<55:
           terminate()
        if xpos<250:
            return 1,1
        else:
            return 1,0
    return 0,0
    



    
def manage_screen():
    GAMEWINDOW.fill(white)    
    surf=obj.render('Tic Tac Toe',True,black)
    GAMEWINDOW.blit(surf,(130,10))
    surf=obj.render('QUIT',True,red)
    GAMEWINDOW.blit(surf,(410,0))
    pygame.draw.line(GAMEWINDOW, black, (180,100), (180,400), 5)
    pygame.draw.line(GAMEWINDOW, black, (280,100), (280,400), 5)
    pygame.draw.line(GAMEWINDOW, black, (80,200), (380,200), 5)
    pygame.draw.line(GAMEWINDOW, black, (80,300), (380,300), 5)    

def terminate():
    pygame.quit()
    sys.exit()

def display_xoxo():
    obj1=pygame.font.Font('freesansbold.ttf',55)

    x=100;y=125
    
    for i in range(9):
       surf1=obj1.render(list[i],True,black)
       GAMEWINDOW.blit(surf1,(x,y))
       x+=110
       if i==2 or i==5 :
        x=100
        y+=100


def get_player1_input():

    event=pygame.event.wait()

    if event.type == pygame.QUIT:
        terminate()    
    if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
        xpos,ypos = event.pos
        
        if xpos>410 and ypos<30:
           terminate()

        p=0
        q=0
        for i in range(9):
            if xpos>(80+p) and xpos<(180+p) and ypos>(100+q) and ypos<(200+q) and list[i]==' ':
                list[i]=player
                occupied.append(i)
                
                get_player2_input()
            p+=100
            
            if i==2 or i==5:
                p=0
                q+=100
  

          

def get_player2_input():
    
    if len(occupied)<9:
          for i in range(9):
                  dummy=[]

                  for j in list:
                      dummy.append(j)
  
                  if i not in occupied:
                                                                   
                       dummy[i]=computer

                       if pre_check_win(dummy):
                           list[i] = computer
                           
                           occupied.append(i)
                           return None
        
          step_2_block=False  
          for i in range(9):
                  dummy=[]

                  for j in list:
                      dummy.append(j)
                  
                                  

                  if i not in occupied:
                                                                   
                       dummy[i]=player

                       if pre_check_win(dummy):
                           list[i] = computer
                           
                           occupied.append(i)
                           step_2_block=True
                           
                           break
                
          if not step_2_block:
              while True:
                     a = random.randint(0,8)
                     if a not in occupied:
                         list[a] = computer
                         
                         occupied.append(a)
                         break              

              
def pre_check_win(dummy):
    l=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in range(len(l)):
        if dummy[l[i][0]]==dummy[l[i][1]]==dummy[l[i][2]]!=' ':
            return 1
    return 0    
    
          
def check_win():
    
    obj=pygame.font.Font('freesansbold.ttf',80)
    l=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in range(len(l)):
        if list[l[i][0]]==list[l[i][1]]==list[l[i][2]]!=' ':
            surf=obj.render('%s WON'%list[l[i][0]],True,green)
            GAMEWINDOW.blit(surf,(130,430))
            if list[l[i][0]]=='X':
                return 'X'
            else:
                return 'O'
            
    if len(occupied)==9:
            surf=obj.render('Match Draw',True,green)
            GAMEWINDOW.blit(surf,(0,430))
            return 3
        
    return 0

while True:
    click,response=intro_screen()
    
    pygame.display.update()

    if click:      
        if not response:
            t=player
            player=computer
            computer=t
        while True:
            manage_screen()

            if not response:
                get_player2_input()
                response+=1

            get_player1_input()

            display_xoxo()

            k=check_win()

            pygame.display.update()

            if k:
                if k==player:
                    your_score+=3
                elif k==computer:
                    computer_score+=3
                else:
                    your_score+=1
                    computer_score+=1
                    
                    
                time.sleep(3)
                list=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
                occupied=[]
                player='X'
                computer='O'
                while True:
                    GAMEWINDOW.blit(end,(0,0))
                    obj1=pygame.font.Font('freesansbold.ttf',100)
                    surf=obj1.render('%s'%your_score,True,black)
                    GAMEWINDOW.blit(surf,(110,100))
                    surf=obj1.render('%s'%computer_score,True,white)
                    GAMEWINDOW.blit(surf,(340,100))
                    event = pygame.event.wait()
                    if event.type == pygame.QUIT:
                        terminate()    
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                        xpos,ypos = event.pos
        
                        if xpos<250:
                            break
                        else:
                            terminate()
                    pygame.display.update()
                break        
                



