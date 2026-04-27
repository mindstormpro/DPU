# DPU
A Dumb Virtual CPU


# INSTRUCTION REFERENCE TABLE
| Code | Sym | Description | In 1 | In 2 | In 3 |
| :---: | :---: | :--- | :---: | :---: | :---: |
| 0000 | NOP | does nothing | N/A | N/A | N/A |
| 0001 | JMP | jumps to a specified address | ADDR pt-1 | ADDR pt-2 | N/A |
| 0010 | RGS | sets a register | REG, 0-3 is A-D | VAL pt-1 | VAL pt-2 |
| 0011 | PSH | pushes the registers to the stack and writes the next address to REG D | N/A | N/A | N/A |
| 0100 | POP | pops the register values from the stack and overwrites the registers | N/A | N/A | N/A |
| 0101 | INP | if there is an input, reads it from it's buffer into a register | Input Buf # | REG, 0-3 is A-D | N/A |
| 0110 | OUT | push a register value into an output buffer | Output Buf # | REG, 0-3 is A-D | N/A |
| 0111 | RAA | adds a value to the specified register and skips the next line if no carry | REG, 0-3 is A-D | VAL pt-1 | VAL pt-2 |
