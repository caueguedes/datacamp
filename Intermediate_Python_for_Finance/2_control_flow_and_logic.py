input_action = False
action = input_action or "Hold"  # Hold

is_trading_day = False
is_trading_day and action  # False

purchases = []
sales = []

num_purchases = len(purchases)
num_sales = len(sales)

if not (purchases or sales):
    print('No sales or purchases')