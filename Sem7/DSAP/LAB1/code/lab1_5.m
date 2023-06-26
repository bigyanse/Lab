clc;
close all;
a = 5;
f = 3;
t = 0:0.01:1;
x = a * sin(2 * pi* f * t);
y = a * cos(2 * pi* f * t);
subplot(221);
plot(t, x);
xlabel('time');
ylabel('amplitude');
title('Continuous Sine/Bigyan Dahal/ACE076BCT025');

subplot(222);
stem(t, x);
xlabel('time');
ylabel('amplitude');
title('Discrete Sine/Bigyan Dahal/ACE076BCT025');

subplot(223);
plot(t, y);
xlabel('time');
ylabel('amplitude');
title('Continuous Cosine/Bigyan Dahal/ACE076BCT025');

subplot(224);
stem(t, y);
xlabel('time');
ylabel('amplitude');
title('Discrete Cosine/Bigyan Dahal/ACE076BCT025');
grid on;