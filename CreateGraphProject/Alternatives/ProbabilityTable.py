from Preferences import ProbabilityValue, Fomulas;
import numpy as np;
import pandas as pd;

def CumulativeBinary(n):
    xParams = range(0, n+1);
    Dict = {};
    for p in np.arange(0.1, 1, 0.1):
        yValues = [Fomulas.B(x, n, p) for x in xParams];
        list = [round(ProbabilityValue.DP(xParams, yValues, 0, i), 4) for i in range(n+1)];
        Dict.update({f"p={round(p,1)}":list});
    df = pd.DataFrame(data=Dict, index=range(n+1));
    print(df);

# Useless Methods..
# This values can get DistributionWithProbability.py
# Therefore, I don't continue
