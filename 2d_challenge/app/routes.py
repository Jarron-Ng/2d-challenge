from flask import render_template
from flask import request
from app import application

@application.route('/', methods = ['GET', 'POST'])
def prediction():
    message = ''
    out = 0
    q1 = ''
    q2 = ''
    q3 = ''
    q4 = ''
    q5 = ''
    if request.method == "POST":
        if q1 and q2 and q3 and q4 and q5 == '':
            message = "This cannot be left blank"
        else:
            q1 = float(request.form['1'])
            q2 = float(request.form['2'])
            q3 = float(request.form['3'])
            q4 = float(request.form['4'])
            q5 = float(request.form['5'])
            y = 60.58552632 + (38.74084289*q1) + (-19.49315787*q2) + (29.62344481*q3) + (11.50934029*q4) + (-2.00743626*q5)
            out = "The predicted number of deaths is:", y
    return render_template('2d_challenge.html', output=out, message=message)


