import numpy as np
import cv2
import os
import pandas as pd

IMG_DIR = 'set5'

data = []

for img_name in os.listdir(IMG_DIR):
    img_path = os.path.join(IMG_DIR, img_name)
    img_array = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    if img_array is not None:
        img_array = img_array.flatten()
        data.append(img_array)

data = np.array(data, dtype=np.uint8)

# Calculate the number of pixel columns based on the flattened image arrays
num_pixel_columns = data.shape[1]

# Create the header with the correct number of pixel columns
header = ",".join([f"pixel_{i}" for i in range(num_pixel_columns)])

# Save the data with the corrected header
np.savetxt('output.csv', data, delimiter=',', header=header, comments='', fmt='%d')

print("CSV generado exitosamente.")

print(pd.read_csv("output.csv"))
