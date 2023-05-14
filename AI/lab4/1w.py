import numpy as np
import nnet as net
import matplotlib.pyplot as plt

x = np.array([[-1.0, -0.9, -0.8, -0.7, -0.6, -0.5]])
y_t = np.array([[-0.9602, -0.5770, -0.0729, 0.3771, 0.6405, 0.6600]])

L = x.shape[0]
K1 = y_t.shape[0]
w1, b1 = net.nwlog(K1, L)
max_epoch = 2000
err_goal = 0.01
disp_freq = 100
lr = 0.1
SSE_vec = []

for epoch in range(1, max_epoch+1):
    y1 = net.logsig(np.dot(w1, x), b1)
    e = y_t - y1
    SSE = net.sumsqr(e)
    if np.isnan(SSE):
        break
    SSE_vec.append(SSE)
    
    
    if SSE < err_goal:
        break
    
    
    d1 = net.deltalog(y1, e) # bład
    dw1, db1 = net.learnbp(x, d1, lr) # wstaeczna propagacja
    w1 += dw1
    b1 += db1
    
    if (epoch % disp_freq) == 0:
        plt.clf()
        print("Epoch: %5d | SSE: %5.5f " % (epoch, SSE))
        plt.plot(x[0],y_t[0],'r',x[0],y1[0],'g')
        plt.grid()
        plt.show()
        plt.pause(1e-2)

print("Epoch: %5d | SSE: %5.5e " % (epoch, SSE))