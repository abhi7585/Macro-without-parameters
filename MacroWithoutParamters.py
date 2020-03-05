from sys import exit
motOpCode = ["MOV", "ADD", "SUB", "MUL", "DIV", "AND", "OR",
             "LOAD", "STORE", "DCR", "INC", "JMP", "JNZ", "HALT"]
keywords = ["MACRO", "CONST", "DOUBLE", "INT", "FLOAT", "SHORT", "LONG", "STRUCT", "IF", "ELSE", "FOR", "SWITCH",
            "CASE", "CHAR", "RETURN", "PRINTF", "SCANF", "AX", "BX", "CX", "DX", "AH", "BH", "CH", "DH", "AL", "BL", "CL", "DL"]
sourceCode = []
macroNames = []
macroDefinition = []
outputSourceCode = []
noOfInstructionSC = 0
noOfMacroCall = 0
expandedCode = 0

mc = int(input("Enter the number of Macro Definition code line : "))
for i in range(mc):
    instruction = input("Enter Macro code instruction {} :". format(i+1))
    macroDefinition.append(instruction)
macroDefinition = [element.upper() for element in macroDefinition]

if macroDefinition[0] == "MACRO" and macroDefinition[-1] == "MEND" and (macroDefinition[1] not in keywords) and (macroDefinition[1] not in motOpCode):
    macroNames.append(macroDefinition[1])
else:
    print("Invalid Macro Definition.")
    exit(0)

sc = int(input("Enter the number of Source code lines : "))
for i in range(sc):
    instruction = input("Enter Source code instruction {} : ". format(i+1))
    sourceCode.append(instruction)   
sourceCode = [element.upper() for element in sourceCode]
for i in range(sc):
    if sourceCode[i] in macroNames:
        noOfMacroCall = noOfMacroCall + 1
    else:    
        noOfInstructionSC = noOfInstructionSC + 1

for i in range(sc):
    if sourceCode[i] in macroNames:
        noOfInstructionMC = 0
        for j in range(2, mc-1):
            temp = macroDefinition[j]
            outputSourceCode.append(temp)
            noOfInstructionMC = noOfInstructionMC + 1
    else:
        temp = sourceCode[i]
        outputSourceCode.append(temp)

print("Expanded Source Code is : ")
for i in outputSourceCode:
        print(i)
        expandedCode = expandedCode + 1

print()
print("No of instructions in input source code : {}".format(noOfInstructionSC))
print("No of macro call : {}".format(noOfMacroCall))
print("No of instructions defined in macro call : {}".format(noOfInstructionMC))
print("Total number of isntructions in expanded code : {}".format(expandedCode))