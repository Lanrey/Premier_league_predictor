from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    pass

@app.route('/predict')
def predict():
    pass

@app.route('/predict/quarter1')
def predict_1():
    pass

@app.route('/predict/quarter2')
def predict_4():
    pass

@app.route('/predict/quarter3')
def predict_8():
    pass

@app.route('/predict/quarter4')
def predict_16():
    pass

if __name__ == '__main__':
    app.run()