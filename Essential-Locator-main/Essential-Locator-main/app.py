import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, DecimalField, FileField
from wtforms.validators import InputRequired, Email, Length,DataRequired
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash


UPLOAD_FOLDER = r'static\images'  
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Using SQLite for simplicity
app.config['SECRET_KEY'] = 'your_secret_key'

#admin password
admin_mail_id = "admin@gmail.com"
admin_password = "123456"
id=1

@app.route('/home')
def index():
    return render_template('index.html')


db = SQLAlchemy(app)
app.app_context().push()



# Define a form for Admin Login
class AdminLoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

# Route for Admin Login
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if email == admin_mail_id and password == admin_password:
            # Admin login successful
            session['admin_logged_in'] = True
            flash('You have been logged in as admin.', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid email or password. Please try again.', 'error')

    return render_template('admin_login.html')

# Route for admin dashboard
@app.route('/admin/dashboard')
def admin_dashboard():

        return render_template('admin_dashboard.html')
    
# Route for Admin Logout
@app.route('/admin_logout')
def admin_logout():
    session.pop('admin_id', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('admin_login'))

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    location_url = db.Column(db.String(100), nullable=False)
    shop_type = db.Column(db.String(50), nullable=False)
    area = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    image = db.Column(db.String(100), nullable=False)

class ShopForm(FlaskForm):
    shop_name = StringField('Shop Name', validators=[DataRequired()])
    location = StringField('Location (Link)', validators=[DataRequired()])
    location_url = StringField('Location (URL)', validators=[DataRequired()])
    shop_type = SelectField('Shop Type', choices=[
        ('Public Washroom', 'Public Washroom'),
        ('Petrol Pump', 'Petrol Pump'),
        ('Medical Store', 'Medical Store'),
        ('Grocery Store', 'Grocery Store'),
        ('Gym', 'Gym'),
        ('Bank', 'Bank')
    ], validators=[DataRequired()])
    area = StringField('Area', validators=[DataRequired()])
    contact_number = StringField('Contact Number', validators=[DataRequired()])
    image = FileField('Upload Image')


# Route for admin view to add ground details
@app.route('/admin/add_shop', methods=['GET', 'POST'])
def add_ground():
    form = ShopForm()
    if form.validate_on_submit():
        # Save form data to the database
        ground = Shop(
            shop_name=form.shop_name.data,
            location=form.location.data,
            location_url=form.location_url.data,
            shop_type=form.shop_type.data,
            contact_number=form.contact_number.data,
            area=form.area.data,
            image=form.image.data.filename  # Save only filename for simplicity
        )
        db.session.add(ground)
        db.session.commit()
        # Save the image file
        image_file = form.image.data
        filename = secure_filename(image_file.filename)
        form.image.data.save(f'static/images/{form.image.data.filename}')
        flash('Your ground has been added successfully!', 'success')
        return redirect(url_for('display_grounds'))
    return render_template('add_shop.html', form=form)

@app.route('/shops')
def display_grounds():
    shops=Shop.query.all()
    return render_template('display_shop.html', shop=shops)


if __name__ == '__main__':
    app.run(debug=True)
