import pygame
pygame.init()
win=pygame.display.set_mode((900,600)) #for creating window
#img = pygame.image.load('#Enter the image')--------for favicon
#pygame.display.set_icon(img)
pygame.display.set_caption("LEVI Vs TITANS") #for naming(title) of window panel
x=50 #position of character
y=525 #for keeping it initially at bottom of win
width=40 #width of character
height=70
vel=15 #velocity

IsJump=False
jumpcount=10

run =True #window will be opened it it becomes false
while run:
    pygame.time.delay(100) #time delay
    #In for loop we will Set the things which we want your game to do when it is in a running state
    for event in pygame.event.get(): #events are anything that user do(keyborad key or mouse clicks)
        if event.type==pygame.QUIT:
            run=False #run will become false and window will be closed
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>vel:
        x-=vel
    if keys[pygame.K_RIGHT] and x<900-width-vel:#should not eceed win
        x+=vel
    if not(IsJump):
        if keys[pygame.K_UP] and y>vel:
            y-=vel
        if keys[pygame.K_DOWN] and y<600-height-vel:#should not eceed win
            y+=vel
        if keys[pygame.K_SPACE]:
            IsJump=True
    else:
        if jumpcount>=-10:
            neg=1 #if we are on first part of jump nothing happens
            #moving character
            if jumpcount<0:
                neg=-1 #if we are on second part it will come back
            y-=(jumpcount**2)*0.5*neg #quadractic equation(if we press space then chracter will be moved upward by given eq) aand here we multiply by negative to move downwards
            jumpcount-=1
        else:
            IsJump=False
            jumpcount=10

    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))#creating a rectangle,giving window(place in which it should be),colour(r,g,b),location on screen in coordinates,width and height
    pygame.display.update()


pygame.quit()