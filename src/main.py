import os
from PIL import Image

def rename_file(filename, new_filename):
	if len(new_filename.split(".")) >= 2:
		os.rename(f"input/{filename}", f"output/{new_filename}")
	else:
		print(f"extension missing: {new_filename}")

def resize_file(filename, width, height):
	with Image.open(f"input/{filename}") as image:
		image.resize((width, height)).save(f"output/{filename}")