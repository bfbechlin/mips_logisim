LW R1 DATA(R0)
LW R2 4(R1)
LW R3 8(R1)
ADD R4 R2 R3
SW R4 12(R1)
LB1:
SUB R4 R4 R3
BGEZ R4 LB1
SW R4 16(R1)
SLL R4 R3 3
SW R4 20(R1)
FINAL_LOOP:
J FINAL_LOOP
DATA:
WORD DATA
WORD 2
WORD 4