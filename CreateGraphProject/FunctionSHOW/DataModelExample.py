from Preferences.StatisticalModel import DataModel;

# Generate DataModel class
A = DataModel("Model A");

# add Datas in DataModel using add(x, y), addAll(*args), addList(x_list, y_list) method

A.add(1, 0.2);
A.add(2, 0.1);
A.add(3, 0.3);
A.add(4, 0.1);
A.add(5, 0.3);

A.addAll(1, 0.2, 2, 0.1, 3, 0.3, 4, 0.1, 5, 0.3);

A.addList([1, 2, 3, 4, 5], [0.2, 0.1, 0.3, 0.1, 0.3]);

# Draw Graph(bar or plot) using showGraph(switch) method
# switch can have "bar" or "plot" value

A.showGraph("plot");
A.showGraph("bar");

# Also you can see or get your Dictionary type Data using showValue() or getDict() method

A.showValue();

xyDict = A.getDict();
print(xyDict);