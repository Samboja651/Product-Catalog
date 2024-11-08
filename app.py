from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# creating database in sqlite3
DATABASE = "products.db"

def get_db():
    '''
    Creates database automatically if it does not exits\n.
    Creates a product table & defines its attributes\n.
    Returns a connection obj to the database.
    '''
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    statement = '''
                CREATE TABLE IF NOT EXISTS PRODUCT(
                Id INT AUTO_INCREMENT,
                Category VARCHAR(20),
                Name VARCHAR(25),
                Description VARCHAR(50),
                Price INT
                );        
    '''
    cursor.execute(statement)
    conn.commit()
    conn.close()
    return conn


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
        
        # STORE THE PRODUCT INTO DB
        get_db() 
        # I could just assign conn to get_db() since it returns a 
        # connection to the database. But if I use conn multilpe times
        # it will increase the run time because conn has to execute getdb first.
        # Instead I'm going to create a new connection directly to database.

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        store_product = '''
                        INSERT INTO PRODUCT(Category, Id, Description, Price)
                        VALUES(?, ?, ?, ?);
        '''
        cursor.execute(store_product, (category, name, description, price))
        conn.commit()
        conn.close()

        return f"{category}, {name}, {description}, {price}"



if __name__ == '__main__':
    app.run(port = 3000, debug = True)