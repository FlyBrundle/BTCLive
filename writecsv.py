import pandas as pd
from time import sleep
import csv
import os

x = 0
fieldnames = ['ind', 'price']

def write_csv():
    '''
    Takes the data from coin market cap and writes it to a csv file
    '''
    x = 0
    # if the file is empty, write headers
    with open('btc_data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        csv_writer.writeheader()

    while True:
        # if the file is not empty, simply append to the end of it
        with open('btc_data.csv', 'a') as csv_file:
            df = pd.read_html('https://coinmarketcap.com/currencies/bitcoin/')
            x += 1
            # take the price from the parsed html and strip all the unnecessary characters
            # converting it to a string
            price = df[0][1][0]
            price_convert = int(float(price.strip(' USD').strip('$').replace(',', '')))
            
            csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
            # create a dictionary of information to append
            info = {'ind' : x, 'price' : price_convert}
            csv_writer.writerow(info)
            # we want to make sure it wrote the data
            print(type(price_convert))

        # this is an arbitrary amount. We ideally want to set this for the
        # amount of time it takes CMC to update.
        sleep(20)
        
write_csv()
