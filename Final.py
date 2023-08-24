import os
import shutil
import tkinter as tk
from tkinter import filedialog


class ItemType:
	def __init__(self, source_folder, destination_folder, valid_extensions):
		
		self.source_folder = source_folder
		self.destination_folder = destination_folder
		self.valid_extensions = valid_extensions
		self.file_list = os.listdir(source_folder)
	
	def move_files(self):
		
		for file in self.file_list:
			
			if any(file.endswith(ext) for ext in self.valid_extensions):
				
				file_full_path_source = os.path.join(self.source_folder, file)
				
				try:
					
					shutil.move(file_full_path_source, self.destination_folder)
					
					print(f"Moved '{file}' to '{self.destination_folder}'")
				
				except FileExistsError:
					
					print(f"File '{file}' already exists in '{self.destination_folder}'. Skipping.")
				
				except Exception as e:
					
					print(f"An error occurred while moving '{file}': {e}")


class Audio(ItemType):
	
	def __init__(self, source_folder, destination_folder):
		valid_extensions = ['.mp3', '.wav', '.flac']
		
		super().__init__(source_folder, destination_folder, valid_extensions)


class Video(ItemType):
	def __init__(self, source_folder, destination_folder):
		valid_extensions = ['.mp4', '.avi', '.mkv']
		
		super().__init__(source_folder, destination_folder, valid_extensions)


class Photos(ItemType):
	def __init__(self, source_folder, destination_folder):
		valid_extensions = ['.jpg', '.jpeg', '.png']
		
		super().__init__(source_folder, destination_folder, valid_extensions)


def set_directories() -> tuple:
	root = tk.Tk()
	root.withdraw()
	root.attributes("-topmost", True)
	
	print("Select the folder to be organized")
	print("")
	
	source_folder = filedialog.askdirectory()
	
	print("Select the directory for audio")
	print("")
	
	audio_directory = filedialog.askdirectory()
	
	print("Select the directory for video")
	print("")
	video_directory = filedialog.askdirectory()
	
	print("Select the directory for photos")
	print("")
	photos_directory = filedialog.askdirectory()
	
	return source_folder, audio_directory, video_directory, photos_directory


def main():
	source_folder, audio_directory, video_directory, photos_directory = set_directories()
	
	audio_handler = Audio(source_folder, audio_directory)
	video_handler = Video(source_folder, video_directory)
	photos_handler = Photos(source_folder, photos_directory)
	
	handlers = [audio_handler, video_handler, photos_handler]
	
	for handler in handlers:
		handler.move_files()


if __name__ == "__main__":
	main()
