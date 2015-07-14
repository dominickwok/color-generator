import urllib2
from bs4 import BeautifulSoup

def run_color_generator(input_hex, num_shades):
    """ generates a color shade list based on a base color (input_hex) and
    number of shades (num_shades)
    """
    # validate user input
    if not validate_input_hex(input_hex):
        return "error: invalid hex code. please input valid hex code of form #xxxxxx"
    if not validate_num_shades(num_shades):
        return "error: invalid number of shades. please input a positive inger"
    if num_shades==1:
        return [input_hex]
    # generate the shades
    return output_shades(input_hex, num_shades)


def validate_input_hex(input_hex):
    """ return true if user input hex is valid hex code, false otherwise
    """
    try:
        check = str(input_hex)
        if input_hex[0] == '#':
            input_hex = input_hex[1:] # if there is a # in front of hex code, strip it
        check = int(input_hex, 16)
        return True
    except:
        return False


def validate_num_shades(num_shades):
    """ return true if user input shade is a positive whole integer, false otherwise
    """
    try:
        check = int(num_shades)
    except ValueError:
        return False
    else:
        if num_shades < 1 or num_shades%1 > 0:
            return False
    return True


def hex_to_rgb(value):
    """ from http://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa
        converts hex code to rgb value
    """
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(rgb):
    """ from http://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa
        converts rgb value to hex code
    """
    return '#%02x%02x%02x' % rgb


def output_shades(base_hex, num_shades):
    """ this function takes the base hex code and creates number of shades
        according to that hex code 
    """
    # convert base_hex to RGB
    base_rgb = hex_to_rgb(base_hex)
    # figure out which of R, G, or B is largest
    val_max = float(max(base_rgb))
    pos_max = base_rgb.index(val_max)
    # create tuple with scalars
    scale_rgb = tuple(val/val_max for val in base_rgb)
    """ 
    {{READABLE VERSION}} create list of values for pos_max
    for i in range(0, num_shades):
        val_max = (50 + i*200/(num_shades-1)) # increment the val_max from 50 to 250
        print rgb_to_hex(tuple(int(scale*val_max) for scale in scale_rgb))
    """
    # {{UNREADABLE VERSION}} create list of values for pos_max
    return [rgb_to_hex( \
                tuple( \
                    int(scale*(50+i*200/(num_shades-1)))\
                for scale in scale_rgb) \
            ) for i in range(0, num_shades)]