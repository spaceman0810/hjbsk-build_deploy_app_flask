from flask import Flask, render_template, request
# Import the Maths package here

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
    except ValueError:
        return "Invalid input. Both 'num1' and 'num2' must be numeric."

    try:
        result = summation(num1, num2)
    except Exception as e:
        return f"An error occurred: {str(e)}"

    return str(result)


@app.route("/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    result = SUBTRACTION(num1,num2)
    return str(result)
    
@app.route("/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here  
    result = multiplication(num1,num2)
    return str(result)
    
@app.route("/")
def render_index_page():
    # Write your code here
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
