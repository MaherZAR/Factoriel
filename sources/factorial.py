from flask import Flask, render_template, request

app = Flask(__name__)
#0000àà00
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def calculate_factorial():
    try:
        num = int(request.form['number'])
        if num < 0:
            return render_template('index.html', error="Please enter a non-negative integer. Thank you.")

        result = factorial(num)
        digit_sum = sum_of_digits(result)
        return render_template('index.html', result=result, digit_sum=digit_sum)

    except ValueError:
        return render_template('index.html', error="Invalid input. Please enter a valid non-negative integer.")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def calculate_factorial():
    try:
        num = int(request.form['number'])
        if num < 0:
            return render_template('index.html', error="Please enter a non-negative integer. Thank you.")

        result = factorial(num)
        digit_sum = sum_of_digits(result)
        return render_template('index.html', result=result, digit_sum=digit_sum)

    except ValueError:
        return render_template('index.html', error="Invalid input. Please enter a valid non-negative integer.")

if __name__ == "__main__":
    app.run(debug=True)
