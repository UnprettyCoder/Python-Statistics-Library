# Discrete Distribution
# DU(a,b), B(n,p), H(N,n,k), G(p), NB(k, p), P(lambda)
# Continuous Distribution
# CU(a,b), N(myu, sigmaSquare), E(lamb), GAM(r, theta)
# chi-Square(phi), t(phi), F(phi1, phi2)

from Preferences import Fomulas;
import math;

class Distributions:
    def __init__(self):
        pass;
    def ExpectedValue(self):
        return "ExpectedValue";
    def Variance(self):
        return "Variance";

class DU(Distributions):
    def __init__(self, p):
        self.p = p;
    def ExpectedValue(self, a, b):
        result = 0;
        for i in range(a,b+1):
            result += i * self.p;
        return result;
    def Variance(self):
        return 0;

class B(Distributions):
    def __init__(self, n, p):
        self.n = n;
        self.p = p;
    def ExpectedValue(self):
        return self.n * self.p;
    def Variance(self):
        return self.n * self.p * (1-self.p);

class H(Distributions):
    def __init__(self, N, n, k):
        self.N = N;
        self.n = n;
        self.k = k;
        self.p = k / N;
    def ExpectedValue(self):
        return self.n * self.k / self.N;
    def Variance(self):
        return self.n * self.p * (1-self.p) * (self.N - self.n) / (self.N - 1);

class G(Distributions):
    def __init__(self, p):
        self.p = p;
    def ExpectedValue(self):
        return 1 / self.p;
    def Variance(self):
        return (1-self.p) / self.p**2;

class NB(Distributions):
    def __init__(self, k, p):
        self.k = k;
        self.p = p;
    def ExpectedValue(self):
        return self.k / self.p;
    def Variance(self):
        return (self.k*(1-self.p)) / self.p**2;

class P(Distributions):
    def __init__(self, lamb):
        self.lamb = lamb;
    def ExpectedValue(self):
        return self.lamb;
    def Variance(self):
        return self.lamb;

class CU(Distributions):
    def __init__(self, a, b):
        self.a = a;
        self.b = b;
    def ExpectedValue(self):
        return (self.a+self.b) / 2;
    def Variance(self):
        return (self.a - self.b)**2 / 12;

class N(Distributions):
    def __init__(self, myu, sigmaSquare):
        self.myu = myu;
        self.sigmaSquare = sigmaSquare;
        self.sigma = math.sqrt(sigmaSquare);
    def ExpectedValue(self):
        return self.myu;
    def Variance(self):
        return self.sigmaSquare;

class E(Distributions):
    def __init__(self, lamb):
        self.lamb = lamb;
    def ExpectedValue(self):
        return 1 / self.lamb;
    def Variance(self):
        return 1 / self.lamb**2;

class GAM(Distributions):
    def __init__(self, r, theta):
        self.r = r;
        self.theta = theta;
    def ExpectedValue(self):
        return self.r / self.theta;
    def Variance(self):
        return self.r / self.theta**2;

class chiSquare(Distributions):
    def __init__(self, phi):
        self.phi = phi;
    def ExpectedValue(self):
        return self.phi;
    def Variance(self):
        return 2 * self.phi;

class t(Distributions):
    def __init__(self, phi):
        self.phi = phi;
    def ExpectedValue(self):
        return 0;
    def Variance(self):
        if self.phi > 2:
            return self.phi / (self.phi - 2);
        return "Variance is Not Founded because phi2 is less than or equal to 2"

class F(Distributions):
    def __init__(self, phi1, phi2):
        self.phi1 = phi1;
        self.phi2 = phi2;
    def ExpectedValue(self):
        if self.phi2 > 2:
            return self.phi2 / (self.phi2 - 2);
        return "ExpectedValue is Not Founded because phi2 is less than or equal to 2";
    def Variance(self):
        if self.phi2 > 4:
            return (2 * self.phi2**2 * (self.phi1+self.phi2-2)) / (self.phi1 * (self.phi2-2)**2 * (self.phi2-4));
        return "Variance is Not Founded because phi2 is less than or equal to 4";