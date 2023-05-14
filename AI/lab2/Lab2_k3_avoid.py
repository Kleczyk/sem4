import skfuzzy as fuzz
from skfuzzy import control as ctrl
import simpful as sf
import numpy as np
import khepera3 as khep

def k3FuzzyAvoidDef():
    MaxProximitiSignal = 4096
    MaxSpeed = 20000
    left = ctrl.Antecedent(np.arange(0,MaxProximitiSignal,1), 'left')
    front = ctrl.Antecedent(np.arange(0,MaxProximitiSignal,1), 'front')
    right = ctrl.Antecedent(np.arange(0,MaxProximitiSignal,1), 'right')
    vl = ctrl.Consequent(np.arange(0,MaxSpeed,1), 'v1')
    vr = ctrl.Consequent(np.arange(0,MaxSpeed,1), 'v2')
    
    left['B'] = fuzz.trimf(left.universe, [0, 0, MaxProximitiSignal])
    left['S'] = fuzz.trimf(left.universe, [0, MaxProximitiSignal, MaxProximitiSignal])

    front['B'] =fuzz.trimf(front.universe, [0, 0, MaxProximitiSignal])
    front['S'] =fuzz.trimf(front.universe, [0, MaxProximitiSignal, MaxProximitiSignal])

    right['B'] =fuzz.trimf(right.universe, [0, 0, MaxProximitiSignal])
    right['S'] =fuzz.trimf(right.universe, [0, MaxProximitiSignal, MaxProximitiSignal])

    vl['back'] = fuzz.trimf(vl.universe, [-MaxSpeed, -MaxSpeed, 0])
    vl['front'] = fuzz.trimf(vl.universe, [0,MaxSpeed, MaxSpeed])

    vr['back'] = fuzz.trimf(vr.universe, [-MaxSpeed, -MaxSpeed, 0])
    vr['front'] = fuzz.trimf(vr.universe, [0,MaxSpeed, MaxSpeed])

    # rules definition
    # Rule in a fuzzy control system, connecting antecedent(s) to consequent(s)
    rule1 =ctrl.Rule(antecedent=(left['S'] & front['S'] & right['S']),consequent=(vl['front'], vr['front']) )
    rule2 =ctrl.Rule(antecedent=(left['S'] & front['S'] & right['B']),consequent=(vl['back'], vr['front']) )
    rule3 =ctrl.Rule(antecedent=(left['S'] & front['B'] & right['S']),consequent=(vl['back'], vr['front']) )
    rule4 =ctrl.Rule(antecedent=(left['S'] & front['B'] & right['B']),consequent=(vl['back'], vr['front']) )
    rule5 =ctrl.Rule(antecedent=(left['B'] & front['S'] & right['S']),consequent=(vl['front'], vr['back']) )
    rule6 =ctrl.Rule(antecedent=(left['B'] & front['B'] & right['S']),consequent=(vl['front'], vr['back']) )
    rule7 =ctrl.Rule(antecedent=(left['B'] & front['S'] & right['B']),consequent=(vl['front'], vr['front']) )
    rule8 =ctrl.Rule(antecedent=(left['B'] & front['B'] & right['B']),consequent=(vl['back'], vr['front']) )
    
    
    #wersja z podążenim w strone światła
    
    # rule1 =ctrl.Rule(antecedent=(left['S'] & front['S'] & right['S']),consequent=(vl['front'], vr['front']) )  
    # rule2 =ctrl.Rule(antecedent=(left['S'] & front['S'] & right['B']),consequent=(vl['front'], vr['back']) )   
    # rule3 =ctrl.Rule(antecedent=(left['S'] & front['B'] & right['S']),consequent=(vl['front'], vr['front']) )  
    # rule4 =ctrl.Rule(antecedent=(left['S'] & front['B'] & right['B']),consequent=(vl['front'], vr['back']) )   
    # rule5 =ctrl.Rule(antecedent=(left['B'] & front['S'] & right['S']),consequent=(vl['back'], vr['front']) )   
    # rule6 =ctrl.Rule(antecedent=(left['B'] & front['B'] & right['S']),consequent=(vl['back'], vr['front']) )   
    # rule7 =ctrl.Rule(antecedent=(left['B'] & front['S'] & right['B']),consequent=(vl['front'], vr['back']) )   
    # rule8 =ctrl.Rule(antecedent=(left['B'] & front['B'] & right['B']),consequent=(vl['front'], vr['front']) ) 
    
    
    rule1 =ctrl.Rule(antecedent=(left['S'] & front['S'] & right['S']),consequent=(vl['front'],  vr['front']) )  
    rule2 =ctrl.Rule(antecedent=(left['S'] & front['S'] & right['B']),consequent=(vl['front'],  vr['back']) )   
    rule3 =ctrl.Rule(antecedent=(left['S'] & front['B'] & right['S']),consequent=(vl['front'],  vr['front']) )  
    rule4 =ctrl.Rule(antecedent=(left['S'] & front['B'] & right['B']),consequent=(vl['front'],  vr['back']) )   
    rule5 =ctrl.Rule(antecedent=(left['B'] & front['S'] & right['S']),consequent=(vl['back'],   vr['front']) )   
    rule6 =ctrl.Rule(antecedent=(left['B'] & front['B'] & right['S']),consequent=(vl['back'],   vr['front']) )   
    rule7 =ctrl.Rule(antecedent=(left['B'] & front['S'] & right['B']),consequent=(vl['front'],  vr['back']) )   
    rule8 =ctrl.Rule(antecedent=(left['B'] & front['B'] & right['B']),consequent=(vl['front'],  vr['front']) )  
    

    
def k3FuzzyAvoidEval(avoid_sym, val_left, val_front, val_right):
    # Compute the fuzzy system
    avoid_sym.input['left'] = val_left
    avoid_sym.input['front'] = val_front
    avoid_sym.input['right'] = val_right
    avoid_sym.compute()
    # print('vl=',avoid_sym.output['vl'], ' vr=',avoid_sym.output['vr'])
    return avoid_sym

#LOOOOOOL

def k3FuzzyAvoidLoop(s):
    avoid_sym = khep.k3FuzzyAvoidDef() # do przygotowania w II części laboratorium
    res = False
    iter = 0
    while iter <= 1000:
        sens = khep.k3ReadAmbientSensors(s) 
        print(sens)
        val_left = max(sens[1],sens[2])
        val_front = max(sens[3],sens[4])
        val_right = max(sens[5],sens[6])
        avoid_sym = k3FuzzyAvoidEval(avoid_sym, val_left, val_front, val_right)
        khep.k3SetSpeed(s,avoid_sym.output['vl'],avoid_sym.output['vr'])
        iter += 1
    
    
k3FuzzyAvoidLoop()