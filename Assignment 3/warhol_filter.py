"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    image = SimpleImage(PATCH_NAME)
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    for y in range(PATCH_SIZE):
        for x in range(PATCH_SIZE):
            pix = image.get_pixel(x,y)
            do_magic(pix, x, y,final_image)



    # This is an example which should generate a pinkish patch
    patch = make_recolored_patch(1.5, 0, 1.5)
    final_image.show()

def do_magic(pix, x, y,final_image):
    for row in range(N_ROWS):
        for column in range(N_COLS):
            final_image.set_pixel((column * PATCH_SIZE) + x, (row * PATCH_SIZE) + y, pix)

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    # TODO: your code here.
    return patch

if __name__ == '__main__':
    main()