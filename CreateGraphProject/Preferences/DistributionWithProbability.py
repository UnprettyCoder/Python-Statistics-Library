# Discrete Distribution
# DU(a,b), B(n,p), H(N,n,k), G(p), NB(k, p), P(lambda)
# Continuous Distribution
# CU(a,b), N(myu, sigmaSquare), E(lamb), GAM(r, theta)
# chi-Square(phi), t(phi), F(phi1, phi2)

import numpy as np;
from Preferences import Fomulas, DistributionsFactors, ProbabilityExpressionInGraph;

def NormalDistribution(myu, sigmaSquare, startX, endX):
    Dist = DistributionsFactors.N(myu, sigmaSquare);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(myu-5*sigmaSquare, myu+5*sigmaSquare+0.01, 0.01);
    y_values = [Fomulas.N(x, myu, sigmaSquare) for x in x_params];

    print(f"E(X)={E}, V(X)={V}");
    ProbabilityExpressionInGraph.CPE("N", x_params, y_values, startX, endX, myu, sigmaSquare);
    
def BinomialDistribution(n ,p, startX, endX):
    Dist = DistributionsFactors.B(n, p);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = range(n+1);
    y_values = [Fomulas.B(x, n, p) for x in x_params];

    print(f"E(X)={E}, V(X)={V}");
    ProbabilityExpressionInGraph.DPE("B", x_params, y_values, startX, endX, n, p);
    
def DiscreteUniformDistribution(a, b, startX, endX):
    Dist = DistributionsFactors.DU(1/(b-a+1));
    E = Dist.ExpectedValue(a, b);
    V = Dist.Variance();
    x_params = range(a, b+1);
    y_values = [Fomulas.DU(x,1/(b-a+1)) for x in x_params];

    print(f"E(X)={E}, V(X)={V}");
    ProbabilityExpressionInGraph.DPE("DU", x_params, y_values, startX, endX, 1/(b-a+1));

# Not Completed
def HypergeometricDistribution(N, n, k, startX, endX):
    Dist = DistributionsFactors.H(N, n, k);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = range(k); # k modification need
    y_values = [Fomulas.H(x,N,n,k) for x in x_params];

    print(f"E(X)={E}, V(X)={V}");
    ProbabilityExpressionInGraph.DPE("H", x_params, y_values, startX, endX, N, n, k);

def GeometricDistribution(p, startX, endX):
    Dist = DistributionsFactors.G(p);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = range(1, 50);
    y_values = [Fomulas.G(x,p) for x in x_params];

    print(f"E(X)={E}, V(X)={V}");
    ProbabilityExpressionInGraph.DPE("G", x_params, y_values, startX, endX, p);

def NegativeBinomialDistribution(k, p, startX, endX):
    Dist = DistributionsFactors.NB(k, p);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = range(k, 10*k);
    y_values = [Fomulas.NB(x,k,p) for x in x_params];

    print(f"E(X)={E}, V(X)={V}");
    ProbabilityExpressionInGraph.DPE("NB", x_params, y_values, startX, endX, k, p);

def PoissonDistribution(lamb, startX, endX):
    Dist = DistributionsFactors.P(lamb);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = range(2*lamb);
    y_values = [Fomulas.P(x, lamb) for x in x_params];

    print(f"E(X)={E}, V(X)={V}");
    ProbabilityExpressionInGraph.DPE("P", x_params, y_values, startX, endX, lamb);

def ContinuousUniformDistribution(a, b, startX, endX):
    Dist = DistributionsFactors.CU(a, b);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(a, b+1, 0.01);
    y_values = [Fomulas.CU(x,a,b) for x in x_params];

    print(f"E(X)={E}, V(X)={V}");
    ProbabilityExpressionInGraph.CPE("CU", x_params, y_values, startX, endX, a, b);

def ExponentialDistribution(lamb, startX, endX):
    Dist = DistributionsFactors.E(lamb);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(0, 10, 0.01); # Modification Need
    y_values = [Fomulas.E(x, lamb) for x in x_params];

    print(f"E(X)={E}, V(X)={V}");
    ProbabilityExpressionInGraph.CPE("E", x_params, y_values, startX, endX, lamb);

def GammaDistribution(r, theta, startX, endX):
    Dist = DistributionsFactors.GAM(r, theta);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(0.01, 20, 0.01);
    y_values = [Fomulas.GAM(x, r, theta) for x in x_params];

    print(f"E(X)={E}, V(X)={V}");
    ProbabilityExpressionInGraph.CPE("GAM", x_params, y_values, startX, endX, r, theta);

def chi_SquareDistribution(phi, startX, endX):
    Dist = DistributionsFactors.chiSquare(phi);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(0, 4*phi, 0.01);
    y_values = [Fomulas.chiSquare(x,phi) for x in x_params];

    print(f"E(X)={E}, V(X)={V}");
    ProbabilityExpressionInGraph.CPE("chi-Square", x_params, y_values, startX, endX, phi);

def t_Distribution(phi, startX, endX):
    Dist = DistributionsFactors.t(phi);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(-5, 5, 0.01);
    y_values = [Fomulas.t(x, phi) for x in x_params];

    print(f"E(X)={E}, V(X)={V}");
    ProbabilityExpressionInGraph.CPE("t", x_params, y_values, startX, endX, phi);

def F_Distribution(phi1, phi2, startX, endX):
    Dist = DistributionsFactors.F(phi1, phi2);
    E = Dist.ExpectedValue();
    V = Dist.Variance();
    x_params = np.arange(0, 10, 0.01);
    y_values = [Fomulas.F(x, phi1, phi2) for x in x_params];

    print(f"E(X)={E}, V(X)={V}");
    ProbabilityExpressionInGraph.CPE("F", x_params, y_values, startX, endX, phi1, phi2);