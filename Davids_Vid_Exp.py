# -*- coding: utf-8 -*-
########################################################
# I know using lots of lists is garbage, but it's easier to read like that
# so that's why I'm doing it. I will make a neater version eventually
########################################################
import pandas as pd
from random import shuffle, choice
from psychopy import visual, core, gui, event
import os
from datetime import datetime

# Get the working directory, where our file is
cwd = os.getcwd()

# Set the name of our spreadsheet with the stimuli in
stimuli = 'Stimuli_List.xlsx'

# Set escape key
escape_key = 'escape'

# 
categories = ['Talking', 'Gaze', 'Expressions', 'Couple Talking', 'Head Turn']

# Get information from the participant and set up our output file
# Create variables to hold the participant information
partinfo = {}
partinfo['Experiment name'] = 'Social Video Experiment'
partinfo['ID'] = ''
partinfo['Experiment date'] = datetime.now().strftime('%Y%m%d_%H%M')

# Show dialog for participant information to be entered
dlg = gui.DlgFromDict(partinfo,
                      title='Participant Info',
                      fixed=['Experiment name', 'Experiment date'],
                      order=['Experiment name', 'Experiment date', 'ID'])

# If the OK button in the dialog isn't pressed, close the experiment
if not dlg.OK:
    print("Experiment cancelled by user")
    core.quit()

# Generate a .csv filename based on the time and participant info
filename = f"{partinfo['Experiment date']}_P{partinfo['ID']}.csv"

# Create an output file, placing it in our output directory
f = open(filename, 'w')

# Write out our header
f.write('block,video,timing,response\n')


# Create our window
win = visual.Window([1024, 768], units="pix",
                    fullscr=False, allowGUI=True,
                    color=(0, 0, 0))

# Create a circle stimulus
circle = visual.Circle(win, radius=5, edges=32, lineColor='red', fillColor='red')


# Load our stimuli list using pandas
# Add "sheet_name = 2" for if it's working from the second sheet
df = pd.read_excel(stimuli)

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
    vid_path = os.path.join(cwd, 'videos', vid)
    vid_path = vid_path + '.mp4'
    
    # Create a movie stimulus
    # Can add more features here if needed
    stim = visual.MovieStim3(win, filename=vid_path, volume = 0, name = vid)
    
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

# Have an introductory rest block
timing = win.flip()
# Write out the block information
f.write(f'rest,NA,{timing},NA\n')
f.flush()
core.wait(4)

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
        
        # Clear the events so any keys pressed previously won't count
        event.clearEvents()
        
        # Extract the time that the video starts
        timing = core.getTime()
        # This runs the actual video
        while mov.status != visual.FINISHED:
            mov.draw()
            # Drawing a circle if needed
            if circ:
                circle.draw()
            win.flip()
        
        # Get the keys that the participant has pressed
        keys = event.getKeys()
        
        # The length of the keys is the number of keys pressed
        key_presses = len(keys)
        
        # Set the response to the default of NA
        response = 'NA'
        
        if key_presses > 0:
            # If the key pressed was the escape key, print that to the output and quit the experiment
            if keys[0] == escape_key:
                response = "User requested to quit: ending experiment"
                f.close()
                win.close()
                core.quit()
            
            # If it wasn't the esc key, and the red dot trial happened, it means they responded
            elif circ:
                response = True
        
        # If no keys were pressed and it was the red dot trial, then they failed to respond
        else:
            if circ:
                response = False
        
        # Extract the name out of the mov stimulus
        name = stim.name
        # Write this trial's information to the output file
        f.write(f'block,{name},{timing},{response}\n')
        f.flush()
        
        # increase the trial num by one
        trial += 1
    
# Close the experiment
f.close()
win.close()
core.quit()
