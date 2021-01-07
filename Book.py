# This order book project is completely CUI (Charater User Interface)
# All the written code is wrote by me only without taking reference
# I have little knowledge of Stock Market so I done this project without help, with my own knowledge
# Read every line carefully before Test this project 


from datetime import datetime #for showing date
import random

# Defined Dictionary
order_book = {
    'order_sell':{
        45.20:456512,
        45.25:46324,
        45.30:7845
    },
    'order_buy':{
        25.10:4578,
        25.15:4545,
        25.20:4512
    },
}

# Type of order
def orderInput():
    return input()

# Check available limit price for buy
def bcheckLimitPrice(order_bookFun, limitPr):
    if limitPr in order_bookFun.keys():
        afterbuy = order_book['order_sell'][limitPr]
        return afterbuy
    else:
        print('Your limit price is not available...')
        print('Would you like to try again press \"Y\" for yes and \"N\" for Exit....')
        ch = orderInput()
        if (ch == 'y' or ch =='Y'):
            exit()
        else:
            buyLimitOrder()

# Check available limit price for sell
def checkLimitPrice(order_bookFun, limitPr):
    if limitPr in order_bookFun.keys():
        afterSell = order_book['order_buy'][limitPr]
        return afterSell
    else:
        print('Your limit price is not available...')
        print('Would you like to try again press \"Y\" for yes and \"N\" for Exit....')
        ch = orderInput()
        if (ch == 'y' or ch =='Y'):
            exit()
        else:
            sellLimitOrder()
# Add stock for buy
def baddStock():
    nextbuyPrice = min(order_book['order_sell'].keys())
    nextbuyPrice = nextbuyPrice - 1
    nextbuyStock = random.randrange(4500,5000)
    order_book['order_sell'][nextbuyPrice] = nextbuyStock

# Add stock for Sell
def addStock():
    nextSellPrice = max(order_book['order_buy'].keys())
    nextSellPrice += 1
    nextSellStock = random.randrange(4500,5000)
    order_book['order_buy'][nextSellPrice] = nextSellStock

# Check less than zero during buy
def blessThanZeroStock(temp):
    for i in range(len(order_book['order_sell'])):
        nxtbuyPrice = max(order_book['order_sell'].keys())
        nxtAfterStock = order_book['order_sell'][nxtbuyPrice]
        nxtAfterStock = nxtAfterStock + temp
        if (nxtAfterStock >= 0):
            temp = nxtAfterStock
            if (temp == 0):
                order_book.pop(['order_sell'][nxtbuyPrice])
                print(order_book['order_sell'])
                # calling add function to add
                baddStock()
                flag = 1
            else:
                order_book['order_sell'][nxtbuyPrice] = temp
        elif (nxtAfterStock < 0):
            order_book.pop(['order_sell'][nxtbuyPrice])
            baddStock()
            continue
        else:
            break
        if (flag == 1):
            break
        else:
            baddStock()

# Check less than zero during Sell
def lessThanZeroStock(temp):
    for i in range(len(order_book['order_buy'])):
        nxtSellPrice = min(order_book['order_buy'].keys())
        nxtAfterStock = order_book['order_buy'][nxtSellPrice]
        nxtAfterStock = nxtAfterStock - temp
        if (nxtAfterStock >= 0):
            temp = nxtAfterStock
            if (temp == 0):
                order_book.pop(['order_buy'][nxtSellPrice])
                print(order_book['order_buy'])
                # calling add function to add
                addStock()
                flag = 1
            else:
                order_book['order_buy'][nxtSellPrice] = temp
        elif (nxtAfterStock < 0):
            order_book.pop(['order_buy'][nxtSellPrice])
            addStock()
            continue
        else:
            break
        if (flag == 1):
            break
        else:
            addStock()

# Sell at Market Order
def sellMarketOrder():
    print('How many stock you want to sell in market order...')
    stockItem = int(orderInput())
    sellPrice = min(order_book['order_buy'].keys())
    afterSell = order_book['order_buy'][sellPrice]
    if (afterSell-stockItem >= 0):
        temp = afterSell-stockItem
        if (temp == 0):
            order_book.pop(['order_buy'][sellPrice])
            addStock()
        else:
            order_book['order_buy'][sellPrice] = temp
        print(order_book['order_buy'])
    elif (afterSell-stockItem < 0):
        temp = afterSell-stockItem
        order_book.pop(['order_buy'][sellPrice])
        addStock()
        lessThanZeroStock(temp)
    else:
        print('Stock Item not Valid...')
        print('Would you like to try again press \"Y\" for yes and \"N\" for Exit....')
        ch = orderInput()
        if (ch == 'y' or ch =='Y'):
            exit()
        else:
            sellMarketOrder()

# Sell at Limit Order
def sellLimitOrder():
    print('How mucch limit price you want to set for sell your stock....')
    stockPrice = int(orderInput())
    print('How much stock you want to sell...?')
    stockItem = int(orderInput())
    afterSell = checkLimitPrice(order_book['order_buy'], stockPrice)
    if (afterSell-stockItem >= 0):
        temp = afterSell-stockItem
        if (temp == 0):
            order_book.pop(['order_buy'][stockPrice])
            addStock()
        else:
            order_book['order_buy'][stockPrice] = temp
        print(order_book['order_buy'])
    elif (afterSell-stockItem < 0):
        temp = afterSell-stockItem
        order_book.pop(['order_buy'][stockPrice])
        addStock()
        print("Your {temp} stock can not be sell because you crossed your limit stock")
        print('Would you like to try again press \"Y\" for yes and \"N\" for Exit....')
        ch = orderInput()
        if (ch == 'y' or ch =='Y'):
            sellLimitOrder()
        else:
            exit()
    else:
        print('Stock Item not Valid...')
        print('Would you like to try again press \"Y\" for yes and \"N\" for Exit....')
        ch = orderInput()
        if (ch == 'y' or ch =='Y'):
            sellLimitOrder()
        else:
            exit()

# Sell at Stop Order
def sellStopOrder():
    print('How much stop price you want to set for sell your stock....')
    sellPrice = int(orderInput())
    print('How much stock you want to sell...?')
    stockItem = int(orderInput())
    if (order_book['order_buy'][sellPrice]):
        afterSell = order_book['order_buy'][sellPrice]
        if (afterSell-stockItem >= 0):
            temp = afterSell-stockItem
            if (temp == 0):
                order_book.pop(['order_buy'][sellPrice])
                addStock()
            else:
                order_book['order_buy'][sellPrice] = temp
            print(order_book['order_buy'])
        elif (afterSell-stockItem < 0):
            temp = afterSell-stockItem
            order_book.pop(['order_buy'][sellPrice])
            addStock()
            lessThanZeroStock(temp)
        else:
            print('Stock Item not Valid...')
            print('Would you like to try again press \"Y\" for yes and \"N\" for Exit....')
            ch = orderInput()
            if (ch == 'y' or ch =='Y'):
                sellStopOrder()
            else:
                exit()
    else:
        print('Your stock will be sell at this price {sellPrice} /-')

# Buy at Market Order
def buyMarketOrder():
    print('How many stock you want to buy in market order...')
    stockItem = int(orderInput())
    buyPrice = max(order_book['order_sell'].keys())
    afterbuy = order_book['order_sell'][buyPrice]
    if (afterbuy-stockItem >= 0):
        temp = afterbuy - stockItem
        if (temp == 0):
            order_book.pop(['order_sell'][buyPrice])
            baddStock()
        else:
            order_book['order_sell'][buyPrice] = temp
        print(order_book['order_sell'])
    elif (afterbuy - stockItem < 0):
        temp = afterbuy - stockItem
        order_book.pop(['order_sell'][buyPrice])
        baddStock()
        blessThanZeroStock(temp)
    else:
        print('Stock Item not Valid...')
        print('Would you like to try again press \"Y\" for yes and \"N\" for Exit....')
        ch = orderInput()
        if (ch == 'y' or ch =='Y'):
            exit()
        else:
            buyMarketOrder()

# Buy at Limit Order
def buyLimitOrder():
    print('How mucch limit price you want to set for buy your stock....')
    stockPrice = int(orderInput())
    print('How much stock you want to buy...?')
    stockItem = int(orderInput())
    afterbuy = checkLimitPrice(order_book['order_sell'], stockPrice)
    if (afterbuy - stockItem >= 0):
        temp = afterbuy - stockItem
        if (temp == 0):
            order_book.pop(['order_sell'][stockPrice])
            baddStock()
        else:
            order_book['order_sell'][stockPrice] = temp
        print(order_book['order_sell'])
    elif (afterbuy - stockItem < 0):
        temp = afterbuy - stockItem
        order_book.pop(['order_sell'][stockPrice])
        baddStock()
        print("Your {temp} stock can not be buy because you crossed your limit stock")
        print('Would you like to try again press \"Y\" for yes and \"N\" for Exit....')
        ch = orderInput()
        if (ch == 'y' or ch =='Y'):
            buyLimitOrder()
        else:
            exit()
    else:
        print('Stock Item not Valid...')
        print('Would you like to try again press \"Y\" for yes and \"N\" for Exit....')
        ch = orderInput()
        if (ch == 'y' or ch =='Y'):
            buyLimitOrder()
        else:
            exit()

# Buy at Stop Order
def buyStopOrder():
    print('How much stop price you want to set for buy your stock....')
    buyPrice = int(orderInput())
    print('How much stock you want to buy...?')
    stockItem = int(orderInput())
    if (order_book['order_sell'][buyPrice]):
        afterbuy = order_book['order_sell'][buyPrice]
        if (afterbuy - stockItem >= 0):
            temp = afterbuy - stockItem
            if (temp == 0):
                order_book.pop(['order_sell'][buyPrice])
                baddStock()
            else:
                order_book['order_sell'][buyPrice] = temp
            print(order_book['order_sell'])
        elif (afterbuy - stockItem < 0):
            temp = afterbuy - stockItem
            order_book.pop(['order_sell'][buyPrice])
            baddStock()
            blessThanZeroStock(temp)
        else:
            print('Stock Item not Valid...')
            print('Would you like to try again press \"Y\" for yes and \"N\" for Exit....')
            ch = orderInput()
            if (ch == 'y' or ch =='Y'):
                buyStopOrder()
            else:
                exit()
    else:
        print('Your stock will be buy at this price {buyPrice} /-')

# Asking for order type
def orderType():
    print('What type of order you want...?')
    choice = input('For Market Order press M... \n For Limit Order press L... \n For Stop Order press S...')
    return choice

tym = datetime.now()
exact_time = tym.strftime("%H:%M:%S")
print('Current time is ',exact_time)
print('What do you want...?')
print('Press S for sell and B for buy...')
user_want = input()

if (user_want=='s' or user_want=='S'):
    print('You selected for Sell')
    c = orderType()
    if (c=='m' or c=='M'):
        sellMarketOrder()
    elif (c=='L' or c=='l'):
        sellLimitOrder()
    elif (c=='S' or c=='s'):
        sellStopOrder()
    else:
        print("You have choosen a wrong option...")
        print("Try Again...")
        exit()

elif (user_want=='b' or user_want=='B'):
    print('You selected for Buy')
    c = orderType()
    if (c=='m' or c=='M'):
        buyMarketOrder()
    elif (c=='L' or c=='l'):
        buyLimitOrder()
    elif (c=='S' or c=='s'):
        buyStopOrder()
    else:
        print("You have choosen a wrong option...")
        print("Try Again...")
        exit()
        
else:
    print("You Entered a illigel character...")
    exit('')