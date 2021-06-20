# TO PLAY ONE OF THE ENDINGS IN WOAM YOU HAVE TO INSTALL THE 'pygame' MODULE #
# HOW TO DO SO: #
# File > Settings > Project: example > Project Interpreter #
# CLICK THE "+" BUTTON AND TYPE "pygame" #
# INSTALL THE PACKAGE #

# Imports Time/ Sleep and Random
import time
import random
import winsound
import urllib.request
import os
import getpass

# Health variable
health = 3

# Save directory
username = getpass.getuser()

# Define dieimg to save an image to the desktop
def dieimg():
    urllib.request.urlretrieve("https://i.ytimg.com/vi/mwuUUY1wuBU/maxresdefault.jpg",
                               "C:\\Users\\" + username + "\\Desktop\\GG_This_Is_For_You.jpg")
    os.startfile('C:\\Users\\' + username + '\\Desktop\\GG_This_Is_For_You.jpg')

# Define winimg to save an image to the desktop
def winimg():
    urllib.request.urlretrieve("https://ih1.redbubble.net/image.695347668.1283/throwpillow,small,1000x-bg,f8f8f8-c,0,200,1000,1000.jpg",
                               "C:\\Users\\" + username + "\\Desktop\\You_Win.jpg")
    os.startfile('C:\\Users\\' + username + '\\Desktop\\You_Win.jpg')

# Start Game Input
winsound.PlaySound('C:\\Users\\' + username + '\\Desktop\\WoamSFX\\menu_music.wav',winsound.SND_ASYNC)
print('''
 __      __                     
/  \    /  \_________    _____  
\   \/\/   /  _ \__  \  /     \ 
 \        (  <_> ) __ \|  Y Y  |
  \__/\  / \____(____  /__|_|  /
       \/            \/      \/
Made by Dxrpy (A.k.a Ethan Crump)
       ''')
start = input('Press the enter key to start ')
winsound.PlaySound(None, winsound.SND_PURGE)

# Plays sound effect
winsound.PlaySound('C:\\Users\\' + username + '\\Desktop\\WoamSFX\\start_game.wav',winsound.SND_ASYNC)
time.sleep(1)
winsound.PlaySound(None, winsound.SND_PURGE)


### Easter Egg ###
if start == ('EthanIsTheBestCoder'):
    print('You win.')
    time.sleep(2)
    print('No questions asked.')
    winimg()
    exit()
elif start == ('3&@5%'):
    print('Not here ya knob.')
    exit()
else:
    pass
### Easter Egg ###


# Simple print messages for instructions and backstory #
print()
print('Your characters name is Woam')
time.sleep(2)
print('Woam is a few chromosomes short.')
time.sleep(2)
print('He also has 3 health points, each failed guess lowers your health.')
print()
time.sleep(3)
print('To start off this journey, Woam was walking around one day and saw something in the bush.')
time.sleep(4)



# For loop to clear the screen
for x in range(9):
    print()



print('BAM! QUEUE THE POKEMON ENCOUNTER MUSIC')
print('(For you numbnuts, that means a wild enemy is attacking.)')
print()
winsound.PlaySound('C:\\Users\\' + username + '\\Desktop\\WoamSFX\\encounter.wav',winsound.SND_ASYNC)
time.sleep(4)


# Determines the enemy hp
firstenemyhp = random.randint(1,10)

# First enemy and fight options
print()
print('The enemy is like', firstenemyhp, 'hp or something')
print('Choose an attack 1-3:')
print()
print('''Take a wizz on his legs (1)
Punch him (2)
Run away (3)''')

# Your attack input
attack1 = input('')


# Pokemon end sound effect
winsound.PlaySound(None, winsound.SND_PURGE)
winsound.PlaySound('C:\\Users\\' + username + '\\Desktop\\WoamSFX\\pokemon_end.wav',winsound.SND_ASYNC)
time.sleep(2)
winsound.PlaySound(None, winsound.SND_PURGE)



# If you choose 1 as your attack
if attack1 == ('1'):
    print('The enemy was intimidated and it got cancer and died.')
    time.sleep(2)

    print('You wander off and find yourself in a hole.')
    time.sleep(1)
    print("Good job.")
    print()

    # Input for stuck in hole
    whatdoyoudo = input('What do you do? (Hint: You should jump): ')


    # If you type 'jump'
    if whatdoyoudo == ('jump'):
        jumprandom = random.randint(1,10)


        # Get a random number from 1 to 10 for a 50/50 chance of getting out
        # 50% chance you dont get out
        if jumprandom >= 1 and jumprandom <= 5:
            print('You didnt jump high enough and you broke your legs')
            time.sleep(1)
            print('You lost 1 health point.')
            health = health - 1
            if health <= 0:
                print('You died.')
                dieimg()
                exit()
            else:
                print('I think you may be a little stuck...')
                time.sleep(2)
                print('Thats a good sign to restart and try again.')
                exit()

        # 50% chance you get out
        else:
            print('You jumped out!')
            time.sleep(2)
            print('And got eaten by a spider lol')
            print()
            exit()

    # If you type 'die'
    elif whatdoyoudo == ('die'):
        print('Well if you say so...')                              # Die response
        time.sleep(1)
        exit()

    # If you type anything else it prints this
    else:
        print('That probably would work i guess.')                  # Correct Response
        time.sleep(1)
        print()
        print('Woam gets out of the hole and is immediately eaten by a snake.')
        time.sleep(3)
        print('You are probably mad as to how the game never really lets you win...')
        time.sleep(2)
        print('But shut up, its my game so I dont care.')
        exit()




# If you choose 2 as your attack
elif attack1 == ('2'):
    print('The enemy grabbed your fist and broke your hand off.')
    time.sleep(2)
    print('You lost 1 health point.')
    health = health - 1
    if health <= 0:
        print()
        print('You died.')
        dieimg()
        exit()


    # Woam in forrest decicion
    else:
        time.sleep(1)
        print()
        print('For some reason it decided that was enough and let you go.')
        time.sleep(3)
        print('Anyway.')
        time.sleep(1)
        print()
        print('You walked into a random forest for some reason.')
        time.sleep(4)
        print('AND SOMEHOW... Managed to drown yourself.')
        time.sleep(3)
        print()
        print("Jesus Christ Woam... I dont even wanna know how you're gunna get out of this.")
        time.sleep(2)
        print('''
Here are your options: 

Keep drowning because you are bored (1)
Drown someone else (2)
Wake up because you were dreaming (3)''')

        # Input for drowning
        drownresp = input()

        # If you chose 1
        if drownresp == ('1'):
            print('Wow, big surprise... You drowned.')
            time.sleep(1)
            exit()

        # If you chose 2
        elif drownresp ==('2'):
            print('Wha-')
            time.sleep(1)
            print("WHY. LITERALLY WHY.")
            time.sleep(2)
            print('DID I MENTION ANY OTHER CHARACTERS?')
            time.sleep(2)
            print('sigh.')
            time.sleep(1)
            print('Im sick of your stupidity, you loose a health point.')
            time.sleep(2)
            print('If you complain ill break your nose.')
            health = health - 1
            if health <= 0:
                print('You died.')
                dieimg()
                exit()
            else:
                time.sleep(3)
                print()
                print('Woam is now feeling tired and starts walking home.')
                time.sleep(3)
                print('He is feeling dizzy and flies away into the abyss.')
                time.sleep(3)
                print('''
Shoot him (1)
Shout at him (2)
Ignore him (3)''')

                # Input for flying away
                woamflewaway = input()

                # If you type 1
                if woamflewaway == ('1'):
                    print('THIS ISNT DUCK HUNT')
                    time.sleep(2)
                    print('You shot him and Woam died.')
                    exit()


                # If you type 2
                elif woamflewaway == ('2'):
                    print('Woam turned around to see who called him.')
                    time.sleep(2)
                    print('He wasnt looking where he was going and hit a wall and got a concussion.')
                    time.sleep(3)
                    print('You lost 1 health point.')
                    health = health - 1
                    if health <= 0:
                        print()
                        print('You died.')
                        dieimg()
                        exit()
                    else:
                        pass


                # If you type 3
                elif woamflewaway == ('3'):
                    print('Woam continued to fly away.')
                    time.sleep(2)
                    print('You...')
                    time.sleep(1)
                    print('You lost the main character.')
                    time.sleep(2)
                    print('I dont know if this is a win or a loss but either way im taking a break.')
                    time.sleep(3)
                    print('Bye bye now... And bye bye Woam lol hes probably dead.')
                    exit()


                # If you type anything other than 1, 2 or 3
                else:
                    print('LEARN TO READ, HOLY-')
                    time.sleep(2)
                    print('Nope, done with you')
                    print()
                    print('You Died.')
                    dieimg()
                    exit()


        # If you chose 3
        elif drownresp == ('3'):
            print('I mean you werent dreaming because Woam genuinely managed to drown himself.')
            time.sleep(3)
            print('But...')
            time.sleep(1)
            print("While we were having this conversation he teleported back home. So you're off the hook.")
            time.sleep(3)
            print()
            print('Now that Woam is safely back home, what should he do?')
            print('''
Play some video games (1)
Have an unconventional seizure (2)
Sleep (3)''')

            # Input for home choice
            homequestion = input()

            # If you pick 1
            if homequestion == ('1'):
                print('You load up a game...')
                print()


                ######################### SNAKE GAME #########################


                # Imports
                import pygame
                import time
                import random
                import getpass
                import urllib.request

                # Var for username
                username = getpass.getuser()
                num = str(0)

                url = "https://i.imgur.com/IdbB5Gy.jpg"
                path = "C:\\Users\\" + username + "\\Desktop\\snek" + num + ".jpg"

                # Saves image of snake to desktop
                for x in range(1):
                    urllib.request.urlretrieve("https://i.imgur.com/IdbB5Gy.jpg",
                                               "C:\\Users\\" + username + "\\Desktop\\snek.jpg")
                    num = int(num)
                    num = num + 1
                    num = str(num)

                # Initialise all imported pygame modules
                pygame.init()

                # All colours
                white = (255, 255, 255)
                yellow = (255, 255, 102)
                black = (0, 0, 0)
                red = (213, 50, 80)
                green = (0, 255, 0)
                blue = (50, 153, 213)

                # Application window size
                dis_width = 600
                dis_height = 400

                # Used window sizes specified before
                dis = pygame.display.set_mode((dis_width, dis_height))
                pygame.display.set_caption('Snakes go brrr')

                # Used to help track time
                clock = pygame.time.Clock()

                # Vars for snake
                snake_block = 10
                snake_speed = 15

                # Fonts used for display text
                font_style = pygame.font.SysFont("bahnschrift", 25)
                score_font = pygame.font.SysFont("jokerman", 35)


                # Defines Your_score
                def Your_score(score):
                    value = score_font.render(" Score: " + str(score), True, yellow)
                    dis.blit(value, [0, 10])


                # Defines our_snake
                def our_snake(snake_block, snake_list):
                    for x in snake_list:
                        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


                # Defines message
                def message(msg, color):
                    mesg = font_style.render(msg, True, color)
                    dis.blit(mesg, [dis_width / 6, dis_height / 3])


                # Defines gameLoop
                def gameLoop():
                    game_over = False
                    game_close = False

                    x1 = dis_width / 2
                    y1 = dis_height / 2

                    x1_change = 0
                    y1_change = 0

                    snake_List = []
                    Length_of_snake = 1

                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

                    while not game_over:

                        while game_close == True:
                            # Game Over screen
                            dis.fill(black)
                            message('''                     You Died!''', red)
                            Your_score(Length_of_snake - 1)

                            test = pygame.font.SysFont("bahnschrift", 25)
                            test2 = test.render('Your score is: ' + str(Length_of_snake - 1), True, red)
                            dis.blit(test2, [220, 240])

                            test3 = pygame.font.SysFont("ESRIAMFMSewer", 50)
                            test4 = test3.render("lllllllll" + str(0), True, black)
                            dis.blit(test4, [0, 0])

                            test5 = pygame.font.SysFont("ESRIAMFMSewer", 50)
                            test6 = test5.render("lllllllll" + str(0), True, black)
                            dis.blit(test6, [0, 20])

                            # Updates application to load previous code
                            pygame.display.update()

                            time.sleep(3)
                            pygame.quit()
                            return


                        # For loop with keybinds for movement
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                game_over = True
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                    x1_change = -snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_RIGHT:
                                    x1_change = snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_UP:
                                    y1_change = -snake_block
                                    x1_change = 0
                                elif event.key == pygame.K_DOWN:
                                    y1_change = snake_block
                                    x1_change = 0

                        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                            game_close = True
                        x1 += x1_change
                        y1 += y1_change
                        dis.fill(black)
                        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
                        snake_Head = []
                        snake_Head.append(x1)
                        snake_Head.append(y1)
                        snake_List.append(snake_Head)
                        if len(snake_List) > Length_of_snake:
                            del snake_List[0]

                        for x in snake_List[:-1]:
                            if x == snake_Head:
                                game_close = True

                        our_snake(snake_block, snake_List)
                        Your_score(Length_of_snake - 1)

                        pygame.display.update()

                        if x1 == foodx and y1 == foody:
                            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                            Length_of_snake += 1

                        clock.tick(snake_speed)

                    pygame.quit()


                # Startup screen, fills screen black and adds text
                dis.fill(black)
                intro = pygame.font.SysFont("bahnschrift", 25)
                intro2 = intro.render('Hello, am snek', True, blue)
                dis.blit(intro2, [230, 20])

                # Loads the saved image from before
                snakeImg = pygame.image.load("C:\\Users\\" + username + "\\Desktop\\snek.jpg")


                # Defines snake
                def snake(x, y):
                    dis.blit(snakeImg, (x, y))


                # Vars for x and y
                x = 50
                y = 80

                # Places snake image on screen
                snake(x, y)

                # Updates application with previous code
                pygame.display.update()
                time.sleep(5)

                gameLoop()

                ######################### SNAKE GAME #########################



                time.sleep(3)
                print('')
                print('Woam lost and immidiatly rage quit.')
                time.sleep(2)
                print('He overreacted and broke his console')
                time.sleep(2)
                print('The thought of it now hurts his soul.')
                time.sleep(2)
                print('Nice job you made him sad, his heart exploded.')
                time.sleep(2)
                print()
                print('You Died.')
                time.sleep(1)
                print('I guess.')
                dieimg()
                exit()

            # If you pick 2
            elif homequestion == ('2'):
                print('Woam hit his head on a table while spazzing out.')
                time.sleep(2)
                print('You lost a health point.')
                health = health - 1
                if health <= 0:
                    print('You died.')
                    dieimg()
                    exit()
                else:
                    print('Luckily, that put Woam to sleep one way or another...')
                    time.sleep(3)
                    print('You know what.')
                    time.sleep(2)
                    print('You did good, you finally ended Woams stupidity for today.')
                    time.sleep(3)
                    print('AND FOR THAT-')
                    time.sleep(1)
                    print()
                    print('YOU WIN!')


            # If you pick 3
            elif homequestion == ('3'):
                print('Woam doesnt know how to sleep.')
                time.sleep(2)
                print('The realisation of this puts Woam into a shock that paralyses him.')
                time.sleep(3)
                print('GG NO RE')
                time.sleep(1)
                print('Seeing as Woam is now immovable, you loose.')
                exit()


            # If you pick anything other than 1, 2 or 3
            else:
                print('Leave.')
                time.sleep(2)
                print('I dont want you here anymore.')
                exit()


        # If you pick anything other than 1, 2 or 3
        else:
            print('Dunno how many times Ive had to type this.')
            time.sleep(2)
            print('BUT LEARN HOW TO READ AND TYPE ONE OF THE NUMBERS.')
            exit()



# If you choose 3 as your attack
elif attack1 == ('3'):
    print('You tried to run away but the enemy shot you in the face.')
    time.sleep(2)
    print('You died.')
    dieimg()
    exit()


# Message if user doesnt type 1, 2 or 3
else:
    print('Clearly you cant read, much like Woam...')
    time.sleep(2)
    print('So guess what?')
    time.sleep(2)
    print('You Died.')
    dieimg()
    exit()


# Day 2
time.sleep(4)
for x in range(9):
    print()
print('DAY 2.')
time.sleep(2)
print('Oh you thought it was over...?')
time.sleep(2)
print('It will never be over...')
time.sleep(2)
print('(until it does i guess)')
print()
time.sleep(1)
print('Anyway.')
print('Woam is now in a hospital because of his previous... uh... ' + '"' + 'experience' + '"')
time.sleep(4)

print()
print('Now to win this day, you are going to have to decode a puzzle.')
print('Throughout your day with Woam, you will find unusual characters such as, $ or % in amongst words.')
print('Find all of these characters and type them into the final box the exact order you found them in.')
print()
input('You got all that? ')
print('Good.')
print()
time.sleep(2)






# First task and options
print('Woam finally wakes up and falls out of bed.')
print('What do you do?')
print()
print('''Get up (1)
Dont get up (2)
Barrel roll (3)''')

# Your attack input
day2first = input()

if day2first == '1':
    print('You g3t up and walk out of the hospital bare naked.')

elif day2first == '2':
    print('Uh... Well... I didnt really think this part out...')
    time.sleep(2)
    print('I dont care, you g3t up anyway.')

elif day2first == '3':
    print('You g3t up with a barrel roll. Points for style.')

else:
    print('You just screwed yourself and you dont even know it...')






# Second task and options
print()
print('While you were in hospital, you got immediately evicted from your house.')
time.sleep(3)
print()
print('Where do you go?')
print()
print('''China (1)
The Streets (2)
The Narrators House(3)''')

# Your input
day2second = input()

if day2second == '1':
    print('HOW?')
    time.sleep(2)
    print('YOU CANT JUST-')
    time.sleep(2)
    print('Wh&tever.')
    time.sleep(2)
    print('You arent going to China, so you are going to live in the trash.')

elif day2second == '2':
    print('Only logical idea youve had so far...')
    time.sleep(2)
    print('You find a tr&sh can, this is your new home.')

elif day2second == '3':
    print('OI NAH-')
    time.sleep(2)
    print('I should shutdown your laptop just for thinking about doing that.')
    time.sleep(3)
    print('Whatever, im sending you to sleep in the tr&sh now tho.')

else:
    print('You just screwed yourself and you dont even know it...')




# Third task and options
print()
print('Because the trash is not sanitary to say the least. You find a raccoon.')
time.sleep(3)
print()
print('What do you do with it?')
print()
print('''Burn it (1)
Eat it (2)
Raise it as your own (3)''')

# Your input
day2third = input()

if day2third == '1':
    print('You m@gically find a match and set him on fire.')
    time.sleep(2)
    print('Cold blooded.')

elif day2third == '2':
    print('I mean hey, I aint judging you.')
    time.sleep(1)
    print('But its a little weird choice of food if i s@y so myself.')

elif day2third == '3':
    print('Pfffft. Boring.')
    time.sleep(1)
    print('Better th@n burning it tho i guess.')

else:
    print('You just screwed yourself and you dont even know it...')




# Fourth task and options
print()
print('So it turns out that Woam got stuck in a cave after protesting about chickens.')
print('Dont ask questions. Just accept it.')
time.sleep(3)
print()
print('What does he do?')
print()
print('''Become a creeper (1)
Break his nose (2)
Start mining down (3)''')

# Your input
day2fourth = input()

if day2fourth == '1':
    print('Sssssss...')
    time.sleep(2)
    print('WAIT NO-')
    time.sleep(1)
    print('BANG.')
    time.sleep(1)
    print()
    print('GamerWoam42 died from an explosion')
    time.sleep(2)
    print('Luckily he re5pawned into an ancient trial.')

elif day2fourth == '2':
    print('He breaks his no5e (again) and blacks out.')
    time.sleep(2)
    print('Amazingly he wakes up in an ancient trial.')

elif day2fourth == '3':
    print('Woam starts mining down with only his bare hands.')
    time.sleep(2)
    print('And mines 5traight into an ancient trial.')

else:
    print('You just screwed yourself and you dont even know it...')





# Fifth task and options
print()
print('Woah...')
time.sleep(2)
print('This is amazing.')
time.sleep(2)
print('There is a giant vault door-')
time.sleep(2)
print('But... But its password protected.')
time.sleep(3)
print()
print('WAIT! There is a note, heres what it says:')
print()
print('"' + 'I have hidden secret characters through out your journey')
print('if im not mistaken, you should have 4 of them.')
print('the last symbol is %. Good luck.' + '"')
time.sleep(3)
input('You got all that? ')
print()
print('SYSTEM MESSAGE: YOU HAVE 3 ATTEMPTS')
password = input('Please input the code: ')
lockdown = 3

while password != ('3&@5%'):
    lockdown = lockdown - 1
    if lockdown <= 0:
        print('YOU HAVE FAILED.')
        time.sleep(2)
        print('OH NO- YOU MESSED UP BAD.')
        time.sleep(2)
        print('THE VAULT IS BREAKING APART-')
        time.sleep(2)
        print('I think...')
        time.sleep(1)
        print('I think you died...')
        time.sleep(2)
        print('WAIT WHATS THIS???')
        time.sleep(2)
        print('A message? From Woam?')
        time.sleep(2)
        print('Dunno how it got here but it reads...')
        time.sleep(2)

        import webbrowser
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1)
        time.sleep(2)
        print('Thank you for playing :D')
        exit()

    else:
        print('INCORRECT!')
        password = input('Please input the code: ')

time.sleep(1)
print('...')
time.sleep(1)
print('ACCESS CODE GRANTED.')
print()
time.sleep(1)
print('OH THANK GOD YOU DIDNT DIE. Wait is that a good or a bad-')
time.sleep(2)
print('Doesnt matter.')
time.sleep(1)
print('What matters is whats inside this vault!')
time.sleep(2)
print('N- Nothing...?')
time.sleep(2)
print('Wait i see something...')
time.sleep(1)
print('Its ANOTHER NOTE.')
time.sleep(2)
print('You arent gunna like what this says....')
bees = input('You wanna take a look? ')

if bees == 'i like bees':
    print("Well you're in luck!")
    time.sleep(2)
    print('''
According to all known laws
of aviation,''')

    time.sleep(2)
    print('''
there is no way a bee
should be able to fly.''')

    time.sleep(2)
    print('''
Its wings are too small to get
its fat little body off the ground.''')

    time.sleep(2)
    print('''
The bee, of course, flies anyway''')

    time.sleep(2)
    print('''
because bees don't care
what humans think is impossible.''')
    time.sleep(2)

    print()
    print('Thank you for playing :D')
    winimg()

else:
    import webbrowser
    print('It reads-')
    time.sleep(1)
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1)
    time.sleep(2)
    print('Thank you for playing :D')
    winimg()


