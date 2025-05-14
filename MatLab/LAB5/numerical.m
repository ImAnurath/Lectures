% Define constants
tau = 0.1;

Uin = @(t) (t <= 0.5);  % Uin is 1 for t <= 0.5, 0 for t > 0.5
% Define the differential equation as a function handle
ode = @(t, Uout) (Uin(t) - Uout) / tau;
% Define the time span (from 0 to 1)
tspan = [0 1];
% Initial condition for Uout at t=0
Uout0 = 0;
% Solve the differential equation using ode45
[t, Uout] = ode45(ode, tspan, Uout0);


% Plot the solution
figure;
plot(t, Uout, 'LineWidth', 2);
xlabel('Time (t)');
ylabel('Uout(t)');
title('Solution of the differential equation');
grid on;
