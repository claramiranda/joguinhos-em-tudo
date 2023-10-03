import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((840,210))
pygame.display.set_caption('Endless Runner')

clock = pygame.time.Clock()
crashed = False

obs1=974
obs2=574
obs3=874

altura=0

gameover=False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill((200,200,250))

    pygame.draw.rect(gameDisplay, (110,110,110), [0,170,840,40])

    if altura == 0 and event.type == pygame.KEYDOWN: altura=4
    if altura%3==1: altura+=3
    if altura%3==0: altura-=3
    if altura>100: altura=99
    if altura<1: altura=0

    if altura<20 and obs1>40 and obs1<94: gameover=True
    if altura<20 and obs2>40 and obs2<94: gameover=True
    if altura<20 and obs3>40 and obs3<94: gameover=True

    if gameover:
        obs1=974
        obs2=574
        obs3=874
        gameover=False

    if obs1>-30: obs1-=2
    else: obs1=850
    if obs2>-30: obs2-=2
    else: obs2=850
    if obs3>-30: obs3-=3
    else: obs3=850

    pygame.draw.line(gameDisplay,  (0, 0, 0), (80, 80-altura), (80, 140-altura))
    pygame.draw.line(gameDisplay,  (0, 0, 0), (60, 100-altura), (100, 100-altura))
    pygame.draw.line(gameDisplay,  (0, 0, 0), (80, 140-altura), (100, 170-altura))
    pygame.draw.line(gameDisplay,  (0, 0, 0), (80, 140-altura), (60, 170-altura))

    pygame.draw.line(gameDisplay,  (200, 0, 0), (obs1, 140), (obs1 + 40, 140))
    pygame.draw.line(gameDisplay,  (200, 0, 0), (obs2, 140), (obs2 + 40, 140))
    pygame.draw.line(gameDisplay,  (200, 0, 0), (obs3, 140), (obs3 + 40, 140))

    pygame.display.flip()

    pygame.display.update()
    clock.tick(120)

pygame.quit()
quit()
#https://licoesautenticas.rj.r.appspot.com/tutoriais/10/index.htm
