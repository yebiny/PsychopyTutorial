#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy.hardware import keyboard


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



def initComponents(Components):
    for Compo in Components:
        Compo.tStart, Compo.tStop = None, None
        Compo.tStartRefresh, Compo.tStopRefresh = None, None
        if hasattr(Compo, 'status'):
            Compo.status = NOT_STARTED

def endRoutine(Components):
    for Compo in Components:
        if hasattr(Compo, "setAutoDraw"):
            Compo.setAutoDraw(False)


class Routine():
    def __init__(self, window, RoutineClock):
       
        self.win = window
        self.frameTl = 0.0001
        self.time = RoutineClock.getTime()
        self.tFlip = window.getFutureFlipTime(clock=RoutineClock)
        self.tGlobal = window.getFutureFlipTime(clock=None)
        #self.frame = RoutineFrame + 1  
    
    def visual(self, Compo, Dur):
        # *Compo* updates
        if Compo.status == NOT_STARTED and self.tFlip >= 0.0-self.frameTl:
            # keep track of start time/frame for later
            Compo.tStart = self.time  # local t and not account for scr refresh
            Compo.tStartRefresh = self.tGlobal
            self.win.timeOnFlip(Compo, 'tStartRefresh')  # time at next scr refresh
            Compo.setAutoDraw(True)
        if Compo.status == STARTED:
            if self.tGlobal > Compo.tStartRefresh + (Dur)-self.frameTl:
                Compo.tStop = self.time  # not accounting for scr refresh
                self.win.timeOnFlip(Compo, 'tStopRefresh')  # time at next scr refresh
                Compo.setAutoDraw(False)
    
    def response(self, Compo, Dur, keyList):

        waitOnFlip=False
        if Compo.status == NOT_STARTED and self.tFlip >= 0-self.frameTl:
            Compo.tStart = self.time  # local t and not account for scr refresh
            Compo.tStartRefresh = self.tGlobal  # on global time
            Compo.status=STARTED
            
            self.win.timeOnFlip(Compo, 'tStartRefresh')  # time at next scr refresh
            self.win.OnFlip = True
            self.win.callOnFlip(Compo.clock.reset)  
            self.win.callOnFlip(Compo.clearEvents, eventType='keyboard')  
        
        if Compo.status == STARTED:
            if self.tGlobal > Compo.tStartRefresh + (Dur)-self.frameTl:
                Compo.tStop = self.time  # not accounting for scr refresh
                Compo.status=FINISHED
                self.win.timeOnFlip(Compo, 'tStopRefresh')  # time at next scr refresh
        theseKeys=[]
        if Compo.status == STARTED and not waitOnFlip:
            theseKeys = Compo.getKeys(keyList=keyList, waitRelease=False)
            
        return theseKeys
