if __name__ == "__main__":
  # Getting Started With Python's list Data Type

  colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet"
  ]
  print(colors)
  print(colors[0])
  print(colors[1])
  print(colors[2])
  print(colors[3])

  print([42, "apple", True, { "name": "John Doe" }, (1, 2, 3), [3.14, 2.78]])

  # Constructing Lists in Python

  # Creating Lists Through Literals

  """
  [item_0, item_1, ..., item_n]
  """

  digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  print(digits)

  fruits = ["apple", "banana", "orange", "kiwi", "grape"]
  print(fruits)

  cities = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Philadelphia"
  ]
  print(cities)

  matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ]
  print(matrix)

  inventory = [
    { "product": "phone", "price": 1000, "quantity": 10 },
    { "product": "laptop", "price": 1500, "quantity": 5 },
    { "product": "tablet", "price": 500, "quantity": 20 }
  ]
  print(inventory)

  functions = [print, len, range, type, enumerate]
  print(functions)

  empty = []
  print(empty)
