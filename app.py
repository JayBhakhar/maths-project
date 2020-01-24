from flask import Flask, render_template, request
import itertools
from itertools import combinations
import matplotlib.pyplot as plt


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


@app.route('/task2')
def task2():
    num = request.args.get('number', default='')
    if num:
        lst = []
        ans = []
        for n in range(int(num)):
            n = n + 1
            lst.append(n)
        for p in itertools.permutations(lst):
            ans.append(p)
    else:
        lst = []
        ans = []
    return render_template('task2.html',lst=lst,ans=ans)


@app.route('/task3')
def task3():
    x1 = [1, 2, 4, 5, 6]
    y1 = [1, 4, 4, 2, 6]
    x2 = [1, 2, 3, 4, 5, 6]
    y2 = [4, 2, 8, 2, 4, 4]
    def graph():
        plt.plot(x1, y1, label="line 1", color='green', linewidth=3,
                 marker='o', markerfacecolor='yellow', markersize=12)
        plt.plot(x2, y2, label="line 2", color='red', linewidth=3,
                 marker='o', markerfacecolor='blue', markersize=12)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Two lines on same graph!')
        plt.legend()
        plt.savefig('static/images/new_plot.png')
    graph()
    return render_template('task3.html', url ='static/images/new_plot.png')


@app.route('/task4')
def task4():
    return  render_template('task4.html')


@app.route('/task5')
def task5():
    return  render_template('task5.html')

app.run(debug=True)