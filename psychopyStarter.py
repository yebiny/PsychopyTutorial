#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os, sys
from psychopy.hardware import keyboard
import csv
import random

# Set Variables 
nTrial=16
nTrialInaBlock=8

TrialTime=2
WaitTime=10000
RestTime=2
StimTime=1
RespTime=1.5
SigKey=['s']
RespKey=['c', 'd']

SigWindow=0.1

# Store info about the experiment session
Date=data.getDateStr().split('_')
expDate=Date[0]+Date[1]+Date[2]

expName = 'FaceRec'
expInfo = {
           'Title': expName, 
           'Date' : expDate, 
           'SubId': '00',
           'Session': '00'
           }
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  
_thisDir = os.path.dirname(os.path.abspath(__file__))

# Save Outputs in this Session
fname = 'output/sub%s_%s_output.csv'%(expInfo['SubId'], expInfo['Session'])
if os.path.isfile(fname):
    print(fname, ' is Already Exist.')
    core.quit()
fout = open(fname, 'w', newline='')
wout=csv.writer(fout)
wout.writerow(info for info in expInfo)
wout.writerow(expInfo[info] for info in expInfo)
wout.writerow(['nTrial', 'SetTime', 'TrialStart', 'StimEnd', 'SignalTime', 'SignalTimeLocal', 'ResponseTimeLocal', 'ResponseKey'])

# Save Random Matrix
nRandom = random.sample([i+1 for i in range(nTrial)], nTrial)
print(nRandom)
fname = 'output/sub%s_%s_matrix.csv'%(expInfo['SubId'], expInfo['Session'])
fmatrix = open(fname, 'w', newline='')
wmatrix = csv.writer(fmatrix)
wmatrix.writerow(nRandom)

# Setup the Window and Keyboard
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
defaultKeyboard = keyboard.Keyboard()

# Initialize "Wait" Components
WaitClock = core.Clock()
WaitText = visual.TextStim(win=win, name='WaitText',
    text='WAIT INSTURCTION',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
WaitSignal = keyboard.Keyboard()

# Initialize "Trial" Components
TrialClock = core.Clock()
Dot = visual.Circle(
    win=win, name='Dot',
    radius=0.008,
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Signal = keyboard.Keyboard()
Response = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  
routineTimer = core.CountdownTimer() 
frameTolerance = 0.001  

# Update Definition
def param_updates(Param, ParamDur, keyList=None):
    if keyList != None: 
        waitOnFlip=False
    if Param.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        Param.frameNStart = frameN  # exact frame index
        Param.tStart = timer  # local t and not account for scr refresh
        Param.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Param, 'tStartRefresh')  # time at next scr refresh
        if keyList!=None:
            Param.status=STARTED
            waitOnFlip = True
            win.callOnFlip(Param.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Param.clearEvents, eventType='keyboard')  
        else:
            Param.setAutoDraw(True)
    if Param.status == STARTED:
        if tThisFlipGlobal > Param.tStartRefresh + ParamDur-frameTolerance:
            Param.tStop = timer  # not accounting for scr refresh
            Param.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Param, 'tStopRefresh')  # time at next scr refresh
            if keyList!=None:
                Param.status=FINISHED
            else:
                Param.setAutoDraw(False)
    theseKeys=[]
    if keyList!=None and Param.status == STARTED and not waitOnFlip:
        theseKeys = Param.getKeys(keyList=keyList, waitRelease=False)
        
    return theseKeys

def getCurrentTime(RoutineClock, frameN):
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


#-------Set Timer "Wait"-------
frameN = 0
WaitClock.reset(-win.getFutureFlipTime(clock="now"))

#------Prepare to start Routine "Wait"-------
continueRoutine = True
WaitComponents = [WaitText, WaitSignal]
initComponents(WaitComponents)

#-------Run Routine "Wait"-------
while continueRoutine:
    # get current time
    timer, tThisFlip, tThisFlipGlobal, frameN = getCurrentTime(WaitClock, frameN)

    # update parameters
    param_updates(WaitText, WaitTime) 
    WaitSigList=param_updates(WaitSignal, WaitTime, SigKey)
    if len(WaitSigList):
        continueRoutine = False
    
    # check continue or not 
    if defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    if not continueRoutine: 
        break
    continueRoutine = False  
    for Compo in WaitComponents:
        if hasattr(Compo, "status") and Compo.status != FINISHED:
            continueRoutine = True
            break  
    if continueRoutine:  
        win.flip()

# -------Ending Routine "Wait"-------
for Compo in WaitComponents:
    if hasattr(Compo, "setAutoDraw"):
        Compo.setAutoDraw(False)
routineTimer.reset()


#-------Save Log File -------
expTime=data.getDateStr().split('_')[-1]
fLog = open('output/sub%s_log.csv'%(expInfo['SubId']), 'a', newline='')
rLog = open('output/sub%s_log.csv'%(expInfo['SubId']), 'r', newline='')
wLog=csv.writer(fLog)
if not  rLog.readline():
    wLog.writerow(['Title', 'Date', 'ID'])
    wLog.writerow([expInfo['Title'], expInfo['Date'], expInfo['SubId']])
    wLog.writerow(['Session', 'StartTime', 'Remarks'])
wLog.writerow([expInfo['Session'], expTime])
fLog.close()

#-------Set Timer "Trial"-------
frameN = 0
TrialClock.reset(-win.getFutureFlipTime(clock="now"))
TrialSetTime=TrialTime+SigWindow

# ------Start Loop "Trial"-------------
for thisTrial in range(1, nTrial):
    
    # ------Set "Stim" Here--------
    thisStim='./stim/%i.jpg'%(nRandom[thisTrial])
    Stim.setImage(thisStim)
    
    #-------Set Each "Trial" Time-------
    routineTimer.add(TrialSetTime)
    TrialStartTime = TrialClock.getTime()
    
    # ------Prepare to start Routine "Trial"-------
    TrialComponents = [Dot, Stim, Signal, Response]
    initComponents(TrialComponents)
    continueRoutine = True
    
    # -------Run Routine "Trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        timer, tThisFlip, tThisFlipGlobal, frameN = getCurrentTime(TrialClock,frameN)
        
        # update parameters
        param_updates(Stim, StimTime) 
        param_updates(Dot, TrialSetTime)     
       
        RespList=param_updates(Response, RespTime, RespKey)     
        if len(RespList):
            Response.keys=RespList[-1].name
            Response.rt=RespList[-1].rt

        SigList=param_updates(Signal, TrialSetTime, SigKey)     
        if len(SigList) and ((timer-TrialStartTime) > (TrialSetTime-(2*SigWindow))):
            Signal.keys=SigList[-1].name
            Signal.rt=SigList[-1].rt
            continueRoutine=False
        
        # check continue or not 
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        if not continueRoutine:  
            break
        continueRoutine = False  
        for Compo in TrialComponents:
            if hasattr(Compo, "status") and Compo.status != FINISHED:
                continueRoutine = True
                break  
        if continueRoutine:  
            win.flip()
    
    # -------Ending Routine "Trial"-------
    for Compo in TrialComponents:
        if hasattr(Compo, "setAutoDraw"):
            Compo.setAutoDraw(False)
    
    # -------Save Data
    dataInfo = [ thisTrial, TrialSetTime, Stim.tStart, Stim.tStop, Stim.tStart+Signal.rt, Signal.rt, Response.rt, Response.keys] 
    wout.writerow(dataInfo)
    print(dataInfo)
    
    # -------Reset Timer For Next Trial-------
    if (thisTrial+1) % nTrialInaBlock == 0:
        if Signal.rt != []:
            TrialSetTime=TrialTime+RestTime+SigWindow
        else:
            TrialSetTime=TrialTime+RestTime
    else:
        if Signal.rt != []:
            TrialSetTime=TrialTime+SigWindow
        else:
            TrialSetTime=TrialTime

fout.close()
fmatrix.close()
flog.close()

win.flip()
logging.flush()
win.close()
core.quit()
