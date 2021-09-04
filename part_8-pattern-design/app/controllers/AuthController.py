from app.models.user import User
from flask_restful import Resource
from flask import render_template, make_response, request, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash


class WebRegisterController(Resource):
    def get(self):
        try:
            view = render_template('register.html')
            return make_response(view)
        except Exception as e:
            flash(f"{e}", 'danger')
            return redirect(request.referrer)

    def post(self):
        try:
            print(request.form)
            password = request.form['password']
            confirmation_password = request.form['confirmation_password']

            if password != confirmation_password:
                raise Exception(
                    'Password and confirmation password does not match')

            check_user = User.objects(email=request.form['email']).first()
            if check_user:
                raise Exception('User already exists!')

            user = User()
            user.name = request.form['name']
            user.email = request.form['email']
            user.password = generate_password_hash(password)
            user.save()

            msg = 'User successfully registered!'
            flash(msg, 'success')

            return redirect('/sign-in')
        except Exception as e:
            flash(f"{e}", 'danger')
            return redirect(request.referrer)


class WebAuthController(Resource):
    def get(self):
        try:
            view = render_template('login.html')
            return make_response(view)
        except Exception as e:
            flash(f"{e}", 'danger')
            return redirect(request.referrer)

    def post(self):
        try:
            email = request.form['email']
            password = request.form['password']
            
            user = User.objects(email=email).first()

            if not user:
                raise Exception('Email or password is invalid!')
            

            if not check_password_hash(user.password, password):
                raise Exception(
                    'Email or password is invalid!'
                )

            msg = f"Hi, {user.name}! How's ur day?"
            flash(msg, 'success')

            session['name'] = user.name
            session['id'] = user.id
            session['logged_in'] = True
            session.permanent = True
            
            return redirect('/todo')
        except Exception as e:
            flash(f"{e}", 'danger')
            return redirect(request.referrer)



class WebLogoutController(Resource):
    def get(self):
        try:
            flash('You have been logout from the system!', 'success')
            session.pop('name', None)
            session.pop('id', None)
            session.pop('logged_in', None)

            return redirect('/sign-in')
        except Exception as e:
            flash(f"{e}", 'danger')
            return redirect(request.referrer)