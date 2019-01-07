from flask import Flask, render_template, request, redirect
from classes.stocker import Stocker
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/graph')
def graph():
  s = Stocker(ticker=request.args.get('symbol','GOOG'))
  data=s.plot_stock(start_date=None, end_date=None, stats=['Close'], plot_type='basic')
  return render_template('graph.html',graph_data=data)

if __name__ == '__main__':
  app.run(port=33507)
