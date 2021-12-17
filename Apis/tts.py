import os
import pygame.mixer as mx
from gtts import gTTS
import uuid

code = uuid.uuid4()
file = f'D:\{code}.mp3'
mx.init()


def say(text):
    engine = gTTS(text=text)
    engine.save(file)
    mx.music.load(file)


def play():
    mx.music.play(loops=0)


def stop():
    mx.music.stop()
    mx.quit()


def pause():
    mx.music.pause()


def delete():
    mx.init()
    mx.stop()
    mx.quit()
    os.remove(file)