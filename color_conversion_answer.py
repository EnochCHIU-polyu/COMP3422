import cv2
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    original_img = cv2.imread('./example_image.jpeg')
    original_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)

    # TODO: now the image value is in range (0, 255), normalize the value into range (0, 1)
    normalized_img = original_img / 255

    # TODO: convert the red-green-blue format into cyan-magenta-yellow
    cmy_img = 1 - normalized_img

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(normalized_img)
    axs[0].set_title('RGB image')
    axs[1].imshow(cmy_img)
    axs[1].set_title('CMY image')
    plt.show()
