import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from skimage import color, exposure
from skimage.feature import hog
import matplotlib.pyplot as plt
import skimage.io
from config import Project


# HOG nhu trong Machine Learning
def get_1d_2d_hog(img):
    if len(img.shape) >= 3 and img.shape[2] == 3:
        img = color.rgb2gray(img)
    hog_image_1d, hog_image_2d = hog(img, orientations=8, pixels_per_cell=(16, 16),
                                     cells_per_block=(1, 1), visualize=True)
    return hog_image_1d, hog_image_2d
# Gia tri tra ve: hog_image_1d la vector dac trung HOG-> su dung de huan luyen mo hinh
# Gia tri tra ve: hog_image_2d la anh chua dac trung HOG(anh bieu dien chieu va do lon)-> xuat ra man hinh de quan sat

# ==================================================

# Ham chuan hoa
def get_hog(img):
    """
    :param img: the 2d rbg image, represented by numpy
    :return: list of feature
    """
    hog_image_1d, hog_image_2d = get_1d_2d_hog(img)
    hog = list(hog_image_1d)
    res = [int(x * 100) for x in hog]
    return res
# Ket qua tra ve la vector dac trung da chuan hoa


# Ham ep anh ve mang 1 chieu
def flatten(img):
    return list(img.flatten())
# Dau vao: Anh -> Dau ra: Mang 1 chieu cua anh

if __name__ == '__main__':
    img = skimage.io.imread("%s/001-nm-01-000-001.png" % Project.test_data_path)
    hog_image_1d, hog_image_2d = get_1d_2d_hog(img)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

    ax1.axis('off')
    ax1.imshow(img, cmap=plt.cm.gray)
    ax1.set_title('Input image')
    ax1.set_adjustable('box')

    # Rescale histogram for better display
    hog_image_rescaled = exposure.rescale_intensity(hog_image_2d, in_range=(0, 0.02))

    ax2.axis('off')
    ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
    ax2.set_title('Histogram of Oriented Gradients')
    ax1.set_adjustable('box')
    plt.show()