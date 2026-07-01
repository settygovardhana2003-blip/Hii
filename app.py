from flask import Flask, request, render_template_string
import sqlite3
import os

app = Flask(__name__)

DB_NAME = 'ev5_bookings.db'

def init_db():
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fullname TEXT,
                rollnumber TEXT,
                gender TEXT,
                hostel TEXT,
                aadhaar TEXT,
                pickup TEXT,
                returndate TEXT
            )
        ''')
        conn.commit()
        conn.close()

init_db()

# --- TEMPLATES ---

# The main booking page HTML
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EV5 Rental Bikes - Anantapur</title>
<style>
    body{font-family:Arial,sans-serif;margin:0;background:#f4f7fc;color:#333;}
    header{background:#007bff;color:white;text-align:center;padding:50px 20px;}
    header h1{margin:0;font-size:38px;}
    header p{font-size:22px;}
    section{max-width:900px;margin:25px auto;background:white;padding:30px;border-radius:10px;box-shadow:0 3px 10px rgba(0,0,0,.1);}
    h2{color:#007bff;}
    input,select{width:100%;padding:10px;margin-top:5px;margin-bottom:15px;border:1px solid #ccc;border-radius:5px;box-sizing:border-box;}
    .gender{margin-bottom:15px;}
    .gender input{width:auto;margin-right:5px;}
    button{background:#007bff;color:white;border:none;padding:12px 25px;border-radius:5px;cursor:pointer;font-size:16px;}
    button:hover{background:#0056b3;}
    .btn{display:inline-block;background:#25D366;color:black;text-decoration:none;padding:12px 20px;border-radius:5px;font-weight:bold;}
    footer{background:black;color:white;text-align:center;padding:15px;margin-top:40px;}
    .success-msg {background: #d4edda; color: #155724; padding: 15px; margin-bottom: 20px; border-radius: 5px; text-align: center;}
</style>
</head>
<body>

<header>
    <h1>🛵 EV5 RENTAL BIKES</h1>
    <p>Affordable Electric Scooter Rentals for Students</p>
</header>

<section>
    <h2>Book Your Ride</h2>
    {% if success %}
        <div class="success-msg">Booking Successful! We will contact you shortly.</div>
    {% endif %}

    <form method="POST" action="/">
        <label>Full Name</label>
        <input type="text" name="fullname" placeholder="Enter your name" required>

        <label>Roll Number</label>
        <input type="text" name="rollnumber" placeholder="Enter Roll Number" required>

        <label>Gender</label>
        <div class="gender">
            <input type="radio" id="male" name="gender" value="Male" required>
            <label for="male">Male</label>
            <input type="radio" id="female" name="gender" value="Female">
            <label for="female">Female</label>
        </div>

        <label>Hostel</label>
        <select name="hostel" required>
            <option value="">Select Hostel</option>
            <option value="Sapthagiri 1">Sapthagiri 1</option>
            <option value="Sapthagiri 2">Sapthagiri 2</option>
        </select>

        <label>Aadhaar Number</label>
        <input type="text" name="aadhaar" maxlength="12" pattern="[0-9]{12}" placeholder="12 Digit Aadhaar Number" required>

        <label>Pickup Date & Time</label>
        <input type="datetime-local" name="pickup" required>

        <label>Return Date & Time</label>
        <input type="datetime-local" name="returndate" required>
        <br>
        <button type="submit">Submit Booking</button>
    </form>
</section>

<footer>© 2026 EV5 Rental Bikes</footer>

</body>
</html>
"""

# The admin dashboard HTML
ADMIN_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Admin Dashboard - EV5</title>
<style>
    body { font-family: Arial, sans-serif; background: #f4f7fc; padding: 20px; margin: 0; }
    h1 { color: #007bff; }
    table { width: 100%; border-collapse: collapse; background: white; box-shadow: 0 3px 10px rgba(0,0,0,0.1); margin-top: 20px; }
    th, td { padding: 12px; border: 1px solid #ddd; text-align: left; }
    th { background: #007bff; color: white; }
    tr:nth-child(even) { background-color: #f9f9f9; }
</style>
</head>
<body>
    <h1>EV5 Admin Dashboard</h1>
    <p>View all incoming rental orders below.</p>
    
    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Roll No</th>
            <th>Gender</th>
            <th>Hostel</th>
            <th>Aadhaar</th>
            <th>Pickup</th>
            <th>Return</th>
        </tr>
        {% for row in rows %}
        <tr>
            <td>{{ row[0] }}</td>
            <td>{{ row[1] }}</td>
            <td>{{ row[2] }}</td>
            <td>{{ row[3] }}</td>
            <td>{{ row[4] }}</td>
            <td>{{ row[5] }}</td>
            <td>{{ row[6] }}</td>
            <td>{{ row[7] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

# --- ROUTES ---

@app.route('/', methods=['GET', 'POST'])
def home():
    success = False
    if request.method == 'POST':
        data = (
            request.form['fullname'],
            request.form['rollnumber'],
            request.form['gender'],
            request.form['hostel'],
            request.form['aadhaar'],
            request.form['pickup'],
            request.form['returndate']
        )
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('INSERT INTO bookings (fullname, rollnumber, gender, hostel, aadhaar, pickup, returndate) VALUES (?, ?, ?, ?, ?, ?, ?)', data)
        conn.commit()
        conn.close()
        success = True
        
    return render_template_string(HTML_TEMPLATE, success=success)

@app.route('/admin')
def admin():
    # Fetch all bookings from the database to display to the owner
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM bookings ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    
    return render_template_string(ADMIN_TEMPLATE, rows=rows)

if __name__ == '__main__':
    app.run(debug=True, port=5000)