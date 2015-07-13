#import bsf from https://pypi.python.org/pypi/beautifulsoup4/4.3.2
#install Aptana if you do not have a python interpreter http://www.aptana.com/products/studio3/download.html (other products work as well)

import urllib2
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


def hex_shades(input_hex, num_shades):
    """ generates a color shade list based on a base color (input_hex) and number of shades (num_shades)

        this code accomplishes this by taking a subset of values from http://www.w3schools.com/tags/ref_colorpicker.asp?colorhex=#FFFFFF

    arguments:
        input_hex: must be a hexacode value starting with a #
        num_shades: the number of shades you want to generate based on base_hex, must be an int in [LB, UB]
    """
    # character limits
    LB = 1
    UB = 20

    # if there is a # in front of hex code, strip it
    if input_hex[0] == '#':
            input_hex = input_hex[1:]
       
    # validate that base hex is a valid hex
    try:
         check = int(input_hex, 16)
    except:
        return 'error: invalid input_hex'

    # validate that num_shades is a valid int > 0
    try:
        check = int(num_shades)
    except ValueError:
        return 'error: invalid num_shades'
    else:
        if num_shades < LB or num_shades > UB:
            return 'error: num_shades must be between '+str(LB)+' and '+str(UB)
        elif num_shades%1 > 0:
            return 'error: num_shades must be a round integer'



    # construct URL to call 

    # call URL and parse out color shades

    # construct shade list according to num_shades

    # return shade list


    # set the beginning and ending day, month, and year of scraper
#    start_date='2014/7/7'
#    end_year='2015'
#    end_month='1'
#    end_day='1'

    # note, this will only update for most recent data; there is a limnit to what can be scraped
    #open airport codes and read this is a file of airport codes one needs data for
#    df = pd.read_csv("11_airportcodes2.csv")

#    df.url = 'http://www.wunderground.com/history/airport/'+df.airport_code+'/'+start_date+'/CustomHistory.html?'
#    df.url += 'dayend='+end_day+'&monthend='+end_month+'&yearend='+end_year+'&req_city=NA&req_state=NA&req_statename=NA&format=1'

#    data_columns=0
#    num_airports=df.shape[0]

    #for all airport codes, write and store data
 #   for i in range(num_airports):

  #      soup=BeautifulSoup(urllib2.urlopen(df.url[i]).read())   # read in url with bs4

   #     print "analyzing "+df.airport_code[i]+" ("+str(100*i/num_airports)+"%)...."            # for the user
   #     line_num=0                                      # initialize line count for url

        #for line in soup.stripped_strings:

         #   if data_columns==0:                         # if first line, then write as index
          #      index_arr=str.split(str(line),",")      # create the index array
           #     index_arr.extend(df.columns)            # with columns from input
            
            #    df4=DataFrame(index=index_arr)          # write to dataframe
             #   data_columns = data_columns+1

            #elif line_num>0:                            # else, as long as not header row, then write to dataframe
            #    data_entry=str.split(str(line),",")     # create the data entry
            #    data_entry.extend(df.ix[i])
            
             #   df4[data_columns]=Series(data_entry,index=index_arr)  # write to dataframe
              #  data_columns=data_columns+1
            
            #line_num = line_num+1;                      # either way, increment line number by 1
    
    return [input_hex, num_shades]

print hex_shades("#e94297", 5)
print hex_shades("e94297", 5)
print hex_shades("e94297", 'abc')
print hex_shades("e94297", 5.3)
print hex_shades("e94297", -5)
print hex_shades("zzzzzz", 5)