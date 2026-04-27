import time
import os
instFile = open("instructions.txt")


# Little Endian-ness for this project
def BiToInt(bi): # little endian to int
    return int(bi[::-1], 2)

currInst = None
counter = 0
instLength = 16

inputBuffer = {}
outputBuffer = {}

regA = "00000000" # data reg
regB = "00000000" # data reg
regC = "00000000" # return addr reg
regD = "00000000"
regStack = {}
delay = 1


    
    


while True:
    counter = counter + 1
    instFile.seek((counter - 1) * instLength, 0)
    currInst = instFile.read(8)

    if currInst == "":
        exit()
    
    inst = currInst[:4]
    data = currInst[4:]
    print(str(counter) + " - " + inst)
    
    os.system("cls")
    print("inst #: " + str('{0:08b}'.format(counter)))
    print("Reg A: " + regA)
    print("Reg B: " + regB)
    print("Reg C: " + regC)
    print("Reg D: " + regD)
    print("Inst: " + inst)
    print("Data: " + data)

    #if inst == "0000":   # 1 -- nop
        # Do Nothing.
    if inst == "0001":    # 2 -- jmp
        counter = BiToInt(data)
    elif inst == "0010":  # 3 -- rgs
        if BiToInt(data[:4]) == 0:
            regA = data[4:]
        elif BiToInt(data[:4]) == 1:
            regB = data[4:]
        elif BiToInt(data[:4]) == 2:
            regC = data[4:]
        elif BiToInt(data[:4]) == 3:
            regD - data[4:]
    elif inst == "0011":  # 4 -- psh
        regs = [regA, regB, regC, regD]
        regStack.append(regs)
        regA = "00000000"
        regB = "00000000"
        regC = "00000000"
        regD = str('{0:08b}'.format(counter + 2))
    elif inst == "0100":  # 5 -- pop
        regs = regStack.pop()
        regA = regs[0]
        regB = regs[1]
        regC = regs[2]
        regD = regs[3]
    elif inst == "0101":  # 6 -- inp (input buffer)
        if inputBuffer[data[:4]][0] == 1:
            inputBuffer[data[:4]][0]
            if BiToInt(data[4:][:4]) == 0:
                regA = inputBuffer[data[:4]][1]
            elif BiToInt(data[4:][:4]) == 1:
                regB = inputBuffer[data[:4]][1]
            elif BiToInt(data[4:][:4]) == 2:
                regC = inputBuffer[data[:4]][1]
            elif BiToInt(data[4:][:4]) == 3:
                regD - inputBuffer[data[:4]][1]
            inputBuffer[data[:4]][1] = ""
            counter = counter + 1
    elif inst == "0110":  # 7 -- out (output buffer)
        if BiToInt(data[4:][:4]) == 0:
            outputBuffer[data[:4]] = regA
        elif BiToInt(data[:4]) == 1:
            outputBuffer[data[d:][:d]] = regB
        elif BiToInt(data[:4]) == 2:
            outputBuffer[data[d:][:d]] = regC
        elif BiToInt(data[:4]) == 3:
            outputBuffer[data[:4]] = regD
    elif inst == "0111":  # 8 -- raa 


    time.sleep(delay)


