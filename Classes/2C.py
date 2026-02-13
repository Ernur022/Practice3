class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Ernur", 18, "Almaty", "Kazakhstan")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)