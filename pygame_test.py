# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 06:14:16 2017

@author: midas
"""

import pygame as pg
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def scale_icon(image_name):
    im_dir = "Icons/"
    return pg.transform.smoothscale(pg.image.load(im_dir + image_name), (20,20))
    
pg.init()
pg.display.set_caption("Door Camera")


# ---Include images ---
power_button = scale_icon('Power_off.png')
lock_button = scale_icon('Lock.png')
unlock_button = scale_icon('Unlock.png')
arrow_button = scale_icon('Arrow.png')

reso = (320,240)
screen = pg.display.set_mode(reso)

running = True

while running:
    for event in pg.event.get():
                if (event.type == pg.QUIT) or (not GPIO.input(27)):
                    running = False
    
    screen.fill((255, 255, 255))
    
    screen.blit(power_button, (5,0))
    screen.blit(lock_button, (5,60))
    screen.blit(unlock_button, (5,120))
    screen.blit(arrow_button, (5, 180))
    
    pg.display.flip()
    