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

  # Using the list() Constructor

  """
  list([iterable])
  """

  print(list((0, 1, 2, 3, 4, 5, 6, 7, 8, 9)))
  print(list({ "circle", "square", "triangle", "rectangle", "pentagon" }))
  print(list({ "name": "John", "age": 30, "city": "New York" }.items()))
  print(list("Pythonista"))
  print(list())

  def fib_generator(stop):
    current_fib, next_fib = 0, 1
    for _ in range(0, stop):
      fib_number = current_fib
      current_fib, next_fib = next_fib, current_fib + next_fib
      yield fib_number

  print(fib_generator(10))
  print(list(fib_generator(10)))
  print([*fib_generator(10)])

  # Building Lists With List Comprehensions

  """
  [expression(item) for item in iterable]
  """

  print([number ** 2 for number in range(1, 11)])
