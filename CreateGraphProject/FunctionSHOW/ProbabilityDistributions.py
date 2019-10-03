from Preferences import Distributions;

# Usage
# DistributionWithProbability.Distribution(*distribution parameters, switch)
# switch can have "f" or "F" values,
# if case "f", This program show Probability Distribution
# if case "F", show Cumulative Probability Distribution

# Available Distributions are existed in "Preferences/Distributions.py"
# Executed Distribution Graph is saved in "GraphSave" folder, the file name is "graphExample.png"
# Look at the Examples below

# ======================EXAMPLES====================== #

# Discrete Distributions
Distributions.DiscreteUniformDistribution(1, 7, "f");
Distributions.BinomialDistribution(10, 0.5, "f");
Distributions.HypergeometricDistribution(100, 40, 32, "f");
Distributions.GeometricDistribution(0.1, "f");
Distributions.NegativeBinomialDistribution(10, 0.3, "f");
Distributions.PoissonDistribution(9, "f");

# Continuous Distributions
Distributions.ContinuousUniformDistribution(2,20,"f");
Distributions.NormalDistribution(10, 2, "f");
Distributions.ExponentialDistribution(0.5, "f");
Distributions.GammaDistribution(9, 0.5, "f");

# chi-Square, t, F Distribution
Distributions.chi_SquareDistribution(8, "f");
Distributions.t_Distribution(5, "f");
Distributions.F_Distribution(4, 5, "f");