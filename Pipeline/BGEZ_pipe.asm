NOP
LW R1 0(R0)
LW R2 4(R0)
NOP
NOP
NOP
NOP
ADD R3 R1 R2
NOP
NOP
NOP
SW R3 12(R0)
BGEZ R1 L1
NOP
NOP
BGEZ R2 L2
NOP
NOP
L1:
SW R1 8(R0)
J FINAL
NOP
NOP
NOP
L2:
SW R2 8(R0)
J FINAL
NOP
NOP
NOP
FINAL:
J FINAL
