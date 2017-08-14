from flask import Flask
from flask import render_template
from FeatureExtraction import neural_net_predictor
from DecisionTree import DecisionTree
from KNN_Predictor import KNN_predictor
from LinearRegression import LinearRegression

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict():
    teams = []
    ranks = []
    return render_template('predict.html', team=teams, rank=ranks)

@app.route('/predict/quarter1')
def predict_1():
    teams = []
    ranks = []
    teams = DecisionTree.team_array
    ranks = DecisionTree.D_predicted_rank
    for i in range(len(ranks)):
        ranks[i] = ranks[i] + 10
    return render_template('predict.html', team=teams, rank=ranks)

@app.route('/predict/quarter2')
def predict_4():
    teams = []
    ranks = []
    teams = neural_net_predictor.team_array
    ranks = neural_net_predictor.predicted_rank
    for i in range(len(ranks)):
        ranks[i] = ranks[i] + 10
    return render_template('predict.html', team=teams, rank=ranks )

@app.route('/predict/quarter3')
def predict_8():
    teams = []
    ranks = []
    teams = LinearRegression.team_array
    ranks = LinearRegression.pred
    for i in range(len(ranks)):
        ranks[i] = ranks[i] + 10
    return render_template('predict.html', team=teams, rank=ranks )

def sorty(teams,ranks):
    team = []

    for i in range(20):
        min_index = 0
        min_value = ranks[min_index]
        for j in range(0,20):
            if min_value > ranks[j]:
                min_index = j
                min_value = ranks[j]
        
        ranks[min_index] = 1000

        team.append(teams[min_index])
    return team
        
        
            
           

@app.route('/predict/quarter4')
def predict_16():
    teams = []
    ranks = []
    teams = KNN_predictor.team_array
    ranks = KNN_predictor.K_predicted_rank
    for i in range(len(ranks)):
        ranks[i] = ranks[i] + 10
    return render_template('predict.html', team=teams, rank=ranks )
   

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5007, debug=True)