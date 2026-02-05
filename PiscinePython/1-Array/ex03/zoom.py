from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    """Programme qui load une image (load_image)
    affiche les informations et zoom (slice) dessus
    re-affiche les informations post-zoom"""
    try:
        array = ft_load("animal.jpeg")
        assert array is not None, "Image cannot be loaded"
        print(array)

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
            f"New shape after slicing: \
                {cropped_arr.shape} or {cropped_arr.squeeze().shape}"
        )
        print(cropped_arr)

        plt.imshow(cropped_arr.squeeze(), cmap="gray")
        plt.title("PEDRO PEDRO PEDRO")
        plt.show()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: interruption signal caught")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
