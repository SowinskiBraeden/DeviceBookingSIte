from src.auth import authentication_blueprint
from flask import render_template

@authentication_blueprint.post("/logout")
def logout():
  session.pop('user_id', None)
  return redirect(url_for('login'), code=200)

@authentication_blueprint.get('/dashboard')
def dashboard():
  if 'user_id' not in session: return redirect(url_for("login"), code=401)
  return render_template('dashboard.html', user_id=session['user_id'])

@authentication_blueprint.get('/login')
def login_get():
  token = request.cookies.get('token')
  if token == '123456': return redirect(url_for("dashboard"), code=200)
  return render_template('login.html', error=None)

@authentication_blueprint.post('/login')
def login_post():
  if valid_login(request.form['user_id'],
                request.form['password']):
    session['user_id'] = request.form['user_id']
    return redirect(url_for("dashboard"), code=200)

  return render_template('login.html', error='Invalid User ID or Password')
