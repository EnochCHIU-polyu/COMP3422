import numpy as np
np.random.seed(233)
import matplotlib.pyplot as plt

import cv2


if __name__ == '__main__':
    original_img = cv2.imread('./example_image.jpeg')
    original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)

    # In this task, you need to find the bit plane for all the RGB channels
    # TODO: (1) initialize a zero numpy array
    bit_image = np.zeros(list(original_img.shape) + [8])

    for row in range(original_img.shape[0]):
        for col in range(original_img.shape[1]):
            for rgb in range(original_img.shape[2]):
                # TODO: (2) get the binary representation of the 8-bit color value
                binary = np.binary_repr(original_img[row, col, rgb], width=8)

                # TODO: (3) iterate through all the bit channels, assign bit values to the corresponding places
                for bit_i, bit in enumerate(binary):
                    bit_image[row, col, rgb, bit_i] = int(bit)

    # Visualization
    fig, axs = plt.subplots(4, 3, figsize=(8, 8))
    axs[0, 0].imshow(original_img)
    axs[0, 0].axis('off')
    axs[1, 0].axis('off')
    axs[2, 0].axis('off')
    axs[3, 0].axis('off')
    axs[3, 2].axis('off')

    for bit in range(8):
        axs[bit // 2, 1 + bit % 2].imshow(bit_image[..., bit])
        axs[bit // 2, 1 + bit % 2].set_title(f'Bit plane {7 - bit}')
        axs[bit // 2, 1 + bit % 2].axis('off')
    plt.show()
