import numpy as np
import matplotlib.image as pimg
from scipy.ndimage.filters import convolve
from tqdm import trange

from util import load_yaml, show_energy


def energy_function(img):
    # You should finish this function!
    # function: given an image, the function should return
    #           the energy map for the image.
    # input: img [w*h*3]
    # output: energy_map [w*h]
    pass


def dp(img_e):
    # You should finish this function!
    # function: given am energy map, the function should 
    #           return a road with the lowest energy.
    # input: img_e [w*h]
    # output: a road (you can design the data structure by yourself)
    pass


def delete_one_road(road, img):
    # You should finish this function!
    # function: given an image and the road with the lowest energy, 
    #           the function should return a new image after deleting 
    #           the road.
    # input: road
    #        img [w*h*3]
    # output: img [(w-1)*h*3]
    pass


def add_road():
    # Optional Task
    # You can design the input and output by yourself
    pass


def func(img, scale, direction):
    # function: given an image and the parameters, the function represents
    #           the process of the seam carving algorithm

    r, c, _ = img.shape
    if scale < 1:
        total = int(c * (1 - scale))
        for i in trange(total):
            energy_map = energy_function(img)
            road = dp(energy_map)
            img = delete_one_road(road, img)

    else:
        # Optional Task
        # You can design the process by yourself
        pass

    return img


def main():
    config = load_yaml("./config.yml")

    direction = config["direction"]
    s = config["scale"]
    image = pimg.imread(config["img_path"])

    energy_map = energy_function(image)
    img_done = func(image, s, direction)

    show_energy(image, energy_map, img_done)
    # pimg.imsave(config["output_path"], img_done)  # save the output image


if __name__ == "__main__":
    main()