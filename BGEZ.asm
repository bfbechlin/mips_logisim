NOP
LW R1 4(R0)
LW R2 0(R1)
LW R3 4(R1)
ADD R4 R2 R3
LB1:
SUB R4 R4 R3
BGEZ R4 LB1
SW R4 8(R1)
SLL R4 R3 3
SW R4 12(R1)
FINAL_LOOP:
J FINAL_LOOP
DATA:
