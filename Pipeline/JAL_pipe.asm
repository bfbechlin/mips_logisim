INICIO:
LW R1 0(R0)
LW R2 4(R0)
NOP
NOP
NOP
ADD R3 R1 R2
NOP
NOP
NOP
SUB R3 R3 R2
NOP
NOP
NOP
JAL LB1
JAL_END:
NOP
NOP
NOP
SW R0 8(R0)
J INICIO
NOP
NOP
NOP
LB1:
SW R31 8(R0)
J INICIO
DATA:
