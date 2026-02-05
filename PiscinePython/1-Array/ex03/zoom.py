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

        zoomed = array[100:500, 450:850]

        img = Image.fromarray(zoomed)
        res = np.asarray(img.convert("L"))
        res = res[:, :, None]

        print(
            f"New shape after slicing: {res.shape} or {res.squeeze().shape}"
        )
        print(zoomed)

        plt.imshow(res, cmap="gray")
        plt.title("PEDRO PEDRO PEDRO")
        plt.show()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: interruption signal caught")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
