import os
import time
import uuid

PAYMENT_REQ_DIR = "../Payment-Service/requests"
PAYMENT_RES_DIR = "../Payment-Service/responses"

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
        
        print("\nOptions:")
        print("1. Proceed to Checkout")
        print("2. Return to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            self.checkout()
        elif choice == "2":
            return
        else:
            print("Invalid choice. Returning to main menu.")

    def clear_cart(self):
        self.items = []
        print("Cart cleared.")

    def send_payment_request(self, card, exp, cvv, amount):
        os.makedirs(PAYMENT_REQ_DIR, exist_ok=True)
        os.makedirs(PAYMENT_RES_DIR, exist_ok=True)

        request_id = str(uuid.uuid4())[:8]

        request_file = os.path.join(PAYMENT_REQ_DIR, f"payment_request_{request_id}.txt")
        response_file = os.path.join(PAYMENT_RES_DIR, f"payment_response_{request_id}.txt")

        with open(request_file, "w") as f:
            f.write(f"CARD={card}\n")
            f.write(f"EXP={exp}\n")
            f.write(f"CVV={cvv}\n")
            f.write(f"AMOUNT={amount}\n")

        print("\nProcessing payment...")

        while not os.path.exists(response_file):
            time.sleep(0.3)

        response = {}
        with open(response_file, "r") as f:
            for line in f:
                if "=" in line:
                    k, v = line.strip().split("=", 1)
                    response[k] = v

        os.remove(response_file)
        return response


    def checkout(self):
        if not self.items:
            print("Your cart is empty.")
            return

        total = sum(item["price"] * item["qty"] for item in self.items)
        print(f"\nYour total is: ${total:.2f}")

        card = input("Enter card number: ")
        exp = input("Enter expiration (MM/YY): ")
        cvv = input("Enter CVV: ")

        confirm = input(f"\nCharge ${total:.2f}? (y/n): ").lower()
        if confirm != "y":
            print("Checkout canceled.")
            return

        response = self.send_payment_request(card, exp, cvv, total)

        if response.get("STATUS") == "APPROVED":
            print("\nPAYMENT APPROVED!")
            print("Payment ID:", response.get("PAYMENT_ID"))
            print("Thank you for your purchase!")
            self.clear_cart()
        else:
            print("\nPAYMENT DENIED.")
            print("Reason:", response.get("REASON", "Unknown error"))
