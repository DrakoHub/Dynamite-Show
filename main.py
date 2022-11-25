from pickle import FALSE
from turtle import delay, width
import pygame, sys, math, time, random, json, gameassets as gmsts
from pygame.locals import QUIT

pygame.init()
pygame.mixer.init()
pygame.font.init()

#video graphics AAAAAAAAAAAAAAA

clock = pygame.time.Clock()
FPS = 60

#window
resolution = (800, 600)
screen = pygame.display.set_mode((resolution))
width = screen.get_width()
height = screen.get_height()
pygame.display.set_caption("The Rock, Scisor and Papers: Dynamite Show ")

#game variables
keys = pygame.key.get_pressed()
game_initialize = True
Game_dev_groug_logo = False
mainMenuDrawer = True
shop = False
# chamar
cutscene_ary = [False, False, False, False, False]
cutscene_pressing = 0
fight_ary = [False, False, False, False]
space_press = False
Iventory_call = False
attack_throws = ""; player_action = ""
alerting = True
#font
font1 = pygame.font.SysFont('freesanbold.ttf', 25)

#images
#corps
TITLE = pygame.image.load("assets/sprites/title.png")
DinoCanibal  = pygame.image.load("Dino canibal.png").convert()

#button
non_play_button_image = pygame.image.load("assets/sprites/menu/buttons/play.png")
non_quit_button_image = pygame.image.load("assets/sprites/menu/buttons/quit.png")
active_play_button_image = pygame.image.load("assets/sprites/menu/buttons/play_active.png")
active_quit_button_image = pygame.image.load("assets/sprites/menu/buttons/quit_active.png")
inactive_fight_buttom = pygame.image.load("assets/sprites/menu/buttons/fight.png")
active_fight_buttom = pygame.image.load( "assets/sprites/menu/buttons/fight_active.png")
inactive_back_buttom = pygame.image.load( "assets/sprites/menu/buttons/back.png")
active_back_buttom = pygame.image.load( "assets/sprites/menu/buttons/back_active.png")
paper_attack_button = pygame.image.load("assets/sprites/menu/attacks/paper.png")
rock_attack_button = pygame.image.load("assets/sprites/menu/attacks/rock.png")
scissor_attack_button = pygame.image.load("assets/sprites/menu/attacks/scissor.png")

#cutscene things
cutscene_1_hawaii = pygame.image.load("assets/sprites/cutscene/hawaii.png")
cutscene_frame = pygame.image.load("assets/sprites/cutscene/cutscene_frame.png")
text_box = pygame.image.load("assets/sprites/menu/hud/text_box.png")
alert_frame = pygame.image.load("assets/sprites/cutscene/alert.png")


#backgrounds
main_menu_sky_paralax = pygame.image.load("assets/sprites/background/main_menu/sky_paralax.png").convert()
main_menu_clouds_paralax = pygame.image.load("assets/sprites/background/main_menu/sky_clouds.png").convert()
main_menu_mountains_paralax = pygame.image.load("assets/sprites/background/main_menu/mountains_paralax.png")
stage_1 = pygame.image.load("assets/sprites/background/stage_1.png").convert()

#fighter
the_rock = pygame.image.load("assets/sprites/entity/fighters/rock.png")
#hands
hand_rock = pygame.image.load("assets/sprites/entity/hands/rock.png")
hand_paper = pygame.image.load("assets/sprites/entity/hands/paper.png")
hand_scissor = pygame.image.load("assets/sprites/entity/hands/scissor.png")

#convert foda
DinoCanibal = pygame.transform.scale(DinoCanibal, resolution)

#convert background
main_menu_sky_paralax = pygame.transform.scale(main_menu_sky_paralax, resolution)
main_menu_clouds_paralax = pygame.transform.scale(main_menu_clouds_paralax, resolution)
main_menu_mountains_paralax = pygame.transform.scale(main_menu_mountains_paralax, resolution)
stage_1 = pygame.transform.scale(stage_1, resolution)
alert_frame = pygame.transform.scale(alert_frame, resolution)
#transform images
cutscene_frame = pygame.transform.scale(cutscene_frame, resolution)
cutscene_1_hawaii = pygame.transform.scale(cutscene_1_hawaii, (256, 192))
the_rock = pygame.transform.scale(the_rock, (256, 192))
hand_rock = pygame.transform.scale(hand_rock, (420, 204))
hand_paper = pygame.transform.scale(hand_paper, (420, 204))
hand_scissor = pygame.transform.scale(hand_scissor, (420, 204))
#main menu
RSPDYSH = pygame.mixer.Sound('assets/audio/intro.mp3')

#Def Functions
class Hud():

    def __init__(self):
        self.image = pygame.image.load("assets/sprites/menu/hud/text_box.png")
        self.rect = self.image.get_rect()

    def DrawAny(self, size, x, y):
        hud = pygame.transform.scale(self.image, size)
        screen.blit(hud, (x, y))

def _paralax(img, vel):
    global width
    rel_width = width % img.get_rect().width
    screen.blit(img, (rel_width - img.get_rect().width, 0))
    if rel_width < 800:
        screen.blit(img, (rel_width, 0))
    width -= vel

def _entering(img, vel, x, y):
    action = False
    if action == False:
      for i in range(0, x):
        screen.blit(img, (i, y)); pygame.time.delay(vel); pygame.display.update()
        if i == x: action = True 
def TextBox(text):
  Texting = text
  Counting = len(text)
  TextBlock = Hud()
  TextBlock.DrawAny((500,100), 150, 500)
  j = 0
  for i in range(0, Counting, 37):
    screen.blit(font1.render(Texting[i:37+i], True, (255,255,255)), (180, 515+j))
    j =+ 18
  pygame.key.stop_text_input()
  
class Fighter():
  def __init__(self,img, enemy_or_player, hp, max_hp, attk, deff):
      self.img = img; self.enemy_or_player = enemy_or_player
      self.hp = hp; self.max_hp = max_hp; self.attk = attk; self.deff = deff
  def BattleAnimation (self):
    if self.enemy_or_player == "player":
      screen.blit(self.img, (50, 320))
    if self.enemy_or_player == "enemy":
      screen.blit(self.img, (450, 160))
 
enemy_attack = ["Rock","Paper","Scissor"]

def Hudding():
  global Iventory_call, alerting, attack_throws, player_action, enemy_attack, action_fighter
  if fight_ary[0] : _paralax(stage_1, 1)
  Enemy_Fighter.BattleAnimation()
  Player_Figther.BattleAnimation()
  Dogman = Hud(); #Fight_button = gmsts.Button
  Dogman.DrawAny((800, 100), 0, 500)
  Dogman.DrawAny((400, 100), 400, 500)
  screen.blit(font1.render("Life", True, (255,255,255)), (50, 510))
  screen.blit(font1.render("Enemy", True, (255,255,255)), (50, 545))
  Player_Health.Draw(100)
  Enemy_Health.Draw(100)
  fight_button = gmsts.Button(screen, 425, 508,inactive_fight_buttom, active_fight_buttom, 170, 85)
  if Iventory_call == False:  
    if fight_button.draw():
      Iventory_call = True
  if Iventory_call == True:
    rock_button = gmsts.Button(screen, 200, 200,rock_attack_button, rock_attack_button, 133, 133)
    scisor_button = gmsts.Button(screen, 333, 200,scissor_attack_button, scissor_attack_button, 133, 133)
    paper_button = gmsts.Button(screen, 466, 200,paper_attack_button, paper_attack_button, 133, 133)
    back_button = gmsts.Button(screen, 200, 150, inactive_back_buttom, active_back_buttom, 64, 32)
    ATTCKS = Hud()
    ATTCKS.DrawAny((438, 200), 180, 180)
    if rock_button.draw(): player_action = "Rock"; attack_throws = enemy_attack[random.randint(0, 2)]; print(attack_throws); Iventory_call = False
    if scisor_button.draw(): player_action = "Scisor"; attack_throws = enemy_attack[random.randint(0, 2)]; print(attack_throws); Iventory_call = False
    if paper_button.draw(): player_action = "Paper"; attack_throws = enemy_attack[random.randint(0, 2)]; print(attack_throws); Iventory_call = False
    if back_button.draw():Iventory_call = False;action_fighter = False
  if player_action == "Rock" or player_action == "Scisor" or player_action == "Paper" and enemy_attack == "Rock" or enemy_attack == "Scisor" or enemy_attack == "Paper":
    if player_action == "Rock" and enemy_attack == "Rock": print("Break"); player_action = ""; enemy_attack = ""
    if player_action == "Scisor" and enemy_attack == "Scisor": print("Break"); player_action = ""; enemy_attack = ""
    if player_action == "Paper" and enemy_attack == "Paper": print("Break"); player_action = ""; enemy_attack = ""

    if enemy_attack == "Rock" and player_action == "Scisor": print("You Lose, Rock break Scissor"); player_action = ""; enemy_attack = ""
    if enemy_attack == "Scisor" and player_action == "Rock": print("You Win, Rock break Scissor"); player_action = ""; enemy_attack = ""
    if enemy_attack == "Paper" and player_action == "Scisor": print("You Win, Scissor cut Paper"); player_action = ""; enemy_attack = ""
    if enemy_attack == "Scisor" and player_action == "Paper": print("You Lose, Scissor cut Paper"); player_action = ""; enemy_attack = ""
    if enemy_attack == "Rock" and player_action == "Paper": print("You Win, Paper wraps Rock"); player_action = ""; enemy_attack = ""
    if enemy_attack == "Paper" and player_action == "Rock": print("You Lose, Paper wraps Rock"); player_action = ""; enemy_attack = ""


  


#animation Functions

def fade(type, delay):
  fade = pygame.Surface(resolution)
  fade.fill((0,0,0))
  def FadeOut():
    for alpha in range(255):
      fade.set_alpha(alpha)
      screen.blit(fade,(0,0))
      pygame.display.update()
      pygame.time.delay(delay)
  def FadeIn():
    for alpha in range(255):
      fade.set_alpha(255 - alpha)
      screen.blit(fade,(0,0))
      pygame.display.update()
      pygame.time.delay(delay)
  if type == "out":
    return FadeOut()
  if type == "in":
    return FadeIn()

def floating(image, x, y, elv, velocity):
  rel_y = y
  CallMan = False
  if True or CallMan:
    for elevation in range(elv):
      rel_y = rel_y + elevation
      screen.blit(image,(x, rel_y))
      pygame.display.update()
      pygame.time.delay(velocity)
      if elevation == elv:
        CallMan = False
        break
  for descent in range(elv):
    rel_y = rel_y - descent
    screen.blit(image,(x, rel_y))
    pygame.time.delay(velocity)
    pygame.display.update()
    CallMan = True



# Fighter
Player_hp = 100;Player_hp_max = 100;Player_attk = 10; Player_deff = 50
Enemy_hp = 100;Enemy_hp_max = 100;Enemy_attk = 10; Enemy_deff = 50
Player_Figther = Fighter(the_rock, "player" ,Player_hp, Player_hp_max, Player_attk, Player_deff)
Enemy_Fighter = Fighter(cutscene_1_hawaii, "enemy" ,Enemy_hp, Enemy_hp_max, Enemy_attk, Enemy_deff)


Player_Health = gmsts.Bar(screen, 50, 525, Player_hp, Player_hp_max, (255, 0,0))
Enemy_Health = gmsts.Bar(screen, 50, 560, Enemy_hp, Enemy_hp_max, (0, 0, 255))

pygame.mixer.music.load("assets/audio/Musica_tema.mp3")

pygame.mixer.music.play()
while game_initialize:
  
  if mainMenuDrawer == True:
      pygame.mixer.music.set_volume(0.6)
      _paralax(main_menu_sky_paralax, 0.5)
      _paralax(main_menu_mountains_paralax, 2)
      _paralax(main_menu_clouds_paralax, 0.5)
      screen.blit(TITLE, (175, 30))
      play_buttom = gmsts.Button(screen, 346, 400, non_play_button_image, active_play_button_image, 128, 64)
      quit_buttom = gmsts.Button(screen, 346, 470, non_quit_button_image, active_quit_button_image, 128, 64)
      if play_buttom.draw():
        fade("out", 5)
        mainMenuDrawer = False
        cutscene_ary[0] = True
        pygame.mixer.music.fadeout(5)
      if quit_buttom.draw():
        game_initialize = False
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        
    # Cutscene 1
  if cutscene_ary[0] == True:
    _paralax(main_menu_sky_paralax, 1)
    screen.blit(cutscene_frame,(0, 0))
    #floating(cutscene_1_hawaii, 272, 204, 5, 50)
    screen.blit(cutscene_1_hawaii, (272, 204))
    TextBox("AAHHAHAH")
    if space_press:
      TextBox("BBBBBBB")
      cutscene_pressing +=1
    if space_press == True and cutscene_pressing == 1:
      TextBox("AFADDVA")
      cutscene_pressing +=1
    if space_press == True and cutscene_pressing == 2:
      TextBox("GFFFADFD")
      cutscene_pressing +=1
    if space_press and cutscene_pressing == 3:
      fade("out", 5)
      cutscene_ary[0] = False
      fight_ary[0] = True
      
  if fight_ary[0] == True:
    Hudding()
    pygame.mixer.music.load("assets/audio/Battle_game.mp3");pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.play()

  clock.tick(FPS)
  for event in pygame.event.get():
    if event.type == QUIT:
      game_initialize = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
          print("Hello, i am your HackPrompt")
        if cutscene_ary[0] and event.key == pygame.K_SPACE:
            space_press = True
        elif space_press == True and event.type == pygame.KEYUP: space_press = False
          
    #screen.fill((255,255,255))
    #Hud_1 = MakeHud(width, 100, 0, height-100, (0,0,0), False)
    #Hud_1.Draw()     
  pygame.display.update()
pygame.quit()


