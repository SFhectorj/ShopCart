import json
import os

class Product:
    def __init__(self, product_id, name, price, description):
        self.id = product_id
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.id}. {self.name} - ${self.price:.2f}"

class ProductCatalogService:
    def __init__(self, data_path="data/products.json"):
        self.products = self.load_products(data_path)

    # Load product database from json file
    def load_products(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Could not find product data: {filepath}!")
        
        with open(filepath, "r") as f:
            product_data = json.load(f)

        products = []
        for p in product_data:
            products.append(Product(p["id"], p["name"], p["price"], p["description"]))
        return products

    def get_products(self):
        return self.products
    
    def get_from_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None
    
    def search_products(self, keyword):
        keyword = keyword.lower()
        # List with matching items
        result_match = []
        for p in self.products:
            # Make sure everything is lowercase for case-insensitive searching
            lower_case_names = p.name.lower()
            description_lower = p.description.lower()

            # Check for keyword
            if keyword in lower_case_names or keyword in description_lower:
                result_match.append(p)

        results = result_match
        return results
                
if __name__ == "__main__":
    catalog = ProductCatalogService()

    # print("Loaded", len(catalog.get_products()), "products!")
    # print("Example:", catalog.get_products()[150])

    # print("All Products:")
    # for p in catalog.get_products():
    #     print(p)
    
    # print("\nSearch Results for 'keyboard':")
    # for p in catalog.search_products("keyboard"):
    #     print(p)

    # print("\nGet Product by ID (3):")
    # item = catalog.get_from_id(3)
    # if item:
    #     print(item)
    # else:
    #     print("Not found")
