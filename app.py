from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout.html')

@app.route('/task1', methods=['GET', 'POST'] )
def task1():
    return render_template('task1.html')


@app.route('/task2')
def task2():
    return render_template('task2.html')


@app.route('/task3')
def task3():
    return render_template('task3.html')


@app.route('/task4')
def task4():
    return  render_template('task4.html')


@app.route('/task5')
def task5():
    return  render_template('task5.html')

app.run(debug=True)