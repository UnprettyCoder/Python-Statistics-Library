# Discrete Distribution
# DU(a,b), B(n,p), H(N,n,k), G(p), NB(k, p), P(lambda)
# Continuous Distribution
# CU(a,b), N(myu, sigmaSquare), E(lamb), GAM(r, theta)
# chi-Square(phi), t(phi), F(phi1, phi2)

import math;

# nCr Definition
def combination(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r));

def DU(x, p):
    return p;

def B(x, n, p):
    return combination(n, x) * p ** x * (1 - p) ** (n - x);

def H(x, N, n, k):
    return (combination(k, x) * combination(N - k, n - x)) / combination(N, n);

def G(x, p):
    return p * (1 - p) ** (x - 1);

def NB(x, k, p):
    return combination(x - 1, k - 1) * p ** k * (1 - p) ** (x - k);

def P(x, lamb):
    return (lamb ** x * math.exp(-lamb)) / math.factorial(x);

def CU(x, a, b):
    return 1 / (b - a);

def N(x, myu, sigmaSquare):
    sigma = math.sqrt(sigmaSquare);
    return (1 / (math.sqrt(2 * math.pi * sigma ** 2))) * math.exp(-(x - myu) ** 2 / (2 * sigma ** 2));

def E(x, lamb):
    return lamb * math.exp(-lamb * x);

def GAM(x, r, theta):
    return (x ** (r - 1) * math.exp(-x / theta)) / (theta ** r * math.gamma(r));

def chiSquare(x, phi):
    return (x ** (phi / 2 - 1) * math.exp(-x / 2)) / (2 ** (phi / 2) * math.gamma(phi / 2));

def t(x, phi):
    return (math.gamma((phi + 1) / 2) * math.pow(1 + x ** 2 / phi, -(phi + 1) / 2)) / (math.sqrt(phi * math.pi) * math.gamma(phi / 2));

def F(x, phi1, phi2):
    return math.gamma((phi1 + phi2) / 2) * (phi1/phi2) ** (phi1/2) * x ** ((phi1 - 2) / 2) / (math.gamma(phi1 / 2) * math.gamma(phi2 / 2) * (1 + phi1/phi2 * x) ** ((phi1 + phi2) / 2));