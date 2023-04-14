from product import Product
from product_collection import ProductCollection

def main():
    collection = ProductCollection()

    p1 = Product(1, "Lettuce")
    collection.add(p1)
    p2 = Product(1, "Cabbage")
    collection.add(p2)

    iterator = collection.create_iterator()
    for i in iterator:
        print(i)

main()