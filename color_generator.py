import urllib2
from bs4 import BeautifulSoup

def hex_shades(input_hex, num_shades):
    """ generates a color shade list based on a base color (input_hex) and number of shades (num_shades)

        this code accomplishes this by taking a subset of values from http://www.w3schools.com/tags/ref_colorpicker.asp?colorhex=#FFFFFF

    arguments:
        input_hex: must be a hexacode string value starting with a #
        num_shades: the number of shades you want to generate based on base_hex, must be an int in [LB, UB]
    """
    # character limits
    bounds = {'lower': 1, 'upper': 20}

    
       
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
    url = "http://www.w3schools.com/tags/ref_colorpicker.asp?colorhex="+input_hex

    # call URL with BS4 and parse out color shades
    soup = BeautifulSoup(urllib2.urlopen(url).read())

    # read in full shade list    
    output_shades = [unicode(tag.string) for tag in soup.find_all('td', {'class':'colorshadetxt'})]

    # select subset of shades according to num_shades
    if num_shades > 10 and num_shades%2==0 :
        print "num_shades is even and greater than 10"
        start_index = (20-num_shades)/2
        end_index = start_index+num_shades
        output_shades = output_shades[start_index:end_index]
    elif num_shades > 10 :
        print "num shades is odd and greater than 10"
        start_index = int(0.5+(20-num_shades)/2)
        end_index = start_index+num_shades
        output_shades = output_shades[start_index:end_index]
    elif num_shades%2==0 :
        print "num shades is even and less than or equal to 10"
    else :
        print "num shades is odd and less than or equal to 10"
    # return output shades
    return output_shades

# tests
print hex_shades("#e94297", 5)
print hex_shades("e94297", 5)
print hex_shades("e94297", 'abc')
print hex_shades("e94297", 5.3)
print hex_shades("e94297", -5)
print hex_shades("zzzzzz", 5)
print hex_shades("#", -5)
print hex_shades(123456, 4)

print len(hex_shades("e94297", 11))
print len(hex_shades("e94297", 12))
print len(hex_shades("e94297", 5))
print len(hex_shades("e94297", 6))