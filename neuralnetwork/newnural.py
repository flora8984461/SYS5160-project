from neupy import algorithms, layers, environment
import numpy as np
import pickle

def testtest(matrixList):
    with open('network.pickle', 'rb') as ff:
        loaded_network = pickle.load(ff)
    
#def testtest():
    
        x_test=np.array(matrixList)
        
        y_train = np.array([1, 0, 2, 3])
        normalizer = max(y_train)
        
#        self.x_test=np.array(matrixList)
    
        b=loaded_network.predict(x_test)*normalizer
        print('Result:',b)

        return b.round()