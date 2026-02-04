from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Charge une image pour afficher son format
    et le contenu de ses pixels en RGB
    on return un NumPy array car array n'existe pas en python"""
    try:
        assert path != "", "Path to img must not be empty"
        assert path.lower().endswith((".jpg", ".jpeg")), (
            "Img must be in jpg or jpeg format"
        )
        img = Image.open(path).convert("RGB")
        array = np.array(img)
        print(f"The shape of image is: {array.shape}")
        return array
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return
    except Exception as error:
        print(f"Error: {error}")
        return

# =============== TESTTTTTTTTTTTSSSSSSS ===============
# from load_image import ft_load

# def main():
#     print(ft_load("landscape.jpg"))

# if __name__ == "__main__":
#     main()
