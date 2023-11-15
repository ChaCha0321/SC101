"""
File: blur.py
Name:CHA_CHU WAN CHI
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original image
    :return: average RBG values of a pixel's nearest neighbors
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            avg_r = 0
            avg_g = 0
            avg_b = 0
            time = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if img.width > x+i >= 0:
                        if img.height > y+j >= 0:
                            # if pixel next to the middle pixel is in the picture, 0~img.width-1 and 0~img.height-1
                            img_next = img.get_pixel(x+i, y+j)
                            avg_r += img_next.red
                            avg_g += img_next.green
                            avg_b += img_next.blue
                            time += 1
            avg_r = avg_r // time
            avg_g = avg_g // time
            avg_b = avg_b // time
            new_img_pixel = new_img.get_pixel(x, y)
            new_img_pixel.red = avg_r
            new_img_pixel.green = avg_g
            new_img_pixel.blue = avg_b
    return new_img


def main():
    """
    Make a blurred image, you can change the times to make image more blurry
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
