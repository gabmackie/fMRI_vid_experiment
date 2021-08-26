# -*- coding: utf-8 -*-
########################################################
# I know using lots of lists is garbage, but it's easier to read like that
# so that's why I'm doing it. I will make a neater version eventually
########################################################
import pandas as pd
from random import shuffle, choice
from psychopy import visual, core
from os import path

# Get our files loaded
# Find the folder with this file in
script_dir = path.dirname(path.abspath(__file__))

# Add the sections that are needed to get from the folder to the videos and to the stimuli list
vid_loc = 'videos'
sheet_loc = 'Stimuli_List.xlsx'

# Join them to make a filepath that will automatically change based on where the script is
videos_path = path.join(script_dir, vid_loc)
sheet_path = path.join(script_dir, vid_loc, sheet_loc)


# Create our window
win = visual.Window([1024, 768], units="pix",
                    fullscr=False, allowGUI=True,
                    color=(-1.0, -1.0, -1.0))

# Create a circle stimulus
circle = visual.Circle(win, radius=5, edges=32, lineColor='red', fillColor='red')


# Load our stimuli list using pandas
# Add "sheet_name = 2" for the real one
df = pd.read_excel(sheet_path)

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
    vid_path = path.join(videos_path, vid)
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