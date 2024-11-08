from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def product_catalog_home():
    name = "shoe"
    description = "This is a nike shoe"
    price = 300
    return render_template(
        'index.html', name = name, description = description,
        price = price)


if __name__ == '__main__':
    app.run(port = 3000, debug = True)