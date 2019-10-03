import numpy as np;

# *args -> Only endX [len(args)==1]
#       -> startX and endX [len(args)==2]

# In fact, the [len(args)==1] function is useless for using this Library

def DP(x_params, y_values, *args):
    if len(args) == 1:
        if args[0] < x_params[0]:
            return 0;
        value = y_values[0];
        if args[0] > x_params[-1]:
            endX = len(x_params)-1;
        else:
            endX = x_params.index(args[0]);
        for y in y_values[:endX+1]:
            value += y;
        return value;
    if len(args) == 2:
        if args[1] > x_params[-1]:
            endX = len(x_params)-1;
        else:
            endX = x_params.index(args[1]);
        if args[0] < x_params[0]:
            startX = 0;
        else:
            startX = x_params.index(args[0]);
        value = y_values[startX];
        for y in y_values[startX+1:endX+1]:
            value += y;
        return value;

def CP(x_params, y_values, *args):
    if len(args) == 1:
        if args[0] < x_params[0]:
            return 0;
        value = y_values[0] * 0.01;
        if args[0] > x_params[-1]:
            endX = len(x_params) - 1;
        else:
            endX = int(np.where(x_params == args[1])[0]);
        for y in y_values[:endX + 1]:
            value += y * 0.01;
        return value;
    if len(args) == 2:
        if(args[0]) < x_params[0]:
            startX = 0;
        else:
            startX = np.argmin(np.abs(x_params - args[0]));
        if(args[1]) > x_params[-1]:
            endX = len(x_params)-1;
        else:
            endX = np.argmin(np.abs(x_params - args[1]));
        value = 0;
        for y in y_values[startX:endX+1]:
            value += y*0.01;
        return value;