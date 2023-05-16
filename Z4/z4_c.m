
% Użyć czterech wybranych, zaimplementowanych (*)
% metod OCTAVE do rozwiązania układów równań liniowych Ax = b dla:


% c) A prostokątnej z większą liczbą kolumn

A = [1,2,3;4,5,6];
b = [14; 32];

% x powinien byc rowny: [1;2;3] lub [2;0;4]

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

