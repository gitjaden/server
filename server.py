from flask import Flask
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from flask"

@app.get("/test")
def test():
    return "Hello from the test page"

@app.get("/about")
def about():
    return "jaden sherpa"

@app.get("/hello")
def hello():
    message = {"message":"Hello there!"}
    return json.dumps(message)
    
    # create an endpoint that says hello using a varaible instead of usig an string 

app.run(debug=True)#that when i save the code, the changes are applied in the server
 
 #Assignment 2
 # Creating a list
fruits = ["apple", "banana", "cherry", "date"]
# Accessing items in the list by index
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry

# Creating a dictionary
person = {
    "name": "Jaden",
    "age": 24,
    "city": "bay area"
}

# Accessing values by key
print(person["name"])  # Output: Jaden
print(person["age"])   # Output: 24

# Modifying values
person["age"] = 24
print(person)  # Output: {'name': 'Jaden', 'age': 24, 'city': 'bay area'}

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using for loop to print each number
for number in numbers:
    print(number)

