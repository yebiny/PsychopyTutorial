from __future__ import absolute_import, division
import numpy as np
import os, sys
from definition import *


# Store info about the experiment session
Date=data.getDateStr()

expName = 'PsychopyTutorial_1st'
expInfo = {
           'Title': expName, 
           'Date' : Date,
           'SubId': '00',
           'Session': '00'
           }
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  

# Setup the Window and Keyboard
win = set_window()
defaultKeyboard = keyboard.Keyboard()

# Initialize "Wait" Components
WaitText = set_text(win, 'WaitText')
WaitSignal = keyboard.Keyboard()
WaitComponents=[WaitText, WaitSignal]

# Initialize "Trial" Components
Dot = set_circle(win, 'Dot')
Stim = set_image(win, 'Stim')
Signal = keyboard.Keyboard()
Response = keyboard.Keyboard()
TrialComponents=[Dot, Stim, Signal, Response]

# Create some handy timers
WaitClock = core.Clock()
TrialClock = core.Clock()
routineTimer = core.CountdownTimer() 
frameTolerance = 0.001  


##############################################
#------------------- WAIT -------------------#
##############################################
# 1. Set "Wait" Timer
WaitClock.reset(-win.getFutureFlipTime(clock="now"))

# 2. Initialize "Wait" Components
initComponents(WaitComponents)

# 3. Start "Wait" Routine
while True:
    # set this routine 
    WaitRoutine = Routine(win, WaitClock)
    
    # components update
    WaitRoutine.visual(WaitText, 1000)    
    signal = WaitRoutine.response(WaitSignal, 1000, ['s'])    
    if len(signal):
        break
    
    if defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    win.flip()

# 4. Ending "Wait" Routine
endRoutine(WaitComponents)



###############################################
#------------------- TRIAL -------------------#
###############################################

# 1. Set Trial timer
TrialClock.reset(-win.getFutureFlipTime(clock="now"))

for i in range(1, 15):
    
    # 2. Initialize Components
    initComponents(TrialComponents)
    
    # 3. Set Trial Routine timer
    setTime=2
    routineTimer.reset()
    routineTimer.add(setTime)
    
    # 4. Set image
    img = './stim/%i.jpg'%(i)
    Stim.setImage(img)

    # 5. Start "Trial" Routine
    while routineTimer.getTime() > frameTolerance:
        # set this flip
        TrialRoutine = Routine(win, TrialClock)
        # components update
        TrialRoutine.visual(Stim, 1)    
        TrialRoutine.visual(Dot, setTime)    
        signal = TrialRoutine.response(Signal, setTime, 's')    
        if len(signal):
            Signal.rt = signal[-1].rt
            break
        response = TrialRoutine.response(Response, setTime, 'r')    
        if len(response):
            Response.rt = response[-1].rt
        # set quit key 
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        win.flip()
    
    print(i, Stim.tStart, Signal.rt, Response.rt)
    
    # 6. Ending Routine "Trial"
    endRoutine(TrialComponents)
    
    
win.flip()
logging.flush()
win.close()
core.quit()
