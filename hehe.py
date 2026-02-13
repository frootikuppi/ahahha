import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800,400)) #screen
pygame.display.set_caption(" QUIZ")
clock=pygame.time.Clock()
test_surface=pygame.Surface((800,800))
test_font=pygame.font.Font('/Users/mikmin/Desktop/ByteBounce.ttf',50)

test_surface=pygame.image.load('/Users/mikmin/Desktop/_ (1).jpeg')
text_surface=test_font.render('LETS START!',False,'Black')
current_screen='start'  
ans=""
correct_screen="false"
test_surf=pygame.image.load('/Users/mikmin/Desktop/Start Button Clipart Transparent Background, Start Button In Pixel Art Style, Start, Button, Pixel Art PNG Image For Free Download.jpeg')

def word_wrap(text, max_width):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        # Check if adding the next word exceeds the width
        if len(current_line) + len(word) + (1 if current_line else 0) <= max_width:
            current_line += (" " if current_line else "") + word
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
                if 320<=mouse_pos[0]<=320+test_surf.get_width() and 200<=mouse_pos[1]<=200+test_surf.get_height():
                    current_screen='next'
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
        test_font2=pygame.font.Font('/Users/mikmin/Desktop/ByteBounce.ttf',29)
        option_button1=pygame.image.load('/Users/mikmin/Desktop/option button.png') #option button image
        option_button2=pygame.image.load('/Users/mikmin/Desktop/option button.png') #option button image
        option_button3=pygame.image.load('/Users/mikmin/Desktop/option button.png') #option button image
        option_button4=pygame.image.load('/Users/mikmin/Desktop/option button.png') #option button image
        option_font1 = pygame.font.Font('/Users/mikmin/Desktop/ByteBounce.ttf',25) #option text font
        option_font2 = pygame.font.Font('/Users/mikmin/Desktop/ByteBounce.ttf',25) #option text font
        option_font3 = pygame.font.Font('/Users/mikmin/Desktop/ByteBounce.ttf',25) #option text font
        option_font4 = pygame.font.Font('/Users/mikmin/Desktop/ByteBounce.ttf',25) #option text font
        character1=pygame.image.load('/Users/mikmin/Desktop/one.png') #char image
        
         # question text 1 
        text_surface1=test_font1.render('QUESTION 1?',False,'Black')
        text2 = " In One Piece, what is the name of Monkey D. Luffy's  signature straw hat's original owner??" 
        text_option1=option_font1.render('A) Silvers Rayleigh',False,'Black') # option 1 text
        text_option2=option_font2.render('B) Gol D. Roger',False,'Black') # option 2 text answer
        text_option3=option_font3.render('C) Red-Haired Shanks',False,'Black') # option 3 text
        text_option4=option_font4.render('D) Monkey D. Dragon',False,'Black') # option 4 text
        screen.blit(test_surface1, (0, 0))     # background FIRST
        screen.blit(text_surface1, (400 - text_surface1.get_width() // 2, 20))    #at top centre
         # 4 option button arranged below the question
        screen.blit(option_button1, (200, 160)) #button 1
        screen.blit(text_option1, (230, 219)) # option text on button 1
        screen.blit(option_button2, (200, 250)) #button 2
        screen.blit(text_option2, (230, 309)) # option text on button 2
        screen.blit(option_button3, (450, 160)) # button 3
        screen.blit(text_option3, (480, 219)) # option text on button 3
        screen.blit(option_button4, (450, 250)) # button 4
        screen.blit(text_option4, (480, 309)) # option text on button 4
        screen.blit(character1, (6, 200)) # char image at bottom left
        #option choose by mouse click
        if event.type==pygame.MOUSEBUTTONDOWN:
            if 200<=mouse_pos[0]<=200+option_button1.get_width() and 160<=mouse_pos[1]<=160+option_button1.get_height():
                ans="a"
                print("option a chosen")
            if 200<=mouse_pos[0]<=200+option_button2.get_width() and 250<=mouse_pos[1]<=250+option_button2.get_height():
                ans="b"
                print("option b chosen")
            if 450<=mouse_pos[0]<=450+option_button3.get_width() and 160<=mouse_pos[1]<=160+option_button3.get_height():
                ans="c"
                print("option c chosen")
            if 450<=mouse_pos[0]<=450+option_button4.get_width() and 250<=mouse_pos[1]<=250+option_button4.get_height():
                ans="d"
                print("option d chosen")
         
                
        #word wrap for long question text
        offset = 15
        for i in word_wrap(text2, 50):
            offset += 20
            text_surface2 = test_font2.render(i, False, 'Black')
            screen.blit(text_surface2, (180, 70 + offset))
        #correct ansswer check
        if ans=="b":
            correct_screen="yes"
            print("correct")
        else:
            correct_screen="false"
            print("wrong")
            #change screen  based on answer
        if correct_screen=="yes":
            screen.fill('white')
            correct_surface1=pygame.image.load('/Users/mikmin/Desktop/correct answe.jpeg')
            correct_text_font=pygame.font.Font('/Users/mikmin/Desktop/Pixel Game.otf',40)
            correct_text=correct_text_font.render('CORRECT!',False,'Black')
            screen.blit(correct_surface1,(0,0))
            screen.blit(correct_text,(200,100))

    else:
        screen.blit(test_surface,(0,0))
        screen.blit(text_surface,(270,100))
        screen.blit(test_surf,(320,200))
    
    key=pygame.key.get_pressed()
    pygame.display.update()
    clock.tick(60)
