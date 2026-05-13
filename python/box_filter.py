import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = img.astype(np.float32)

# Kernel size
k = 3
kernel = np.ones((k, k)) / (k * k)

h, w, c = img.shape
output = np.zeros_like(img)

pad = k // 2

# Apply filter channel-wise
for channel in range(3):
    padded = np.pad(img[:, :, channel], pad, mode='edge')

    for i in range(h):
        for j in range(w):
            window = padded[i:i+k, j:j+k]
            output[i, j, channel] = np.sum(window * kernel)

# Clip and convert
output = np.clip(output, 0, 255).astype(np.uint8)

# Display
plt.subplot(121)
plt.imshow(img.astype(np.uint8))
plt.title("Original")

plt.subplot(122)
plt.imshow(output)
plt.title("Filtered")

plt.show()