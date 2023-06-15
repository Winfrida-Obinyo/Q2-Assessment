// **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// methods.


// input
// Recipes
// output
// Different types of recipes
// Process
// Creating a class known as Recipe ans pass in the attributes
// create sublasses and pass in unique properties
class Recipe {
    constructor(uniqueIngredients, preparationTime, cookingMethod, nutritionalInformation) {
      this.uniqueIngredients = uniqueIngredients;
      this.preparationTime = preparationTime;
      this.cookingMethod = cookingMethod;
      this.nutritionalInformation = nutritionalInformation;
    }
  }
  
  class MoroccanRecipe extends Recipe {
    constructor(uniqueIngredients, preparationTime, cookingMethod, nutritionalInformation) {
      super(uniqueIngredients, preparationTime, cookingMethod, nutritionalInformation);
      
    }
  }
  
  class EthiopianRecipe extends Recipe {
    constructor(uniqueIngredients, preparationTime, cookingMethod, nutritionalInformation) {
      super(uniqueIngredients, preparationTime, cookingMethod, nutritionalInformation);
      
    }
  }
  
  class NigerianRecipe extends Recipe {
    constructor(uniqueIngredients, preparationTime, cookingMethod, nutritionalInformation) {
      super(uniqueIngredients, preparationTime, cookingMethod, nutritionalInformation);
      
    }
  }

    // **Ancestral Stories:** In many African cultures, the art of storytelling is passed
    // down from generation to generation. Imagine you're creating an application that
    // records these oral stories and translates them into different languages. The
    // stories vary by length, moral lessons, and the age group they are intended for.
    // Think about how you would model `Story`, `StoryTeller`, and `Translator`
    // objects, and how inheritance might come into play if there are different types of
    // stories or storytellers.

//   Input

//    Stories
//   output

//   application that will record the Stories
//   translate the stories into different languages
//   Process
//   creating a class and pass in the attributesmp
//   create methods(record the stories,translating to different languages)
class Story {
    constructor(length, moralLessons, ageGroup) {
      this.length = length;
      this.moralLessons = moralLessons;
      this.ageGroup = ageGroup;
    }
  }
  
  class StoryTeller {
    constructor(name, stories) {
      this.name = name;
      this.stories = stories;
    }
  }
  
  class Translator {
    constructor(languages) {
      this.languages = languages;
    }
  
    translate(story, targetLanguage) {
      // Implementation of translation logic
    }
  }
   let = recordStories extends AncestralStories(length,moralLessons,ageGroup){

}

// **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to create classes 
// to model `Species`, `Predator`, `Prey`, etc., and think about how
// these classes might relate to each other through inheritance.

// input
// wildlifePreservation
// output
// tracking different species
// process
// creating  class and pass in the attributes
// creating subclasses 
// creating a method


class Species {
    constructor(diet, typicalLifespan, migrationPatterns) {
      this.diet = diet;
      this.typicalLifespan = typicalLifespan;
      this.migrationPatterns = migrationPatterns;
    }
  }
  
  class Predator extends Species {
    constructor(diet, typicalLifespan, migrationPatterns) {
      super(diet, typicalLifespan, migrationPatterns);
      
    }
  }
  
  class Prey extends Species {
    constructor(diet, typicalLifespan, migrationPatterns) {
      super(diet, typicalLifespan, migrationPatterns);
      
    }
  }

// **African Music Festival:** You're in charge of organizing a Pan-African music
// festival. Many artists from different countries, each with their own musical style
// and instruments, are scheduled to perform. You need to write a program to
// manage the festival lineup, schedule, and stage arrangements. Think about how
// you might model the `Artist`, `Performance`, and `Stage` classes, and consider
// how you might use inheritance if there are different types of performances or
// stages.

// INPUT
// Music Festival
// OUTPUT
// Program that manages music festive
// Process
// create a class and pass in the attributes
// create a subclasses
// create methods

class Artist {
    constructor(name, musicalStyle, instruments) {
      this.name = name;
      this.musicalStyle = musicalStyle;
      this.instruments = instruments;
    }
  }
  
  class Performance {
    constructor(artists, startTime, endTime) {
      this.artists = artists;
      this.startTime = startTime;
      this.endTime = endTime;
    }
  }
  
  class Stage {
    constructor(name, location, capacity) {
      this.name = name;
      this.location = location;
      this.capacity = capacity;
    }
  
    assignPerformance(performance) {
      
    }
  }








// Create a class called Product with attributes for name, price, and quantity.
// Implement a method to calculate the total value of the product (price * quantity).
// Create multiple objects of the Product class and calculate their total values.

// input
// product
// output
// total value ot the product
// process
// create a class and pass the attributes
// create method to calculte the total value of the product 
// create objects of the class product and caete the total values

class Product{
    constructor(price,quantity){
        this.price = price
        this.quantity = quantity

    }
}



// Implement a class called Student with attributes for name, age, and grades (a
//     list of integers). Include methods to calculate the average grade, display the
//     student information, and determine if the student has passed (average grade >=
//     60). Create objects for the Student class and demonstrate the usage of these
//     methods.

// input
// Student
// output
// process
// create a class and pass in the attributes
// create methods
// create object of class student that will demontrate the usage of the methods

class Student{
    constructor(name,age,grades,){
        this.name = name,
        this.age = age,
        this.grades = grades

    }

}



// Create a FlightBooking class that represents a flight booking system. Implement
// methods to search for available flights based on destination and date, reserve
// seats for customers, manage passenger information, and generate booking
// confirmations.


// input
// FlightBooking
// output
// Available flights
// process
// create a class that represents the booking system
// create methods for available flights

class FlightBooking{
    constructor(destination,date,reserveSeats,passengerInformation,bookingConfirmations){
        this.destination = destination
        this.date= date
        this.reserveSeats = reserveSeats
        this.passengerInformation = passengerInformation
        this.bookingConfirmations = bookingConfirmations

    }
}




// Create a LibraryCatalog class that handles the cataloging and management of
// books in a library. Implement methods to add new books, search for books by
// title or author, keep track of available copies, and display book details.
