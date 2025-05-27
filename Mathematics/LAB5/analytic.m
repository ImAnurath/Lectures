% Define symbolic variables
syms Uout(t) t
% Define RC as a constant
RC = 0.1;
% Solve the equation for t <= 0.5 (Uin = 1)
ode1 = diff(Uout, t) + Uout/RC == 1/RC;  % Uin = 1
cond1 = Uout(0) == 0;  % Initial condition at t = 0
Uout1(t) = dsolve(ode1, cond1);
% Solve the equation for t > 0.5 (Uin = 0)
ode2 = diff(Uout, t) + Uout/RC == 0;  % Uin = 0
% Use the value of Uout at t = 0.5 from the first solution as the initial condition for the second
cond2 = Uout(0.5) == Uout1(0.5);  
Uout2(t) = dsolve(ode2, cond2);
% Define a time vector from 0 to 1 with steps of 0.01
t_vals = 0:0.01:1;
% Evaluate the solutions numerically for both regions
Uout_vals = zeros(size(t_vals));
for i = 1:length(t_vals)
    t_val = t_vals(i);
    
    if t_val <= 0.5
        % Use the first solution for t <= 0.5
        Uout_vals(i) = double(Uout1(t_val));
    else
        % Use the second solution for t > 0.5
        Uout_vals(i) = double(Uout2(t_val));
    end
end

% Plot the solution
figure;
plot(t_vals, Uout_vals, 'LineWidth', 2);
xlabel('Time (t)');
ylabel('Uout(t)');
title('Solution of the differential equation');
grid on;
