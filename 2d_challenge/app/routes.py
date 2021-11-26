from flask import render_template
from flask import request
from app import application


# used to check if user input only int or float
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


# used Z-normalization with miu and sigma from training dataset, hardcoded values
def normalize_data(f1, f2, f3, f4, f5):
    out1 = (f1-57.778289)/18.684820
    out2 = (f2-754.382664)/944.193308
    out3 = (f3-61.074145)/23.551458
    out4 = (f4-33.634868)/2.783995
    out5 = (f5-39341.920322)/9267.747811
    return out1, out2, out3, out4, out5


@application.route('/', methods=['GET', 'POST'])
def prediction():
    message = ''
    rounded = 0
    # check if method is POST
    if request.method == "POST":
        # Parse data from HTML into python
        q1 = request.form['1']
        q2 = request.form['2']
        q3 = request.form['3']
        q4 = request.form['4']
        q5 = request.form['5']
        # check input is not empty
        if q1 == '' or q2 == '' or q3 == '' or q4 == '' or q5 == '':
            message = "* Please fill in all fields *"
        # check if input is only int/float
        elif isfloat(q1) is False or isfloat(q2) is False or isfloat(q3) is False or isfloat(q4) is False or isfloat(q5) is False:
            message = "*Only numbers and decimals allowed!*"
        else:
            a = float(q1)
            b = float(q2)
            c = float(q3)
            d = float(q4)
            e = float(q5)
            n1, n2, n3, n4, n5 = normalize_data(a,b,c,d,e)
            # beta values from model
            y = 60.58552632 + (38.74084289*n1) + (-19.49315787*n2) + (29.62344481*n3) + (11.50934029*n4) + (-2.00743626*n5)
            rounded = int(y)
    return render_template('2d_challenge.html', output=rounded, message=message)


