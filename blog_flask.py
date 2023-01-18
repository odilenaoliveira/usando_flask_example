from flask import Flask, render_template, Response
import pygal

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/about')
def sobre():

    return 'sobre a página'
@app.route('/graph/')
def graph():
        """ render svg graph """
        bar_chart = pygal.Bar()
        bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        bar_chart = bar_chart.render_data_uri()
        return render_template('bar_chart.html',bar_chart=bar_chart)

# chamando as funções
if __name__ == "__main__":
	app.run(debug=True)
