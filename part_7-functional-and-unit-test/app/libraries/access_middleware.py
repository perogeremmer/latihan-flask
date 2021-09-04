from functools import wraps
from flask import session, request, flash, redirect

def auth_required(fn):
    @wraps(fn)
    def wrap(*args, **kwargs):
        print(session)
        if 'logged_in' not in session:
            flash('You need to login first.', 'danger')
            return redirect('/sign-in')
        return fn(*args, **kwargs)
    return wrap