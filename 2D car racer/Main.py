import pygame 
import random
import sys

pygame.init()

#screen
screen = pygame.display.set_mode((840, 640))

#icon
icon = pygame.image.load("Assets/images/Icon.png")
pygame.display.set_icon(icon)

#Captions
Title = pygame.display.set_caption("2D Car Racer")

#Background
background = pygame.image.load("Assets/images/background.png")
bg_movement = 0
length = 640

#player
player_img = pygame.image.load("Assets/images/player_car.png")
player = pygame.transform.scale(player_img, (100, 200))
player_rect = player.get_rect(center = (480, 500))

#obstacle
obstacle_img = pygame.image.load("Assets/images/Obstacle_1.png")
obstacle_scale = pygame.transform.scale(obstacle_img, (100, 200))
obstacle2_img = pygame.image.load("Assets/images/obstacle_2.png")
obstacle2_scale = pygame.transform.scale(obstacle2_img, (100, 200))
obstacle_List = []
spawn_points_list = [(350, 10), (480, 15), (610, 20), (620, 5)]
SPAWNOBSTACLE = pygame.USEREVENT
pygame.time.set_timer(SPAWNOBSTACLE, (1000))

def create_obstacle():
    new_obstacle = obstacle_scale.get_rect(midbottom = random.choice(spawn_points_list))
    return new_obstacle

def move_obstacles(obstacles):
    for obstacle in obstacles:
        obstacle.centery += 5
    return obstacles    
 
def show_obstacles(obstacles):
    for obstacle in obstacles:
        screen.blit(obstacle_scale, obstacle)
        
def Detect_collision(obstacles):
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            print("Collision Detected")
        
def Game_Loop():
    running = True
    while True:
        
        global bg_movement
        global obstacle_List
        
        
        screen.fill((0, 0, 0))
        screen.blit(background, (0, bg_movement))
        screen.blit(background, (0, bg_movement - length))
        
        
        
        if bg_movement == +length:
            screen.blit(background, (0, bg_movement - length))
            bg_movement = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == SPAWNOBSTACLE:
                    obstacle_List.append(create_obstacle())
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_rect.centerx -= 120
                if event.key == pygame.K_RIGHT:
                    player_rect.centerx += 120    
                
                if player_rect.centerx >= 670:
                    print("Game Over")
                if player_rect.centerx <= 200:
                    print("Game Over") 
                       
                        
                                                                
        bg_movement += 4
        obstacle_List = move_obstacles(obstacle_List)
        show_obstacles(obstacle_List)
        Detect_collision(obstacle_List)
        screen.blit(player, player_rect)
        pygame.display.update() 
        
        
Game_Loop()        