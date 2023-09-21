from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Display an h1 element with the title
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string_param>')
def print_string(string_param):
    # Print the string to the console
    print(string_param)
    # Display the string in the web browser
    return f'<h1>Printed String: {string_param}</h1>'

@app.route('/count/<int_param>')
def count(int_param):
    int_param = int(int_param)  # Convert the parameter to an integer
    numbers = '\n'.join(str(i) for i in range(int_param))  # Exclude int_param itself
    return numbers

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    num1 = float(num1)
    num2 = float(num2)

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"

    return str(result)


if __name__ == '__main__':
    app.run(debug=True)
