from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configure the MySQL database connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456789',
    database='SEARCH_ENGINE'
)
print("Database Configuration Successful!")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    cursor = db.cursor()
    cursor.execute("SELECT * FROM search_results WHERE keyword LIKE %s", ('%' + keyword + '%',))
    results = cursor.fetchall()
    cursor.close()
    return render_template('search_results.html', results=results)

@app.route('/add_result', methods=['POST'])
def add_result():
    keyword = request.form['keyword']
    result_text = request.form['result_text']

    cursor = db.cursor()
    cursor.execute("INSERT INTO search_results (keyword, result_text) VALUES (%s, %s)", (keyword, result_text))
    db.commit()
    cursor.close()

    return redirect(url_for('index'))

@app.route('/add_resultpage')
def add_resultpage():
    return render_template('add_results.html')

if __name__ == '__main__':
    app.run(debug=True)
