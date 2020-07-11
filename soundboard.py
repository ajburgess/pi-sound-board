import pygame
import time
import glob
import os

def play_sound_for_button(button_name):
    if button_name in sounds:
        sound = sounds[button_name]
        pygame.mixer.Sound.play(sound)

pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# TODO: Scan for MP3 files and convert to WAV
# using "mpg123 -w dest.wav src.mp3"

sounds = { }
paths = glob.glob("/media/pi/*/*.wav")
for path in paths:
    button_name = os.path.splitext(os.path.basename(path))[0]
    sound = pygame.mixer.Sound(path)
    sounds[button_name] = sound

buttons = { 0: 'x', 1: 'a', 2: 'b', 3: 'y' }

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            button = buttons[event.button]
            if button:
                play_sound_for_button(button)