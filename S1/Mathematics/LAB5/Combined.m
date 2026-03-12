%LAB5
% Analytical Solution (from analytic.m)
syms Uout(t) t
RC = 0.1;

% Solve the equation for t <= 0.5 (Uin = 1)
ode1 = diff(Uout, t) + Uout/RC == 1/RC;
cond1 = Uout(0) == 0;
Uout1(t) = dsolve(ode1, cond1);

% Solve the equation for t > 0.5 (Uin = 0)
ode2 = diff(Uout, t) + Uout/RC == 0;
cond2 = Uout(0.5) == Uout1(0.5);
Uout2(t) = dsolve(ode2, cond2);

% Evaluate analytical solution
t_vals = 0:0.01:1;
Uout_vals = zeros(size(t_vals));
for i = 1:length(t_vals)
    t_val = t_vals(i);
    if t_val <= 0.5
        Uout_vals(i) = double(Uout1(t_val));
    else
        Uout_vals(i) = double(Uout2(t_val));
    end
end

% Numerical Solution (from numerical.m)
tau = 0.1;
Uin = @(t) (t <= 0.5);
ode = @(t, Uout) (Uin(t) - Uout) / tau;
tspan = [0 1];
Uout0 = 0;
[t_num, Uout_num] = ode45(ode, tspan, Uout0);

% Plot Combined Results
figure;
plot(t_vals, Uout_vals, 'r-', 'LineWidth', 2, 'DisplayName', 'Analytical Solution');
hold on;
plot(t_num, Uout_num, 'b--', 'LineWidth', 2, 'DisplayName', 'Numerical Solution');
hold off;

% Add Labels and Legend
xlabel('Time (t)');
ylabel('Uout(t)');
title('Analytical vs Numerical Solution');
legend('show');
grid on;
%AV