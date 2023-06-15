#  **African Cuisine:** You're creating a recipe app specifically for African cuisine.
#  The app needs to handle recipes from different African countries, each with its
#  unique ingredients, preparation time, cooking method, and nutritional
#  information. Consider creating a `Recipe` class, and think about how you might
#  create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
#  `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
#  methods.


# input
#  Recipes
# output
#  Different types of recipes
#  Process
#  Creating a class known as Recipe ans pass in the attributes
# create sublasses and pass in unique properties



class Recipe:
    def __init__(self, unique_ingredients, preparation_time, cooking_method, nutritional_information):
        self.unique_ingredients = unique_ingredients
        self.preparation_time = preparation_time
        self.cooking_method = cooking_method
        self.nutritional_information = nutritional_information

class MoroccanRecipe(Recipe):
    def __init__(self, unique_ingredients, preparation_time, cooking_method, nutritional_information):
        super().__init__(unique_ingredients, preparation_time, cooking_method, nutritional_information)
        

class EthiopianRecipe(Recipe):
    def __init__(self, unique_ingredients, preparation_time, cooking_method, nutritional_information):
        super().__init__(unique_ingredients, preparation_time, cooking_method, nutritional_information)
        

class NigerianRecipe(Recipe):
    def __init__(self, unique_ingredients, preparation_time, cooking_method, nutritional_information):
        super().__init__(unique_ingredients, preparation_time, cooking_method, nutritional_information)
        
        
        
    #  **Ancestral Stories:** In many African cultures, the art of storytelling is passed
    #  down from generation to generation. Imagine you're creating an application that
    #  records these oral stories and translates them into different languages. The
    #  stories vary by length, moral lessons, and the age group they are intended for.
    #  Think about how you would model `Story`, `StoryTeller`, and `Translator`
    #  objects, and how inheritance might come into play if there are different types of
    #  stories or storytellers.

# //   Input

# //   Ancestral Stories
# //   output

# //   application that will record the Stories
# //   translate the stories into different languages
# //   Process
# //   creating a class and pass in the attributesmp
# //   create methods(record the stories,translating to different languages)
class Story:
    def __init__(self, length, moral_lessons, age_group):
        self.length = length
        self.moral_lessons = moral_lessons
        self.age_group = age_group

class StoryTeller:
    def __init__(self, name, stories):
        self.name = name
        self.stories = stories

class Translator:
    def __init__(self, languages):
        self.languages = languages

    def translate(self, story, target_language):
    
        pass

        
        
#  Create a class called Product with attributes for name, price, and quantity.
#  Implement a method to calculate the total value of the product (price * quantity).
#  Create multiple objects of the Product class and calculate their total values.

#  input
#  product
#  output
#  total value ot the product
#  process
#  create a class and pass the attributes
#  create method to calculte the total value of the product 
#  create objects of the class product and caete the total values

class Product:
    def __init__(self,price,quantity):
        self.price = price
        self.quantity = quantity
        
# // **Wildlife Preservation:** You're a wildlife conservationist working on a
# // program to track different species in a national park. Each species has its own
# // characteristics and behaviors, such as its diet, typical lifespan, migration
# // patterns, etc. Some species might be predators, others prey. You'll need to create classes 
# // to model `Species`, `Predator`, `Prey`, etc., and think about how
# // these classes might relate to each other through inheritance.

# // input
# // wildlifePreservation
# // output
# // tracking different species
# // process
# // creating  class and pass in the attributes
# // creating subclasses 
# // creating a method


class Species:
    def __init__(self, diet, typical_lifespan, migration_patterns):
        self.diet = diet
        self.typical_lifespan = typical_lifespan
        self.migration_patterns = migration_patterns

class Predator(Species):
    def __init__(self, diet, typical_lifespan, migration_patterns):
        super().__init__(diet, typical_lifespan, migration_patterns)
        

class Prey(Species):
    def __init__(self, diet, typical_lifespan, migration_patterns):
        super().__init__(diet, typical_lifespan, migration_patterns)
        
        
        
# // **African Music Festival:** You're in charge of organizing a Pan-African music
# // festival. Many artists from different countries, each with their own musical style
# // and instruments, are scheduled to perform. You need to write a program to
# // manage the festival lineup, schedule, and stage arrangements. Think about how
# // you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# // how you might use inheritance if there are different types of performances or
# // stages.

# // INPUT
# // Music Festival
# // OUTPUT
# // Program that manages music festive
# // Process
# // create a class and pass in the attributes
# // create a subclasses
# // create methods        
class Artist:
    def __init__(self, name, musical_style, instruments):
        self.name = name
        self.musical_style = musical_style
        self.instruments = instruments

class Performance:
    def __init__(self, artists, start_time, end_time):
        self.artists = artists
        self.start_time = start_time
        self.end_time = end_time

class Stage:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity

    # def assign_performance(self, performance):
        


# // Create a class called Product with attributes for name, price, and quantity.
# // Implement a method to calculate the total value of the product (price * quantity).
# // Create multiple objects of the Product class and calculate their total values.

# // input
# // product
# // output
# // total value ot the product
# // process
# // create a class and pass the attributes
# // create method to calculte the total value of the product 
# // create objects of the class product and caete the total values
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def calculate_total_value(self):
#         return self.price * self.quantity       
    

# // Implement a class called Student with attributes for name, age, and grades (a
# //     list of integers). Include methods to calculate the average grade, display the
# //     student information, and determine if the student has passed (average grade >=
# //     60). Create objects for the Student class and demonstrate the usage of these
# //     methods.

# // input
# // Student
# // output
# // process
# // create a class and pass in the attributes
# // create methods
# // create object of class student that will demontrate the usage of the methods

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def display_information(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def has_passed(self):
        average_grade = self.calculate_average_grade()
        return average_grade >= 60

       

# // Create a FlightBooking class that represents a flight booking system. Implement
# // methods to search for available flights based on destination and date, reserve
# // seats for customers, manage passenger information, and generate booking
# // confirmations.



       

