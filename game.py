import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400)) #screen
pygame.display.set_caption("RIDDLE QUIZ")
clock=pygame.time.Clock()
test_surface=pygame.Surface((800,800))
test_font=pygame.font.Font('/Users/mikmin/Desktop/ByteBounce.ttf',50)

test_surface=pygame.image.load('/Users/mikmin/Desktop/_ (1).jpeg')
text_surface=test_font.render('LETS START!',False,'Black')
current_screen='start'  
test_surf=pygame.image.load('/Users/mikmin/Desktop/Start Button Clipart Transparent Background, Start Button In Pixel Art Style, Start, Button, Pixel Art PNG Image For Free Download.jpeg')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
                if 320<=mouse_pos[0]<=320+test_surf.get_width() and 200<=mouse_pos[1]<=200+test_surf.get_height():
                    print("clicked")
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN: 
                current_screen='next'  
                print('key down')      
        if event.type==pygame.KEYUP:
                print('key up')
        

    #draw our elements
    #update everything
    mouse_pos=pygame.mouse.get_pos()
    if current_screen=='next': #screen 2
        screen.fill('white')
        test_surface1=pygame.image.load('/Users/mikmin/Desktop/Blue sky cloud in pixel art style _ Premium Vector.jpeg')
        test_font1=pygame.font.Font('/Users/mikmin/Desktop/ByteBounce.ttf',35)
        test_font2=pygame.font.Font('/Users/mikmin/Desktop/ByteBounce.ttf',25)
        text_surface1=test_font1.render('QUESTION 1?',False,'Black')
        text_surface2=test_font2.render(" In One Piece, what is the name of Monkey D. Luffy’s signature straw hat's original owner??",False,'Black')
        screen.blit(test_surface1, (0, 0))     # background FIRST
        screen.blit(text_surface1, (300, 50)) 
        screen.blit(text_surface2, (150, 150))
    else:
        screen.blit(test_surface,(0,0))
        screen.blit(text_surface,(270,100))
        screen.blit(test_surf,(320,200))
    
    key=pygame.key.get_pressed()
    pygame.display.update()
    clock.tick(60)
