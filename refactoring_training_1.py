import dataclasses
import random


@dataclasses.dataclass
class Product:
    id: str
    name: str
    price: float
    weight: float
    stock_quantity: int
    reserved_quantity: int = 0


class Warehouse:
    def __init__(self, id: str, address: str, stock: dict[str, int]):
        self.id = id
        self.address = address
        self.stock = stock or {}

    def has_product(self, product_id: str, quantity: int) -> bool:
        return self.stock.get(product_id, 0) >= quantity


class OrderFulfillmentService:
    def __init__(self):
        # Static sample inventory for demo/main usage
        self.inventory = [
            Product("ELEC001", "Bluetooth Speaker", 49.99, 1.2, 10),
            Product("ELEC002", "Wireless Headphones", 79.99, 0.8, 25),
            # Add more if needed
        ]
        # Static sample warehouses for demo/main usage
        self.warehouses = [
            Warehouse(
                "WH-NY",
                "200 Broadway, New York, NY 10007",
                {"ELEC001": 6, "ELEC002": 12},
            ),
            Warehouse(
                "WH-NJ",
                "1 Harbor St, Newark, NJ 07114",
                {"ELEC001": 8, "ELEC002": 14},
            ),
        ]

    def process_order_fulfillment(
        self,
        order_id: str,
        customer_id: str,
        items: dict[str, int],
        shipping_address: str,
        payment_method: str,
        is_priority_shipping: bool,
    ) -> str:
        # Validate inventory and calculate costs
        subtotal = 0.0
        weight = 0.0
        unavailable_items = []
        warehouse_assignments = {}

        for product_id, quantity in items.items():
            # Find product
            product = None
            for p in self.inventory:
                if p.id == product_id:
                    product = p
                    break

            if product is None or product.stock_quantity < quantity:
                unavailable_items.append(product_id)
                continue

            # Calculate costs
            subtotal += product.price * quantity
            weight += product.weight * quantity

            # Find best warehouse
            best_warehouse = None
            min_distance = float("inf")
            for w in self.warehouses:
                if w.has_product(product_id, quantity):
                    distance = self._calculate_distance(w.address, shipping_address)
                    if distance < min_distance:
                        min_distance = distance
                        best_warehouse = w.id

            warehouse_assignments[product_id] = best_warehouse

        if unavailable_items:
            return f"Order failed: Items unavailable: {', '.join(unavailable_items)}"

        # Calculate shipping cost
        shipping_cost = 0.0
        if weight <= 5.0:
            shipping_cost = 15.99 if is_priority_shipping else 7.99
        elif weight <= 20.0:
            shipping_cost = 25.99 if is_priority_shipping else 12.99
        else:
            shipping_cost = weight * 2.5 if is_priority_shipping else weight * 1.5

        # Apply customer discounts
        customer = self._find_customer_by_id(customer_id)
        discount = 0.0
        if customer.type == "PREMIUM" and subtotal > 100:
            discount = subtotal * 0.15
        elif customer.type == "GOLD" and subtotal > 50:
            discount = subtotal * 0.10
        elif customer.type == "SILVER" and subtotal > 25:
            discount = subtotal * 0.05

        # Process payment
        total = subtotal - discount + shipping_cost
        if payment_method == "CREDIT_CARD":
            total += total * 0.029  # Processing fee
        elif payment_method == "PAYPAL":
            total += total * 0.034  # Processing fee

        # Reserve inventory
        for product_id, quantity in items.items():
            for p in self.inventory:
                if p.id == product_id:
                    p.stock_quantity -= quantity
                    p.reserved_quantity += quantity
                    break

        # Generate fulfillment instructions
        instructions = []
        instructions.append(f"FULFILLMENT ORDER: {order_id}")
        instructions.append(f"Customer: {customer.name}")
        instructions.append(
            f"Shipping: {'PRIORITY' if is_priority_shipping else 'STANDARD'}"
        )
        instructions.append(f"Total: ${total:.2f}")
        instructions.append("Warehouse Assignments:")

        for product_id, warehouse_id in warehouse_assignments.items():
            instructions.append(f"- Product {product_id} from Warehouse {warehouse_id}")

        # Log transaction
        print(
            f"Order processed: {order_id} | Total: ${total:.2f} | Items: {len(items)}"
        )

        return "\n".join(instructions)

    def _calculate_distance(self, addr1: str, addr2: str) -> float:
        # Simplified distance calculation
        return random.random() * 100  # Mock implementation

    def _find_customer_by_id(self, customer_id: str):
        # Mock implementation
        class Customer:
            def __init__(self, id, name, type):
                self.id = id
                self.name = name
                self.type = type

        return Customer(customer_id, "John Doe", "PREMIUM")


if __name__ == "__main__":
    service = OrderFulfillmentService()
    result = service.process_order_fulfillment(
        order_id="12345",
        customer_id="123456",
        items={"ELEC001": 1, "ELEC002": 2},
        shipping_address="123 Main St, New York, NY 10001",
        payment_method="PAYPAL",
        is_priority_shipping=False,
    )
    print(result)
    '''
    Your Mission: Apply all 6 refactoring techniques to improve this code

Identified Problems:

Monster method doing too many things
Magic numbers scattered throughout
Repeated patterns (loops, calculations)
Poor variable naming
Complex nested logic
Suggested Refactorings:

Rename: Improve variable names (entry, p, w, etc.)
Extract Method: Break down into logical chunks:
Product validation and costing
Warehouse assignment logic
Shipping cost calculation
Discount calculation
Payment processing
Inventory reservation
Instruction generation
Introduce Local Variable: Extract complex expressions and magic numbers:
Fee percentages (0.029, 0.034)
Weight thresholds (5.0, 20.0)
Shipping rates
Discount thresholds and rates
Introduce Parameter: Make rates and thresholds configurable
Introduce Field: Add class-level constants for all the magic numbers
Inline: Remove any unnecessary intermediate variables
Bonus Challenges:

Identify which loops could be extracted into separate methods
Consider how to make the discount calculation more maintainable
Think about separation of concerns (calculation vs. formatting vs. logging)
Deliverable: Share 2-3 key refactorings your team applied and the improvement they made


https://refactoring.com/
'''