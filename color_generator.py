import urllib2
from bs4 import BeautifulSoup

def hex_shades(input_hex, num_shades):
    """ generates a color shade list based on a base color (input_hex) and number of shades (num_shades)

        this code accomplishes this by taking a subset of values from http://www.w3schools.com/tags/ref_colorpicker.asp?colorhex=#FFFFFF

    arguments:
        input_hex: must be a hexacode string value starting with a #
        num_shades: the number of shades you want to generate based on base_hex, must be an int in [LB, UB]
    output:
        output_shades: list of shades with length = num_shades
    """
    # character limits
    bounds = {'lower': 1, 'upper': 19}

    # validate that base hex is a valid hex string
    try:
        check = str(input_hex)
        if input_hex[0] == '#':
            input_hex = input_hex[1:] # if there is a # in front of hex code, strip it
        check = int(input_hex, 16)
    except:
        return 'error: invalid input_hex'

    # validate that num_shades is a valid int > 0
    try:
        check = int(num_shades)
    except ValueError:
        return 'error: invalid num_shades'
    else:
        if num_shades < bounds['lower'] or num_shades > bounds['upper']:
            return 'error: num_shades must be between '+str(bounds['lower'])+' and '+str(bounds['upper'])
        elif num_shades%1 > 0:
            return 'error: num_shades must be a round integer'

    # construct URL to call 
    url = "http://www.w3schools.com/tags/http_colorshades.asp?colorhex="+input_hex

    # call URL with BS4 and parse out color shades
    soup = BeautifulSoup(urllib2.urlopen(url).read())

    # read in full shade list    
    output_shades = [unicode(tag.string) for tag in soup.find_all('td', {'class':'colorshadetxt'})]

    # select subset of shades according to num_shades
    index_out = shade_bounds(num_shades)

    # return subsetted shade list to user
    return output_shades[index_out[0]:index_out[1]:index_out[2]]
    
def shade_bounds(num_shades):
    """ 'intelligently' figures out which shades in shade list to return based on num_shades

        assumes that the number of shades is = 19, based on w3 color generator
    """
    # case 1: num_shades is even and greater than 10
    if num_shades > 10 and num_shades%2==0 :
        start_index = (20-num_shades)/2
        return [start_index,start_index+num_shades,1]
    # case 2: num shades is odd and greater than 10
    elif num_shades > 10 :
        start_index = int(0.5+(20-num_shades)/2)+1
        return [start_index,start_index+num_shades,1]
    # case 3: num shades is even and less than or equal to 10
    elif num_shades%2==0 :
        start_index = 10 - num_shades+1
        return [start_index,start_index + (2*num_shades)-1,2]
    # case 4: num shades is odd and less than or equal to 10
    else :
        start_index = 10 - num_shades+1
        return [start_index,start_index + 2*num_shades,2]
