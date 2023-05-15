
% Użyć czterech wybranych, zaimplementowanych (*)
% metod OCTAVE do rozwiązania układów równań liniowych Ax = b dla:


% a) A kwadratowej, nieosobliwej

A1 = hilb(5);
b1 = [5; 71/20; 197/70; 657/280; 1271/630];
% x powinien byc rowny: [1; 2; 3; 4; 5]

% Metoda 1: Backslash
x_bs = A1 \ b1;
disp("\nBackslash:");
disp(x_bs);

% b) A kwadratowej osobliwej
% Metoda 2: BiConjugate Gradient (BiCG) *macierz musi byc kwadratowa*

A2 = [1, 2, 3; 4, 5, 6; 7, 8, 9];
b2 = [14; 32; 50];
max_iterations = 1000;
tolerance = 1e-6;

% x powinien byc rowny: [1;2;3]
disp("\nBICG:");
x_bicg = bicg(A2, b2, tolerance, max_iterations);
disp(x_bicg);

% c) A prostokątnej z większą liczbą kolumn
% Metoda 3: LSQNONNEG
pkg load optim;
disp("\nlsqnonneg:");
A3 = [1,2,3;4,5,6];
b3 = [14; 32];
x_lsqnonneg = lsqnonneg(A3, b3);
disp(x_lsqnonneg);

% d) A prostokątnej z większa liczbą wierszy
% Metoda 4 pinv:
disp("\pinv (A/b):");
A4 = [1, 2; 3, 4; 5, 6];
b4 = [7; 8; 9];

x_4 = pinv(A4) * b4;
disp(x_4);

