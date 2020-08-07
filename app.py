from flask import Flask, render_template, g, request, flash
from database import get_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/', methods=['POST', 'GET'])
def index():
    db = get_db()
    if(request.method == 'POST'):
        firstName = request.form['firstname']
        lastName = request.form['lastname']
        email = request.form['email']
        phoneNumber = request.form['phone']
        cusMessage = request.form['message']
        db.execute('insert into contact_data (firstname, lastname, email, phone, customerdata) values (?, ?, ?, ?, ?)', [firstName, lastName, email, phoneNumber,cusMessage])
        db.commit()
        flash('Customer feedback submitted successfully', 'success')
    return render_template('formpage.html', FN="First Name:", LN="Last Name:", \
    email="Email:", PH="Phone:", msg="Feedback:", sbt="Submit" )

@app.route('/view')
def view():
    db = get_db()
    cur = db.execute('select * from contact_data')
    results = cur.fetchall()    
    return render_template('details.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)