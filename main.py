from services.product_catalog import ProductCatalogService

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
    print("3. Checkout")
        #Print("Accessibility")
    print("5. Exit")

def main():
    main_menu()
    choice = input("\nSelect an option (1-4): ").strip()
if __name__ == "__main__":
    main()