from neupy import algorithms, layers, environment, storage
import numpy as np
import pickle

x_train = np.array([[ 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 1, 0, 0, 0,
                     0, 0, 0, 1, 1, 0, 0, 0,
                     0, 0, 0, 0, 1, 0, 0, 0,
                     0, 0, 0, 0, 1, 0, 0, 0,
                     0, 0, 0, 0, 1, 0, 0, 0,
                     0, 0, 0, 0, 1, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0 ,0, 0, 0,
                     0, 1, 1, 1, 1, 1, 1, 0,
                     0, 1, 0, 0, 0, 0, 1, 0, 
                     0, 1, 0, 0, 0, 0, 1, 0,
                     0, 1, 0, 0, 0, 0, 1, 0,
                     0, 1, 0, 0, 0, 0, 1, 0,
                     0, 1, 1, 1, 1, 1, 1, 0,
                     0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0 ,0, 0, 0,
                      0, 1, 1, 1, 1, 1, 1, 0,
                      0, 1, 0, 0, 0, 0, 1, 0,
                      0, 0, 0, 0, 0, 1, 0, 0,
                      0, 0, 0, 0, 1, 0, 0, 0,
                      0, 0, 0, 1, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 1, 1, 0,
                      0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0 ,0, 0, 0,
                     0, 1, 1, 1, 1, 1, 1, 0,
                     0, 0, 0, 0, 0, 0, 1, 0,
                     0, 0, 1, 1, 1, 1, 1, 0,
                     0, 0, 0, 0, 0, 0, 1, 0,
                     0, 0, 0, 0, 0, 0, 1, 0,
                     0, 1, 1, 1, 1, 1, 1, 0,
                     0, 0, 0, 0, 0, 0, 0, 0]])
        
y_train = np.array([1, 0, 2, 3])
normalizer = max(y_train)
y_train_normalized=y_train/normalizer
network = algorithms.RMSProp(
                [
                    layers.Input(64),
                    layers.Sigmoid(2),
                    layers.Sigmoid(1),
                ],
                step=0.1,
            )
            
network.train(x_train, y_train_normalized, epochs=10000)

with open('network.pickle', 'wb') as f:
    pickle.dump(network, f)

