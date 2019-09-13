# Get the projected total sales.
# 9/1/2019
# CTI-110 P2T1 - Sales Prediction
# Derik Graves
total_sales = float (input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profits.
print(' The profit is $', format(profit, ',.2f'))
