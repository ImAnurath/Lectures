%LAB1
% Data
t_C = [13, 14, 17, 18, 19, 15, 13, 31, 32, 29, 27]';
t_F = [55, 58, 63, 65, 66, 59, 56, 87, 90, 85, 81]';

% Initial Parameters
initial_P_values = [1, 2, 3, 4]; % Different initial P values. Just randomly selected
theta_results = zeros(2, length(initial_P_values)); % End results

% Calculations for initial P vals
for idx = 1:length(initial_P_values)
    P = eye(2) * initial_P_values(idx); % Initial gain matrix
    theta = [0; 0]; % Initial guess for [k1; k2]

    % RLSE calculation
    for k = 1:length(t_C)
        % [Matrix 2x3] -> [Matrix 3x2]' 
        % Regressor vector: Phi_k = [t_C(k), 1]' 
        % This is the vector of regressors for the current data point.
        % The first element is the current input value t_C(k), and the second element is a constant term (1) for the bias.
        Phi_k = [t_C(k), 1]';

        % Prediction error: error = t_F(k) - Phi_k' * theta
        % This is the difference between the actual output value t_F(k) and the predicted output value based on the current parameters theta.
        % The predicted output value is calculated as the dot product of the regressor vector Phi_k and the parameter vector theta.
        error = t_F(k) - Phi_k' * theta;

        % Gain calculation: K = P * Phi_k / (1 + Phi_k' * P * Phi_k)
        % This is the gain calculation for the RLSE algorithm.
        % The gain K is a measure of how much the parameters should be updated based on the current error.
        % The denominator (1 + Phi_k' * P * Phi_k) is a normalization term that prevents the gain from becoming too large.
        % The term Phi_k' * P * Phi_k is the covariance of the regressor vector Phi_k with respect to the parameter vector theta.
        K = P * Phi_k / (1 + Phi_k' * P * Phi_k);

        % Parameter update: theta = theta + K * error
        % This is the update rule for the parameter vector theta.
        % The parameters are updated by adding the product of the gain K and the error.
        % This update rule is based on the gradient descent algorithm, which minimizes the mean squared error between the predicted and actual output values.
        theta = theta + K * error;

        % Covariance update: P = P - K * Phi_k' * P
        % This is the update rule for the covariance matrix P.
        % The covariance matrix P represents the uncertainty of the parameter vector theta.
        % The update rule is based on the Sherman-Morrison formula, which is a recursive formula for updating the inverse of a matrix.
        P = P - K * Phi_k' * P;
    end

    % Store results for current P
    theta_results(:, idx) = theta;
end

% Using pinv() for comparison
X = [t_C, ones(length(t_C), 1)];
theta_pinv = pinv(X) * t_F;

% Display Results
disp('Estimated parameters using RLSE for different initial P values:');
disp(theta_results);

disp('Estimated parameters using pinv():');
disp(theta_pinv);

% Plotting the dependency of k1 and k2 on initial P
figure;
subplot(2, 1, 1);
plot(initial_P_values, theta_results(1, :), '-o', 'LineWidth', 2);
xlabel('Initial P Value');
ylabel('k1');
title('Dependency of k1 on Initial P');
grid on;

subplot(2, 1, 2);
plot(initial_P_values, theta_results(2, :), '-o', 'LineWidth', 2);
xlabel('Initial P Value');
ylabel('k2');
title('Dependency of k2 on Initial P');
grid on;

% Plotting data points and fitted line for pinv()
figure;
scatter(t_C, t_F, 'filled');
hold on;
t_F_pred = X * theta_pinv;
plot(t_C, t_F_pred, '-r', 'LineWidth', 2);
xlabel('t_C [Celsius]');
ylabel('t_F [Fahrenheit]');
title('Observed Data and Fitted Line');
legend('Data Points', 'Fitted Line (pinv())', 'Location', 'Best');
grid on;
%AV
