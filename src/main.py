import os

def rename_file(filename, new_filename):
	if len(new_filename.split(".")) >= 2:
		os.rename(f"input/{filename}", f"output/{new_filename}")
	else:
		print(f"extension missing: {new_filename}")