import yaml
import matplotlib.pyplot as plt

def load_yaml(file_path, verbose=True):
    with open(file_path, "r") as f:
        yml_file = yaml.load(f, Loader=yaml.SafeLoader)
    if verbose:
        print("Load yaml file from {}".format(file_path))
    return yml_file

def show_energy(img, img_e, img_f):

    plt.rcParams['figure.figsize'] = (15, 12)
    plt.rcParams['image.interpolation'] = 'nearest'
    plt.rcParams['image.cmap'] = 'gray'

    fig = plt.gcf()
    fig.set_size_inches(12, 5)

    plt.title('Energy_map')
    plt.subplot(131)
    plt.imshow(img)
    plt.subplot(132)
    plt.imshow(img_e)
    plt.subplot(133)
    plt.imshow(img_f)
    plt.show()