# Discrete Distribution
# DU(a,b), B(n,p), H(N,n,k), G(p), NB(k, p), P(lambda)
# Continuous Distribution
# CU(a,b), N(myu, sigmaSquare), E(lamb), GAM(r, theta)
# chi-Square(phi), t(phi), F(phi1, phi2)

import numpy as np;
from Preferences import MadeBarChartOrPlot, Fomulas, DistributionsFactors, ProbabilityValue;

def NormalDistribution(myu, sigmaSquare, switch):
    Dist = DistributionsFactors.N(myu, sigmaSquare);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(myu-5*sigmaSquare, myu+5*sigmaSquare+0.01, 0.01);
    y_values = [Fomulas.N(x, myu, sigmaSquare) for x in x_params];
    P = ProbabilityValue.CP(x_params, y_values, 7, 10);

    MadeBarChartOrPlot.plot(x_params, y_values, switch, "Normal Distribution", myu, sigmaSquare);
    print(f"E(X)={E}, V(X)={V}");
    print(f"P = {P}");

def BinomialDistribution(n ,p, switch):
    Dist = DistributionsFactors.B(n, p);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(0, n+1, 1);
    y_values = [Fomulas.B(x, n, p) for x in x_params];
    #P = ProbabilityValue.DP(x_params, y_values, 3, 6);

    MadeBarChartOrPlot.barChart(x_params, y_values, switch, "Binomial Distribution", n, p);

    print(f"E(X)={E}, V(X)={V}");
    #print(f"P = {P}");

def DiscreteUniformDistribution(a, b, switch):
    Dist = DistributionsFactors.DU(1/(b-a+1));
    E = Dist.ExpectedValue(a, b);
    V = Dist.Variance();
    x_params = np.arange(a, b+1, 1);
    y_values = [Fomulas.DU(x,1/(b-a+1)) for x in x_params];

    MadeBarChartOrPlot.barChart(x_params, y_values, switch, "Discrete Uniform Distribution", 1/(b-a+1));
    print(f"E(X)={E}, V(X)={V}");

# Not Completed
def HypergeometricDistribution(N, n, k, switch):
    Dist = DistributionsFactors.H(N, n, k);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(0, k, 1); # k modification need
    y_values = [Fomulas.H(x,N,n,k) for x in x_params];

    MadeBarChartOrPlot.barChart(x_params, y_values, switch, "HyperGeometric Distribution", N, n, k);
    print(f"E(X)={E}, V(X)={V}");

def GeometricDistribution(p, switch):
    Dist = DistributionsFactors.G(p);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(1, 50, 1);
    y_values = [Fomulas.G(x,p) for x in x_params];

    MadeBarChartOrPlot.barChart(x_params, y_values, switch, "Geometric Distribution", p);
    print(f"E(X)={E}, V(X)={V}");

def NegativeBinomialDistribution(k, p, switch):
    Dist = DistributionsFactors.NB(k, p);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(k, 10*k, 1);
    y_values = [Fomulas.NB(x,k,p) for x in x_params];

    MadeBarChartOrPlot.barChart(x_params, y_values, switch, "Negative Binomial Distribution", k, p);
    print(f"E(X)={E}, V(X)={V}");

def PoissonDistribution(lamb, switch):
    Dist = DistributionsFactors.P(lamb);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = range(2*lamb);
    y_values = [Fomulas.P(x, lamb) for x in x_params];

    MadeBarChartOrPlot.barChart(x_params, y_values, switch, "Poisson Distribution", lamb);
    print(f"E(X)={E}, V(X)={V}");

def ContinuousUniformDistribution(a, b, switch):
    Dist = DistributionsFactors.CU(a, b);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(a, b+1, 0.01);
    y_values = [Fomulas.CU(x,a,b) for x in x_params];

    MadeBarChartOrPlot.plot(x_params, y_values, switch, "Continuous Uniform Distribution", a, b);
    print(f"E(X)={E}, V(X)={V}");

def ExponentialDistribution(lamb, switch):
    Dist = DistributionsFactors.E(lamb);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(0, 10, 0.01); # Modification Need
    y_values = [Fomulas.E(x, lamb) for x in x_params];

    MadeBarChartOrPlot.plot(x_params, y_values, switch, "Exponential Distribution", lamb);
    print(f"E(X)={E}, V(X)={V}");

def GammaDistribution(r, theta, switch):
    Dist = DistributionsFactors.GAM(r, theta);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(0.01, 20, 0.01);
    y_values = [Fomulas.GAM(x, r, theta) for x in x_params];

    MadeBarChartOrPlot.plot(x_params, y_values, switch, "GAMMA Distribution", r, theta);
    print(f"E(X)={E}, V(X)={V}");

def chi_SquareDistribution(phi, switch):
    Dist = DistributionsFactors.chiSquare(phi);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(0, 4*phi, 0.01);
    y_values = [Fomulas.chiSquare(x,phi) for x in x_params];

    MadeBarChartOrPlot.plot(x_params, y_values, switch, "chi-Square Distribution", phi);
    print(f"E(X)={E}, V(X)={V}");

def t_Distribution(phi, switch):
    Dist = DistributionsFactors.t(phi);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(-5, 5, 0.01);
    y_values = [Fomulas.t(x, phi) for x in x_params];

    MadeBarChartOrPlot.plot(x_params, y_values, switch, "t Distribution", phi);
    print(f"E(X)={E}, V(X)={V}");

def F_Distribution(phi1, phi2, switch):
    Dist = DistributionsFactors.F(phi1, phi2);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(0, 10, 0.01);
    y_values = [Fomulas.F(x, phi1, phi2) for x in x_params];

    MadeBarChartOrPlot.plot(x_params, y_values, switch, "F Distribution", phi1, phi2);
    print(f"E(X)={E}, V(X)={V}");