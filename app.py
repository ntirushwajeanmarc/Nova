from flask import Flask, render_template, request, redirect, session

user = 'johnmarc2k18@gmail.com'
password = '12345'
bookings = []  # Initialize an empty list to store bookings
roomPrice = ["200$","300$","500$","600$"]

app = Flask(__name__)
app.secret_key = 'fc62fd5d-8247-4c1d-9496-f75a929001f9'

@app.route('/')
def home():
    return render_template('home.html',roomPrice = roomPrice)

@app.route('/admin', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email == user and password == password:
            session['logged_in'] = True  
            return redirect('/dashboard')
            
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session and session['logged_in']:
        return render_template('page.html', user=user, bookings=bookings)  # Pass bookings data to page.html
    else:
        return redirect('/admin')  # Redirect to login page if user is not logged in

@app.route('/book', methods=['POST', 'GET'])
def book():
    if request.method == 'POST':
        emailx = request.form.get('email')
        name = request.form.get('name')
        checkin_date = request.form.get('checkin_date')
        checkout_date= request.form.get('checkout_date')
        message = request.form.get('message')
        # Assuming you want to store the email and password of the booking
        booking = {'email': emailx, 'name': name,'checkin_date':checkin_date,
        'checkout_date':checkout_date,'message':message}
        bookings.append(booking)  # Add the booking to the list of bookings
        print(bookings)  # Optional: Print the bookings list for debugging
    return render_template('book.html')
@app.route('/service')
def service():
    return render_template('services.html')

if __name__ == '__main__':
    app.run(debug=True)
