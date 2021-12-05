import psycopg2
from flask import Flask, render_template

from queries import db_conn

app = Flask(__name__, template_folder="templates")
db = db_conn.DBConn()


@app.route('/rentals')
def rentals():
    data = db.execute("SELECT * FROM rentals ORDER BY rental_id", 5000)
    header = db.columns('rentals')
    return render_template('tables.html', header=header, rows=data)


@app.route('/addresses')
def addresses():
    data = db.execute("SELECT * FROM addresses ORDER BY address_id", 5000)
    header = db.columns('addresses')
    return render_template('tables.html', header=header, rows=data)


@app.route('/branches')
def branches():
    data = db.execute("SELECT * FROM branches ORDER BY branch_id", 5000)
    header = db.columns('branches')
    return render_template('tables.html', header=header, rows=data)


@app.route('/brands')
def brands():
    data = db.execute("SELECT * FROM brands ORDER BY brand_id", 5000)
    header = db.columns('brands')
    return render_template('tables.html', header=header, rows=data)


@app.route('/cars')
def cars():
    data = db.execute(
        "SELECT * FROM cars "
        "join car_model cm on cm.model_id = cars.model_id "
        "join brands b on b.brand_id = cm.brand_id",
        5000)
    header = db.columns('cars')
    header.extend(db.columns('car_model'))
    header.extend(db.columns('brands'))
    return render_template('tables.html', header=header, rows=data)


@app.route('/customers')
def customers():
    data = db.execute("SELECT * FROM customers ORDER BY customer_id", 5000)
    header = db.columns('customers')
    return render_template('tables.html', header=header, rows=data)


@app.route('/states')
def states():
    data = db.execute("SELECT * FROM states ORDER BY state_id", 5000)
    header = db.columns('states')
    return render_template('tables.html', header=header, rows=data)


@app.route('/exception')
def exception():
    try:
        data = db.execute("CALL delete_or_update_model_price(205::money, 50::money);", 5000)
        header = db.columns('states')
        return render_template('tables.html', header=header, rows=data)
    except psycopg2.ProgrammingError:
        return render_template('message.html', message='You are going to delete too many rows, change your input')


@app.route('/function/<string:start_date>/<string:end_date>')
def function(start_date, end_date):
    data = db.execute(f"select * from get_start_end_rental_data('{start_date}'::timestamp, '{end_date}'::timestamp);",
                      5000)
    header = ['Rental id', 'Start date', 'End date']
    return render_template('tables.html', header=header, rows=data)


@app.route('/function')
def function_with_defaults():
    data = db.execute(f"select * from get_start_end_rental_data();",
                      5000)
    header = ['Rental id', 'Start date', 'End date']
    return render_template('tables.html', header=header, rows=data)
