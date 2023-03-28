fis = mamfis();

fis = addInput(fis,[-2 2],'Name','AA');
fis = addInput(fis,[-2 2],'Name','BB');

fis = addMF(fis,'AA','trapmf',[-5 -4 -2 0],'Name','A_1');
fis = addMF(fis,'AA','trimf',[-2 0 2],'Name','A_2');
fis = addMF(fis,'AA','trapmf',[0 2 4 5],'Name','A_3');

fis = addMF(fis,'BB','trapmf',[-5 -4 -2 0],'Name','B_1');
fis = addMF(fis,'BB','trimf',[-2 0 2],'Name','B_2');
fis = addMF(fis,'BB','trapmf',[0 2 4 5],'Name','B_3');


fis = addOutput(fis,[-1 1],'Name','CC');
fis = addMF(fis,'CC','trapmf',[-5 -4 -1 0],'Name','C_1');
fis = addMF(fis,'CC','trimf',[-1 0 1],'Name','C_2');
fis = addMF(fis,'CC','trapmf',[0 1 4 5],'Name','C_3');




rule1 = "If AA is A_1 and BB is B_2  then CC is C_1";
rule2 = "If AA is A_1 and BB is B_3  then CC is C_2";
rule3 = "If AA is A_2 and BB is B_2  then CC is C_2";
rule4 = "If AA is A_2 and BB is B_3  then CC is C_3";
rules = [rule1; rule2; rule3; rule4]

fis = addRule(fis,rules);

figure;
subplot(2,1,1);
plotmf(fis,'input',1);
title('AA');
subplot(2,1,2);
plotmf(fis,'input',2);
title('BB');
figure;
plotmf(fis,'output',1);
title('CC');
figure;
gensurf(fis);
title('Surface of outpout');


AA = -1.7;
BB = 0.9;

input_vals = [AA, BB];
CC_vals = evalfis(input_vals, fis);
disp(['Output CC :  ', num2str(CC_vals)]);





