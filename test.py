from __future__ import absolute_import, division
import numpy as np
import os, sys
from definition import *

# Response  ->  dot color change 
# Signal time :  0-2 -> 1-2


# Store info about the experiment session
Date=data.getDateStr()

expName = 'YYB'
expInfo = {
           'Title': expName, 
           'Date' : Date,
           'SubId': '00',
           'Session': '00'
           }
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  
print(dlg)

# Setup the Window and Keyboard
win = set_window()
defaultKeyboard = keyboard.Keyboard()

# Initialize "Wait" Components
WaitClock = core.Clock()
WaitText = set_text(win, 'WaitText')
WaitText.text = 'Hello'
WaitSignal = keyboard.Keyboard()

# Initialize "Trial" Components
TrialClock = core.Clock()
Dot = set_circle(win, 'Dot')
Stim = set_image(win, 'Stim')
Signal = keyboard.Keyboard()
Response = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  
routineTimer = core.CountdownTimer() 
frameTolerance = 0.001  

def updateparam(Compo, dur, setTime):
    if routineTimer.getTime() > setTime-dur:
        if Compo.status==False: 
            Compo.tStart  = TrialClock.getTime()
        win.timeOnFlip(Compo, 'tStartRefresh')  
        Compo.setAutoDraw(True)
        Compo.status=True
    else:
        win.timeOnFlip(Compo, 'tStopRefresh')  # time at next scr refresh
        Compo.setAutoDraw(False)
        Compo.status=False

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
            win.OnFlip = True
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


##############################################
#------------------- WAIT -------------------#
##############################################
# 1. Set "Wait" Timer
frameN = 0
WaitClock.reset(-win.getFutureFlipTime(clock="now"))

# 2. Set Components
continueRoutine = True
WaitComponents = [WaitText, WaitSignal]
initComponents(WaitComponents)

# 3. Start Routine
while True:
    time, tThisFlip, tThisFlipGlobal, frameN=getCurrentTime(RoutineClock, win, frameN) 
    
    # update parameters
    update(WaitText, 3, tThisFlip, tThisFlipGlobal, win) 
    update(WaitSignal, 10000, tThisFlip, tThisFlipGlobal, win) 
    if len(theseKeys):
        print(theseKeys)
        break
    
    # Finish if not continueRoutine
    if defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    win.flip()

# 4. Ending Routine
endRoutine(WaitComponents)

###############################################
#------------------- TRIAL -------------------#
###############################################



# 1. Set Trial timer
frameN = 0
TrialClock.reset(-win.getFutureFlipTime(clock="now"))
for i in range(1, 15):
    # 2. Set Components
    TrialComponents = [Stim]#, Stim, Signal, Response]
    initComponents(TrialComponents)
    
    # 3. Set Trial Routine timer
    TrialSetTime=3
    routineTimer.reset()
    routineTimer.add(TrialSetTime)
    
    # 4. Set image
    img = './stim/%i.jpg'%(i)
    Stim.setImage(img)
    
    # 5. Run Routine Trial
    while routineTimer.getTime() > frameTolerance:
        time, tThisFlip, tThisFlipGlobal, frameN=getCurrentTime(RoutineClock, win, frameN) 

        updateparam(Stim, 3, 1)
        updateparam(Dot, 3, 2)

        # set quit key 
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        win.flip()
    
    print(i, routineTimer.getTime(), Stim.tStart)
    
    # 6. Ending Routine "Trial"
    endRoutine(TrialComponents)
    
    
win.flip()
logging.flush()
win.close()
core.quit()
