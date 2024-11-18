import random
import pgzrun

TITLE="Bumble bee game"

HEIGHT=500
WIDTH=600
score=0
gameover=False

bee=Actor("bee")
bee.pos=(100,100)

flower=Actor("flower")
flower.pos=(200,250)

def draw():
    screen.blit("bg",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score: "+ str(score), color="red", topleft=(10,10) )

    if gameover:
        screen.fill("red")
        screen.draw.text("Time is up! your final score is: "+ str(score), color="black", midtop=(300,10), fontsize=40)




def place_flower():
    flower.x=random.randint(70,550)
    flower.y=random.randint(50,450)

def time_up():
    global gameover
    gameover=True


def update():
    global score

    if keyboard.left:
        bee.x=bee.x-2
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.up:
        bee.y=bee.y-2
    if keyboard.down:
        bee.y=bee.y+2
    
    if bee.colliderect(flower):
        score+=10
        place_flower()

clock.schedule(time_up,60.0)

    








pgzrun.go()