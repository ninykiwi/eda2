# MATA54 - Estrutura de Dados e Algoritmos 2
### Objetivo
O trabalho tem como objetivo consolidar o conhecimento sobre as características do problema deordenação externa. Neste contexto, o estudante deverá entregar o código-fonte, livre de erros para que seja possível compilá-lo e executá-lo de acordo com a presente especificação. O programa entregue deve ser capaz de ordenar um arquivo de entrada levando em consideração restrições de tamanho memória interna e números de arquivos a serem manipulados simultaneamente.

### Sobre o método de ordenação
entregar o c´odigo-fonte, livre de erros para que
seja poss´ıvel compil´a-lo e execut´a-lo de acordo com a presente especifica¸c˜ao. O programa entregue
deve ser capaz de ordenar um arquivo de entrada levando em considera¸c˜ao restri¸c˜oes de tamanho
mem´oria interna e n´umeros de arquivos a serem manipulados simultaneamente.

### Sobre a interface de entrada e sa´ıda
Seu programa deve ser executado em linha de comando (prompty shell), recebendo trˆes parˆametros
de entrada: o valor de p, o nome do arquivo de entrada e o nome no arquivo de sa´ıda. Os registros a
serem ordenados no arquivo de entrada ser˜ao n´umeros inteiros, um por linha.
Como ilustra¸c˜ao, suponha que o nome do execut´avel ´e pway, o nome do arquivo de entrada ´e
input.txt, do arquivo de sa´ıda ´e output.txt e p = 2. Na linha de comando, deve-se digitar:
#### pways 3 input.txt output.txt
Observe que p < 2 n˜ao uma op¸c˜ao v´alida. </br>
Como sa´ıda, a execu¸c˜ao do programa, al´em de fornecer or registros do arquivo de entrada ordenados, ele deve exibir como sa´ıda trˆes valores: o n´umero de registros processados; p; o n´umero de
sequˆencias iniciais geradas; e o n´umero de passagens para se obter uma ´unica sequˆencia ordenada. Por
exemplo, suponha que o arquivo de entrada input.txt cont´em os seguintes 25 registros
#### 18 7 3 24 15 5 20 25 16 14 21 19 1 4 13 9 22 11 23 8 17 6 12 2 10
Ent˜ao, as seguintes sa´ıdas devem ser exibidas para em fun¸c˜ao do valor de p usado:
#### /pways 3 input.txt output.txt
#### #Regs Ways #Runs #Parses
#### 25 3 5 2
#### ./pways 2 input.txt output.txt
#### #Regs Ways #Runs #Parses
#### 25 2 7 3
#### ./pways 4 input.txt output.txt
#### #Regs Ways #Runs #Parses
#### 25 4 4 1

### Considera¸c˜oes e crit´erios
<ul>
• A implementa¸c˜ao n˜ao deve usar m´etodos de ordena¸c˜ao em mem´oria interna em nenhuma fase
da ordena¸c˜ao externa. Al´em disso, arquivos de entrada e sa´ıda tempor´arios devem ser usados.
Qualquer manipula¸c˜ao de arquivos como sequˆencias em mem´oria interna n˜ao ser´a permitida. N˜ao atender tais restri¸c˜oes ou usar de pl´agio implicar´a em nota zero no trabalho.
</ul>
<ul>
• O trabalho ´e individual e valer´a uma nota de 0 a 10. Tal nota ser´a usada para alterar a menor
nota P de uma das provas, substituindo-a por (P + T)/2 contanto que P < T. A entrega do
trabalho ´e de car´ater opcional.
</ul>
<ul>
• Os arquivos de entrada e sa´ıda podem ser grandes. Portanto, o programa n˜ao deve conter
qualquer restri¸c˜ao com rela¸c˜ao ao n´umero de registros no arquivo de entrada.
</ul>
<ul>
• O c´odigo deve ser entregue de forma que sua corre¸c˜ao possa ser realizada independente da
m´aquina hospedeira. Para tanto, servi¸cos em nuvem podem ser usados desde que a autoriza¸c˜ao
de acesso esteja liberada ao professor.
</ul>
<ul>
• Trabalhos que contenham erros de compila¸c˜ao n˜ao ser˜ao corrigidos. A linguagem de programa¸c˜ao
a ser utilizada ´e de livre escolha entre C, C++, Java ou Python. Outras linguagens podem ser
permitidas, deste que previamente autorizadas.
</ul>
<ul>
• O trabalho deve ser entregue em 30 dias a partir da data desta divulga¸c˜ao.
</ul>
