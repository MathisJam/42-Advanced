from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    '''Programme qui permet de tourner l'image
    - On charge l'image avec ft_load qui gere les erreurs
    - On prepare les dimensions du crop
    - On crop l'image avec ces dimensions
    - On affiche la shape et l'array du cropped
    - On squeeze pour supprimer le dernier axe (canal rgb)
    - On inverse les lignes x et y
    - On recreer une array avec ces new line
    - On print la shape et l'array du transposed
    - On affiche l'image en grey'''
    try:
        array = ft_load("animal.jpeg")
        assert array is not None, "Image cannot be loaded"

        img = Image.fromarray(array)

        crop_size = 400
        w, h = img.size
        left = (w - crop_size) // 2 + 100
        top = (h - crop_size) // 2 - 100
        right = left + crop_size
        bottom = top + crop_size

        cropped_img = img.crop((left, top, right, bottom))
        cropped_arr = np.asarray(cropped_img.convert("L"))
        cropped_arr = cropped_arr[:, :, None]

        print(
            f"The shape of image is: \
                {cropped_arr.shape} or {cropped_arr.squeeze().shape}"
        )
        print(cropped_arr)

        arr = cropped_arr.squeeze()
        transposed_arr = [[arr[j][i] for j in range(len(arr))]
                          for i in range(len(arr[0]))]
        transposed_arr = np.array(transposed_arr)
        print(f"New shape after Transpose: {transposed_arr.shape}")
        print(transposed_arr)

        plt.imshow(transposed_arr, cmap="gray")
        plt.title("PEDRO PEDRO PEDRO")
        plt.show()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: interruption signal caught")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
