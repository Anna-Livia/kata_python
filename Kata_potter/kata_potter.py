def cash_register(basket):
    if sum(basket) == 0:
        return 0
    basket = [book for book in basket if book > 0]
    possible_orders = [order_generator(list(basket), index) for index in range(1, len(basket) + 1)]
    possible_prices = [order_pricer(order) for order in possible_orders]
    return min([amount for amount in possible_prices if amount > 0])


def order_generator(basket, max_bundle):
    order = []
    books = basket
    for bundle_size in reversed(range(1, max_bundle + 1)):
        bundles, remainder = bundle_finder(books, bundle_size)
        order.insert(0, bundles)
        books = remainder
    return order


def bundle_finder(books, bundle_size):
    number_of_bundle = 0
    while len(books) >= bundle_size:
        counter = 0
        for tome in range(len(books)):
            counter += 1
            books[tome] -= 1
            if counter == bundle_size:
                number_of_bundle += 1
                books = [book for book in books if book > 0]
                break
    return number_of_bundle, books


def order_pricer(order):
    price_per_bundle = [8, 8 * 2 * 0.95, 8 * 3 * 0.90, 8 * 4 * 0.80, 8 * 5 * 0.75]
    return sum([order[index] * price_per_bundle[index] for index in range(len(order))])
