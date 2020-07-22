from __future__ import absolute_import, division
import numpy as np
import os, sys
from definition import *


# Store info about the experiment session
Date=data.getDateStr().split('_')

expName = 'FaceRec'
expInfo = {
           'Title': expName, 
           'SubId': '00',
           'Session': '00'
           }
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  
_thisDir = os.path.dirname(os.path.abspath(__file__))

# Setup the Window and Keyboard
win = set_window()
defaultKeyboard = keyboard.Keyboard()

# Initialize "Wait" Components
WaitClock = core.Clock()
WaitText = set_text(win, 'WaitText')
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
    # get current time
    timer, tThisFlip, tThisFlipGlobal, frameN = getCurrentTime(WaitClock, win, frameN)

    # update parameters
    param_updates(WaitText, 1000000) 
    WaitSigList=param_updates(WaitSignal, 100000, ['s'])
    if len(WaitSigList):
        continueRoutine = False
    
    # Finish if not continueRoutine
    if defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    if not continueRoutine: 
        break
    
    # Check continue or not
    for Compo in WaitComponents:
        if hasattr(Compo, "status") and Compo.status != FINISHED:
            continueRoutine = True
        else: continueRoutine = False    
    if continueRoutine:  
        win.flip()

# 4. Ending Routine
for Compo in WaitComponents:
    if hasattr(Compo, "setAutoDraw"):
        Compo.setAutoDraw(False)
routineTimer.reset()



###############################################
#------------------- TRIAL -------------------#
###############################################
# 1. Set Trial timer
frameN = 0
TrialClock.reset(-win.getFutureFlipTime(clock="now"))

# 2. Set Components
TrialComponents = [Dot, Stim, Signal, Response]
initComponents(TrialComponents)
continueRoutine = True

# 3. Set Trial Routine timer
TrialSetTime=3
routineTimer.add(TrialSetTime)

# 4. Set image
Stim.setImage('./stim/1.jpg')

# 5. Run Routine Trial
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    timer, tThisFlip, tThisFlipGlobal, frameN = getCurrentTime(TrialClock, win, frameN)
    
    # update parameters
    param_updates(Stim, 1) 
    param_updates(Dot, TrialSetTime)     
   
    RespList=param_updates(Response, TrialSetTime, ['r'])     
    if len(RespList):
        Response.keys=RespList[-1].name
        Response.rt=RespList[-1].rt

    SigList=param_updates(Signal, TrialSetTime, ['s'])     
    if len(SigList):
        Signal.keys=SigList[-1].name
        Signal.rt=SigList[-1].rt
        continueRoutine = False
      
    # check continue or not 
    if defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    if not continueRoutine:  
        break
    continueRoutine = False  
    for Compo in TrialComponents:
        if hasattr(Compo, "status") and Compo.status != FINISHED:
            continueRoutine = True
            
            #break  
    if continueRoutine:  
        win.flip()

# 6. Ending Routine "Trial"
for Compo in TrialComponents:
    if hasattr(Compo, "setAutoDraw"):
        Compo.setAutoDraw(False)

    
win.flip()
logging.flush()
win.close()
core.quit()
