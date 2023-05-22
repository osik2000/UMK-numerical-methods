% ============================== PRZYKLAD 1 ==============================

A1 = [4, 12, -16; 12, 37, -43; -16, -43, 98];
L1_1 = chol(A1, "lower");
s1 = sparse(A1);
L1_2 = full(ichol(s1));
%oczekiwany wynik L1 to =
%
%  [ 2   0   0]
%  [ 6   1   0]
%  [-8  -5   3]

disp("\nA1:");
disp(A1);
disp("\nL1_1 [chol(A1, \"lower\")]:");
disp(L1_1);
disp("\nL1_2 [full(ichol(sparse(A1)))]:");
disp(L1_2);
disp("\nL1 * L1^t:");
disp(L1_1 * L1_1');
disp("\n");

% ============================== PRZYKLAD 2 ==============================

A2 = [16, 4, 8, 4, 4; 4, 10, 2, 2, 2; 8, 2, 14, 6, 8; 4, 2, 6, 11, 5; 4, 2, 8, 5, 14];
L2_1 = chol(A2, "lower");
s2 = sparse(A2);
L2_2 = full(ichol(s2));
%oczekiwany wynik L2 to =
%
%   [4   0     0        0        0]
%   [1   3     0        0        0]
%   [2   0     3.1623   0        0]
%   [1   0.33  1.2649   2.879    0]
%   [1   0.33  2.8974   1.5171   1]

disp("\nA2:");
disp(A2);
disp("\nL2_1 [chol(A2, \"lower\")]:");
disp(L2_1);
disp("\nL2_2 [full(ichol(sparse(A2)))]:");
disp(L2_2);
disp("\nL2 * L2^t:");
disp(L2_1 * L2_1');
disp("\n");

% ============================== PRZYKLAD 3 ==============================

A3 = [9, 12; 12, 25];
L3_1 = chol(A3, "lower");
s3 = sparse(A3);
L3_2 = full(ichol(s3));
%oczekiwany wynik L3 to =
%
%   [3   0]
%   [4   3]

disp("\nA3:");
disp(A3);
disp("\nL3_1 [chol(A3, \"lower\")]:");
disp(L3_1);
disp("\nL3_2 [full(ichol(sparse(A3)))]:");
disp(L3_2);
disp("\nL3 * L3^t:");
disp(L3_1 * L3_1');
disp("\n");

% ============================== PRZYKLAD 4 ==============================

A4 = [36, -18, 0; -18, 17, 4; 0, 4, 21];
L = chol(A4)

L4_1 = chol(A4, "lower");
s4 = sparse(A4);
L4_2 = full(ichol(s4));
%oczekiwany wynik L4 to =
%
%  [ 6   0        0     ]
%  [-3   2.8284   0     ]
%  [ 0   1.4142   4.3589]

disp("\nA4:");
disp(A4);
disp("\nL4_1 [chol(A4, \"lower\")]:");
disp(L4_1);
disp("\nL4_2 [full(ichol(sparse(A4)))]:");
disp(L4_2);
disp("\nL4 * L4^t:");
disp(L4_1 * L4_1');
disp("\n");

% ============================== PRZYKLAD 5 ==============================

A5 = [4, 12, -16; 12, 37, -43; -16, -43, 98];
L5_1 = chol(A5, "lower");
s5 = sparse(A5);
L5_2 = full(ichol(s5));
%oczekiwany wynik L5 to =
%
%  [ 2   0   0]
%  [ 6   1   0]
%  [-8  -5   3]

disp("\nA5:");
disp(A5);
disp("\nL5_1 [chol(A5, \"lower\")]:");
disp(L5_1);
disp("\nL5_2 [full(ichol(sparse(A5)))]:");
disp(L5_2);
disp("\nL5 * L5^t:");
disp(L5_1 * L5_1');
disp("\n");

