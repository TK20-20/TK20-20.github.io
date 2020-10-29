import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def t(x):
    y = x == 0 
    return y

plt.subplot(321)
x3=np.linspace(-5, 5,11)
y3=t(x3)
plt.stem(x3,y3)
plt.grid(True)
plt.title('冲激序列')

def u(x):
    y = x > 0
    return y

plt.subplot(322)
x4=np.linspace(-5, 5, 10)
y4=u(x4)
plt.stem(x4,y4)
plt.grid(True)
plt.title('阶跃序列')

x=np.linspace(0,5,20)
plt.subplot(323)
y2=np.sin(0.5*np.pi*x+2)
plt.title(r'正弦序列$x(n)=sin(π/2*x+2)$')
plt.grid(True)
plt.stem(x,y2)

x1=np.linspace(0,10,10)
plt.subplot(324)
y5=0.6**x1
plt.grid(True)
plt.title(r'实指数序列$x(n)=0.6^x$')
plt.stem(x1,y5)

X=[2,1.5,1,0.5];y1=[]
for i in range(32):
      y1.append(X[i%4])

plt.subplot(325)
x5=np.linspace(0,5,20)
y5=x5
plt.stem(x5,y5)
plt.grid(True)
plt.title(r'纯虚数指数序列')

plt.subplot(326)
y5=[8,3.4,1.8,5.6,2.9,0.7]
plt.grid(True)
plt.title(r'复指数序列')
plt.stem(y5)

plt.show()