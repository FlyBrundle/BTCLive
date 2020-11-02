# BTCLive

## About
As part of my independent module for learning Matplotlib,  I wanted to extract stock data and display it on a plot. Yahoo discontinued their finance app, so rather than stock data 
I decided to use Bitcoin price data from coinmarketcap instead. It is drawn using the read_html() and displaying the specific blocks that are necessary for the data I was looking for.

My intention over time is to create something resembling the CMC graph as much as possible, integrated with multiple currencies that will output to a CSV. Hopefully this will automate
the process of checking prices, and will also generate the specific information I am looking for.

TODO: Include functionality for multiple coins, add threading, possibly integrate with flask

## How to Use
* Run the writecsv file first
* Run the btclive.py file second
