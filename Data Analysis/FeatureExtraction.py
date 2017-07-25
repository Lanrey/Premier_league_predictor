import pandas
import numpy as np
from sklearn.neural_network import MLPRegressor


class neural_net_predictor: 
        dataset = pandas.read_csv('/home/lanrey/htdocs/BPL_Pred/2015.csv')
        dataset2 = pandas.read_csv('/home/lanrey/htdocs/BPL_Pred/footyData.csv')
                
        #load dataset
        array = dataset.values
        array2 = dataset2.values

        output_array = []
        feature_array = []

        team_array = []
        #output_array2 = []
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
        
        
        clf = MLPRegressor(solver='adam',alpha=0.1, hidden_layer_sizes=(1000,),random_state=0)
        clf.fit(D,output_array)
        predicted_rank = clf.predict(Df)
        print(predicted_rank)



