from flask import Flask,request
import json
from config import db

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


products = []

@app.get("/api/products")
def get_products():
    return json.dumps(products)  

@app.post("/api/products")  
def save_product():
    product = request.get_json()
    print(f"this is my new products {products}")
    # products.append(product)
    db.products.insert_one(product)
    return json.dumps(product)
    
@app.put("/api/products/<int:index>")
def update_product(index):
    updated_product = request.get_json()
    print(F"Product: {updated_product}: {index}")

    if 0 <= index <= request.get_json():
         products[index] = updated_product
         return json.dumps(updated_product)
    else: 
        return "that index does not exist"

    

@app.delete("/api/products/<int:index>")
def delete_product(index):
    print(f"delete: {index}")

    if index >=0 and index < len(products):
        deleted_product = products.pop(index)
        return json.dumps(deleted_product)
    else: 
        return "that index does not exist"


# create an endpoint that says hello using a varaible instead of usig an string 

app.run(
    debug=True,
)
# that when i save the code, the changes are applied in the server
 







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


