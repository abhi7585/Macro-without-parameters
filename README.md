# Macro-without-parameters
Developed a working of Macro expansion for an IBM 360 / 370 assembler. The main motive is to create macro expansion and create Macro Name Table and Macro Definition Table. 

Aim: Defining a macro without argument, expanding macro calls & generating expanded source code.
Instructions to the students:
1) Write a ALP using few instructions & Macro calls
2) Define domain/body of the Macro (3-5 instructions in a simple way)
3) Write a program which will replace each Macro call with its domain & performs expansion of the
Macro.
4) Show the input source code with Macro call & output the expanded source code
5) Also output the following statistics:
- Number of instructions in input source code (excluding Macro calls)
- Number of Macro calls
- Number of instructions defined in the Macro call
- Total number of instructions in the expanded source code.

Input 1: Input Source code with Macro calls
```
MOV R
ABHISHEK
DCR R
AND R
ABHISHEK
MUL 88
HALT
```
Input 2: Macro definition
```
MACRO
ABHISHEK
 ADD 30
 SUB 25
 OR R
MEND
```
Output source code after Macro expansion:
```
MOV R
ADD 30
SUB 25
OR R
DCR R
AND R
ADD 30
SUB 25
OR R
MUL 88
HALT
```
Statistical output:
Number of instructions in input source code (excluding Macro calls) = 5
Number of Macro calls = 2
Number of instructions defined in the Macro call = 3
Total number of instructions in the expanded source code = 11
