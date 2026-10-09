def average(values):
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def first_item(items):
    if not items:
        raise ValueError("items must not be empty")
    return items[0]
