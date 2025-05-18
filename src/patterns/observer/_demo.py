from patterns.observer.store import BookCustomer, BookStore

if __name__ == "__main__":
    store = BookStore()
    customer1 = BookCustomer(store)
    customer2 = BookCustomer(store)

    # Initially, the book is out of stock
    print("Setting stock to 0.")
    store.update_quantity(0)

    # The book comes back in stock
    print("Setting stock to 5.")
    store.update_quantity(5)

    # Remove customer1 from the notification list
    store.remove_customer(customer1)

    # Simulate the situation where the stock changes again
    print("\nSetting stock to 2.")
    store.update_quantity(2)
