class Store():

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, product, price):
        self.items[product] = price

    def delete_item(self, product):
        if product in self.items:
            del self.items[product]
        else:
            print(f'{product} отсутствует в ассортименте')

    def get_price(self, product):
        p = self.items.get(product)
        print(f" {product} стоит {p} руб")

    def update_price(self, product, new_price):
        if product in self.items:
            self.items[product] = new_price
        else:
            print(f'{product} отсутствует в ассортименте')

    def info(self):
        print(self.name)
        print(self.address)
        print(self.items)


store1 = Store("Продукты у дома", "Москва, Лавровый пер., 16")
store1.add_item("яблоко", 150)
store1.add_item("банан", 50)
store1.add_item("груша", 250)

store1.info()

store2 = Store("Магазин одежды", "пр. Мира, 2")
store2.add_item("футболка", 350)
store2.add_item("джинсы", 2500)

store2.info()

store3 = Store("Аптека", "ул. Летная, 12")
store3.add_item("анальгин", 300)
store3.add_item("витамины", 1000)

store3.info()

store3.get_price("анальгин")
store3.update_price("анальгин", 400)
store3.get_price("анальгин")

store3.delete_item("анальгин")
store3.info()
