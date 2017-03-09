# gesture-keyboard
Gesture keyboard is a library used to convert accelerometer data to a sequence of characters and sentences.

## Demostration Video
Click here to watch the demonstration video

## Module

In order to get the accelerometer data, I build a module using an Arduino, a MPU-6050 as accelerometer and a HC-06 to enable bluetooth comunication. The entire module gets powered by using a power bank.

![The Arduino Module](images/module.jpg)

When someone press the first button, the module starts to send accelerometer data to the pc.
When the button is relased, the transmission stops.

## Library

