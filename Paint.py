import pygame
pygame.init()
screen=pygame.Surface((700,550))
win=pygame.display.set_mode((700,650))
pygame.display.set_caption("Paint")
screen.fill((255,255,255))
run=True
c11=(200,200,200)
c1=(0,0,0)
c2=(255,255,255)
c3=(255,0,0)
c4=(0,255,0)
c5=(0,0,255)
c6=(255,255,0)
c7=(255,0,255)
c8=(0,255,255)
ccol=c1
csize=2
l=[(0,550,50,50),(0,600,50,50),(50,550,50,50),(50,600,50,50),(100,550,50,50),(100,600,50,50),(150,550,50,50),(150,600,50,50)]
font=pygame.font.SysFont("Sans", 32)
atclear=False
atsave=False
atfill=False
while run:
    mx,my=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    if pygame.mouse.get_pressed(num_buttons=3)[0]:
        cit=pygame.mouse.get_pos()
    else:
        cit=False
    win.fill(c2)
    for i in range(1,9):
        pygame.draw.rect(win, eval("c"+str(i)),l[i-1])
        if cit and l[i-1][0]<mx<l[i-1][0]+50 and l[i-1][1]<my<l[i-1][1]+50:
            ccol=eval("c"+str(i))
    pygame.draw.circle(win,ccol,(450,575),5)
    pygame.draw.circle(win,ccol,(470,575),10)
    pygame.draw.circle(win,ccol,(500,575),15)
    pygame.draw.circle(win,ccol,(540,575),20)
    pygame.draw.circle(win,c1,(450,575),5,width=1)
    pygame.draw.circle(win,c1,(470,575),10,width=1)
    pygame.draw.circle(win,c1,(500,575),15,width=1)
    pygame.draw.circle(win,c1,(540,575),20,width=1)

    if 300<mx<400 and 605<my<645:
        atclear=True
        cleartxt=font.render("CLEAR",True,c1,c11)
    else:
        atclear=False
        cleartxt=font.render("CLEAR",True,c1,c2)
    if 320<mx<380 and 555<my<595:
        atsave=True
        savetxt=font.render("SAVE",True,c1,c11)
    else:
        atsave=False
        savetxt=font.render("SAVE",True,c1,c2)
    if 470<mx<530 and 605<my<645:
        atfill=True
        filltxt=font.render("FILL",True,c1,c11)
    else:
        atfill=False
        filltxt=font.render("FILL",True,c1,c2)
    clearct=cleartxt.get_rect()
    clearct.center=(350,625)
    win.blit(cleartxt,clearct)
    saverct=savetxt.get_rect()
    saverct.center=(350,575)
    win.blit(savetxt,saverct)
    fillrct=filltxt.get_rect()
    fillrct.center=(500,625)
    win.blit(filltxt,fillrct)
    pygame.draw.line(win,(0,0,0),(0,550),(700,550))
    win.blit(screen,(0,0))
    if 0<mx<700 and 0<my<550:
        pygame.draw.circle(win,ccol,(mx,my),5*csize)
        pygame.draw.circle(win,c11,(mx,my),5*csize,width=1)
        pygame.mouse.set_visible(False)
        if cit:
             pygame.draw.circle(screen, ccol, (mx,my),5*csize)
    else:
        pygame.mouse.set_visible(True)
    if cit and 445<mx<455 and 570<my<580:
        csize=1
    if cit and 460<mx<480 and 565<my<585:
        csize=2
    if cit and 485<mx<515 and 560<my<590:
        csize=3
    if cit and 520<mx<560 and 555<my<595:
        csize=4
    if atclear and cit:
        screen.fill((255,255,255))
    if atsave and cit:
        pygame.image.save(screen, "Painted.jpg")
    if atfill and cit:
        screen.fill(ccol)
    pygame.display.update()
pygame.quit()