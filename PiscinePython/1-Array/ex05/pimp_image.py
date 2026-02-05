import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    '''Inverse la couleur de l'image
    en gardant la meme shape'''

    inv_arr = 255 - array
    plt.imshow(inv_arr)
    try:
        plt.show()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: interruption signal caught")
    return inv_arr


def ft_red(array) -> np.ndarray:
    '''Change la couleur de l'image
    en rouge en gardant la meme shape
    - On met juste canal G et B a 0'''
    red = array.copy()
    red[:, :, 1] = 0
    red[:, :, 2] = 0

    # print(f"The shape of image is: {red.shape}")
    # print(red)
    plt.imshow(red)
    try:
        plt.show()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: interruption signal caught")
    return red


def ft_green(array) -> np.ndarray:
    '''Change la couleur de l'image
    en vert en gardant la meme shape
    - On met juste canal R et B a 0'''
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0

    # print(f"The shape of image is: {green.shape}")
    # print(green)
    plt.imshow(green)
    try:
        plt.show()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: interruption signal caught")
    return green


def ft_blue(array) -> np.ndarray:
    '''Change la couleur de l'image
    en bleu en gardant la meme shape
    - On met juste canal R et G a 0'''
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0

    # print(f"The shape of image is: {blue.shape}")
    # print(blue)
    plt.imshow(blue)
    try:
        plt.show()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: interruption signal caught")
    return blue


def ft_grey(array) -> np.ndarray:
    '''Change la couleur de l'image
    en gris en gardant la meme shape
    - Les pixels sont en uint8 de base (0 a 255)
    - On passe en int le temps de faire addition + div entiere
    - On repasse en uint8 apres'''
    grey = array.copy()

    avg = ((array[:, :, 0].astype(int) +
           array[:, :, 1].astype(int) +
           array[:, :, 2].astype(int)) // 3).astype(np.uint8)

    grey[:, :, 0] = avg
    grey[:, :, 1] = avg
    grey[:, :, 2] = avg

    # print(f"The shape of image is: {grey.shape}")
    # print(grey)
    plt.imshow(grey)
    try:
        plt.show()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: interruption signal caught")
    return grey

# =============== LES TESSSSSSSSSSSSTTTTTTTTTTTTSSSSSSSSS ================
# from load_image import ft_load
# def main():
#     array = ft_load("landscape.jpg")
#     if array is None:
#         exit()
#     ft_invert(array)
#     ft_red(array)
#     ft_green(array)
#     ft_blue(array)
#     ft_grey(array)
#     print(ft_invert.__doc__)

# if __name__ == "__main__":
#     main()
