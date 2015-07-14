import urllib2
from bs4 import BeautifulSoup

def run_color_generator(input_hex, num_shades):
    """ generates a color shade list based on a base color (input_hex) and
    number of shades (num_shades)
    """
    # validate user input
    assert validate_input_hex(input_hex), "error: invalid hex code. please input valid hex code of form #xxxxxx"
    assert validate_num_shades(num_shades), "error: invalid number of shades. please input a positive inger" 
    # generate the shades
    return output_shades(input_hex, num_shades)


def validate_input_hex(input_hex):
    """ return true if user input hex is valid hex code, false otherwise """
    try:
        check = str(input_hex)
        if input_hex[0] == '#':
            input_hex = input_hex[1:] # if there is a # in front of hex code, strip it
        check = int(input_hex, 16)
        return True
    except:
        return False

def validate_num_shades(num_shades):
    """ return true if user input shade is a positive whole integer, false otherwise"""
    try:
        check = int(num_shades)
    except ValueError:
        return False
    else:
        if num_shades < 1 or num_shades%1 > 0:
            return False
    return True

""" from http://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa"""
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

""" from http://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa"""
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def output_shades(base_hex, num_shades):
    """ this function takes the base hex code and creates number of shades
        according to that hex code 
    """
    # initialize scale values
    start = 0.4
    final = 1.6
    # calculate scale range
    scale_range = [start+i*(final-start)/(num_shades-1) for i in range(0, num_shades)]
    # convert base_hex to RGB
    base_rgb = hex_to_rgb(base_hex)
    # using RGB of base_hex, calculate everything within 0.4 to 1.6 of RGB values
    for scale in scale_range:
        print rgb_to_hex(tuple(scale*rgb for rgb in base_rgb))

    # return list
    return True
