name = input("enter your name:")
my_lists ='''
Sugar     60/kg
Oil       100/ltr
Rice      60/kg
Dal       150/kg
Salt      50/kg
Turmaric  150/kg
Mirchi    120/kg 
'''

price = 0
pricelst =[]
totalprice  = 0
finalprice = 0
itemlst = []
quantitylst = []
pricelist =[]
# rates for items
items = {'sugar':60,'oil':100, 'rice':60, 'dal':150, 'salt':50, 'turmaric':150, 'mirchi':120}
choice =int(input("for list of items press 1:"))
if choice == 1:
    print(my_lists)
for i in range(len(items)):
    x =int(input("if you want to buy press 1 otherwise press 2 for exit:"))
    if x == 2:
        break
    if x == 1:
        item = input("enter your item names:")
        quantity = int(input("enter your quantity:"))
        if item in items.keys():
            price = quantity*(items[item]) 
            pricelst.append((item,quantity,items,price))
            totalprice += price 
            itemlst.append(item)
            quantitylst.append(quantity)
            pricelist.append(price)
            gst = (totalprice*5/100)
            finalamount = gst+totalprice
        else:
            print("item not available")
    else:
        print("entered wrong no")

    y =input("can i  bill the my items yes or no:")
    if y == 'yes':
        pass
        if finalamount != 0:
            print("="*20, "nagendra super market","="*20)
            print("="*20, "bangalure","="*20)
            print("Name:",name)
            print("-"*50)
            print("sno",""*3,"items",""*5, "quantity",""*5, "price")

            for i in range(len(pricelst)): 
                print(i, 3*'',5*'',itemlst[i], 5*'',quantitylst[i],    5*'', pricelist[i])
        print(50*'-') 
        print(50*'',"Totalprice:","Rs",totalprice)
        print("gst amount",50*'',"Rs",gst)
        print(50*'-')
        print(30*' ', "Finalamount","Rs",finalamount)
        print(50*'-')
        print(50*'',"Thanks For Shopping")
        print(50*'-')       


