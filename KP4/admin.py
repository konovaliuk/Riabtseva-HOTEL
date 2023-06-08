from flask import current_app, session, redirect, render_template, url_for
from sqlalchemy.orm import Session
from sqlalchemy.testing.suite.test_reflection import users


from _dao_.user_dao_ import UserDAOim


# def read_users():
#     if not 'logout' in session or not session['logout'] or not session['role_id'] == 1:
#         return redirect(url_for('home'))
#     engine = current_app.config['engine']
#     user_table = current_app.config['tables']['users']
#     with Session(engine) as s:
#         users_ = user_table.read_all(s)
#         data = {'users': [{
#             'id': users.user_id,
#             'first_name': users.first_name,
#             'last_name': users.last_name,
#             'email': users.email,
#             'role_id': users.role_id
#         } for users in users_]}
#         return render_template("admin.html", data=data)

def read_users():
    if not 'logout' in session or not session['logout'] or not session['role_id'] == 1:
            return redirect(url_for('home'))
    session['role_id'] = users.role_id
    return render_template("admin.html")



