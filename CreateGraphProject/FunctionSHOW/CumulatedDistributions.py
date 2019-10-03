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

# Discrete Cumulative Distributions
Distributions.DiscreteUniformDistribution(1, 7, "F");
Distributions.BinomialDistribution(10, 0.5, "F");
Distributions.HypergeometricDistribution(100, 40, 32, "F");
Distributions.GeometricDistribution(0.1, "F");
Distributions.NegativeBinomialDistribution(10, 0.3, "F");
Distributions.PoissonDistribution(9, "F");

# Continuous Cumulative Distributions
Distributions.ContinuousUniformDistribution(2,20,"F");
Distributions.NormalDistribution(10, 2, "F");
Distributions.ExponentialDistribution(0.5, "F");
Distributions.GammaDistribution(9, 0.5, "F");

# chi-Square, t, F Cumulative Distribution
Distributions.chi_SquareDistribution(8, "F");
Distributions.t_Distribution(5, "F");
Distributions.F_Distribution(4, 5, "F");