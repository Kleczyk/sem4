

import skfuzzy as fuzz
from skfuzzy import control as ctrl
import simpful as sf
import numpy as np


FS = sf.FuzzySystem()
MaxProximitiSignal = 4096
MaxSpeed = 20000

L_S = sf.FuzzySet(points=[[0., 0.],  [MaxProximitiSignal, 1.]], term="S")
L_B = sf.FuzzySet(points=[[0., 1.], [MaxProximitiSignal,0]], term="B")
FS.add_linguistic_variable("left", sf.LinguisticVariable([L_S, L_B], concept="left"))

R_S = sf.FuzzySet(points=[[0., 0.],  [MaxProximitiSignal, 1.]], term="S")
R_B = sf.FuzzySet(points=[[0., 1.], [MaxProximitiSignal,0]], term="B")
FS.add_linguistic_variable("right", sf.LinguisticVariable([R_S, R_B], concept="right"))

F_S= sf.FuzzySet(points=[[0., 0.],  [MaxProximitiSignal, 1.]], term="S")
F_B= sf.FuzzySet(points=[[0., 1.], [MaxProximitiSignal,0]], term="B")
FS.add_linguistic_variable("front", sf.LinguisticVariable([F_S, F_B], concept="front"))


FS.set_crisp_output_value("left_while_front", -MaxSpeed)
FS.set_crisp_output_value("left_while_back", MaxSpeed)

FS.set_crisp_output_value("right_while_front", -MaxSpeed)
FS.set_crisp_output_value("right_while_back", MaxSpeed)


 # rule1 =ctrl.Rule(antecedent=(left['S'] & front['S'] & right['S']),consequent=(vl['front'], vr['front']) )
 # rule2 =ctrl.Rule(antecedent=(left['S'] & front['S'] & right['B']),consequent=(vl['back'], vr['front']) )
 # rule3 =ctrl.Rule(antecedent=(left['S'] & front['B'] & right['S']),consequent=(vl['back'], vr['front']) )
 # rule4 =ctrl.Rule(antecedent=(left['S'] & front['B'] & right['B']),consequent=(vl['back'], vr['front']) )
 # rule5 =ctrl.Rule(antecedent=(left['B'] & front['S'] & right['S']),consequent=(vl['front'], vr['back']) )
 # rule6 =ctrl.Rule(antecedent=(left['B'] & front['B'] & right['S']),consequent=(vl['front'], vr['back']) )
 # rule7 =ctrl.Rule(antecedent=(left['B'] & front['S'] & right['B']),consequent=(vl['front'], vr['front']) )
 # rule8 =ctrl.Rule(antecedent=(left['B'] & front['B'] & right['B']),consequent=(vl['back'], vr['front']) )
 
# Define fuzzy rules
R1 = "IF (left IS S) AND (front IS S) AND (right IS S) THEN (vl IS left_while_front)  "  #AND (vr IS right_while_front))
R2 = "IF (left IS S) AND (front IS S) AND (right IS B) THEN (vl IS left_while_back)  "  #AND (vr IS right_while_front)
R3 = "IF (left IS S) AND (front IS B) AND (right IS S) THEN (vl IS left_while_back)   "  #AND (vr IS right_while_front))
R4 = "IF (left IS S) AND (front IS B) AND (right IS B) THEN (vl IS left_while_back)   "  #AND (vr IS right_while_front))
R5 = "IF (left IS B) AND (front IS S) AND (right IS S) THEN (vl IS left_while_front) "  #AND (vr IS right_while_back))
R6 = "IF (left IS B) AND (front IS B) AND (right IS S) THEN (vl IS left_while_front) "  #AND (vr IS right_while_back))
R7 = "IF (left IS B) AND (front IS S) AND (right IS B) THEN (vl IS left_while_front)  "  #AND (vr IS right_while_front))
R8 = "IF (left IS B) AND (front IS B) AND (right IS B) THEN (vl IS left_while_back)   "  #AND (vr IS right_while_front))

R9= "IF (left IS S) AND (front IS S) AND (right IS S) THEN   (vr IS right_while_front)"
R10 = "IF (left IS S) AND (front IS S) AND (right IS B) THEN (vr IS right_while_front)"
R11 = "IF (left IS S) AND (front IS B) AND (right IS S) THEN  (vr IS right_while_front)"
R12 = "IF (left IS S) AND (front IS B) AND (right IS B) THEN  (vr IS right_while_front)"
R13 = "IF (left IS B) AND (front IS S) AND (right IS S) THEN (vr IS right_while_back)"
R14 = "IF (left IS B) AND (front IS B) AND (right IS S) THEN (vr IS right_while_back)"
R15 = "IF (left IS B) AND (front IS S) AND (right IS B) THEN  (vr IS right_while_front)"
R16 = "IF (left IS B) AND (front IS B) AND (right IS B) THEN  (vr IS right_while_front)"




FS.add_rules([R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R11, R12 , R13 ,R14, R15, R16])

FS.set_variable("left", 100)
FS.set_variable("front", 3000)
FS.set_variable("right", 3000)




outputs=FS.Sugeno_inference(["vr","vl"])
print(outputs['vr'])
print(outputs['vl'])
 
x=outputs['vl']

print(x,f"shape : {x.shape} type : {type(x)}  ")


FS.plot_variable("left")
# FS.plot_variable("front")
# FS.plot_variable("right")




#FS.plot_surface(["left", "right"], output, detail=40, color_map='plasma')


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Przykładowe dane
x = np.linspace(0, 4000, 10)
y = np.linspace(0, 4000, 10)
X, Y = np.meshgrid(x, y)

right = np.arange(0, 4000, 10)

z = np.zeros_like(x)

for i in range(10):
    for j in range(10):
        FS.set_variable("left", x[i])
        FS.set_variable("front", y[j])
        FS.set_variable("right", 0)
        outputs=FS.Sugeno_inference(["vr","vl"])
        z[i][j]=outputs['vl']
        # print(f"left: {left[i]} front: {front[j]} vl: {vl[i][j]}")
        # print(f"i {i} j {j}")
        #print(outputs['vl'])
        
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
print(left.shape)
print(front.shape)
print(vl.shape)
print(type(left))
print(type(front))
print(type(vl))
surf = ax.plot_surface(x, y, z)



# # Inicjowanie wykresu
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Rysowanie powierzchni
# surf = ax.plot_surface(x, y, z, cmap='coolwarm')

# Dodawanie etykiet osi
ax.set_xlabel('left')
ax.set_ylabel('front')
ax.set_zlabel('output vl')

# Dodawanie kolorowej mapy
fig.colorbar(surf)

# Wyświetlanie wykresu
plt.show()