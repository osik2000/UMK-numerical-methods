
% Użyć czterech wybranych, zaimplementowanych (*)
% metod OCTAVE do rozwiązania układów równań liniowych Ax = b dla:


% a) A kwadratowej, nieosobliwej

A = hilb(5);
b = [5; 71/20; 197/70; 657/280; 1271/630];
% x powinien byc rowny: [1; 2; 3; 4; 5]

% Metoda 1: Backslash
x_1 = A \ b;
disp("\nBackslash:");
disp(x_1);

% Metoda 2: BiConjugate Gradient (BiCG) *macierz musi byc kwadratowa*
disp("\nBICG:");
x_2 = bicg(A, b);
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

