import matplotlib.pyplot as plt;

def D_CumulatedDistribution(y_values):
    cum_val = y_values[0];
    cumulatedValues = [cum_val];
    for y in y_values[1:]:
        cum_val += y;
        cumulatedValues.append(cum_val);
    return cumulatedValues;

def C_CumulatedDistribution(y_values):
    cum_val = y_values[0] * 0.01;
    cumulatedValues = [cum_val];
    for y in y_values[1:]:
        cum_val += y * 0.01;
        cumulatedValues.append(cum_val);
    return cumulatedValues;

def barChart(x_params, y_values, switch, *args):
    fig, ax = plt.subplots();
    if switch == "f":
        ax.bar(x_params, y_values, color="green", alpha=0.3);
        ax.set(xlabel="X", ylabel="f(x)", title=f"{args[0]} ~ {[arg for arg in args[1:]]}");
    if switch == "F":
        plus = "Cumulated ";
        ax.bar(x_params, D_CumulatedDistribution(y_values), color="green", alpha=0.3);
        ax.set(xlabel="X", ylabel="F(x)", title=f"{plus+args[0]} ~ {[arg for arg in args[1:]]}");
    ax.grid();

    plt.savefig("GraphSave/graphExample.png");
    plt.show();

def plot(x_params, y_values, switch, *args):
    fig, ax = plt.subplots();
    if switch == "f":
        ax.plot(x_params, y_values, color="red", alpha=0.7);
        ax.set(xlabel="X", ylabel="f(x)", title=f"{args[0]} ~ {[arg for arg in args[1:]]}");
    if switch == "F":
        plus = "Cumulated ";
        ax.plot(x_params, C_CumulatedDistribution(y_values), color="red", alpha=0.7);
        ax.set(xlabel="X", ylabel="F(x)", title=f"{plus + args[0]} ~ {[arg for arg in args[1:]]}");
    ax.grid();

    plt.savefig("GraphSave/graphExample.png");
    plt.show();