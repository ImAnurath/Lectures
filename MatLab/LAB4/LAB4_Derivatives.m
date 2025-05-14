% Define the function
f = @(x) exp(x);

% Reference point
x0 = 0;

% Step sizes
h1 = 0.1;
h2 = 0.01;
%%
% Analytical values
f_analytical = f(x0);  % f(x)
f1_analytical = exp(x0);  % f'(x)
f2_analytical = exp(x0);  % f''(x)

%% Numerical derivatives for h1
% First Column
f1_numerical1_h1 = (f(x0 + h1) - f(x0 - h1)) / (2 * h1); % First derivative
f2_numerical1_h1 = (f(x0 + h1) - 2 * f(x0) + f(x0 - h1)) / (h1^2); % Second derivative

% Second Column
f1_numerical2_h1 = (-f(x0 + 2*h1) + 8*f(x0 + h1) - 8*f(x0 - h1) + f(x0 - 2*h1)) / (12*h1); % First derivative
f2_numerical2_h1 = (-f(x0 + 2*h1) + 16*f(x0 + h1) - 30*f(x0) + 16*f(x0 - h1) - f(x0 - 2*h1)) / (12*h1^2);% Second derivative

%% Numerical derivatives for h2
% First Column
f1_numerical1_h2 = (f(x0 + h2) - f(x0 - h2)) / (2 * h2); % First derivative
f2_numerical1_h2 = (f(x0 + h2) - 2 * f(x0) + f(x0 - h2)) / (h2^2); % Second derivative

% Second Column
f1_numerical2_h2 = (-f(x0 + 2*h2) + 8*f(x0 + h2) - 8*f(x0 - h2) + f(x0 - 2*h2)) / (12*h2);% First derivative
f2_numerical2_h2 = (-f(x0 + 2*h2) + 16*f(x0 + h2) - 30*f(x0) + 16*f(x0 - h2) - f(x0 - 2*h2)) / (12*h2^2);% Second derivative

%% Relative errors

fprintf('\nRelative errors for Column 1 h1 = %.2f:\n', h1);
fprintf('Error in f''(x): %.5e\n', abs(f1_numerical1_h1 - f1_analytical) / abs(f1_analytical));
fprintf('Error in f''''(x): %.5e\n', abs(f2_numerical1_h1 - f2_analytical) / abs(f2_analytical));

fprintf('\nRelative errors for Column 1 h2 = %.2f:\n', h2);
fprintf('Error in f''(x): %.5e\n', abs(f1_numerical1_h2 - f1_analytical) / abs(f1_analytical));
fprintf('Error in f''''(x): %.5e\n', abs(f2_numerical1_h2 - f2_analytical) / abs(f2_analytical));

%%

fprintf('\nRelative errors for Column 2 h1 = %.2f:\n', h1);
fprintf('Error in f''(x): %.5e\n', abs(f1_numerical2_h1 - f1_analytical) / abs(f1_analytical));
fprintf('Error in f''''(x): %.5e\n', abs(f2_numerical2_h1 - f2_analytical) / abs(f2_analytical));

fprintf('\nRelative errors for Column 2 h2 = %.2f:\n', h2);
fprintf('Error in f''(x): %.5e\n', abs(f1_numerical2_h2 - f1_analytical) / abs(f1_analytical));
fprintf('Error in f''''(x): %.5e\n', abs(f2_numerical2_h2 - f2_analytical) / abs(f2_analytical));

%% 2. Given Function by data points
x3 = 0;
der_518 = (f(x3 + h1) - f(x3 - h1)) / (2 * h1); % First derivative
der_519 = (-f(x3 + 2*h1) + 8*f(x3 + h1) - 8*f(x3 - h1) + f(x3 - 2*h1)) / (12*h1); % First derivative
fprintf('First Derivate according to (5.1.8): %.5e\n', der_518);
fprintf('First Derivate according to (5.1.9): %.5e\n', der_519);

der_531 = (f(x3 + h1) - 2 * f(x3) + f(x3 - h1)) / (h1^2); % Second derivative
der_532 = (-f(x3 + 2*h1) + 16*f(x3 + h1) - 30*f(x3) + 16*f(x3 - h1) - f(x3 - 2*h1)) / (12*h1^2); % Second derivative
fprintf('Second Derivate according to (5.3.1): %.5e\n', der_531);
fprintf('Second Derivate according to (5.3.2): %.5e\n', der_532);

%% 3. Newton Part
x = [-0.2 -0.1 0 0.1 0.2];
y = [1.2214 1.1052 1 0.9048 0.8187];
middle_point = x3;

% Compute the divided differences table
n = length(x);
D = zeros(n, n);  % Divided differences table
D(:,1) = y';  % First column is y values

% Fill in the table with divided differences
for j = 2:n
    for i = 1:n-j+1
        D(i,j) = (D(i+1,j-1) - D(i,j-1)) / (x(i+j-1) - x(i));
    end
end

l2_prime = D(1,2);
l4_prime = D(1,4);
l2_double_prime = D(1,3);
l4_double_prime = D(1,5);

fprintf('First derivative at x = 0: %.4f\n', l2_prime);
fprintf('First derivative at x = 0: %.4f\n', l4_prime);
fprintf('Second derivative at x = 0: %.4f\n', l2_double_prime);
fprintf('Second derivative at x = 0: %.4f\n', l4_double_prime);