from services.product_catalog import ProductCatalogService
from services.cart_service import CartService

# Handle user interaction and navigation between menus

def main_menu():
    """
    Display main menu and prompt user for input
    """
    print("\n============================")
    print("         SHOPCART")
    print("For all of you daily needs!")
    print("============================")
    print("\033[4mWELCOME!\033[0m")
    print()
    print("Browse our product catalog with ease!")
    print("Navigate using only simple commands \nto browse and build up your cart.")
    print("You’ll see your total amount before \nchecking out to ensure a smooth process.")
    print()
    print("\033[4mYou have options!\033[0m")
    print()
    print("1. Browse Products")
    print("2. View Cart")
    print("3. Exit")

def browse_products(catalog, cart):
    
    while True:
        print("\n============================")
        print("         Catalog🛍️")
        print("============================")
        products = catalog.get_products()
        # Show 20 products
        for p in products[:20]:
            print(p)
        print(f"\nShowing {min(20, len(products))} of {len(products)} products.")
        print("\nOptions:")
        print("1. View Product Details")
        print("2. Add item to cart")
        print("3. Return to Main Menu")

        choice = input("Select an Option: ").strip()

        if choice == "1":
            view_product_details(catalog, cart)
        elif choice == "2":
            product_id_input = input("\nEnter the product ID to view details or 'B' to go back (You'll lose anything typed): ").strip()
            if product_id_input.lower() == 'b':
                return browse_products(catalog, cart)
            try:
                product_id = int(product_id_input)
            except ValueError:
                print("Invalid input. Please enter a numeric Product ID")
                return
            product = catalog.get_from_id(product_id)
            if not product:
                print("Product not found. Please enter a valid Product ID.")
                return
            try:
                qty = int(input("Enter the quantity desired: ").strip())
                if qty <= 0:
                    print("Quantity must be greater than zero.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue
            confirm = input(f"You're adding {product.name} (x{qty}). Is that correct?" "\nEnter 'y' to proceed or 'n' to return to product details without adding to cart: ").strip().lower()

            if confirm == "y":
                cart.add_item(product, qty)
            else:
                print(" Returning to product details...")

        elif choice == "3":
            break
        else:
            print("Invalid Choice: Select a valid option.")

def view_product_details(catalog, cart):
    '''
    Display product deatils and add to cart
    '''
    product_id_input = input("\nEnter the product ID to view details (or 'B' to go back):").strip()

    if product_id_input.lower() == 'b':
        return
    
    try:
        product_id = int(product_id_input)
    except ValueError:
        print("Invalid input. Please enter a numeric Product ID")
        return

    product = catalog.get_from_id(product_id)
    if not product:
        print("Product not found. Please enter a valid Product ID.")
        return
    
    while True:
        print("\n========================================")
        print("            🔎 Product Details")
        print("========================================")
        print(f"ID:          {product.id}")
        print(f"Name:        {product.name}")
        print(f"Price:       ${product.price:.2f}")
        print(f"Description: {product.description}")
        print("----------------------------------------")
        print("1. Add to Cart")
        print("2. Return to Product List")

        choice = input("Select an option: ").strip()
        if choice == "1":
            try:
                qty = int(input("Enter the quantity desired: ").strip())
                if qty <= 0:
                    print("Quantity must be greater than zero.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue
            confirm = input(f"You're adding {product.name} (x{qty}). Is that correct?" "\nEnter 'y' to proceed or 'n' to return to product details without adding to cart: ").strip().lower()

            if confirm == "y":
                cart.add_item(product, qty)
            else:
                print(" Returning to product details...")
        elif choice == "2":
            return
        else:
            print("Invalid choice. Please try again.")

def main():
    catalog = ProductCatalogService("data/products.json")
    cart = CartService()

    while True:
        main_menu()
        choice = input("\nSelect an option (1-3): ").strip()
        if choice == "1":
            browse_products(catalog, cart)
        # elif choice == "2":
        #     view_product_details(catalog, cart)
        elif choice == "2":
            cart.view_cart()
        elif choice == "3":
            confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()
            if confirm == "y":
                print("Thank you for using ShopCart! Goodbye!")
                break
        else:
            print("Invalid Choice. Please select an option from the menu.")

if __name__ == "__main__":
    main()
