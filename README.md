# PyTriggerBSOD
A simple python function that forces a BSOD on Windows computers

This was translated from https://github.com/bemxio/mario-head/blob/main/main.cpp \
Tested on:
 - Windows 10 Pro

## How to use
Put BSOD.py in the same folder as your program, then add the import line:
```python
import BSOD
```
When you want to trigger a BSOD in your program, you simply type:
```python
BSOD.trigger()
```

## How to use it without importing it
If you don't want to import the module, you can import all the required BSOD modules in your file and then copy over the `trigger()` function to the file you are using.

# THIS ONLY WORKS ON WINDOWS
It will prevent the application from being cross-platform.
