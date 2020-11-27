# Analytical Solution of 2nd order DE: $ u'' + 2 u' + 5u = 0 $, $u(0)= 0 , u'(0) = 1 $.
# First rewrite this scalar problem to the standard form, $u' = Au$ .
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import expm

A = np.array([[0, 1], [-5, -2]])
u0 = np.transpose([0, 1])

t0 = 0
N = 60
h = 0.1
time = []
result = []
time.append(t0)
result.append(np.transpose(u0))
for k in range(1, N):
    t = k*h
    u = np.dot(expm(A*t),u0)
    result.append(np.transpose(u))
    time.append(t)

u1= np.zeros(len(time))
u2 = np.zeros(len(time))
for k in range(0, len(time)):
    u1[k] = result[k][0]
    u2[k] = result[k][1]

plt.figure(figsize=(10,7))
plt.subplot(2,1,1)
plt.plot(time,result)
plt.xlabel('t'), plt.ylabel('u')
plt.legend(('u1', 'u2'), loc = 0)
plt.grid()
plt.subplot(2,1,2)
plt.plot(u1,u2,u1[0],u2[0],'ro')
plt.xlabel('u1'), plt.ylabel('u2')
plt.legend(('(u_1(t), u_2(t))', 'initial condition'))
plt.title('The phase portriat')
plt.axis([-0.2, 0.4, -1, 2])
plt.grid()
plt.savefig('lcc.png', dpi=300, bbox_inches='tight')
plt.show()

