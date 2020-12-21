pizzas = ["bbq", "chicken", "olive", "cheese", "anchovies"]
for pizza in pizzas:
  print (f"I love {pizza}!")
print ("I really love pizza!")

animals = ["chimpanzee", "orangutan", "babboon", "gibbon"]
for monkey in animals:
  print (f"A {monkey} would make a great pet.")

squares = []
for value in range (1, 11):
  squares.append(value ** 2)
print (squares)

squares = [value ** 2 for value in range (1,11)]
print (squares)
max(squares)

list_20 = []
for value in range (1,21):
  list_20.append(value)
print (list_20)

list_1mil = []
for value in range (1, 15):
  list_1mil.append(value)
print (list_1mil)

list_2 = [value ** 2 for value in range (1, 11)]
print (list_2)
print(max(list_2))
print(min(list_2))
print(float(sum(list_2)))
