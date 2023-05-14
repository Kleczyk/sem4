fis = mamfis();

fis = addInput(fis,[-2 2],'Name','X_1');
fis = addInput(fis,[-2 2],'Name','X_2');

fis = addMF(fis,'X_1','trapmf',[-5 -4 -2 0],'Name','A_1');
fis = addMF(fis,'X_1','trimf',[-2 0 2],'Name','A_2');
fis = addMF(fis,'X_1','trapmf',[0 2 4 5],'Name','A_3');

fis = addMF(fis,'X_2','trapmf',[-5 -4 -2 0],'Name','B_1');
fis = addMF(fis,'X_2','trimf',[-2 0 2],'Name','B_2');
fis = addMF(fis,'X_2','trapmf',[0 2 4 5],'Name','B_3');


fis = addOutput(fis,[-1 1],'Name','Y');
fis = addMF(fis,'Y','trapmf',[-5 -4 -1 0],'Name','C_1');
fis = addMF(fis,'Y','trimf',[-1 0 1],'Name','C_2');
fis = addMF(fis,'Y','trapmf',[0 1 4 5],'Name','C_3');




rule1 = "If X_1 is A_1 and X_2 is B_2  then Y is C_1";
rule2 = "If X_1 is A_1 and X_2 is B_3  then Y is C_2";
rule3 = "If X_1 is A_2 and X_2 is B_2  then Y is C_2";
rule4 = "If X_1 is A_2 and X_2 is B_3  then Y is C_3";
rules = [rule1; rule2; rule3; rule4]

fis = addRule(fis,rules);

figure;
subplot(2,1,1);
plotmf(fis,'input',1);
title('X_1');
subplot(2,1,2);
plotmf(fis,'input',2);
title('X_2');
figure;
plotmf(fis,'output',1);
title('Y');
figure;
gensurf(fis);
title('Surface of outpout');


X_1 = -1.7;
X_2 = 0.9;

input_vals = [X_1, X_2];
Y_vals = evalfis(input_vals, fis);
disp(['Output Y :  ', num2str(Y_vals)]);





