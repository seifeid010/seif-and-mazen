cart = []
def add_item():
    name = input("Item name: ").strip()
    try:
        price = float(input("Price: "))
        if price <= 0:
            print("❌ Price must be positive.")
            return
    except ValueError:
        print("❌ Invalid price.")
        return
    try:
        quantity = int(input("Quantity: "))
        if quantity <= 0:
            print("❌ Quantity must be positive.")
            return
    except ValueError:
        print("❌ Invalid quantity.")
        return
    for item in cart:
        if item["item"].lower() == name.lower():
            item["quantity"] += quantity
            print("✅ Quantity updated.")
            return
    cart.append({
        "item": name,
        "price": price,
        "quantity": quantity
    })
    print("✅ Item added to cart.")
def remove_item():
    name = input("Item name to remove: ").strip()
    for item in cart:
        if item["item"].lower() == name.lower():
            try:
                quantity = int(input("Quantity to remove: "))
                if quantity <= 0:
                    print("❌ Quantity must be positive.")
                    return
            except ValueError:
                print("❌ Invalid quantity.")
                return
            if quantity > item["quantity"]:
                print("❌ Cannot remove more than existing quantity.")
                return
            item["quantity"] -= quantity
            if item["quantity"] == 0:
                cart.remove(item)
            print("✅ Item updated.")
            return
    print("❌ Item not found.")
def show_cart():
    if not cart:
        print("🛒 Cart is empty.")
        return
    print("\n--- Your Cart ---")
    for item in cart:
        total = item["price"] * item["quantity"]
        print(f'{item["item"]} — {item["quantity"]} × {item["price"]} = {total}')
def show_total():
    total_price = sum(item["price"] * item["quantity"] for item in cart)
    print(f"\n💰 Total price: {total_price}")
def main():
    while True:
        print("\n===== Grocery Cart Manager =====")
        print("1. Add item")
        print("2. Remove item")
        print("3. Show cart")
        print("4. Show total price")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            show_cart()
        elif choice == "4":
            show_total()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid option.")
if __name__ == "__main__":
    main()