from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="awards_db"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/awards')
def show_awards():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT DISTINCT award_name FROM awards")
    awards = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('awards.html', awards=awards)

@app.route('/year', methods=['GET'])
def show_awards_by_year():
    year = request.args.get('year')
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM awards WHERE year = %s", (year,))
    awards = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('year.html', year=year, awards=awards)

@app.route('/country')
def show_awards_by_country():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT DISTINCT country FROM awards")
    countries = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('countries.html', countries=countries)

@app.route('/country/<country>')
def show_awards_by_selected_country(country):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM awards WHERE country = %s", (country,))
    awards = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('country_awards.html', country=country, awards=awards)

@app.route('/university')
def show_awards_by_university():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT DISTINCT university FROM awards")
    universities = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('universities.html', universities=universities)

@app.route('/university/<university>')
def show_awards_by_selected_university(university):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM awards WHERE university = %s", (university,))
    awards = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('university_awards.html', university=university, awards=awards)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        university = request.form['university']
        country = request.form['country']

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO registrations (first_name, last_name, email, university, country, award_year, award_name)
            VALUES (%s, %s, %s, %s, %s, 2026, 'Fields Medal')
        """, (first_name, last_name, email, university, country))
        connection.commit()
        cursor.close()
        connection.close()
        return 'Registration Successful!'
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
