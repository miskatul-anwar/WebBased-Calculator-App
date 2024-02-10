
from flask import Flask, render_template, request

app = Flask(__name__)

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        result = None
        if operation == 'add':
            result = sum(num1, num2)
        elif operation == 'sub':
            result = sub(num1, num2)
        elif operation == 'mul':
            result = mul(num1, num2)
        elif operation == 'div':
            if num2 != 0:
                result = div(num1, num2)
            else:
                result = 'Error: Division by zero'

        return render_template('calculator.html', result=result)

    return render_template('calculator.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)