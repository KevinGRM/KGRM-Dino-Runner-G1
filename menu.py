import pygame

from dino_runner.components import button
from dino_runner.utils.constants import TITLE, ICON

from dino_runner.components.game import Game

pygame.init()

#create game window
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

half_screen_width = SCREEN_WIDTH // 2
half_screen_height = SCREEN_HEIGHT // 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
pygame.display.set_icon(ICON)

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)
Sound_Start = pygame.mixer.music.load("dino_runner/assets/Themes/INICIO.mp3")
Sound_Start = pygame.mixer.music.play()
#load button images
resume_img = pygame.image.load("dino_runner/assets/images/button_resume.png").convert_alpha()
options_img = pygame.image.load("dino_runner/assets/images/button_options.png").convert_alpha()
quit_img = pygame.image.load("dino_runner/assets/images/button_quit.png").convert_alpha()
video_img = pygame.image.load('dino_runner/assets/images/button_video.png').convert_alpha()
audio_img = pygame.image.load('dino_runner/assets/images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('dino_runner/assets/images/button_keys.png').convert_alpha()
back_img = pygame.image.load('dino_runner/assets/images/button_back.png').convert_alpha()

#create button instances weigth and heigth
resume_button = button.Button(half_screen_width - 100, 125, resume_img, 1)##304, 125
options_button = button.Button(half_screen_width- 105, 250, options_img, 1)##297 250
quit_button = button.Button(half_screen_width- 64, 375, quit_img, 1)##336 375
video_button = button.Button(half_screen_width- 175, 75, video_img, 1)##226 75
audio_button = button.Button(half_screen_width- 175, 200, audio_img, 1)##225 200
keys_button = button.Button(half_screen_width- 150, 325, keys_img, 1)##246 325
back_button = button.Button(half_screen_width- 65, 450, back_img, 1)##332 450

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((52, 78, 91))

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        Sound_Start = pygame.mixer.pause()       
        game = Game()
        game.run()
        ##game_paused = False
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      if video_button.draw(screen):
        print("Video Settings")
      if audio_button.draw(screen):
        print("Audio Settings")
      if keys_button.draw(screen):
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "main"
  else:
    draw_text("PYGAME & PYTHON", font, TEXT_COL, half_screen_width- 230, 200)
    draw_text("Press SPACE to pause", font, TEXT_COL, half_screen_width- 240, 390)
    draw_text("By Kevin_GRM", font, TEXT_COL, half_screen_width- 150, 250)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()