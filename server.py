from flask import Flask
from http import HTTPStatus
from flask import jsonify, request

app = Flask(__name__) #instance of Flask application


# http://127.0.0.1:5000/
@app.route("/", methods=["GET"])
def index():
    return "Welcome to Flask frame work!"


# http://127.0.0.1:5000/
@app.route("/cohort-62", methods=["GET"])
def cohort62():
    students_list = [ "Michael", "Tyler", "Carlos", "Jonathan", "Robert", "Ashton", "Kirt"]
    return students_list

# http://127.0.0.1:5000/cohort-100
@app.route("/cohort-100", methods=["GET"])
def cohort100():
    students_list = [ "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
    return students_list

# http://127.0.0.1:5000/contact
@app.route("/contact", methods=["GET"])
def contact():
    information = {
        "email": "carlos.work@gmail.com",
        "phone": "123-456-7890",
        "address": "123 Main St, Anytown, USA"
    }
    return information

# http://127.0.0.1:5000/course-information
@app.route("/course-information", methods=["GET"])
def course():
    course_information = {
        "course_name": "Full Stack Web Development",
        "duration": "6 months",
        "instructor": "Leo",
        "level": "Beginner"
    }
    return course_information


# ----------- COUPONS --------------
# list of coupons
# number of coupons


coupons_list = [
        {"_id": 1, "code": "SAVE10", "discount": "10%"},
        {"_id": 2, "code": "FREESHIP", "discount": "Free Shipping"},
        {"_id": 3, "code": "WELCOME15", "discount": "15%"},
        {"_id": 4, "code": "HOLIDAY20", "discount": "20%"},
]

# endpoint 1: /coupons
# http://127.0.0.1:5000/coupons
@app.route("/api/coupons", methods=["GET"])
def coupons():
    return coupons_list

# endpoint 2: /coupons/count
# http://127.0.0.1:5000/coupons/count
@app.route("/api/coupons/count", methods=["GET"])
def coupon_count():
    return {"count": len(coupons_list)}

#------- Minichallenge --------
# create a /user endpoint
# return a dictionary with name, role, is _active, and favorite-technologies
#Test it by visiting http://127.0.0.1:5000/user

#http://127.0.0.1:5000/user
@app.route("/user", methods=["GET"])
def user():
    user_info = {
        "name": "Carlos",
        "role": "Student",
        "is_active": True,
        "favorite_technologies": ["Phython", "JavaScripyt", "Flask", "React"]

    }
    return {"User-Info": (user_info)}, HTTPStatus.OK


#path parameter
#Is a dynamic part of the URL used to identify a specific item or resource within an API
# @app.route("/greet/<string:name>")
# def greet(name):
#     return {"message": f"Hello {name}"}

#list of products
products = [
  {
    "_id": 1,
    "title": "Nintendo Switch",
    "price": 299.99,
    "category": "Entertainment",
    "image": "https://picsum.photos/seed/1/300/300"
  },
  {
    "_id": 2,
    "title": "Smart Refrigerator",
    "price": 999.99,
    "category": "Kitchen",
    "image": "https://picsum.photos/seed/2/300/300"
  },
  {
    "_id": 3,
    "title": "Bluetooth Speaker",
    "price": 79.99,
    "category": "Electronics",
    "image": "https://picsum.photos/seed/3/300/300"
  }
]

#Get /api/products endpoint that return a list of products
@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify({
        "success": True,
        "message": "Products retrieved successfully",
        "data": products
    }), HTTPStatus.OK       #200

#Get /api/products
#http://127.0.0.1:5000/api/products/<int:product_id>
@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    for product in products:
        print(product)
        if product["_id"] == product_id:
            return jsonify({
                "success": True,
                "message": "Product retrieved successfully",
                "data": product
            }), HTTPStatus.OK
    return jsonify({
        "success": False,
        "message": "Product not found",
        "data": None
    }), HTTPStatus.NOT_FOUND     #404



# Post /api/products
#http://127.0.0.1:5000/api/products
@app.route("/api/products", methods=["POST"])
def create_product():
    print(request.get_json())
    new_product = request.get_json()
    products.append(new_product)
    return jsonify({
        "success": True,
        "message": "Product created successfully",
        "data": new_product
    }), HTTPStatus.CREATED      #201


#ASSIGNMENNT 2 
# Post /api/coupons
#http://127.0.0.1:5000/api/coupons
@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    print(request.get_json())
    new_coupon = request.get_json()
    coupons_list.append(new_coupon)
    return jsonify({
        "success": True,
        "message": "Coupon created successfully",
        "data": new_coupon
    }), HTTPStatus.CREATED


# api/coupons/<int:coupon_id>
#http://127.0.0.1:5000/api/coupons/<int:coupon_id>
@app.route("/api/coupons/<int:coupon_id>", methods=["GET"])
def get_coupon(coupon_id):
    for coupon in coupons_list:
        print(coupon)
        if coupon["_id"] == coupon_id:
            return jsonify({
                "success": True,
                "message": "Coupon retrieved successfully",
                "data": coupon
            }), HTTPStatus.OK
    return "Coupon not found", HTTPStatus.NOT_FOUND
 


#PUT /api/products
#Put adds
@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    updated_data = request.get_json()
    print(updated_data)
    for product in products:
        if product["_id"] == product_id:
            
            product["title"] = updated_data("title")
            product["price"] = updated_data("price")
            product["category"] = updated_data("category")
            product["image"] = updated_data("image")

            return jsonify({
                "success": True,
                "message": "Product updated successfully",
                "data": product
            }), HTTPStatus.OK
    return jsonify({
        "success": False,
        "message": "Product not found",
        "data": None
    }), HTTPStatus.NOT_FOUND






#DELETE /api/products
#http://127.0.0.1:5000/api/products/<int:product_id>
@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    for product in products:  #for index, product in enumerate(products):
        if product["_id"] == product_id:
            products.remove(product) #removes by using the method .remove
                                     #use .pop(index) if you want to remove by index
            return jsonify({
                "success": True,
                "message": "Product deleted successfully",
                "data": product
            }), HTTPStatus.OK
    return jsonify({
        "success": False,
        "message": "Product not found",
        "data": None
    }), HTTPStatus.NOT_FOUND


if __name__ == "__main__":
    app.run(debug=True)
# When this file is run directly: __name__ == "__main__"
#  When this file is imported as a module: __name__ == "server.py"