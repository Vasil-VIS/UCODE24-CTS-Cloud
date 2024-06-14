from math import sinh, cosh, asinh, sqrt


class Computation:
    def __init__(self, s, k, h, w):
        self.s = s
        self.k = k
        self.h = h
        self.w = w
        self.H = k*w
        self.xR = self.compute_xr()
        self.xL = self.compute_xl()
        self.y_xR = self.compute_y_xr()
        self.y_xL = self.compute_y_l()
        self.L_xR = self.compute_L(self.xR)
        self.L_xL = self.compute_L(self.xL)
        self.L_T = self.compute_L_T()
        self.V_R = self.compute_V(self.L_xR)
        self.V_L = self.compute_V(self.L_xL)
        self.T_R = self.compute_T(self.V_R)
        self.T_L = self.compute_T(self.V_L)

    def compute_asinh(self, value):
        value = asinh(value)
        return value

    def compute_xr(self):
        return self.s/2 - self.k*self.compute_asinh((self.h/2)/(self.k*sinh((self.s/2)/self.k)))

    def compute_xl(self):
        return self.s - self.xR

    def compute_y_xr(self):
        value = (self.w*self.xR)/self.H
        cosine_h = cosh(value)-1
        return self.k*cosine_h
        
    def compute_y_l(self):
        return self.h + self.y_xR

    def compute_L(self, x):
        return self.k*sinh((self.w*x)/self.H)

    def compute_L_T(self):
        return self.L_xL + self.L_xR
    
    def compute_V(self, L):
        if self.h == 0:
            return (self.w*self.L_T)/2
        else:
            return self.w*L
    
    def compute_T(self, V):
        return sqrt(self.H**2 + V**2)