fis = mamfis();

fis = addInput(fis,[0 10],'Name','obsluga');
fis = addInput(fis,[0 10],'Name','jedzenie');

fis = addMF(fis,'obsluga','gaussmf',[1.5 0],'Name','slaba');
fis = addMF(fis,'obsluga','gaussmf',[1.5 5],'Name','dobra');
fis = addMF(fis,'obsluga','gaussmf',[1.5 10],'Name','wspaniala');

fis = addMF(fis,'jedzenie','trapmf',[-2 0 1 3],'Name','zepsute');
fis = addMF(fis,'jedzenie','trapmf',[7 9 10 12],'Name','wyborne');

fis = addOutput(fis,[-10 40],'Name','napiwek');
fis = addMF(fis,'napiwek','trimf',[-10 0 10],'Name','maly');
fis = addMF(fis,'napiwek','trimf',[10 15 20],'Name','sredni');
fis = addMF(fis,'napiwek','trimf',[ 20 , 30 ,40 ],'Name','duzy');

rule1 = "if obsluga is slaba then napiwek is maly";
rule2 = "if obsluga is dobra then napiwek is sredni";
rule3 = "if obsluga is wspaniala then napiwek is duzy";
rule4 = "if jedzenie is zepsute then napiwek is maly";
rule5 = "if jedzenie is wyborne then napiwek is duzy";
rules = [rule1; rule2; rule3; rule4; rule5];

fis = addRule(fis,rules);

figure;
subplot(2,1,1);
plotmf(fis,'input',1);
title('Obsluga');
subplot(2,1,2);
plotmf(fis,'input',2);
title('Jedzenie');
figure;
plotmf(fis,'output',1);
title('Napiwek');
figure;
gensurf(fis);
title('powierzchnia wyjścia systemu');


obsluga_val = 0;
jedzenie_val = 0;

input_vals = [obsluga_val, jedzenie_val];
napiwek_val = evalfis(input_vals, fis);
disp(['Wartość napiwku Min: ', num2str(napiwek_val)]);

obsluga_val = 10;
jedzenie_val = 10;

input_vals = [obsluga_val, jedzenie_val];
napiwek_val = evalfis(input_vals, fis);
disp(['Wartiwku ość napMax: ', num2str(napiwek_val)]);
