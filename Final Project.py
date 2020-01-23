import pygame

clicked = 0

green = (0, 200, 0)  # colours
light_green = (0, 255, 0)
red = (200, 0, 0)
light_red = (255, 0, 0)
light_blue = (0, 0, 255)
light_purple = (255, 0, 255)

startOn = True  # The start on and the parts on are for starting and stopping each stage of the  game
switchOn = False
gripOn = False
endcapOn = False
emmiterOn = False
bladeOn = False

bluecrystalOn = True   # each section of parts is for each stage of the game
redcrystalOn = True
greencrystalOn = True
purplecrystalOn = True

quigonswitchOn = True
lukeswitchOn = True
obiwanswitchOn = True
anakinswitchOn = True

dookugripOn = True
kitfistogripOn = True
darthvadergripOn = True
obiwangripOn = True

winduendcapOn = True
obiwanendcapOn = True
lukeendcapOn = True
quigonendcapOn = True

winduemmiterOn = True
maulemmiterOn = True
quigonemmiterOn = True
lukeemmiterOn = True


def text_objects(text, font):  # this function is for placing text on to shapes for buttons
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def buttons(msg,x, y, w, h, ic, ac, action=None):  # this function is for making buttons with text. The msg is the message, x is the x position, y is the y position, w is the width, h is the height, ic is the initial colour,
    # ac is the active colour, and there is no action
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if msg == "Blueberry": # this message I would put in the message section when I call the function if I wanted no text on the button
        if x + w > mouse[0] > x and y + h > mouse[1] > y:  #  this tracks the position of the mouse when it is on the shape which activte the actove colour
            pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                Clickedrect = True
                return Clickedrect
        else:
            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    else:  # this is the  same as the code above except it will have text on it because the msg is not blueberry
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                Clickedrect = True
                return Clickedrect
        else:
            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

        smallText = pygame.font.Font("freesansbold.ttf", 30)  # this is the font and size
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))  # this just centers the text on the shape
        gameDisplay.blit(textSurf, textRect)


def buttonsq(msg, x, y, w, h, ic, ac, action=None):  # this function is the same  at the one above except is have the ability to quit for the quit button
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if msg == "Blueberry":
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                Clickedquit = True
                return Clickedquit
        else:
            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    else:
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                Clickedquit = True
                return Clickedquit
        else:
            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smallText = pygame.font.Font("freesansbold.ttf", 30)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(textSurf, textRect)


def buttonimg(x, y, w, h):  # this is used for making images into buttons
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1:
            Clickedimg = True
            return Clickedimg


pygame.init()
gameDisplay = pygame.display.set_mode((1200, 950))  # sets size of the game screen
pygame.display.set_caption("Lightsaber Creator")  # sets the title of
background_1 = pygame.image.load("Background.jpg").convert()  # loads image in
background_2 = pygame.image.load("StartBackground.jpg").convert()
gameDisplay.blit(background_2, [-168, 0])  # inserts background

run = True

while run:
    pygame.time.delay(300)
    for event in pygame.event.get():  # is  for stopping the while loop
        if event.type == pygame.QUIT:
            run = False

    if startOn:
        buttons("Start", 520, 415, 160, 60, green, light_green, "Next")  # function is called variables are given values
        Clickedrect = buttons("Start", 520, 415, 160, 60, green, light_green, "Next")
        if Clickedrect == True:
            startOn = False
    else:
        gameDisplay.blit(background_1, [0, 0])  # switches background after start button is clicked
        pygame.display.update()

        if bluecrystalOn == True:  # blue crystal on is already true so it runs the code
            bluecrystal = pygame.image.load("blue crystal.png")  # loads image
            bluecrystal = pygame.transform.scale(bluecrystal, (200, 150))  # transform the dimensions of the image to a width of 200 and height of 150
            gameDisplay.blit(bluecrystal, [-25, -5])  # position of image
            Clickedimg = buttonimg(-25, -5, 200, 150)  # calls function for clicking the button
            if Clickedimg == True:
                bluecrystalOn = False  # turns false to start next portion of code
                redcrystalOn = 2  # turns other variables to digits so it doesn't run their second parts
                greencrystalOn = 2
                purplecrystalOn = 2
        elif bluecrystalOn == False:
            gameDisplay.blit(bluecrystal, [600, 404])  # moves image to new position
            bluecrystal = pygame.transform.scale(bluecrystal, (80, 60))  # makes the image smaller
            pygame.display.update()
            switchOn = True  # activates next section of the game

        if redcrystalOn == True:  # code is the same as above but different variable names and images
            redcrystal = pygame.image.load("red crystal.png")
            redcrystal = pygame.transform.scale(redcrystal, (190, 147))
            gameDisplay.blit(redcrystal, [1035, -5])
            Clickedimg = buttonimg(1035, -5, 190, 147)
            if Clickedimg == True:
                redcrystalOn = False
                bluecrystalOn = 2
                greencrystalOn = 2
                purplecrystalOn = 2
        elif redcrystalOn == False:
            gameDisplay.blit(redcrystal, [602, 407])
            redcrystal = pygame.transform.scale(redcrystal, (67, 51))
            pygame.display.update()
            switchOn = True

        if greencrystalOn == True:  # code is the same as above but different variable names and images
            greencrystal = pygame.image.load("green crystal.png")
            greencrystal = pygame.transform.scale(greencrystal, (200, 150))
            gameDisplay.blit(greencrystal, [1035, 650])
            Clickedimg = buttonimg(1035, 650, 200, 150)
            if Clickedimg == True:
                greencrystalOn = False
                bluecrystalOn = 2
                redcrystalOn = 2
                purplecrystalOn = 2
        elif greencrystalOn == False:
            gameDisplay.blit(greencrystal, [600, 400])
            greencrystal = pygame.transform.scale(greencrystal, (80, 60))
            pygame.display.update()
            switchOn = True

        if purplecrystalOn == True:  # code is the same as above but different variable names and images
            purplecrystal = pygame.image.load("purple crystal.png")
            purplecrystal = pygame.transform.scale(purplecrystal, (200, 150))
            gameDisplay.blit(purplecrystal, [-25, 650])
            Clickedimg = buttonimg(-25, 650, 200, 150)
            if Clickedimg == True:
                purplecrystalOn = False
                bluecrystalOn = 2
                redcrystalOn = 2
                greencrystalOn = 2
        elif purplecrystalOn == False:
            gameDisplay.blit(purplecrystal, [610, 400])
            purplecrystal = pygame.transform.scale(purplecrystal, (80, 60))
            pygame.display.update()
            switchOn = True

        if switchOn == True:
            pygame.time.delay(300)
            if quigonswitchOn == True:  # code is the same as above but different variable names and images
                quigonswitch = pygame.image.load("qui gon switch.png")
                quigonswitch = pygame.transform.scale(quigonswitch, (200, 150))
                gameDisplay.blit(quigonswitch, [0, 0])
                Clickedimg2 = buttonimg(0, 0, 200, 150)
                if Clickedimg2 == True:
                    quigonswitchOn = False
                    lukeswitchOn = 2
                    obiwanswitchOn = 2
                    anakinswitchOn = 2
            elif quigonswitchOn == False:
                gameDisplay.blit(quigonswitch, [600, 410])
                quigonswitch = pygame.transform.scale(quigonswitch, (80, 60))
                pygame.display.update()
                gripOn = True

            if lukeswitchOn == True:  # code is the same as above but different variable names and images
                lukeswitch = pygame.image.load("luke switch.png")
                lukeswitch = pygame.transform.scale(lukeswitch, (200, 150))
                gameDisplay.blit(lukeswitch, [1000, 0])
                Clickedimg = buttonimg(1000, 0, 200, 150)
                if Clickedimg == True:
                    lukeswitchOn = False
                    quigonswitchOn = 2
                    obiwanswitchOn = 2
                    anakinswitchOn = 2
            elif lukeswitchOn == False:
                gameDisplay.blit(lukeswitch, [597, 410])
                lukeswitch = pygame.transform.scale(lukeswitch, (80, 60))
                pygame.display.update()
                gripOn = True

            if obiwanswitchOn == True:  # code is the same as above but different variable names and images
                obiwanswitch = pygame.image.load("obi wan switch.png")
                obiwanswitch = pygame.transform.scale(obiwanswitch, (200, 150))
                gameDisplay.blit(obiwanswitch, [1000, 625])
                Clickedimg = buttonimg(1000, 625, 200, 150)
                if Clickedimg == True:
                    obiwanswitchOn = False
                    quigonswitchOn = 2
                    lukeswitchOn = 2
                    anakinswitchOn = 2
            elif obiwanswitchOn == False:
                gameDisplay.blit(obiwanswitch, [600, 400])
                obiwanswitch = pygame.transform.scale(obiwanswitch, (80, 60))
                pygame.display.update()
                gripOn = True

            if anakinswitchOn == True:  # code is the same as above but different variable names and images
                anakinswitch = pygame.image.load("anakin switch.png")
                anakinswitch = pygame.transform.scale(anakinswitch, (200, 150))
                gameDisplay.blit(anakinswitch, [0, 625])
                Clickedimg = buttonimg(0, 625, 200, 150)
                if Clickedimg == True:
                    anakinswitchOn = False
                    quigonswitchOn = 2
                    lukeswitchOn = 2
                    obiwanswitchOn = 2
            elif anakinswitchOn == False:
                gameDisplay.blit(anakinswitch, [600, 400])
                anakinswitch = pygame.transform.scale(anakinswitch, (80, 60))
                pygame.display.update()
                gripOn = True


            if gripOn == True:
                pygame.time.delay(300)
                if dookugripOn == True:  # code is the same as above but different variable names and images
                    dookugrip = pygame.image.load("dooku grip.png")
                    dookugrip = pygame.transform.scale(dookugrip, (300, 150))
                    gameDisplay.blit(dookugrip, [0, 0])
                    Clickedimg = buttonimg(0, 0, 300, 150)
                    if Clickedimg == True:
                        dookugripOn = False
                        kitfistogripOn = 2
                        darthvadergripOn = 2
                        obiwangripOn = 2
                elif dookugripOn == False:
                    gameDisplay.blit(dookugrip, [508, 416])
                    dookugrip = pygame.transform.scale(dookugrip, (100, 40))
                    pygame.display.update()
                    endcapOn = True

                if kitfistogripOn == True:  # code is the same as above but different variable names and images
                    kitfistogrip = pygame.image.load("kit fisto grip.png")
                    kitfistogrip = pygame.transform.scale(kitfistogrip, (304, 150))
                    gameDisplay.blit(kitfistogrip, [900, 0])
                    Clickedimg = buttonimg(900, 0, 300, 150)
                    if Clickedimg == True:
                        kitfistogripOn = False
                        dookugripOn = 2
                        darthvadergripOn = 2
                        obiwangripOn = 2
                elif kitfistogripOn == False:
                    gameDisplay.blit(kitfistogrip, [507, 413])
                    kitfistogrip = pygame.transform.scale(kitfistogrip, (103, 50))
                    pygame.display.update()
                    endcapOn = True

                if darthvadergripOn == True:  # code is the same as above but different variable names and images
                    darthvadergrip = pygame.image.load("darth vader grip.png")
                    darthvadergrip = pygame.transform.scale(darthvadergrip, (300, 150))
                    gameDisplay.blit(darthvadergrip, [900, 600])
                    Clickedimg = buttonimg(900, 600, 300, 150)
                    if Clickedimg == True:
                        darthvadergripOn = False
                        dookugripOn = 2
                        kitfistogripOn = 2
                        obiwangripOn = 2
                elif darthvadergripOn == False:
                    gameDisplay.blit(darthvadergrip, [508, 413])
                    darthvadergrip = pygame.transform.scale(darthvadergrip, (100, 50))
                    pygame.display.update()
                    endcapOn = True

                if obiwangripOn == True:  # code is the same as above but different variable names and images
                    obiwangrip = pygame.image.load("obi wan grip.png")
                    obiwangrip = pygame.transform.scale(obiwangrip, (300, 150))
                    gameDisplay.blit(obiwangrip, [0, 600])
                    Clickedimg = buttonimg(0, 600, 300, 150)
                    if Clickedimg == True:
                        obiwangripOn = False
                        dookugripOn = 2
                        darthvadergripOn = 2
                        kitfistogripOn = 2
                elif obiwangripOn == False:
                    gameDisplay.blit(obiwangrip, [506, 413])
                    obiwangrip = pygame.transform.scale(obiwangrip, (100, 50))
                    pygame.display.update()
                    endcapOn = True


                if endcapOn == True:
                    pygame.time.delay(300)
                    if winduendcapOn == True:  # code is the same as above but different variable names and images
                        winduendcap = pygame.image.load("windu end cap.png")
                        winduendcap = pygame.transform.scale(winduendcap, (200, 150))
                        gameDisplay.blit(winduendcap, [0, 0])
                        Clickedimg = buttonimg(0, 0, 200, 150)
                        if Clickedimg == True:
                            winduendcapOn = False
                            obiwanendcapOn = 2
                            lukeendcapOn = 2
                            quigonendcapOn = 2
                    elif winduendcapOn == False:
                        gameDisplay.blit(winduendcap, [442, 411])
                        winduendcap = pygame.transform.scale(winduendcap, (75, 50))
                        pygame.display.update()
                        emmiterOn = True

                    if obiwanendcapOn == True:  # code is the same as above but different variable names and images
                        obiwanendcap = pygame.image.load("obi wan end cap.png")
                        obiwanendcap = pygame.transform.scale(obiwanendcap, (200, 150))
                        gameDisplay.blit(obiwanendcap, [1000, 0])
                        Clickedimg = buttonimg(1000, 0, 200, 150)
                        if Clickedimg == True:
                            obiwanendcapOn = False
                            winduendcapOn = 2
                            lukeendcapOn = 2
                            quigonendcapOn = 2
                    elif obiwanendcapOn == False:
                        gameDisplay.blit(obiwanendcap, [444, 411])
                        obiwanendcap = pygame.transform.scale(obiwanendcap, (75, 50))
                        pygame.display.update()
                        emmiterOn = True

                    if lukeendcapOn == True:  # code is the same as above but different variable names and images
                        lukeendcap = pygame.image.load("luke end cap.png")
                        lukeendcap = pygame.transform.scale(lukeendcap, (200, 140))
                        gameDisplay.blit(lukeendcap, [975, 600])
                        Clickedimg = buttonimg(975, 600, 200, 140)
                        if Clickedimg == True:
                            lukeendcapOn = False
                            obiwanendcapOn = 2
                            winduendcapOn = 2
                            quigonendcapOn = 2
                    elif lukeendcapOn == False:
                        gameDisplay.blit(lukeendcap, [451, 413])
                        lukeendcap = pygame.transform.scale(lukeendcap, (65, 50))
                        pygame.display.update()
                        emmiterOn = True

                    if quigonendcapOn == True:  # code is the same as above but different variable names and images
                        quigonendcap = pygame.image.load("qui gon end  cap.png")
                        quigonendcap = pygame.transform.scale(quigonendcap, (200, 140))
                        gameDisplay.blit(quigonendcap, [0, 600])
                        Clickedimg = buttonimg(0, 600, 200, 140)
                        if Clickedimg == True:
                            quigonendcapOn = False
                            obiwanendcapOn = 2
                            winduendcapOn = 2
                            lukeendcapOn = 2
                    elif quigonendcapOn == False:
                        gameDisplay.blit(quigonendcap, [456, 413])
                        quigonendcap = pygame.transform.scale(quigonendcap, (65, 50))
                        pygame.display.update()
                        emmiterOn = True

                    if emmiterOn == True:
                        pygame.time.delay(300)
                        if winduemmiterOn == True:  # code is the same as above but different variable names and images
                            winduemmiter = pygame.image.load("windu emmiter.png")
                            winduemmiter = pygame.transform.scale(winduemmiter, (200, 150))
                            gameDisplay.blit(winduemmiter, [0, 0])
                            Clickedimg = buttonimg(0, 0, 200, 150)
                            if Clickedimg == True:
                                winduemmiterOn = False
                                maulemmiterOn = 2
                                quigonemmiterOn = 2
                                lukeemmiterOn = 2
                        elif winduemmiterOn == False:
                            gameDisplay.blit(winduemmiter, [670, 411])
                            winduemmiter = pygame.transform.scale(winduemmiter, (60, 50))
                            pygame.display.update()
                            bladeOn = True

                        if maulemmiterOn == True:  # code is the same as above but different variable names and images
                            maulemmiter = pygame.image.load("maul emmiter.png")
                            maulemmiter = pygame.transform.scale(maulemmiter, (200, 150))
                            gameDisplay.blit(maulemmiter, [1000, 0])
                            Clickedimg = buttonimg(1000, 0, 200, 150)
                            if Clickedimg == True:
                                maulemmiterOn = False
                                winduemmiterOn = 2
                                quigonemmiterOn = 2
                                lukeemmiterOn = 2
                        elif maulemmiterOn == False:
                            gameDisplay.blit(maulemmiter, [668, 408])
                            maulemmiter = pygame.transform.scale(maulemmiter, (75, 57))
                            pygame.display.update()
                            bladeOn = True

                        if quigonemmiterOn == True:  # code is the same as above but different variable names and images
                            quigonemmiter = pygame.image.load("qui  gon emmiter.png")
                            quigonemmiter = pygame.transform.scale(quigonemmiter, (200, 150))
                            gameDisplay.blit(quigonemmiter, [1000, 600])
                            Clickedimg = buttonimg(1000, 600, 200, 150)
                            if Clickedimg == True:
                                quigonemmiterOn = False
                                winduemmiterOn = 2
                                maulemmiterOn = 2
                                lukeemmiterOn = 2
                        elif quigonemmiterOn == False:
                            gameDisplay.blit(quigonemmiter, [665, 414])
                            quigonemmiter = pygame.transform.scale(quigonemmiter, (60, 50))
                            pygame.display.update()
                            bladeOn = True

                        if lukeemmiterOn == True:  # code is the same as above but different variable names and images
                            lukeemmiter = pygame.image.load("luke emmiter.png")
                            lukeemmiter = pygame.transform.scale(lukeemmiter, (200, 150))
                            gameDisplay.blit(lukeemmiter, [0, 600])
                            Clickedimg = buttonimg(0, 600, 200, 150)
                            if Clickedimg == True:
                                lukeemmiterOn = False
                                winduemmiterOn = 2
                                maulemmiterOn = 2
                                quigonemmiterOn = 2
                        elif lukeemmiterOn == False:
                            gameDisplay.blit(lukeemmiter, [662, 414])
                            lukeemmiter = pygame.transform.scale(lukeemmiter, (60, 50))
                            pygame.display.update()
                            bladeOn = True

                        if bladeOn == True:
                            pygame.time.delay(300)
                            if bluecrystalOn == False:  # chooses the colour based off the crystal picked at the start
                                if lukeemmiterOn ==  False:  # each has specific positions based off their dimensions
                                    pygame.draw.rect(gameDisplay, light_blue, (718, 424, 300, 30))
                                elif quigonemmiterOn == False:
                                    pygame.draw.rect(gameDisplay, light_blue, (720, 423, 300, 30))
                                elif maulemmiterOn == False:
                                    pygame.draw.rect(gameDisplay, light_blue, (741, 421, 300, 30))
                                elif winduemmiterOn == False:
                                    pygame.draw.rect(gameDisplay, light_blue, (726, 420, 300, 30))

                            if redcrystalOn == False:  # code is the same as above but different colours
                                if lukeemmiterOn ==  False:
                                    pygame.draw.rect(gameDisplay, light_red, (718, 424, 300, 30))
                                elif quigonemmiterOn == False:
                                    pygame.draw.rect(gameDisplay, light_red, (72, 423, 300, 30))
                                elif maulemmiterOn == False:
                                    pygame.draw.rect(gameDisplay, light_red, (741, 421, 300, 30))
                                elif winduemmiterOn == False:
                                    pygame.draw.rect(gameDisplay, light_red, (726, 420, 300, 30))

                            if purplecrystalOn == False:  # code is the same as above but different colours
                                if lukeemmiterOn ==  False:
                                    pygame.draw.rect(gameDisplay, light_purple, (718, 424, 300, 30))
                                elif quigonemmiterOn == False:
                                    pygame.draw.rect(gameDisplay, light_purple, (720, 423, 300, 30))
                                elif maulemmiterOn == False:
                                    pygame.draw.rect(gameDisplay, light_purple, (741, 421, 300, 30))
                                elif winduemmiterOn == False:
                                    pygame.draw.rect(gameDisplay, light_purple, (726, 420, 300, 30))

                            if greencrystalOn == False:  # code is the same as above but different colours
                                if lukeemmiterOn ==  False:
                                    pygame.draw.rect(gameDisplay, light_green, (718, 424, 300, 30))
                                elif quigonemmiterOn == False:
                                    pygame.draw.rect(gameDisplay, light_green, (720, 423, 300, 30))
                                elif maulemmiterOn == False:
                                    pygame.draw.rect(gameDisplay, light_green, (741, 421, 300, 30))
                                elif winduemmiterOn == False:
                                    pygame.draw.rect(gameDisplay, light_green, (726, 420, 300, 30))

    buttonsq("Quit", 520, 20, 160, 60, red, light_red, "Quit")  # calls quit button function
    Clickedquit = buttonsq("Quit", 520, 20, 160, 60, red, light_red, "Quit")
    if Clickedquit == True:
        pygame.quit()
        quit()
    pygame.display.update()

pygame.quit()