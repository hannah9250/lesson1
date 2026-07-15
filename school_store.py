items = ["pencil,", "pen", "notebook","rubber", "scale"]
stock = [20,15,0,10,5]
price = [10,15,5,2,6]
available_items = [items[i] for i in range(len(items))if stock[i]>0 ]
print("items in currently in stock: ", available_items)
inventory = dict(zip(items,stock))
print(inventory)
newprice = list(map(lambda x : round(x * 1.10, 2), price))
print(newprice)
user = input("enter the item you want to buy: ")
if user not in inventory: 
    print("not available")
    exit()
if inventory[user] == 0: 
    print("sorry this item is out of stock")
    exit()
index = items.index(user)
print("PURCHASE DETAILS")
print("item name:", user)
print("available stock: ", stock[index])
print("price after 10% markup: ", newprice[index])
