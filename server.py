from flask import Flask

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


# endpoint 1: /coupons
# http://127.0.0.1:5000/coupons
@app.route("/coupons", methods=["GET"])
def coupons():
    coupons_list = [
        {"code": "SAVE10", "discount": "10%"},
        {"code": "FREESHIP", "discount": "Free Shipping"},
        {"code": "WELCOME15", "discount": "15%"},
        {"code": "HOLIDAY20", "discount": "20%"},
    ]
    return coupons_list

# endpoint 2: /coupons/count
# http://127.0.0.1:5000/coupons/count
@app.route("/coupons/count", methods=["GET"])
def coupon_count():
    coupons_list = [
        {"code": "SAVE10", "discount": "10%"},
        {"code": "FREESHIP", "discount": "Free Shipping"},
        {"code": "WELCOME15", "discount": "15%"},
        {"code": "HOLIDAY20", "discount": "20%"},
    ]
    return {"count": len(coupons_list)}


if __name__ == "__main__":
    app.run(debug=True)
# When this file is run directly: __name__ == "__main__"
#  When this file is imported as a module: __name__ == "server.py"