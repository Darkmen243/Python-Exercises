'''
inventory = {
    "apple": 10,
    "banana": 5
}

Implement:

add_item(name, qty)

remove_item(name, qty)

Prevent negative values
'''
inventory = {
    "apple": 10,
    "banana": 5
}
def add_item(inv : dict, name: str, qty: int):
    if qty<=0:
        raise ValueError("Quantity must be a positive number.")
    if qty>0:
         inv[name] = inv.get(name, 0) + qty

def remove_item(inv : dict, name: str, qty: int):
    if qty<=0:
        raise ValueError("Quantity must be a positive number.")
    if name not in inv:
       raise KeyError("This item is not in the inventory.")
    if inv[name] < qty:
       raise ValueError("Not enough items in inventory")
    inv[name]-=qty
remove_item(inventory,"apple",2)
add_item(inventory,"orange",3)
print(inventory)