
% Użyć czterech wybranych, zaimplementowanych (*)
% metod OCTAVE do rozwiązania układów równań liniowych Ax = b dla:


% b) A kwadratowej, osobliwej

A = [1, 2, 3; 4, 5, 6; 7, 8, 9];
b = [14; 32; 50];
max_iterations = 1000;
tolerance = 1e-6;
% x powinien byc rowny: [1;2;3] lub [-2;8;0] lub [2;0;4]

% Metoda 1: Backslash
x_1 = A \ b;
disp("\nBackslash:");
disp(x_1);

% Metoda 2: BiConjugate Gradient (BiCG) *macierz musi byc kwadratowa*
disp("\nBICG:");
x_2 = bicg(A, b, tolerance, max_iterations);
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

