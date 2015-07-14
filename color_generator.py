import urllib2
from bs4 import BeautifulSoup

def hex_shades(input_hex, num_shades):
    """ generates a color shade list based on a base color (input_hex) and number of shades (num_shades)

        this code accomplishes this by taking a subset of values from http://www.w3schools.com/tags/ref_colorpicker.asp?colorhex=#FFFFFF

    arguments:
        input_hex: must be a hexacode string value starting with a #
        num_shades: the number of shades you want to generate based on base_hex, must be an int in [LB, UB]
    functions:
        shade_bounds: used to calculate the bounds 
    output:
        output_shades: list of shades with length = num_shades
    """
   
    # validate user input
    assert validate_input_hex(input_hex), "error: invalid hex code. please input valid hex code of form #xxxxxx"
    assert validate_num_shades(num_shades), "error: invalid number of shades. please input a positive inger" 
   # return method_1(input_hex, num_shades);


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
        if num_shades < 0 or num_shades%1 > 0:
            return False
    return True

""" next two functions are from http://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa"""
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb