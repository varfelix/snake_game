#!/usr/bin/python3
import pygame 
from pygame.locals import *
import time
import random
import copy

#this can be tuple?
LEFT=0
RIGHT=1
UP=2
DOWN=3

small_snake_img_left=pygame.image.load('./images/small_snake.png')
big_snake_img_left=pygame.image.load('./images/big_snake.png')
    
small_snake_img_right=pygame.image.load('./images/small_snake_right.png')
big_snake_img_right=pygame.image.load('./images/big_snake_right.png')
    
small_snake_img_up=pygame.image.load('./images/small_snake_up.png')
big_snake_img_up=pygame.image.load('./images/big_snake_up.png')
    
small_snake_img_down=pygame.image.load('./images/small_snake_down.png')
big_snake_img_down=pygame.image.load('./images/big_snake_down.png')

felix=pygame.image.load('./images/felix.png')

class Snake:
    length=1  #current length of the snake
    big_image_list = [big_snake_img_left, \
                      big_snake_img_right,\
                      big_snake_img_up,   \
                      big_snake_img_down]

    small_image_list = [small_snake_img_left, \
                        small_snake_img_right,\
                        small_snake_img_up,   \
                        small_snake_img_down]
    # directionn of movement 0=left 1=right 2=up 3= down 
    current_direction=1
    #give displacement used for sname. indexed by direction, 0=left 1=right..
    displacement = [[-35,0], [35,0],[0,-35],[0,35]]
    gap = [[-50,0], [50,0],[0,-50],[0,50]]
    gap_scale=5

    one_time_print = True
    speed = 30  #current speed
    width=10    #width of the snake
        
    def __init__(self, speed, location):
        #list of all coordinates of the parts of the snake
        #we can also use list as list of tuple (x,y,direction)
        self.location = [[00,00]] #direction of the 1st head at begning
        self.direction = [-1] #direction for using image for each part of the snake
        self.speed=speed
        self.location[0][0]=location[0]
        self.location[0][1]=location[1]

    def print_location(self):
        print(type(self).__name__, "x=", self.location[0][0], "y=", self.location[0][1])
    
    def turn(self, direction):
        self.current_direction=direction

    def move_one(self):
        #pop tail and add as head in the direction of movement
        #self.location[-1] = (self.location[0.x])
        #print (self.location)
        #print (self.displacement)
        newhead = [ self.location[0][0] + self.displacement[self.current_direction][0], \
                    self.location[0][1] + self.displacement[self.current_direction][1]]
        self.location.pop()
        self.location.insert(0,newhead)
        newdirection = self.direction.pop()
        newdirection = self.current_direction
        self.direction.insert(0,newdirection)
    
    def draw(self, win):
        for i in range(len(self.location)):
            #win.blit(self.small_image_list[self.direction[i]], \
            #    (self.location[i][0], self.location[i][1]))
            win.blit(self.small_image_list[self.direction[i]], \
                (self.location[i][0], self.location[i][1]))
            #if(self.one_time_print):
            #    print("x=", self.location[i][0], "y=", self.location[i][1])
            #self.one_time_print=False
    
        #pygame.draw.rect(win,blue,[x1- (snake_block/2),y1-(snake_block/2),snake_block*snake_len,snake_block])
        #if snake_size_counter > 0:
        #    win.blit(big_snake_img,(x1- (snake_block/2),y1-(snake_block/2)))
        #    snake_size_counter = snake_size_counter-1
        #else:
        #    win.blit(small_snake_img,(x1- (snake_block/2),y1-(snake_block/2)))
        
        #pygame.draw.rect(win,blue,[x1- (snake_block/2),y1-(snake_block/2),snake_block*snake_len,snake_block])
        
    def eat_one(self):
        #add to tail in opposite direction of the current tail
        newtail = copy.deepcopy(self.location[-1])
        newdirection = copy.deepcopy(self.direction[-1])
        newtail[0] = newtail[0] - (5*(self.displacement[newdirection][0]))
        newtail[1] = newtail[1] - (5*(self.displacement[newdirection][1]))
        self.location.insert(len(self.location), newtail)
        self.direction.insert(len(self.direction), newdirection)
        self.length += 1

    def check_ate(self, foodx,foody):
        if self.location[0][0]< foodx+45 and self.location[0][0]>foodx-45 \
            and self.location[0][1]<foody+45 and self.location[0][1] >foody-45:
            return True;
        else:
            return False

#def message(msg,color,w,h):
    #mesg = font_style.render(msg, True, color)
    #dis.blit(mesg, [w/2, h/2])

def gameLoop():  # creating a function
    print("in game loop")
    #game_over = False
    #game_close = False

    #foodx = round(random.randrange(0, h - snake_block) / 10.0) * 10.0
    #foody = round(random.randrange(0, w - snake_block) / 10.0) * 10.0

def main():
    pygame.init()
    infoObject = pygame.display.Info()
    #w = int((infoObject.current_w)/2)
    #h = int((infoObject.current_h/2))
    w = infoObject.current_w - 300
    h = infoObject.current_h - 450

    snake  = Snake(50,[100,200])
    snake.print_location()
    snake1 = Snake(50,[200,300])
    snake1.print_location()
    snake.print_location()

    #w=1000
    #h=1000
    win = pygame.display.set_mode((w,h))
    pygame.display.update()
    pygame.display.set_caption('First game by varun(game is snake)')
    blue=(250,220,220)
    red=(255,0,0)

    big_snake_img=big_snake_img_left
    small_snake_img=small_snake_img_left

    game_over=False

    x1 = w/2
    y1 = h/2
    score=0
    snake_speed=30
    snake_block=40
    snake_len=1

    x1_change = 0       
    y1_change = 0
    
    clock = pygame.time.Clock()
    

    font_style = pygame.font.SysFont(None, 50)   

    #foodx = round(random.randrange(, h - snake_block) / 10.0) * 10.0
    #foody = round(random.randrange(0, w - snake_block) / 10.0) * 10.0
    #foodx = random.randrange(200, h - 200)
    #foody = random.randrange(200, w - 200)
    foodx = random.randrange(200, 2000)
    foody = random.randrange(200, 1000)
    snake_size_counter=0
 
    while not game_over:
        #while game_close == True:
        #   win.fill((0,0,0))
        #   message("You Lost! Press Q-Quit or C-Play Again", red)
        #   pygame.display.update()
        #   for event in pygame.event.get():
        #        if event.type == pygame.KEYDOWN:
        #            if event.key == pygame.K_q:
        #                game_over = True
        #                game_close = False
        #            if event.key == pygame.K_c:
        #                gameLoop()
        #for event in pygame.event.get():
        #        if event.type == pygame.KEYDOWN:
        #            if event.key == pygame.K_q:
        #                game_over = True
        #                game_close = False
        #            if event.key == pygame.K_c:
        #                gameLoop()
        

        for event in pygame.event.get():
            #print(event)
            if event.type==pygame.QUIT:
               game_over=True 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_direction='L'
                    big_snake_img=big_snake_img_left
                    small_snake_img=small_snake_img_left
                    x1_change = -10
                    y1_change = 0
                    snake.current_direction = LEFT
                    snake1.current_direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    current_direction='R'
                    big_snake_img=big_snake_img_right
                    small_snake_img=small_snake_img_right
                    x1_change = 10
                    y1_change = 0
                    snake.current_direction = RIGHT
                    snake1.current_direction = RIGHT
                elif event.key == pygame.K_UP:
                    current_direction='U'
                    big_snake_img=big_snake_img_up
                    small_snake_img=small_snake_img_up
                    y1_change = -10
                    x1_change = 0
                    snake.current_direction = UP
                    snake1.current_direction = UP
                elif event.key == pygame.K_DOWN:
                    current_direction='D'
                    big_snake_img=big_snake_img_down
                    small_snake_img=small_snake_img_down
                    y1_change = 10
                    x1_change = 0
                    snake.current_direction = DOWN
                    snake1.current_direction = DOWN
        if x1 >= w-(snake_block/5) or x1-(snake_block/5) < 0 or y1 >= h-(snake_block/5) or y1-(snake_block/5) < 0:
            #game_over = True
            game_over = False
 
        
        x1 += x1_change
        y1 += y1_change  
        win.fill((0,0,0))
        snake.move_one()
        snake.draw(win)
        snake1.move_one()
        snake1.draw(win)
        #pygame.draw.rect(win,blue,[x1- (snake_block/2),y1-(snake_block/2),snake_block*snake_len,snake_block])
     #   if snake_size_counter > 0:
     #       win.blit(big_snake_img,(x1- (snake_block/2),y1-(snake_block/2)))
     #       snake_size_counter = snake_size_counter-1
     #   else:
     #       win.blit(small_snake_img,(x1- (snake_block/2),y1-(snake_block/2)))
        
        #pygame.draw.rect(win,blue,[x1- (snake_block/2),y1-(snake_block/2),snake_block*snake_len,snake_block])
        pygame.draw.rect(win,(255,0,0), [foodx,foody,snake_block,snake_block])
    #    for tail_counter in range(score):
    #        win.blit(small_snake_img_left,(x1- (snake_block/2) - (5*tail_counter*x1_change),y1-(snake_block/2)-(5*tail_counter*y1_change)))
        #if x1< foodx+45 and x1>foodx-45 and y1<foody+45 and y1 >foody-45:
        if snake.check_ate(foodx,foody):
            print("Yummy!!")
            #foodx = round(random.randrange(0, h - snake_block) / 10.0) * 10.0
            #foody = round(random.randrange(0, w - snake_block) / 10.0) * 10.0
            #foodx = random.randrange(200, h - 200)
            #foody = random.randrange(200, w - 200)
            foodx = random.randrange(200, 2000)
            foody = random.randrange(200, 1000)
            snake_len=snake_len+1
            score=score+1
            snake_speed=snake_speed+3
            print(score)
            #print(foodx,foody)
            snake_size_counter = 80
            snake.eat_one()
            snake.length += 1

        if snake1.check_ate(foodx,foody):
            print("Yummy 4 me 2!!")
            foodx = random.randrange(200, 2000)
            foody = random.randrange(200, 1000)
            print(score)
            snake1.eat_one()
            snake1.length += 1

        pygame.display.update()
        
       
        #clock.tick(snake_speed)
        clock.tick(15)
    pygame.quit()
    quit()
gameLoop()
print("Ready?Sorry it aldready started.")
main()
