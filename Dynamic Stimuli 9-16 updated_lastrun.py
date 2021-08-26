#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on Tue 23 Oct 2018 12:32:25 BST
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Dynamic Stimuli 9-16 updated'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/scratch/groups/Projects/P1366/fMRI/Dynamic Stimuli 9-16 updated.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "WaitFor5"
WaitFor5Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u'Wait for scanner',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
Instructions2 = visual.TextStim(win=win, name='Instructions2',
    text='In this next task you will see more clips of faces. \nPlease indicate with the right button of the clicker when you see a female face, and respond with the left button when you see a male face.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
DynamicAnger9 = visual.MovieStim3(
    win=win, name='DynamicAnger9',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Anger 9.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1600, 1050),
    depth=-1.0,
    )
DynamicAnger10 = visual.MovieStim3(
    win=win, name='DynamicAnger10',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Anger 10.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-2.0,
    )
DynamicAnger11 = visual.MovieStim3(
    win=win, name='DynamicAnger11',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Anger 11.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-3.0,
    )
DynamicAnger12 = visual.MovieStim3(
    win=win, name='DynamicAnger12',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Anger 12.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-4.0,
    )
DynamicAnger13 = visual.MovieStim3(
    win=win, name='DynamicAnger13',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Anger 13.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-5.0,
    )
DynamicAnger14 = visual.MovieStim3(
    win=win, name='DynamicAnger14',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Anger 14.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-6.0,
    )
DynamicAnger15 = visual.MovieStim3(
    win=win, name='DynamicAnger15',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Anger 15.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-7.0,
    )
DynamicAnger16 = visual.MovieStim3(
    win=win, name='DynamicAnger16',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Anger 16.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-8.0,
    )
DynamicFear9 = visual.MovieStim3(
    win=win, name='DynamicFear9',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Fear 9.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-9.0,
    )
DynamicFear10 = visual.MovieStim3(
    win=win, name='DynamicFear10',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Fear 10.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-10.0,
    )
DynamicFear11 = visual.MovieStim3(
    win=win, name='DynamicFear11',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Fear 11.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-11.0,
    )
DynamicFear12 = visual.MovieStim3(
    win=win, name='DynamicFear12',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Fear 12.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-12.0,
    )
DynamicFear13 = visual.MovieStim3(
    win=win, name='DynamicFear13',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Fear 13.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-13.0,
    )
DynamicFear14 = visual.MovieStim3(
    win=win, name='DynamicFear14',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Fear 14.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-14.0,
    )
DynamicFear15 = visual.MovieStim3(
    win=win, name='DynamicFear15',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Fear 15.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-15.0,
    )
DynamicFear16 = visual.MovieStim3(
    win=win, name='DynamicFear16',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Fear 16.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-16.0,
    )
DynamicHappy9 = visual.MovieStim3(
    win=win, name='DynamicHappy9',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Happy 9.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-17.0,
    )
DynamicHappy10 = visual.MovieStim3(
    win=win, name='DynamicHappy10',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Happy 10.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-18.0,
    )
DynamicHappy11 = visual.MovieStim3(
    win=win, name='DynamicHappy11',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Happy 11.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-19.0,
    )
DynamicHappy12 = visual.MovieStim3(
    win=win, name='DynamicHappy12',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Happy 12.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-20.0,
    )
DynamicHappy13 = visual.MovieStim3(
    win=win, name='DynamicHappy13',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Happy 13.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-21.0,
    )
DynamicHappy14 = visual.MovieStim3(
    win=win, name='DynamicHappy14',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Happy 14.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-22.0,
    )
DynamicHappy15 = visual.MovieStim3(
    win=win, name='DynamicHappy15',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Happy 15.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-23.0,
    )
DynamicHappy16 = visual.MovieStim3(
    win=win, name='DynamicHappy16',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Happy 16.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-24.0,
    )
DynamicSad9 = visual.MovieStim3(
    win=win, name='DynamicSad9',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Sad 9.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-25.0,
    )
DynamicSad10 = visual.MovieStim3(
    win=win, name='DynamicSad10',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Sad 10.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-26.0,
    )
DynamicSad11 = visual.MovieStim3(
    win=win, name='DynamicSad11',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Sad 11.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-27.0,
    )
DynamicSad12 = visual.MovieStim3(
    win=win, name='DynamicSad12',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Sad 12.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-28.0,
    )
DynamicSad13 = visual.MovieStim3(
    win=win, name='DynamicSad13',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Sad 13.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-29.0,
    )
DynamicSad14 = visual.MovieStim3(
    win=win, name='DynamicSad14',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Sad 14.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-30.0,
    )
DynamicSad15 = visual.MovieStim3(
    win=win, name='DynamicSad15',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Sad 15.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-31.0,
    )
DynamicSad16 = visual.MovieStim3(
    win=win, name='DynamicSad16',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Sad 16.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-32.0,
    )
DynamicSurprise9 = visual.MovieStim3(
    win=win, name='DynamicSurprise9',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Surprise 9.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-33.0,
    )
DynamicSurprise10 = visual.MovieStim3(
    win=win, name='DynamicSurprise10',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Surprise 10.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-34.0,
    )
DynamicSurprise11 = visual.MovieStim3(
    win=win, name='DynamicSurprise11',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Surprise 11.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-35.0,
    )
DynamicSurprise12 = visual.MovieStim3(
    win=win, name='DynamicSurprise12',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Surprise 12.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-36.0,
    )
DynamicSurprise13 = visual.MovieStim3(
    win=win, name='DynamicSurprise13',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Surprise 13.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-37.0,
    )
DynamicSurprise14 = visual.MovieStim3(
    win=win, name='DynamicSurprise14',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Surprise 14.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-38.0,
    )
DynamicSurprise15 = visual.MovieStim3(
    win=win, name='DynamicSurprise15',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Surprise 15.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-39.0,
    )
DynamicSurprise16 = visual.MovieStim3(
    win=win, name='DynamicSurprise16',
    noAudio = False,
    filename='/home/a/am1912/Downloads/Surprise 16.mov',
    ori=0, pos=(0, 0), opacity=1,
    size=(1680, 1050),
    depth=-40.0,
    )

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WaitFor5"-------
t = 0
WaitFor5Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
WaitForScanner = event.BuilderKeyResponse()
# keep track of which components have finished
WaitFor5Components = [WaitForScanner, text]
for thisComponent in WaitFor5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "WaitFor5"-------
while continueRoutine:
    # get current time
    t = WaitFor5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WaitForScanner* updates
    if t >= 0.0 and WaitForScanner.status == NOT_STARTED:
        # keep track of start time/frame for later
        WaitForScanner.tStart = t
        WaitForScanner.frameNStart = frameN  # exact frame index
        WaitForScanner.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(WaitForScanner.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if WaitForScanner.status == STARTED:
        theseKeys = event.getKeys(keyList=['5'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            WaitForScanner.keys = theseKeys[-1]  # just the last key pressed
            WaitForScanner.rt = WaitForScanner.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WaitFor5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WaitFor5"-------
for thisComponent in WaitFor5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if WaitForScanner.keys in ['', [], None]:  # No response was made
    WaitForScanner.keys=None
thisExp.addData('WaitForScanner.keys',WaitForScanner.keys)
if WaitForScanner.keys != None:  # we had a response
    thisExp.addData('WaitForScanner.rt', WaitForScanner.rt)
thisExp.nextEntry()
# the Routine "WaitFor5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(160.000000)
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [Instructions2, DynamicAnger9, DynamicAnger10, DynamicAnger11, DynamicAnger12, DynamicAnger13, DynamicAnger14, DynamicAnger15, DynamicAnger16, DynamicFear9, DynamicFear10, DynamicFear11, DynamicFear12, DynamicFear13, DynamicFear14, DynamicFear15, DynamicFear16, DynamicHappy9, DynamicHappy10, DynamicHappy11, DynamicHappy12, DynamicHappy13, DynamicHappy14, DynamicHappy15, DynamicHappy16, DynamicSad9, DynamicSad10, DynamicSad11, DynamicSad12, DynamicSad13, DynamicSad14, DynamicSad15, DynamicSad16, DynamicSurprise9, DynamicSurprise10, DynamicSurprise11, DynamicSurprise12, DynamicSurprise13, DynamicSurprise14, DynamicSurprise15, DynamicSurprise16]
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions2* updates
    if t >= 0.0 and Instructions2.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions2.tStart = t
        Instructions2.frameNStart = frameN  # exact frame index
        Instructions2.setAutoDraw(True)
    frameRemains = 0.0 + 10.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if Instructions2.status == STARTED and t >= frameRemains:
        Instructions2.setAutoDraw(False)
    
    # *DynamicAnger9* updates
    if t >= 16.0 and DynamicAnger9.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicAnger9.tStart = t
        DynamicAnger9.frameNStart = frameN  # exact frame index
        DynamicAnger9.setAutoDraw(True)
    frameRemains = 16.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicAnger9.status == STARTED and t >= frameRemains:
        DynamicAnger9.setAutoDraw(False)
    
    # *DynamicAnger10* updates
    if t >= 18.0 and DynamicAnger10.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicAnger10.tStart = t
        DynamicAnger10.frameNStart = frameN  # exact frame index
        DynamicAnger10.setAutoDraw(True)
    frameRemains = 18.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicAnger10.status == STARTED and t >= frameRemains:
        DynamicAnger10.setAutoDraw(False)
    
    # *DynamicAnger11* updates
    if t >= 20.0 and DynamicAnger11.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicAnger11.tStart = t
        DynamicAnger11.frameNStart = frameN  # exact frame index
        DynamicAnger11.setAutoDraw(True)
    frameRemains = 20.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicAnger11.status == STARTED and t >= frameRemains:
        DynamicAnger11.setAutoDraw(False)
    
    # *DynamicAnger12* updates
    if t >= 22.0 and DynamicAnger12.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicAnger12.tStart = t
        DynamicAnger12.frameNStart = frameN  # exact frame index
        DynamicAnger12.setAutoDraw(True)
    frameRemains = 22.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicAnger12.status == STARTED and t >= frameRemains:
        DynamicAnger12.setAutoDraw(False)
    
    # *DynamicAnger13* updates
    if t >= 24.0 and DynamicAnger13.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicAnger13.tStart = t
        DynamicAnger13.frameNStart = frameN  # exact frame index
        DynamicAnger13.setAutoDraw(True)
    frameRemains = 24.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicAnger13.status == STARTED and t >= frameRemains:
        DynamicAnger13.setAutoDraw(False)
    
    # *DynamicAnger14* updates
    if t >= 26.0 and DynamicAnger14.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicAnger14.tStart = t
        DynamicAnger14.frameNStart = frameN  # exact frame index
        DynamicAnger14.setAutoDraw(True)
    frameRemains = 26.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicAnger14.status == STARTED and t >= frameRemains:
        DynamicAnger14.setAutoDraw(False)
    
    # *DynamicAnger15* updates
    if t >= 28.0 and DynamicAnger15.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicAnger15.tStart = t
        DynamicAnger15.frameNStart = frameN  # exact frame index
        DynamicAnger15.setAutoDraw(True)
    frameRemains = 28.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicAnger15.status == STARTED and t >= frameRemains:
        DynamicAnger15.setAutoDraw(False)
    
    # *DynamicAnger16* updates
    if t >= 30.0 and DynamicAnger16.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicAnger16.tStart = t
        DynamicAnger16.frameNStart = frameN  # exact frame index
        DynamicAnger16.setAutoDraw(True)
    frameRemains = 30.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicAnger16.status == STARTED and t >= frameRemains:
        DynamicAnger16.setAutoDraw(False)
    
    # *DynamicFear9* updates
    if t >= 48.0 and DynamicFear9.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicFear9.tStart = t
        DynamicFear9.frameNStart = frameN  # exact frame index
        DynamicFear9.setAutoDraw(True)
    frameRemains = 48.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicFear9.status == STARTED and t >= frameRemains:
        DynamicFear9.setAutoDraw(False)
    
    # *DynamicFear10* updates
    if t >= 50.0 and DynamicFear10.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicFear10.tStart = t
        DynamicFear10.frameNStart = frameN  # exact frame index
        DynamicFear10.setAutoDraw(True)
    frameRemains = 50.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicFear10.status == STARTED and t >= frameRemains:
        DynamicFear10.setAutoDraw(False)
    
    # *DynamicFear11* updates
    if t >= 52.0 and DynamicFear11.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicFear11.tStart = t
        DynamicFear11.frameNStart = frameN  # exact frame index
        DynamicFear11.setAutoDraw(True)
    frameRemains = 52.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicFear11.status == STARTED and t >= frameRemains:
        DynamicFear11.setAutoDraw(False)
    
    # *DynamicFear12* updates
    if t >= 54.0 and DynamicFear12.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicFear12.tStart = t
        DynamicFear12.frameNStart = frameN  # exact frame index
        DynamicFear12.setAutoDraw(True)
    frameRemains = 54.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicFear12.status == STARTED and t >= frameRemains:
        DynamicFear12.setAutoDraw(False)
    
    # *DynamicFear13* updates
    if t >= 56.0 and DynamicFear13.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicFear13.tStart = t
        DynamicFear13.frameNStart = frameN  # exact frame index
        DynamicFear13.setAutoDraw(True)
    frameRemains = 56.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicFear13.status == STARTED and t >= frameRemains:
        DynamicFear13.setAutoDraw(False)
    
    # *DynamicFear14* updates
    if t >= 58.0 and DynamicFear14.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicFear14.tStart = t
        DynamicFear14.frameNStart = frameN  # exact frame index
        DynamicFear14.setAutoDraw(True)
    frameRemains = 58.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicFear14.status == STARTED and t >= frameRemains:
        DynamicFear14.setAutoDraw(False)
    
    # *DynamicFear15* updates
    if t >= 60.0 and DynamicFear15.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicFear15.tStart = t
        DynamicFear15.frameNStart = frameN  # exact frame index
        DynamicFear15.setAutoDraw(True)
    frameRemains = 60.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicFear15.status == STARTED and t >= frameRemains:
        DynamicFear15.setAutoDraw(False)
    
    # *DynamicFear16* updates
    if t >= 62.0 and DynamicFear16.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicFear16.tStart = t
        DynamicFear16.frameNStart = frameN  # exact frame index
        DynamicFear16.setAutoDraw(True)
    frameRemains = 62.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicFear16.status == STARTED and t >= frameRemains:
        DynamicFear16.setAutoDraw(False)
    
    # *DynamicHappy9* updates
    if t >= 80.0 and DynamicHappy9.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicHappy9.tStart = t
        DynamicHappy9.frameNStart = frameN  # exact frame index
        DynamicHappy9.setAutoDraw(True)
    frameRemains = 80.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicHappy9.status == STARTED and t >= frameRemains:
        DynamicHappy9.setAutoDraw(False)
    
    # *DynamicHappy10* updates
    if t >= 82.0 and DynamicHappy10.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicHappy10.tStart = t
        DynamicHappy10.frameNStart = frameN  # exact frame index
        DynamicHappy10.setAutoDraw(True)
    frameRemains = 82.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicHappy10.status == STARTED and t >= frameRemains:
        DynamicHappy10.setAutoDraw(False)
    
    # *DynamicHappy11* updates
    if t >= 84.0 and DynamicHappy11.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicHappy11.tStart = t
        DynamicHappy11.frameNStart = frameN  # exact frame index
        DynamicHappy11.setAutoDraw(True)
    frameRemains = 84.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicHappy11.status == STARTED and t >= frameRemains:
        DynamicHappy11.setAutoDraw(False)
    
    # *DynamicHappy12* updates
    if t >= 86.0 and DynamicHappy12.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicHappy12.tStart = t
        DynamicHappy12.frameNStart = frameN  # exact frame index
        DynamicHappy12.setAutoDraw(True)
    frameRemains = 86.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicHappy12.status == STARTED and t >= frameRemains:
        DynamicHappy12.setAutoDraw(False)
    
    # *DynamicHappy13* updates
    if t >= 88.0 and DynamicHappy13.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicHappy13.tStart = t
        DynamicHappy13.frameNStart = frameN  # exact frame index
        DynamicHappy13.setAutoDraw(True)
    frameRemains = 88.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicHappy13.status == STARTED and t >= frameRemains:
        DynamicHappy13.setAutoDraw(False)
    
    # *DynamicHappy14* updates
    if t >= 90.0 and DynamicHappy14.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicHappy14.tStart = t
        DynamicHappy14.frameNStart = frameN  # exact frame index
        DynamicHappy14.setAutoDraw(True)
    frameRemains = 90.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicHappy14.status == STARTED and t >= frameRemains:
        DynamicHappy14.setAutoDraw(False)
    
    # *DynamicHappy15* updates
    if t >= 92.0 and DynamicHappy15.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicHappy15.tStart = t
        DynamicHappy15.frameNStart = frameN  # exact frame index
        DynamicHappy15.setAutoDraw(True)
    frameRemains = 92.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicHappy15.status == STARTED and t >= frameRemains:
        DynamicHappy15.setAutoDraw(False)
    
    # *DynamicHappy16* updates
    if t >= 94.0 and DynamicHappy16.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicHappy16.tStart = t
        DynamicHappy16.frameNStart = frameN  # exact frame index
        DynamicHappy16.setAutoDraw(True)
    frameRemains = 94.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicHappy16.status == STARTED and t >= frameRemains:
        DynamicHappy16.setAutoDraw(False)
    
    # *DynamicSad9* updates
    if t >= 112.0 and DynamicSad9.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicSad9.tStart = t
        DynamicSad9.frameNStart = frameN  # exact frame index
        DynamicSad9.setAutoDraw(True)
    frameRemains = 112.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicSad9.status == STARTED and t >= frameRemains:
        DynamicSad9.setAutoDraw(False)
    
    # *DynamicSad10* updates
    if t >= 114.0 and DynamicSad10.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicSad10.tStart = t
        DynamicSad10.frameNStart = frameN  # exact frame index
        DynamicSad10.setAutoDraw(True)
    frameRemains = 114.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicSad10.status == STARTED and t >= frameRemains:
        DynamicSad10.setAutoDraw(False)
    
    # *DynamicSad11* updates
    if t >= 116.0 and DynamicSad11.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicSad11.tStart = t
        DynamicSad11.frameNStart = frameN  # exact frame index
        DynamicSad11.setAutoDraw(True)
    frameRemains = 116.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicSad11.status == STARTED and t >= frameRemains:
        DynamicSad11.setAutoDraw(False)
    
    # *DynamicSad12* updates
    if t >= 118.0 and DynamicSad12.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicSad12.tStart = t
        DynamicSad12.frameNStart = frameN  # exact frame index
        DynamicSad12.setAutoDraw(True)
    frameRemains = 118.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicSad12.status == STARTED and t >= frameRemains:
        DynamicSad12.setAutoDraw(False)
    
    # *DynamicSad13* updates
    if t >= 120.0 and DynamicSad13.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicSad13.tStart = t
        DynamicSad13.frameNStart = frameN  # exact frame index
        DynamicSad13.setAutoDraw(True)
    frameRemains = 120.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicSad13.status == STARTED and t >= frameRemains:
        DynamicSad13.setAutoDraw(False)
    
    # *DynamicSad14* updates
    if t >= 122.0 and DynamicSad14.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicSad14.tStart = t
        DynamicSad14.frameNStart = frameN  # exact frame index
        DynamicSad14.setAutoDraw(True)
    frameRemains = 122.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicSad14.status == STARTED and t >= frameRemains:
        DynamicSad14.setAutoDraw(False)
    
    # *DynamicSad15* updates
    if t >= 124.0 and DynamicSad15.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicSad15.tStart = t
        DynamicSad15.frameNStart = frameN  # exact frame index
        DynamicSad15.setAutoDraw(True)
    frameRemains = 124.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicSad15.status == STARTED and t >= frameRemains:
        DynamicSad15.setAutoDraw(False)
    
    # *DynamicSad16* updates
    if t >= 126.0 and DynamicSad16.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicSad16.tStart = t
        DynamicSad16.frameNStart = frameN  # exact frame index
        DynamicSad16.setAutoDraw(True)
    frameRemains = 126.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicSad16.status == STARTED and t >= frameRemains:
        DynamicSad16.setAutoDraw(False)
    
    # *DynamicSurprise9* updates
    if t >= 144.0 and DynamicSurprise9.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicSurprise9.tStart = t
        DynamicSurprise9.frameNStart = frameN  # exact frame index
        DynamicSurprise9.setAutoDraw(True)
    frameRemains = 144.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicSurprise9.status == STARTED and t >= frameRemains:
        DynamicSurprise9.setAutoDraw(False)
    
    # *DynamicSurprise10* updates
    if t >= 146.0 and DynamicSurprise10.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicSurprise10.tStart = t
        DynamicSurprise10.frameNStart = frameN  # exact frame index
        DynamicSurprise10.setAutoDraw(True)
    frameRemains = 146.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicSurprise10.status == STARTED and t >= frameRemains:
        DynamicSurprise10.setAutoDraw(False)
    
    # *DynamicSurprise11* updates
    if t >= 148.0 and DynamicSurprise11.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicSurprise11.tStart = t
        DynamicSurprise11.frameNStart = frameN  # exact frame index
        DynamicSurprise11.setAutoDraw(True)
    frameRemains = 148.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicSurprise11.status == STARTED and t >= frameRemains:
        DynamicSurprise11.setAutoDraw(False)
    
    # *DynamicSurprise12* updates
    if t >= 150.0 and DynamicSurprise12.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicSurprise12.tStart = t
        DynamicSurprise12.frameNStart = frameN  # exact frame index
        DynamicSurprise12.setAutoDraw(True)
    frameRemains = 150.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicSurprise12.status == STARTED and t >= frameRemains:
        DynamicSurprise12.setAutoDraw(False)
    
    # *DynamicSurprise13* updates
    if t >= 152.0 and DynamicSurprise13.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicSurprise13.tStart = t
        DynamicSurprise13.frameNStart = frameN  # exact frame index
        DynamicSurprise13.setAutoDraw(True)
    frameRemains = 152.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicSurprise13.status == STARTED and t >= frameRemains:
        DynamicSurprise13.setAutoDraw(False)
    
    # *DynamicSurprise14* updates
    if t >= 154.0 and DynamicSurprise14.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicSurprise14.tStart = t
        DynamicSurprise14.frameNStart = frameN  # exact frame index
        DynamicSurprise14.setAutoDraw(True)
    frameRemains = 154.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicSurprise14.status == STARTED and t >= frameRemains:
        DynamicSurprise14.setAutoDraw(False)
    
    # *DynamicSurprise15* updates
    if t >= 156.0 and DynamicSurprise15.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicSurprise15.tStart = t
        DynamicSurprise15.frameNStart = frameN  # exact frame index
        DynamicSurprise15.setAutoDraw(True)
    frameRemains = 156.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicSurprise15.status == STARTED and t >= frameRemains:
        DynamicSurprise15.setAutoDraw(False)
    
    # *DynamicSurprise16* updates
    if t >= 158.0 and DynamicSurprise16.status == NOT_STARTED:
        # keep track of start time/frame for later
        DynamicSurprise16.tStart = t
        DynamicSurprise16.frameNStart = frameN  # exact frame index
        DynamicSurprise16.setAutoDraw(True)
    frameRemains = 158.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if DynamicSurprise16.status == STARTED and t >= frameRemains:
        DynamicSurprise16.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
