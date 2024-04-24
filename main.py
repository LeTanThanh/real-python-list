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

  # Accessing Items in a List: Indexing

  """
  list_object[index]
  """

  languages = ["Python", "Java", "JavaScript", "C++", "Go", "Rust"]
  print(languages)
  print(languages[0])
  print(languages[1])
  print(languages[2])
  print(languages[3])
  print(languages[4])
  print(languages[5])
  print(len(languages)) # 6
  # languages[6]
  # IndexError

  print(languages[-1])
  print(languages[-2])
  print(languages[-3])
  print(languages[-4])
  print(languages[-5])
  print(languages[-6])
  # languages[-7]
  # IndexError

  employees = [
    ("John", 30, "Software Engineer"),
    ("Alice", 25, "Web Developer"),
    ("Bob", 45, "Data Analyst"),
    ("Mark", 22, "Intern"),
    ("Samantha", 36, "Project Manager")
  ]
  print(employees)
  print(employees[1][0])
  print(employees[1][1])
  print(employees[1][2])

  employees = [
    { "name": "John", "age": 30, "job": "Software Engineer" },
    { "name": "Alice", "age": 25, "job": "Web Developer" },
    { "name": "Bob", "age": 45, "job": "Data Analyst" },
    { "name": "Mark", "age": 22, "job": "Intern" },
    { "name": "Samantha", "age": 36, "job": "Project Manager" }
  ]
  print(employees[3]["name"])
  print(employees[3]["age"])
  print(employees[3]["job"])

  # Retrieving Multiple Items From a List: Slicing

  """
  list_object[start:stop:step]
  """

  letters = ["A", "a", "B", "b", "C", "c", "D", "d"]
  print(letters)

  upper_letters = letters[0::2]
  print(upper_letters)

  lower_letters = letters[1::2]
  print(lower_letters)

  digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  print(digits)

  first_three = digits[:3]
  print(first_three)

  middle_four = digits[3:7]
  print(middle_four)

  last_three = digits[-3:]
  print(last_three)

  every_two = digits[::2]
  print(every_two)

  every_three = digits[::3]
  print(every_three)

  """
  slice(start, stop, step)
  """

  letters = ["A", "a", "B", "b", "C", "c", "D", "d"]
  print(letters)

  slice_object = slice(0, None, 2)
  print(slice_object)
  print(type(slice_object))
  upper_letters = letters[slice_object]
  print(upper_letters)

  slice_object = slice(1, None, 2)
  print(slice_object)
  print(type(slice_object))
  lower_letters = letters[slice_object]
  print(lower_letters)

  """
  Finally, it's important to note that out of range values for start and stop don't cause slicing expression to raise a TypeError.
  In general, you'll observe the following behaviors:

  - If start is before the beginning of the list, which can happen when you use negative indices, then Python will use 0 instead.
  - If start is greater than stop, then slicing will return an empty list.
  - If stop is beyond the length of the the list, then Python will use the length of the list instead.

  Here are some examples that show these behaviors in action:
  """

  colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
  print(colors)
  print(len(colors)) # 7
  print(colors[-8:])
  print(colors[8:])
  print(colors[:8])

  # Creating Copies of a List

  """
  In Python, you'll have two kinds of mechanisms to create copies of an existing list.
  You can create either

  1. A shallow copy
  2. A deep copy
  """

  # Aliases of a List

  countries = ["United States", "Canada", "Poland", "Germany", "Austria"]
  print(countries)

  nations = countries
  print(nations)

  print(id(countries))
  print(id(nations))
  print(countries is nations)

  countries[0] = "United States of America"
  print(countries)
  print(nations)

  # Shallow Copies of a List

  """
  A shallow copy of an existing list is a new list containing references to the objects stored in the original list.
  In other words, when you create a shallow copy of a list, Python constructs a new list with a new identity.
  Then, it inserts references to the objects to the objects in the original list into the new list.

  There are at least three different ways to create a shallow copis of an existing list.
  You can use:

  1. The slicing operator, [:]
  2. The .copy() method
  3. The copy() function from the copy module


  These three tools demonstrate equivalent behavior.
  So, to kick things off, you'll start exploring the slicing operator:
  """

  countries = ["United States", "Canada", "Poland", "Germany", "Austria"]
  print(countries)

  nations = countries[:]
  print(nations)
  print(id(countries) == id(nations))       # False
  print(id(countries[0]) == id(nations[0])) # True
  print(id(countries[1]) == id(nations[1])) # True

  countries[0] = "United States of America"
  print(countries)
  print(nations)
  print(id(countries) == id(nations))       # False
  print(id(countries[0]) == id(nations[0])) # False
  print(id(countries[1]) == id(nations[1])) # True

  """
  On the first line of this piece of code, you update the item at index 0 in countries.
  This change doesn't affect the item at index 0 in nations.
  Now the first items in the list are completely different objects with their own identoties.
  The rest of the items, however, continue to share the same identity.
  So, they're the same object in each case.

  Because making copies of a list is such a common operation, the list class hash a dedicated method for it.
  The method is called .copy(), and it returns a shallow copy of the target list:
  """

  countries = ["United States", "Canada", "Poland", "Germany", "Austria"]
  print(countries)

  nations = countries.copy()
  print(nations)
  print(id(countries) == id(nations))       # False
  print(id(countries[0]) == id(nations[0])) # True
  print(id(countries[1]) == id(nations[1])) # True

  countries[0] = "United States of America"
  print(countries)
  print(nations)
  print(id(countries) == id(nations))       # False
  print(id(countries[0]) == id(nations[0])) # False
  print(id(countries[1]) == id(nations[1])) # True

  from copy import copy

  countries = ["United States", "Canada", "Poland", "Germany", "Austria"]
  print(countries)

  nations = copy(countries)
  print(nations)
  print(id(countries) == id(nations))       # False
  print(id(countries[0]) == id(nations[0])) # True
  print(id(countries[1]) == id(nations[1])) # True

  countries[0] = "United States of America"
  print(countries)
  print(nations)
  print(id(countries) == id(nations))       # False
  print(id(countries[0]) == id(nations[0])) # False
  print(id(countries[1]) == id(nations[1])) # True