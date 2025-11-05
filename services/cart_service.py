class CartService:
    def __init__(self):
        self.items = []

    def add_item(self, product, qty):
        '''
        Adds products to the cart and increments qty if the item is already in the cart.
        '''
        for item in self.items:
            if item["id"] == product.id:
                item["qty"] += qty
                print(f"Added {qty} moe '{product.name}' to your cart.")
                return
        # If product not already in cart
        self.items.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "qty": qty
        })
        print(f"'{product.name}' added to your cart!")


    def view_cart(self):
        '''
        Display the products currently in the cart.
        '''
        if not self.items:
            print("\nIt's currently empty and lonley here.")
            return
        
        print("\n========================================")
        print("               🛒 Your Cart")
        print("========================================")
        total = 0
        for item in self.items:
            subtotal = item["price"] * item["qty"]
            total += subtotal
            print(f"{item['name']} (x{item['qty']}) - ${subtotal:.2f}")
        print("----------------------------------------")
        print(f"Total: ${total:.2f}")
        print("========================================")

    def clear_cart(self):
        self.items = []
        print("Cart cleared.")
