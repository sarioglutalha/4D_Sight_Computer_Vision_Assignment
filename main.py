
import numpy as np
from PIL import Image

big_path = input("Please enter the path to the images.\nBig Image Path: ")
sml_path = input("Small Image Path: ")

sml_img = Image.open(sml_path)
big_img = Image.open(big_path)

big = np.asarray(big_img)
bigY, bigX  = big.shape[:2]

for i in range(0,271,90):
	print(f"Trying find match with {i} degrees version.")

	sml = np.asarray(sml_img)
	smlY, smlX = sml.shape[:2]

	match = [[x1,y1,x1 + smlX,y1 + smlY] for x1 in range(0, bigX - smlX + 1) for y1 in range(0, bigY - smlY + 1) if (big[y1:y1 + smlY, x1:x1 + smlX] == sml).all()]

	if not match:
		sml_img = sml_img.rotate(90)
		print(f"No matches found.")
	else:
		x1,y1,x2,y2 = match[0][:]
		print(f"matched:\nx1: {x1}\ny1: {y1}\nx2: {x2}\ny2: {y2}")
		break