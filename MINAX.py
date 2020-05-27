import numpy as np

def Minax(X,Y):
    new_X = np.array(X)
    new_Y = np.array(Y)
    
    arg_max = np.argmax(new_Y)
    arg_min = np.argmin(new_Y)
    
    y_max,x_max = new_Y[arg_max],new_X[arg_max]
    y_min,x_min = new_Y[arg_min],new_X[arg_min]
    
    ###
    sorted_Y = np.sort(new_Y)
    first_min, second_min, third_min, fourth_min, fifth_min = sorted_Y[0], sorted_Y[1], sorted_Y[2], sorted_Y[3],sorted_Y[4]
    first_max, second_max, third_max, fourth_max, fifth_max = sorted_Y[-1],sorted_Y[-2],sorted_Y[-3],sorted_Y[-4],sorted_Y[-5]
    
    arg_first_max  = Y.index(first_max)
    arg_second_max = Y.index(second_max)
    arg_third_max  = Y.index(third_max)
    arg_fourth_max = Y.index(fourth_max)
    arg_fifth_max  = Y.index(fifth_max)
    
    
    arg_first_min  = Y.index(first_min)
    arg_second_min = Y.index(second_min)
    arg_third_min  = Y.index(third_min)
    arg_fourth_min = Y.index(fourth_min)
    arg_fifth_min  = Y.index(fifth_min)
    
    ###
    return ('TOP 5 MAX:',  (new_X[arg_first_max], new_Y[arg_first_max]),
                            (new_X[arg_second_max],new_Y[arg_second_max]),
                            (new_X[arg_third_max], new_Y[arg_third_max]),
                            (new_X[arg_fourth_max], new_Y[arg_fourth_max]),
                            (new_X[arg_fifth_max], new_Y[arg_fifth_max]),
           
            'TOP 5 MIN:',  (new_X[arg_first_min], new_Y[arg_first_min]),
                            (new_X[arg_second_min],new_Y[arg_second_min]),
                            (new_X[arg_third_min], new_Y[arg_third_min]),
                            (new_X[arg_fourth_min], new_Y[arg_fourth_min]),
                            (new_X[arg_fifth_min], new_Y[arg_fifth_min]),
           )
