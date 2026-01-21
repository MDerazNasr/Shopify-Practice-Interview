"""
Shopify Pair Programming Practice Interview
============================================

Welcome! In this exercise, you'll build an inventory management system for a 
small e-commerce store. This is a collaborative exercise - think out loud, 
ask questions, and work through the problem step by step.

SCENARIO:
---------
You're building the backend for a store that sells products. The store needs to:
1. Track products with their name, price, and quantity in stock
2. Process customer orders (which may contain multiple products)
3. Handle inventory updates when orders are placed
4. Calculate order totals with potential discounts

STARTER CODE:
-------------
Below is some basic structure to get you started. You'll extend this to 
implement the required functionality.

TASKS (in order of priority):
-----------------------------
1. Complete the Product class with proper initialization and a method to 
   check if a given quantity is available in stock.

2. Implement the Inventory class that can:
   - Add products to the inventory
   - Look up products by name
   - Update stock levels

3. Implement the Order class that can:
   - Add items (product + quantity) to an order
   - Calculate the total price
   - Validate that all items are in stock before placing

4. STRETCH: Add a discount system where:
   - Orders over $100 get 10% off
   - Orders over $200 get 15% off

Feel free to modify the starter code as needed!
"""


class Product:
    """Represents a product in the store."""
    
    def __init__(self, name: str, price: float, quantity: int):
        # TODO: Initialize the product
        pass
    
    def is_available(self, requested_quantity: int) -> bool:
        """Check if the requested quantity is available in stock."""
        # TODO: Implement this method
        pass


class Inventory:
    """Manages the store's product inventory."""
    
    def __init__(self):
        # TODO: Initialize the inventory storage
        pass
    
    def add_product(self, product: Product) -> None:
        """Add a product to the inventory."""
        # TODO: Implement this method
        pass
    
    def get_product(self, name: str) -> Product | None:
        """Look up a product by name. Returns None if not found."""
        # TODO: Implement this method
        pass
    
    def update_stock(self, name: str, quantity_change: int) -> bool:
        """
        Update stock level for a product.
        quantity_change can be positive (restock) or negative (sale).
        Returns True if successful, False if product not found or insufficient stock.
        """
        # TODO: Implement this method
        pass


class Order:
    """Represents a customer order."""
    
    def __init__(self, inventory: Inventory):
        # TODO: Initialize the order
        pass
    
    def add_item(self, product_name: str, quantity: int) -> bool:
        """
        Add an item to the order.
        Returns True if the product exists and has sufficient stock.
        Returns False otherwise.
        """
        # TODO: Implement this method
        pass
    
    def calculate_total(self) -> float:
        """Calculate the total price of the order (before any discounts)."""
        # TODO: Implement this method
        pass
    
    def place_order(self) -> bool:
        """
        Finalize the order by deducting items from inventory.
        Returns True if successful, False if any item is no longer available.
        """
        # TODO: Implement this method
        pass


# ============================================================================
# TESTING AREA - Use this to test your implementation
# ============================================================================

if __name__ == "__main__":
    # Example usage - uncomment and modify as you implement
    
    # Create some products
    # laptop = Product("Laptop", 999.99, 10)
    # mouse = Product("Mouse", 29.99, 50)
    # keyboard = Product("Keyboard", 79.99, 30)
    
    # Set up inventory
    # inv = Inventory()
    # inv.add_product(laptop)
    # inv.add_product(mouse)
    # inv.add_product(keyboard)
    
    # Create and process an order
    # order = Order(inv)
    # order.add_item("Laptop", 2)
    # order.add_item("Mouse", 3)
    # print(f"Order total: ${order.calculate_total():.2f}")
    # order.place_order()
    
    # Verify inventory updated
    # print(f"Laptops remaining: {inv.get_product('Laptop').quantity}")
    
    print("Ready to start! Uncomment the test code as you implement.")
