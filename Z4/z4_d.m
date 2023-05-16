
% Użyć czterech wybranych, zaimplementowanych (*)
% metod OCTAVE do rozwiązania układów równań liniowych Ax = b dla:


% d) A prostokątnej z większa liczbą wierszy

A = [12 13 14; 14 15 16; 16 17 18; 18 19 20; 20 21 22];
b = [880;1012;1144;1276;1408];
% x powinien byc rowny: [11;22;33] lub [0;44;22]


% Metoda 1: Backslash
x_1 = A \ b;
disp("\nBackslash:");
disp(x_1);

% Metoda 2: Linsolve
disp("\nLINSOLVE");
x_2 = linsolve(A, b);
disp(x_2);

% Metoda 3: LSQNONNEG
pkg load optim;
disp("\nlsqnonneg:");
x_3 = lsqnonneg(A, b);
disp(x_3);

% Metoda 4 pinv:
disp("\pinv (A/b):");
x_4 = pinv(A) * b;
disp(x_4);

