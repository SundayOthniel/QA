# class Cars:
#     def __init__(self):
#         pass
#     def printt(self, color):
#         return f'This car is {color}' 
# car = Cars()
# print(car.printt('red'))

# class In(Cars):
#     def __str__(self):
#         return In()

# print(f'this is for class ck \b')

class Car:
    def __init__(self):
        pass

    def printt(self, color):
        return f'This car is {color}'

class Car:
    def __init__(self, color):
        self.color = color

    def print_color(self):
        return f'This car is {self.color}'

# Define the subclass In which inherits from Car
class In(Car):
    def __init__(self, color, model):
        super().__init__(color)
        self.model = model

    def print_details(self):
        return f'This car is {self.color} and the model is {self.model}'

# Create an instance of In
ck = In('red', 'sedan')

# Print inherited and new values
print(ck.print_color())           # Inherited method from Car class
print(ck.print_details())         # Method from In class

print(f'this is for class ck: {ck}')
