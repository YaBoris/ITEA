class Shop:

    all_sold_goods = 0

    def __init__(self, name, sold_goods=0):
        self.sold_goods = sold_goods
        self.name = name
        print("Created new store: {}". format(self.name))
        Shop.all_sold_goods += self.sold_goods

    def sold_now(self, number_of_goods):
        self.sold_goods += number_of_goods
        Shop.all_sold_goods += number_of_goods

    def get_all_sold_goods(self):
        print("The total number of all goods sold in all stores now: {}".format(Shop.all_sold_goods))


shops = []

shop1 = Shop("Berezka")
shops.append(shop1)
shop2 = Shop("Veselka", 10)
shops.append(shop2)
shop3 = Shop("Market")
shops.append(shop3)

for shop_name in shops:
    while True:
        try:
            print("Enter sold goods today in {}: ".format(shop_name.name))
            sold_goods_now = int(input())
            if sold_goods_now < 0:
                raise ValueError
            shop_name.sold_now(sold_goods_now)
            break
        except ValueError:
            print("Enter correct value for sold goods: positive integer")

Shop.get_all_sold_goods()
