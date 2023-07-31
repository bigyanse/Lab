clc;
clear all;
close all;
x1=input('Input sequence x[n]: ');
x2=input('Starting time index of x[n]: ');
h1=input('Impulse response h[n]: ');
h2=input('Starting time index of h[n]: ');
y=conv(x1,h1);
n=x2+h2:length(y)+x2+h2-1;
display('The convoluted sequence is given below');
y
stem(n,y);
xlabel('time');
ylabel('amplitude');
title('Linear Convolution/Bigyan Dahal/ACE076BCT025');
grid on;