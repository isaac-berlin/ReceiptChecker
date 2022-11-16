from receipt import receipt
from shopper import shopper
from item import item

Isaac = shopper("Isaac", "A")
Ethan = shopper("Ethan", "B")
Steve = shopper("Steve", "C")


test = receipt("Awesome Store", [Isaac, Ethan, Steve])
test.add_item(item("Apple", 1.00, "Fruit"), [Isaac, Ethan, Steve])
test.add_item(item("Banana", 1.00, "Fruit"), [Ethan, Steve])
test.add_item(item("Orange", 1.00, "Fruit"), [Isaac, Ethan])
test.add_item(item("Pineapple", 1.00, "Fruit"), [Steve])
test.add_item(item("Watermelon", 1.00, "Fruit"), [Isaac, Ethan, Steve])
print(test.shoppers)