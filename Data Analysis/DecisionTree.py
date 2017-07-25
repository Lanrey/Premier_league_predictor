import pandas
import numpy as np
from sklearn import tree
class DecisionTree:
    dataset = pandas.read_csv('/home/lanrey/htdocs/BPL_Pred/2015.csv')
    dataset2 = pandas.read_csv('/home/lanrey/htdocs/BPL_Pred/footyData.csv')

    #load dataset
    array = dataset.values
    array2 = dataset2.values

    output_array = []
    feature_array = []

    team_array = []
    feature_array2 = []

    for i in range(len(array)):
        row = array[i]
        output_array.append(row[0])
        d = np.delete(row, (0), axis=0)
        feature_array.append(d)
    D = np.array(feature_array)

    for j in range(len(array2)):
        row = array2[j]
        team_array.append(row[1])
        d = np.delete(row, (0,1), axis=0)
        feature_array2.append(d)
    Df = np.array(feature_array2)


    D_predict = tree.DecisionTreeRegressor()
    D_predict.fit(D, output_array)
    D_predicted_rank = D_predict.predict(Df)
    print('Decision regressor*******************')
    for i in range(len(team_array)):
        print(f'{team_array[i]} {D_predicted_rank[i]}')