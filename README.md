# logisim-computer

A "computer" made with [logisim evolution](https://github.com/logisim-evolution/logisim-evolution) and python during dicember 2022 in my third year of high school.

Google slides [computer logisim](https://docs.google.com/presentation/d/1hx7jZSbXReomKKLNCeCIdDt5UXV5rjtDp2bpkS4e1x0/edit?usp=sharing)

# Premise

This project is poorly done, however it is a milestone for myself of a few years ago who had just learned, broadly speaking, the various architectures such as Von Neuman and Harvard. I didn't know assembly, but I learned about RISC and this was enough for me to create the assembler. Initially I learned about the functioning of basic components such as flip-flops, adders, ALUs and then I continued on my own thanks only to my creativity and logic.




https://github.com/user-attachments/assets/fde12286-d4a0-4cbe-824f-4169276ae018


# Technical Specifications

- Instruction-Set: RISC 
- Execution model: REG-REG
- Architecture: Harvard
- Number of registers: 16 
- Op-code length: 4 bit (16 instructions)
- Instructions length: 2 byte (16 bit)
- Instruction memory: 512 byte (256 instructions)
- Ram: 256 byte

## Instruction Set

| Op-code | Syntax                  | Function             |
|---------|-------------------------|----------------------|
| "0000"  | Nope                    | Nope                 |
| "0001"  | Add rd,rs1,rs2          | Add                  |
| "0010"  | Sub rd,rs1,rs2          | Subtract             |
| "0011"  | Addi rd,rs1,im1         | Add immediate        |
| "0100"  | Jump cn, ia             | Conditioned jump     |
| "0101"  | Gosub, ia               | go to sub            |
| "0110"  | Return                  | return               |
| "0111"  | Loadi rd im1            | load byte immediate  |
| "1000"  | Load rd, rs1, im1       | load byte register   |
| "1001"  | Storei rst im1          | store byte immediate |
| "1010"  | Store rst, rs1, im1     | store byte register  |
| "1011"  | Ass rd, im1             | Assign               |
| "1100"  | Screen rx, ry, rgb, clr | Modify Screen        |
