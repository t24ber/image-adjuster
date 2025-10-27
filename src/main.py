import os
from PIL import Image


def rename_file(filename, new_filename):
	os.rename(f"input/{filename}", f"output/{new_filename}")
	print(f"====> Renamed {filename} to {new_filename}")

def resize_image(filename, new_dimensions):

	with Image.open(f"input/{filename}") as image:

		if len(new_dimensions) == 2:

			width = new_dimensions[0]
			height = new_dimensions[1]

		else:

			width = new_dimensions[0]
			height = int(width * (image.height/image.width))

		image.resize((width, height)).save(f"output/{filename}")
		print(f"====> Resized {filename} to {filename}({width}, {height})")
		os.remove(f"input/{filename}")


def check_extension(filename):
	return filename.endswith((".jpg", ".jpeg", ".png", ".webp"))


if __name__ == "__main__":

	print("image-adjuster:\n")

	for filename in os.listdir("input"):
		if check_extension(filename):
			print(filename)

	print("\n1. rename images")
	print("2. resize images")

	mode = int(input("\nEnter number: "))

	if mode == 1:

		print("\nimage-adjuster ... rename images:\n")

		for filename in os.listdir("input"):
			if check_extension(filename):
				new_filename = f"{input(f"Rename {filename} to: ")}{os.path.splitext(filename)[1]}"
				if not new_filename.startswith("."):
					rename_file(filename, new_filename)

		print("\nDone!")

	elif mode == 2:

		print("\nimage-adjuster ... resize images:\n")

		for filename in os.listdir("input"):
			if check_extension(filename):
				with Image.open(f"input/{filename}") as image:
					new_dimensions = f"{input(f"Resize {filename}({image.width}, {image.height}) to: ")}"
					if new_dimensions != "":
						new_dimensions = [int(new_dimension) for new_dimension in new_dimensions.split(",")]
						resize_image(filename, new_dimensions)

		print("\nDone!")

	else:
		print(f"{mode} wasn't a mode")