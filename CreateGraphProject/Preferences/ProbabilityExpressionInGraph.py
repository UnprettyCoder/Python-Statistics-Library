from Preferences import ProbabilityValue;
import matplotlib.pyplot as plt;
import numpy as np;

def DPE(DistName, x, y, startX, endX, *args):
    if endX > x[-1]:
        endX = len(x) - 1;
    else:
        endX = x.index(endX);
    if startX < x[0]:
        startX = 0;
    else:
        startX = x.index(startX);
    fig, ax = plt.subplots();
    ax.bar(x, y, color="green", alpha=0.3);
    ax.bar(x[startX:endX+1], y[startX:endX+1], color="red", alpha=0.5);
    ax.set(xlabel="X", ylabel="f(X)", title=f"[X~{DistName}{args}] Range Probability [{startX} < =X <= {endX}]");
    ax.grid();
    plt.savefig("GraphSave/graphExample.png");
    plt.show();
    print(f"P[{startX} <= X <= {endX}] = {ProbabilityValue.DP(x, y, startX, endX)}");
    print(f"[X~{DistName}{args}] Range Probability\n");
    
def CPE(DistName, x, y, startx, endx, *args):
    if (startx) < x[0]:
        startX = 0;
    else:
        startX = np.argmin(np.abs(x - startx));
    if (endx) > x[-1]:
        endX = len(x) - 1;
    else:
        endX = np.argmin(np.abs(x - endx));
    fig, ax = plt.subplots();
    ax.plot(x, y, color="black", alpha=0.5);
    ax.plot(x[startX:endX+1], y[startX:endX+1], color="red", alpha=0.5, linewidth=3);
    ax.bar(x[startX:endX+1], y[startX:endX+1], color="green", alpha=0.3, width=0.01);
    ax.set(xlabel="X", ylabel="f(X)", title=f"[X~{DistName}{args}] Range Probability [{startx} <= X <= {endx}]");
    ax.grid();
    plt.savefig("GraphSave/graphExample.png");
    plt.show();
    print(f"P[{startx} <= X <= {endx}] = {ProbabilityValue.CP(x, y, startx, endx)}");
    print(f"[X~{DistName}{args}] Range Probability\n");