# map()
# applies a function to each item in an iterable (list, tuple, etc.)
# map(function,iterable)

store = [
    ("shirt", 20.00),
    ("pants", 25.00),
    ("jacket", 50.00),
    ("socks", 10.00)
]


to_euros = lambda data : (data[0],data[1]*0.82)
print(store)
store_euros = map(to_euros,store)
print(store_euros)
store_euros = list(map(to_euros,store))
print(store_euros)
print()


to_dollars = lambda data : (data[0],data[1]/0.82)
print(store)
store_dollars = map(to_dollars,store)
print(store_dollars)
store_dollars = list(map(to_dollars,store))
print(store_dollars)
print()


