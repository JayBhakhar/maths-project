from flask import Flask, render_template, request
import itertools
from itertools import combinations


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('layout.html')

#task1?n=544&r=45

@app.route('/task1')
def task1():
    number = request.args.get('number', default='')
    r = request.args.get('r', default='')
    if number and r:
        combs = combinations(range(int(number)), int(r))
    else:
        combs = []
    return render_template('task1.html', combs=combs, number=number, r=r)


@app.route('/task2', methods=['GET', 'POST'])
def task2():
    if request.method == 'POST':
        lst = []
        num = request.form.get('num')
        for n in range(num):
            n = n + 1
            lst.append(n)

        for p in itertools.permutations(lst):
            print(''.join(str(x) for x in p))
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