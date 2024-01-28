import pygame

pygame.init()
import random

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

#game_files
game_sprites = {}
game_sounds = {}
background = 'snake_gallery/snake_sprites/snkbg.png'
welcome_bg = 'snake_gallery/snake_sprites/snkwelcome.png'

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("SnakesWithArpit")
pygame.display.update()                          # display me koi bhi changes krne ke baad isko run krna hota hai to update it
font = pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()        

# Game specific variables

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    # print(snk_list)
    for x,y in snk_list:
        # print(x,y)
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size],0,2)
        

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.blit(game_sprites["welcome_bg"],(160,200))
        gameWindow.blit(game_sprites['myphoto.png'],(330,50))
        text_screen("Welcome to Snake game by Arpit", red, 170, 250)
        text_screen("Press Space Bar To Play the game", red, 160, 320)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)


# Game Loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0     #Giving speed to our snake but starting me rest pe rakhna hai isliye 0
    velocity_y = 0
    snake_size = 10
    fps = 65
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    init_velocity = 5
    score = 0
    
    snk_list = []           #it is a list of list of co-ordinates of snake recs which append with each passing loops
    snk_length = 1      #an int value which keeps on increasing when snake eat food

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

            gameWindow.fill(black)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        
        else:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True


                if event.type == pygame.KEYDOWN:           
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity     #agr aisa nhi krenge to vel resultant diagonal ho jayega aur snake head diagonally move krega
                        velocity_y = 0
                        
                    
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:        #axis upper left corner se defined hai upward -y and downward +y                              
                        velocity_y = -init_velocity                #right me +x and left me -x
                        velocity_x = 0         

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<9 and abs(snake_y - food_y)<9:    #ye food aur snake ke centers ke beech kitna distance hoga taki snake food ko kha le                                                             
                score +=5                                             #abs absolute value ke liye hai
                # print("Score: ", score * 10)
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length += 1
                if score>int(hiscore):
                    hiscore = score

        
            gameWindow.blit(game_sprites["background"],(0,0))
            text_screen("Score: " + str(score), white,5,5)
            text_screen("Hiscore: " + str(hiscore), white, 630, 5)      #score screen
            pygame.draw.circle(gameWindow, red,(food_x,food_y),5.0)   #isko bhi white game window ke code ke neeche hi rakhna hai vrna show nhi krega 
            
            
            head = []                   #initialy 1 head append krne ke liye vrna snake dikhega nhi
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            

            if len(snk_list)>snk_length:    #this function deletes old rectangle co-ordinate  of snake i.e. tail or 0th rec
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True


            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

            plot_snake(gameWindow, black, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)   # frames per sec return krega


    pygame.quit()
    quit()



if __name__ == "__main__":
    game_sprites['background'] = pygame.image.load(background).convert()
    game_sprites['welcome_bg'] = pygame.image.load(welcome_bg).convert()
    game_sprites['myphoto.png'] = pygame.image.load('snake_gallery/snake_sprites/myphoto.png').convert_alpha()
    welcome()
    
    
 