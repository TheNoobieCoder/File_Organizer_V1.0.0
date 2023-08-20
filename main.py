import time
import tkinter as tk
import os
from tkinter import filedialog

# Defualt destination paths

username                = os.getlogin()

video_directory_path    = f"C:/Users/{username}/Videos"
audio_directory_path    = f"C:/Users/{username}/Music"
photo_directory_path    = f"C:/Users/{username}/Pictures"

# Dialogs Functions

def welcome():
	print("Welcome to my file organizer V 1.0.0")
	print("")


def actions_dialog():
	print("Select the action you wish to be performed by typing the corresponding number:")
	print("_______________________________________")
	print("1. Move photos in folder to the Pictures folder")
	print("2. Move audio files into Music folder")
	print("3. Move video files into Videos folder")
	print("_______________________________________")
	print("4. Set new destination folder for audio files")
	print("5. Set new destination folder for video files")
	print("6. Set new destination folder for executables files")


# File selection Functions

def select_file():
	
	file_path = filedialog.askdirectory()
	
	return file_path


# File moving functions

def move_photos():
	
	print("move photos reached")

def move_audio():
	print("move audio reached")

def move_video():
	
	print("Something")




	



if __name__ == '__main__':
	
	welcome()
	
	actions_dialog()
	
	action  = input()
	
	
	if action.isnumeric() and action.isnumeric() in range(1,7) and len(action) == 1:
		
		action = int(action)
		
		# Define a dictionary to map action values to corresponding functions
		
		case_handlers = {1: move_photos,
		                 2: move_audio,
		                 3: move_video
		}
		
		# Get the appropriate handler function based on the action value

		handler = case_handlers.get(action)
		
		handler()  # Call the handler function
		
		
		
	
	print("Select the action")