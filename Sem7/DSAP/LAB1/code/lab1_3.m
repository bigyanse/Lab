clc;
close all;
a = 5;
f = 3;
t = 0:0.01:1;
x = a * cos(2 * pi* f * t);
plot(t, x);
xlabel('time');
ylabel('amplitude');
title('Continuous Cosine/Bigyan Dahal/ACE076BCT025');
grid on;