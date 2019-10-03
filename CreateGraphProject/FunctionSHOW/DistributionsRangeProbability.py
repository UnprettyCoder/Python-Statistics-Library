from Preferences import DistributionWithProbability;

# Usage
# DistributionWithProbability.Distribution(*distribution parameters, minKey, maxKey)

# Available Distributions are existed in "Preferences/DistributionWithProbability.py"
# Executed Distribution Graph is saved in "GraphSave" folder, the file name is "graphExample.png"
# Look at the Examples below

# ======================EXAMPLES====================== #

# Discrete DistributionWithProbability
DistributionWithProbability.DiscreteUniformDistribution(1, 7, 2, 4);
DistributionWithProbability.BinomialDistribution(10, 0.5, 2, 5);
DistributionWithProbability.HypergeometricDistribution(100, 40, 32, 7, 15);
DistributionWithProbability.GeometricDistribution(0.1, 2, 6);
DistributionWithProbability.NegativeBinomialDistribution(10, 0.3, 11, 28);
DistributionWithProbability.PoissonDistribution(9, 1, 4);

# Continuous DistributionWithProbability
DistributionWithProbability.ContinuousUniformDistribution(2, 20, 4, 10);
DistributionWithProbability.NormalDistribution(10, 2, 11, 17);
DistributionWithProbability.ExponentialDistribution(0.5, 1, 5);
DistributionWithProbability.GammaDistribution(9, 0.5, 2, 7);

# chi-Square, t, F Distribution
DistributionWithProbability.chi_SquareDistribution(8, 1, 3);
DistributionWithProbability.t_Distribution(5, -6, -2);
DistributionWithProbability.F_Distribution(4, 5, 1, 4);