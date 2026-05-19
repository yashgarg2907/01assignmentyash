cost_price = int(input("Enter cost price : "))
selling_price = int(input("Enter selling price : "))
if selling_price > cost_price:
    profit = (selling_price-cost_price)
    profit_percentage = (profit/cost_price)*100
    print("profit =", profit)
    print("profit_percentage =", profit_percentage)
else:
    selling_price < cost_price
    loss = cost_price - selling_price
    loss_percentage = (loss/cost_price)*100
    print("loss =" , loss)
    print("loss_percentage =", loss_percentage)

