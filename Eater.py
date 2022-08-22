import pygame
import random
import tkinter
import os
from tkinter.constants import *
pygame.init()
pygame.mixer.init()

white = (230,230,250)
red = (255, 0, 0)
black = (0, 0, 0)
blue  = (0,0,255)
height = 400
width = 600

gamewindow = pygame.display.set_mode((width,height))
pygame.display.set_caption("Eater")
pygame.display.update()

clock = pygame.time.Clock()
font =  pygame.font.SysFont(pygame.font.get_fonts()[0], 20)
if (not os.path.exists("High_Score.txt")):
    with open("High_Score.txt", "w") as High_Score:
        High_Score.write("0")

with open("High_Score.txt", "r") as h:
    High_Score = h.read()

def text_screen(test, color, x ,y):
    screen_score = font.render(test, True, color)
    gamewindow.blit(screen_score, [x,y])

def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill((233,210,229))
        text_screen("Welcome to Eater", blue, 200, 150)
        text_screen("Press Space Bar To Play", red, 180, 190)
        pygame.mixer.music.load("Start.mp3")
        pygame.mixer.music.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
    
        pygame.display.update()
        clock.tick(30)   

def gameloop():

    exit_game = False
    game_over = False
    eater_x = 25
    eater_y = 25
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(0,width)
    food_y = random.randint(0,height)
    eater_size = 15
    food_size = eater_size
    score = 0
    fps = 30
    global High_Score
    
    
    while not exit_game:
        if game_over:
            with open("High_Score.txt", "w") as h:
                h.write(str(High_Score))
             
            gamewindow.fill(white)
            #pygame.mixer.music.load("YouAreDead.mp3")
            #pygame.mixer.music.play()
                   
            text_screen("Game Over!!! Press Enter To Continue", red, width/4, height/4)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_RETURN:
                        pygame.mixer.music.load("Start.mp3")
                        pygame.mixer.music.play()

                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_RIGHT:
                        velocity_x = +5
                        velocity_y = 0
                        
                    if event.key == pygame.K_LEFT:
                        velocity_x = -5
                        velocity_y = 0
                        
                    if event.key == pygame.K_UP:
                        velocity_y = -5
                        velocity_x = 0
                        
                    if event.key == pygame.K_DOWN:
                        velocity_y =+ 5
                        velocity_x = 0

                        
            gamewindow.fill(white)
            text_screen("Score: " + str(score), blue ,5,5)
            text_screen("High Score: "+ str(High_Score), blue ,width-150,5)
            
            
            if abs(eater_x - food_x)<5 and (eater_y - food_y)<5:
                score = score + 1
                pygame.mixer.music.load("EatingSound.mp3")
                pygame.mixer.music.play()
                food_x = random.randint(0,width)
                food_y = random.randint(0,height)
            
                if score>int(High_Score):
                    High_Score = score 
         
                          
            if eater_x < 0 or eater_x > width or eater_y < 0 or eater_y > height:
                game_over = True
                pygame.mixer.music.load("CollisionSound.mp3")
                pygame.mixer.music.play()

                       
            eater_x = eater_x +  velocity_x
            eater_y = eater_y +  velocity_y

            pygame.draw.rect(gamewindow ,black, [eater_x, eater_y, eater_size, eater_size])
            pygame.draw.rect(gamewindow, red, [food_x, food_y ,food_size/2 , food_size/2])
        
        pygame.display.update()
        clock.tick(fps)
       
    pygame.quit()

welcome() 
           




