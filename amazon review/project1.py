import numpy as np

T_avperceptron = 5
T_avgpa = 5
L_avgpa=10


### Part I
def hinge_loss( feature_matrix, labels,theta, theta_0):
    ###### Args:
    ###Feature matrix- a Numpy matrix describing the given data. Each row represents a single data point
    ### labels - a numpy array where  where kth element of the array is the correct classification of the kth row of the feature matrix
    ### theta -
    ### theta_0 -

    ##returns

    raise NotImplementedError
def perceptron( feature_matrix, labels, T):
    ###### Args:
    ###Feature matrix- a Numpy matrix describing the given data. Each row represents a single data point
    ### labels - a numpy array where  where kth element of the array is the correct classification of the kth row of the feature matrix
    
    ##returns
    ## initial theta is zero
    ## initial theta_0 is 0
    ## Loop through all the dataSets
    ## call perception_single_step_update( feature_matrix(i), labels(i),theta, theta_0 

    raise NotImplementedError


def perceptron_single_step_update( feature_vector, label, current_theta, current_theta_0):
    
    ##returns
    ## if Loss function is > 0
    ## theta(k+1)= theta(k)+yx
    ## theta_0(k+1)=theta(k)+y
    

    raise NotImplementedError


    
