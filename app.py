from flask import Flask, render_template, request

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("home.html")

@app.get("/view_products") #view page
def product_catalog_home():
    name = "shoe"
    description = "This is a nike shoe"
    price = 300
    return render_template(
        'view_products.html', name = name, description = description,
        price = price)

@app.route("/add_product", methods=['GET', 'POST'])
def add_new_product():
    if request.method == "GET":
        return render_template("add_product.html")
    if request.method == "POST":
        category = request.form["category"]
        name = request.form["p_name"]
        description = request.form["description"]
        price = request.form["price"]
        
        return f"{category}, {name}, {description}, {price}"



if __name__ == '__main__':
    app.run(port = 3000, debug = True)