class OnlineStore:
    def __init__(self):
        self.users = []
        self.products = []
        self.orders = []

    def register_user(self, user):
        self.users.append(user)

    def add_product(self, product):
        self.products.append(product)

    def place_order(self, user, product):
        if product in self.products:
            self.orders.append((user, product))
            return "Order placed successfully"
        return "Product not available"

# Exemplo de uso
store = OnlineStore()
store.register_user("Alice")
store.add_product("Laptop")
print(store.place_order("Alice", "Laptop"))