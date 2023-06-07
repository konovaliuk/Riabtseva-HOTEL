import json

from flask import render_template, url_for, redirect, request, flash
from flask_login import current_user, logout_user, LoginManager

from app import app
from flask_forms import *
from flask_forms import Booking

from services.room_services import *
from services.booking_services import *
from services.user_services import *

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)
login_manager.login_message_category = 'info'


# app = Flask(__name__)


@login_manager.user_loader
def load_user(user_id):
    try:
        print('Load user:', user_id)
        return get_user_by_id(user_id)
    except:
        return None


@app.route('/')
def home():
    return render_template('home.html', user=current_user)


@app.route("/sign_up/homepage", methods=['POST', 'GET'])
@app.route("/login/homepage", methods=['POST', 'GET'])
# @login_required
def homepage():
    return render_template('homepage.html', user=current_user)


@app.route('/admin')
# @login_required
def admin():
    if current_user.is_authenticated and current_user.role_id == 1:
        return render_template('admin.html')
    else:
        flash('You do not have permission to access this page.', 'error')
        print('SMTH WRONG')
        return redirect(url_for('homepage'))


@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    form = SignUp()
    error = None

    if form.validate_on_submit():
        user_ = create_user(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
        if not user_:
            error = 'Invalid credentials'
        else:
            return redirect(url_for('homepage'))

    return render_template('sign_up.html', title='Реєстрація', form=form)


@app.route("/booking", methods=['POST', 'GET'])
# @login_required
def booking():
    form = Booking()
    error = None

    if form.is_submitted():
        # user_id = current_user.id

        number_people = form.number_people.data
        check_in_date = form.check_in_date.data
        check_out_date = form.check_out_date.data
        room_type = form.room_type.data

        available_rooms = []
        all_available_rooms = get_available_rooms_for(room_type, number_people)

        for room_data in all_available_rooms:
            if room_available(room_data[0]):
                available_rooms.append(parse_room_data(room_data))

        if not available_rooms:
            print('empty available_rooms')
        else:
            return render_template('booking_res.html', available_rooms=available_rooms)

    return render_template('booking.html', form=form)


@app.route('/booking_res', methods=['POST', 'GET'])
def booking_res():
    if request.method == 'POST':
        pass

    return render_template('booking_res.html', available_rooms=request.args.get('available_rooms'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = validate_login(email=form.email.data, password=form.password.data)

        if user == False:
            error = 'Invalid credentials'
        else:
            return redirect(url_for('homepage'))

    return render_template('sequrity/login.html', title='Увійти', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/room/add', methods=['POST'])
def add_room():
    print(request)
    selected_room = request.form.get('room')
    selected_room = json.loads(selected_room.replace("'", '"'))  # Convert the JSON string to a dictionary
    # user_id = current_user.get_id()
    # print('Current User ID:', user_id)
    user_id = 41
    print(current_user)
    print('Print1:', selected_room)

    if current_user and selected_room:
        room_id = selected_room['room_id']
        room_type = selected_room['room_type']
        number_people = selected_room['max_capacity']
        check_in_date = request.form.get('checkin-date')
        check_out_date = request.form.get('checkout-date')
        update_status(room_id, 'booked')
        room_add(room_id, user_id, room_type, check_in_date, check_out_date, number_people)

    return redirect(url_for('homepage'))


@app.route('/profile', methods=['GET', 'POST'])
# @login_required
def profile():
    # user_id = current_user.get_id()
    user_id = 41
    # bookings = user_bookings(user_id)
    bookings, total_coast = user_bookings(user_id)

    return render_template('profile.html', user=current_user, bookings=bookings, total_coast=total_coast)


@app.route("/all_right", methods=['POST'])
def all_right():
    return render_template('all_right.html')


@app.route('/delete_booking/<int:booking_id>/<int:room_id>', methods=['POST'])
# @login_required
def delete_u_booking(booking_id, room_id):
    # user_id = current_user.get_id()
    user_id = 41
    success = delete_booking(user_id, booking_id)

    if success:
        update_status(room_id, 'available')
        flash('Booking deleted successfully!', 'success')
    else:
        flash('Failed to delete booking.', 'error')

    return redirect(url_for('profile'))
