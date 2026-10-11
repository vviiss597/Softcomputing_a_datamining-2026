import matplotlib.pyplot as plt
import numpy as np

class MathFunction:
    def __init__(self, name: str, function, color: str, style:str): # for 初始化
        # :str 只是提示不會影響輸出
        self.name = name
        self.function = function
        self.color = color
        self.style = style

    def evaluate(self, x):  # method that returns f(x) for an input array x
        return self.function(x)

    def plot(self, ax, x_range): # method that plots the curve on the given axis.
       y = self.evaluate(x_range)
       ax.plot(x_range, y, color = self.color, linestyle=self.style, label = self.name)

    def derivative(self, ax, x_range):
        y = self.evaluate(x_range) #f(x)的值
        dy_dx = np.gradient(y, x_range[1]-x_range[0]) 
        # dy/dx 求微分
        ax.plot(x_range, dy_dx, color = self.color, linestyle=self.style, label = self.name + "'")

def f(x): # MathFunction的function(callable)直接打f，不需要多打(x)
    return x**2
def g(x):
    return np.sin(x)
def h(x):
    return np.exp(x)

f = MathFunction("Quadratic", f, "red", "solid")
g = MathFunction("Sine", g, "blue", "dashed")
h = MathFunction("Exponential", h, "green", "dotted")


fig, ax = plt.subplots(figsize = (8, 6))

x_range = np.arange(-2, 2, 0.0001) 
#arange第三個值設定間格大小
#linspace則是設定間格大小

f.plot(ax, x_range)
g.plot(ax, x_range)
h.plot(ax, x_range)

ax.set_title("Function Comparison", fontsize=20, family="Arial", fontweight="bold")
ax.set_xlabel("x", fontsize=14, family="Arial")
ax.set_ylabel("f(x)", fontsize=14, family="Arial")
ax.grid(True)
ax.legend()


#2nd Plot for Derivatives

fig2, ax2 = plt.subplots(figsize = (8, 6))

f.derivative(ax2, x_range) #x_range已經設過了
g.derivative(ax2, x_range)
h.derivative(ax2, x_range)

ax2.set_title("Derivatives Comparison", fontsize=20, family="Arial", fontweight="bold")
ax2.set_xlabel("x", fontsize=14, family="Arial")
ax2.set_ylabel("f'(x)", fontsize=14, family="Arial")
ax2.grid(True)
ax2.legend()

plt.show()