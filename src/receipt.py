from datetime import date
from item import item


# TODO: fix remove_item

class receipt:
    def __init__(self, store: str, shoppers: list):
        self.date = date.today()
        self.store = store

        self.shoppers = {}
        for shopper in shoppers:
            self.shoppers[shopper.name] = []

        self.items = []
        self.total = 0

    def add_item(self, added_item: item, shoppers: list):
        """
        Adds an item to the receipt and splits the cost between the shoppers
        :param added_item: The item to be added, must be an item object
        :param shoppers: The shoppers who will split the cost of the item, must be a list of shopper objects
        """
        self.items.append(added_item)
        self.total += added_item.price

        for shopper in shoppers:
            self.shoppers[shopper.name].append((added_item.name, added_item.price / len(shoppers)))

    def remove_item(self, removed_item: item, shoppers: list):
        self.items.remove(removed_item)
        self.total -= removed_item.price

        for shopper in shoppers:
            self.shoppers[shopper.name] -= (removed_item.name, removed_item.price / len(shoppers))

    def __str__(self):
        ret = f"Receipt for {self.store} on {self.date} \n"

        ret += f"Total: ${self.total}"
        return ret
