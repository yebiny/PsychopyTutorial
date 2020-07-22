#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
# Setup the Window and Keyboard
def set_window():
    window = visual.Window(
        size=(1024, 768), fullscr=True, screen=0, 
        winType='pyglet', allowGUI=False, allowStencil=False,
        monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
        blendMode='avg', useFBO=True, 
        units='height')
    return window

def set_text(win, name):
    text = visual.TextStim(win=win, name=name,
        text='You can change this sentence with Component.text',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    return text

def set_circle(win, name):
    circle = visual.Circle(
        win=win, name=name,
        radius=0.008,
        ori=0, pos=(0, 0),
        lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
        fillColor=[-1,-1,-1], fillColorSpace='rgb',
        opacity=1, depth=-1.0, interpolate=True)
    return circle

def set_image(win, name):

    image = visual.ImageStim(
        win=win,
        name=name, 
        image=None, mask=None,
        ori=0, pos=(0, 0), size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)

    return image


def getCurrentTime(RoutineClock, win, frameN):
    timer = RoutineClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=RoutineClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  
    return timer, tThisFlip, tThisFlipGlobal, frameN

def initComponents(RoutineComponents):
    for Compo in RoutineComponents:
        Compo.keys, Compo.rt = [], []
        Compo.tStart, Compo.tStop = None, None
        Compo.tStartRefresh, Compo.tStopRefresh = None, None
        if hasattr(Compo, 'status'):
            Compo.status = NOT_STARTED

