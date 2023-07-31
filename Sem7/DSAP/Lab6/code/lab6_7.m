clc;
clear all;
close all;
t=0:0.001:1;
cwtstruct=cwtft((cos(2*3.14*1000*t)), 'plot');