import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def loadDataset(fileName, samples):
    x = []
    train_data = pd.read_csv(fileName)
    x = np.array(train_data.iloc[0:samples, :])  # No incluye la primera columna (pixel_0)
    return x

 
x = loadDataset("output.csv", 100)
digit = x[0]
digit_pixels = digit.reshape(28, 28)
plt.imshow(digit_pixels, cmap='gray')
plt.show()