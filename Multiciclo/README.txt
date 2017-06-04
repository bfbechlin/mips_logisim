**BGEZ**

 31-26   25-21    20-16   15-0
*000001*   rt  * 00001 * offset

Devido a extensão do OPCODE da instrução foi necessário adicionar hardware de
comparação com os bits 20-16. Como a lógica ALUcontrol só permite acionar duas
operações sem a utilização do campo de função que nessa instrução está sobreescrita
pelo offset, foi necessário adicionar um multiplexador para a segunda entrada com a 
constante 0. Dessa forma a ALU opera rt - 0 para setar seus bits de sinais. 

O sinal RegDst também foi reutilizado visto que em conjunto com PCWriteCond não surtiria 
nenhum mal aos demais estados e sinais de controle, assim não foi necessário aumentar a
memória com novos bits de controle.

Outras opções eram possíveis mas iriam adicionar mais hardware. Visto que não
é possível selecionar o segundo registrador do banco de registradores e isso
deveria ser feito em dois estados distintos devido ao registrado de estado que
existe entre a ALU e o banco de registradores.


