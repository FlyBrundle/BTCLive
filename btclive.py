from init import *

pd.set_option('display.max_columns', 10)
plt.style.use('seaborn-bright')

index = count()
x_vals = []
y_vals = []

def axes(min_price, max_price):
    '''
    Creates a custom range for the y axis values based off the minimum
    and maximum value ranges

    Values are taken from the csv file to which we are writing

    :param min_price: minimum number for the y_ticks value range
    :param max_price: maximum number for the y_ticks value range
    '''
    step = int((max_price - min_price) / 5)
    y_tick_vals = [int(i) for i in range(min_price, max_price + 1, step)]

    return y_tick_vals

def animate(i):
    ''' Creates the matplotlib graph and animates it using FuncAnimation '''
    df = pd.read_csv(os.path.join('btc_data.csv'))
    x_vals = df['ind']
    y_vals = df['price']
    today = datetime.date.today()
    today.strftime('%m %d, %Y')
    min_price = min(y_vals) - 50
    max_price = max(y_vals) + 50
    y_tick_vals = axes(min_price, max_price)

    plt.cla()
    
    plt.plot(x_vals, y_vals, color = 'r', linewidth = 2,
            markevery = 1, label = 'BTC price ($)')

    # set up the graph
    plt.ylim(min(y_vals), max(y_vals) + 50)
    plt.yticks(y_tick_vals)
    plt.tick_params(color = 'gray', labelcolor = 'gray')
    plt.ylabel('Price ($)')
    plt.title(f'BTC price ($) trending for {today}')
    plt.legend(loc = 'upper left')
    plt.grid(axis = 'y')

# for the smoothest transition, the interval parameter needs to
# equal the same sleep time used in the write csv file
ani = FuncAnimation(plt.gcf(), func = animate, interval = 10000)

plt.tight_layout()
plt.show()
