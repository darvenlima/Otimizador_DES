# Otimizador ope-source para simulação de eventos discretos


O objetivo desse trabalho foi desenvolver uma ferramenta open-source de  Otimização para simulação de eventos discretos. Para auxiliar projetos na área de otimização via simulação, tanto para empresas que não possuem softwares comerciais e para pesquisadores da área. 

# Visão geral do projeto

O funcionamento do otimizador se utiliza de um algoritmo genético como meta-heurística, uma rede neural para criar o metamodelo, assim acelerando o tempo de execução do código. A forma de conectar o modelo de siulação com o código de otimização ocorre via arquivos externos (.txt), para disponibilizar maior flexibilidade na linguagens que podem ser usadas para a modelagem computacional, atualmente pode ser utlizado python, R, C e C++ 

# Como utilizar o projeto 

Antes de iniciar o uso do otimizador, deve-se adaptar o código da simulação com a leitura e escrita dos arquivos .txt.
o formato dos arquivos de entrada e de saída precisão seguir essa estrutura. Primeira linha com os nomes das variavéis separadas por vírgula e, na linha de baixo os valores de cada uma das variáveis em ordem, também separada por vírgula.


Para acessar otimizador:

Pré-requisitos: python 3.9 

clonar repositório em uma pasta vazia:
git clone https://github.com/darvenlima/OtimizadorDES

para executar o projeto, existe na pasta dist o executável do código, porém ele ainda possui muita lentidão e necessita de melhorias.
Mas é possível utiliza-lo executando pela interface gráfica. Na pasta do projeto execute o comando:

python .\interface.py


