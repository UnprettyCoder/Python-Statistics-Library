import matplotlib.pyplot as plt;

class DataModel:
    def __init__(self, dataName):
        self.dataName = dataName;
        self.xyDict = {};

    def add(self, x, y):
        self.xyDict[x] = y;

    def addList(self, x, y):
        for x, y in zip(x, y):
            self.xyDict[x] = y;

    def addAll(self, *args):
        x = []; y = [];
        for i in range(len(args)):
            if i % 2 == 0:  x.append(args[i]);
            else:   y.append(args[i]);
        for x, y in zip(x, y):
            self.xyDict[x] = y;

    def showValue(self):
        print(self.xyDict);

    def showGraph(self, switch):
        x = [x for x in self.xyDict.keys()];
        y = [y for y in self.xyDict.values()];
        fig, ax = plt.subplots();
        if switch == "bar":
            ax.bar(x, y, color="green", alpha=0.3);
        if switch == "plot":
            ax.plot(x, y, color="red", alpha=0.5);
        ax.set(xlabel="x", ylabel="y", title=f"{self.dataName}");
        ax.grid();
        plt.savefig("../GraphSave/graphExample.png");
        plt.show();

    def getDict(self):
        return self.xyDict;
