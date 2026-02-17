class OrderProcessor:
    def __init__(self):
        self.inventory = []
        self.warehouses = []

    def process_order(
        self, *, items, quantities, prices, customer_type, region, expedited
    ):
        total = 0  # Total what?

        # Apply special tax
        for i in range(len(items)):
            total += quantities[i] * prices[i]
            if items[i].startswith("ELEC"):
                total += quantities[i] * prices[i] * 0.15  # Electronics tax

        # Apply discount
        if customer_type == "PREMIUM":
            if region == "US":
                total = total - (total * 0.15)
            elif region == "EU":
                total = total - (total * 0.12)
            else:
                total = total - (total * 0.08)
        elif customer_type == "REGULAR":
            if region == "US":
                total = total - (total * 0.05)
            else:
                total = total - (total * 0.03)

        # Add shipping
        if expedited:
            if total > 100:
                total += 25
            else:
                total += 15
        else:
            if total > 50:
                total += 0
            else:
                total += 8.50

        self._log_transaction(total, customer_type)
        self._update_inventory(items, quantities)

        return total

    def _log_transaction(self, total, customer_type):
        print(f"Processed order: ${total}")

    def _update_inventory(self, items, quantities):
        pass  # Mock implementation


if __name__ == "__main__":
    order_processor = OrderProcessor()
    order_processor.process_order(
        items=["ELEC001", "ELEC002", "ELEC003", "BOOK001"],
        quantities=[1, 2, 3, 2],
        prices=[10, 20, 30, 15],
        customer_type="PREMIUM",
        region="US",
        expedited=True,
    )

"""
TODO LIST
- [ ] Rename (customerType → customerTier, total → orderTotal)
- [ ] Introduce Local Variable (extract 0.15 → PREMIUM_DISCOUNT_RATE)
- [ ] Extract Method (discount calculation → calculateDiscount())
- [ ] Extract Method (tax calculation → addTax())
- [ ] Extract Method (shipping calculation → addShipping())
- [ ] Introduce Parameter (make tax rate configurable)
- [ ] Introduce Field (add TAX_RATE as class field)
- [ ] Inline (remove unnecessary intermediate variable if created)

https://refactoring.com/
"""