# -*- coding: utf-8 -*-
########################################################
# This is the more basic experiment, without fancy stuff, but it works.
# I know using lots of lists is garbage, but it's easier to read like that
# so that's why I'm doing it. I will make a neater version eventually
########################################################
import pandas as pd
from random import shuffle, choice
from psychopy import visual, core
from os.path import join

# Create our window
win = visual.Window([1024, 768], units="pix",
                    fullscr=False, allowGUI=True,
                    color=(-1.0, -1.0, -1.0))

# Create a circle stimulus
circle = visual.Circle(win, radius=5, edges=32, lineColor='red', fillColor='red')

path = 'C:/Users/gabri/Documents/Programming/Davids_Video_Experiment/videos/'

# Add "sheet_name = 2" for the real one
df = pd.read_excel("C:/Users/gabri/Documents/Programming/Davids_Video_Experiment/videos/Stimuli_List.xlsx")

# Extract the number of rows, aka vidoes, in our sheet
rows = df.shape[0]

# Create a list for our stimuli, and lists for each category
stimuli = []

talk = []
gaze = []
expression = []
couple = []
head = []

# Run through every row and sort the video
for row in range(rows):
    
    # Read the category and the video name
    cat = df.loc[row, 'Category']
    vid = df.loc[row, 'Video']
    
    # Generate a filepath from the name
    vid_path = join(path, vid)
    vid_path = vid_path + '.mp4'
    
    # Create a movie stimulus
    # Can add more features here if needed
    stim = visual.MovieStim3(win, filename=vid_path)
    
    # Put it into the relevant category
    if cat == 'Talking':
        talk.append(stim)
    elif cat == 'Gaze':
        gaze.append(stim)
    elif cat == 'Expressions':
        expression.append(stim)
    elif cat == 'Couple Talking':
        couple.append(stim)
    elif cat == 'Head Turn':
        head.append(stim)
    else:
        print("There is a stimulus that doesn't match a known category")

# Shuffle the videos within a category, and add them to our stimuli list
shuffle(talk)
shuffle(gaze)
shuffle(expression)
shuffle(couple)
shuffle(head)

stimuli.append(gaze)
stimuli.append(talk)
stimuli.append(expression)
stimuli.append(couple)
stimuli.append(head)

# Shuffle the blocks
shuffle(stimuli)

# EXPERIMENT STARTS HERE
# Set the clock (Not sure what it does, don't delete)
globalClock = core.Clock()

# Have an introductory second
win.flip()
core.wait(1)

# Run each cateogry of stimulus at a time
for block in stimuli:
    # Calculate the number of trials in a block
    length = len(block)
    # Pick a random trial to play the red dot
    red_trial = choice(range(length)) + 1
    trial = 1
    
    # Now play each video within that block
    # You need to be careful how much you put in here, because it can slow the code down
    for stim in block:
        # Assign the stimuli to our mov object
        mov = stim
        
        # Set the trial to be a red-dot or normal trial
        # This is seperate from the while loop in case we want a user response to 
        # end the dot. We'd do that by setting it to false
        if trial == red_trial:
            circ = True
        else:
            circ = False
        
        # This runs the actual video
        while mov.status != visual.FINISHED:
            mov.draw()
            # Drawing a circle if needed
            if circ:
                circle.draw()
            win.flip()
            
        # Add a trial if needed
        trial += 1
    
# Close the experiment
win.close()
core.quit()