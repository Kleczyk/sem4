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
    


    left['S'] = fuzz.trimf(left.universe, [0, 0, MaxProximitiSignal])
    left['B'] = fuzz.trimf(left.universe, [0, MaxProximitiSignal, MaxProximitiSignal])

    front['S'] =fuzz.trimf(front.universe, [0, 0, MaxProximitiSignal])
    front['B'] =fuzz.trimf(front.universe, [0, MaxProximitiSignal, MaxProximitiSignal])

    right['S'] =fuzz.trimf(right.universe, [0, 0, MaxProximitiSignal])
    right['B'] =fuzz.trimf(right.universe, [0, MaxProximitiSignal, MaxProximitiSignal])

    vl['back'] = fuzz.trimf(vl.universe, [-MaxSpeed, -MaxSpeed, 0])
    vl['front'] = fuzz.trimf(vl.universe, [0,MaxSpeed, MaxSpeed])

    vr['back'] = fuzz.trimf(vr.universe, [-MaxSpeed, -MaxSpeed, 0])
    vr['front'] = fuzz.trimf(vr.universe, [0,MaxSpeed, MaxSpeed])
    
    left.view()
    vl.view()

    # rules definition
    # Rule in a fuzzy control system, connecting antecedent(s) to consequent(s)
    # rule1 =ctrl.Rule(antecedent=(left['S'] & front['S'] & right['S']),consequent=(vl['front'], vr['front']) )
    # rule2 =ctrl.Rule(antecedent=(left['S'] & front['S'] & right['B']),consequent=(vl['back'], vr['front']) )
    # rule3 =ctrl.Rule(antecedent=(left['S'] & front['B'] & right['S']),consequent=(vl['back'], vr['front']) )
    # rule4 =ctrl.Rule(antecedent=(left['S'] & front['B'] & right['B']),consequent=(vl['back'], vr['front']) )
    # rule5 =ctrl.Rule(antecedent=(left['B'] & front['S'] & right['S']),consequent=(vl['front'], vr['back']) )
    # rule6 =ctrl.Rule(antecedent=(left['B'] & front['B'] & right['S']),consequent=(vl['front'], vr['back']) )
    # rule7 =ctrl.Rule(antecedent=(left['B'] & front['S'] & right['B']),consequent=(vl['front'], vr['front']) )
    # rule8 =ctrl.Rule(antecedent=(left['B'] & front['B'] & right['B']),consequent=(vl['back'], vr['front']) )
    
    S
    #wersja z podążenim w strone światła
    
    # rule1 =ctrl.Rule(antecedent=(left['S'] & front['S'] & right['S']),consequent=(vl['front'], vr['front']) )  
    # rule2 =ctrl.Rule(antecedent=(left['S'] & front['S'] & right['B']),consequent=(vl['front'], vr['back']) )   
    # rule3 =ctrl.Rule(antecedent=(left['S'] & front['B'] & right['S']),consequent=(vl['front'], vr['front']) )  
    # rule4 =ctrl.Rule(antecedent=(left['S'] & front['B'] & right['B']),consequent=(vl['front'], vr['back']) )   
    # rule5 =ctrl.Rule(antecedent=(left['B'] & front['S'] & right['S']),consequent=(vl['back'], vr['front']) )   
    # rule6 =ctrl.Rule(antecedent=(left['B'] & front['B'] & right['S']),consequent=(vl['back'], vr['front']) )   
    # rule7 =ctrl.Rule(antecedent=(left['B'] & front['S'] & right['B']),consequent=(vl['front'], vr['back']) )   
    # rule8 =ctrl.Rule(antecedent=(left['B'] & front['B'] & right['B']),consequent=(vl['front'], vr['front']) )  
    
    FS = sf.FuzzySystem()
    
    MaxProximitiSignal = 4096
    MaxSpeed = 20000
    
    L_S = FuzzySet(points=[[0., 0.],  [MaxProximitiSignal, 1.]], term="S")
    L_B = FuzzySet(points=[[0., 1.], [MaxProximitiSignal,0]], term="B")
    FS.add_linguistic_variable("left", LinguisticVariable([L_S, L_B], concept="left"))
    
    R_S = FuzzySet(points=[[0., 0.],  [MaxProximitiSignal, 1.]], term="S")
    R_B = FuzzySet(points=[[0., 1.], [MaxProximitiSignal,0]], term="B")
    FS.add_linguistic_variable("right", LinguisticVariable([R_S, R_B], concept="right"))
    
    F_S= FuzzySet(points=[[0., 0.],  [MaxProximitiSignal, 1.]], term="S")
    F_B= FuzzySet(points=[[0., 1.], [MaxProximitiSignal,0]], term="B")
    FS.add_linguistic_variable("front", LinguisticVariable([F_S, F_B], concept="front"))
    
    

    FS.add_linguistic_variable("Service", LinguisticVariable([S_1, S_2, S_3], concept="Service quality"))

    
    
    # Create a fuzzy system object

    # A simple fuzzy inference system for the tipping problem
    # Create a fuzzy system object
    FS = FuzzySystem()

    # Define fuzzy sets and linguistic variables
    S_1 = FuzzySet(points=[[0., 1.],  [5., 0.]], term="poor")
    S_2 = FuzzySet(points=[[0., 0.], [5., 1.], [10., 0.]], term="good")
    S_3 = FuzzySet(points=[[5., 0.],  [10., 1.]], term="excellent")
    FS.add_linguistic_variable("Service", LinguisticVariable([S_1, S_2, S_3], concept="Service quality"))

    F_1 = FuzzySet(points=[[0., 1.],  [10., 0.]], term="rancid")
    F_2 = FuzzySet(points=[[0., 0.],  [10., 1.]], term="delicious")
    FS.add_linguistic_variable("Food", LinguisticVariable([F_1, F_2], concept="Food quality"))

    # Define output crisp values
    FS.set_crisp_output_value("small", 5)
    FS.set_crisp_output_value("average", 15)

    # Define function for generous tip (food score + service score + 5%)
    FS.set_output_function("generous", "Food+Service+5")

    # Define fuzzy rules
    R1 = "IF (Service IS poor) OR (Food IS rancid) THEN (Tip IS small)"
    R2 = "IF (Service IS good) THEN (Tip IS average)"
    R3 = "IF (Service IS excellent) OR (Food IS delicious) THEN (Tip IS generous)"
    FS.add_rules([R1, R2, R3])

    # Set antecedents values
    FS.set_variable("Service", 4)
    FS.set_variable("Food", 8)

    # Perform Sugeno inference and print output
    print(FS.Sugeno_inference(["Tip"]))

    
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
        sens = khep.k3ReadProximitySensors(s)
        print(sens)
        val_left = max(sens[1],sens[2])
        val_front = max(sens[3],sens[4])
        val_right = max(sens[5],sens[6])
        avoid_sym = k3FuzzyAvoidEval(avoid_sym, val_left, val_front, val_right)
        khep.k3SetSpeed(s,avoid_sym.output['vl'],avoid_sym.output['vr'])
        iter += 1
    
    
k3FuzzyAvoidLoop()
