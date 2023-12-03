
print("welcom to no nan bakery")

# the price of bread
prices = {
    "barbary": 2000,
    "lavash": 1500,
    "boget": 1800,
    "taftoon": 2200,
    "sangak": 2500,
}
    
def bakery():
    total_cost = 0
    while True:
        bread_type = input("what kind of bread do you want? (barbary , lavash , boget , taftoon , sangak): ")
        if bread_type in prices:
            quantity = int(input("how many bread do you want?"))
            cost = prices[bread_type] * quantity
            total_cost += cost
            print(f"the price of bread {bread_type} you {cost} $.")
        else:
            print("this bread is not available.")
        # again order
        again_order = input("do you have another order(Y/N)? ")
        if again_order.upper() == "N":

            break

        print(f"your total price",(total_cost),"$")

bakery()