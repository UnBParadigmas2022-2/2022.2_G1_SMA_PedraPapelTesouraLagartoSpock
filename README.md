# Pedra Papel Tesoura Lagarto Spock

**Disciplina**: FGA0210 - PARADIGMAS DE PROGRAMAÇÃO - T01 <br>
**Nro do Grupo**: G1<br>
**Paradigma**: SMA<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0012002 |  Álvaro Gouvea |
| 19/0044799 |  Antônio Ferreira de Castro Neto |
| 19/0042419 |  Davi Matheus da Rocha de Oliveira |
| 17/0142329 |  Francisco Emanoel Ferreira |
| 19/0014032 |  Guilherme Rogelin Vial |
| 18/0022237 |  Liverson Furtado Severo |
| 14/0155350 |  Matheus Filipe Faria Alves de Andrade |
| 19/0058650 |  Natanael Fernandes Coelho Filho |

## Sobre 
O jogo Pedra, Papel, Tesoura, Lagarto, Spock! é uma aplicação de Sistemas Multiagentes no qual é simulado um torneio de Pedra, Papel e Tesoura num estilo diferente.

Existem 6 tipos de Agentes (players), com um Model e a Simulação que consiste nas partidas 1 e 2, e depois a grande final. Dentre os 6 jogadores, o usuário escolhe 4 para preencher as partidas 1 e 2, cada jogador com um modelo de jogo diferente:

- Pedrão: apenas joga pedra.
- Papelão: apenas joga papel.
- Randão: joga de forma randômica.
- Bomsão: se adapta de acordo com as partidas anteriores.
- Arnaldo: tem maiores chances de vencer apenas 1 partida.
- Ruanzão: tem maiores chances de perder todas as partidas.


O jogo em questão foi inspirado na série The Big Bang Theory: o contexto pode ser compreendido com esse [vídeo](https://youtu.be/7QiiFEbGYnQ?t=86)

## Uso 

As regras do jogo vão um pouco além do Pedra, Papel, Tesoura convecional:

```
- Tesoura corta papel
- Papel cobre pedra
- Pedra esmaga lagarto
- Lagarto envenena Spock
- Spock esmaga (ou derrete) tesoura
- Tesoura decapita lagarto
- Lagarto come papel
- Papel refuta Spock
- Spock vaporiza pedra
- Pedra amassa tesoura
```

1 - Escolha 4 dos 6 jogadores para jogar a primeira e segunda partida.

2 - Veja as rodadas e vencedor da primeira e segunda partida.

3 - Veja as rodadas e vencedor da partida final e o vencedor.

## Screenshots
## Menu Inicial
![image1](imgs/1.png)

## Primeira partida
![image2](imgs/2.png)

## Partida final e o vencedor
![image3](imgs/3.png)

## Instalação 
**Linguagens**: Python<br>
**Tecnologias**: Mesa<br>
Utilizamos um Makefile para auxiliar na execução da aplicação.

Para instalar as dependências:

```make build```

Para rodar a aplicação:

```make run```

## Vídeo
o vídeo de apresentação pode ser visitado por esse [link](https://youtu.be/xEa0UJh7P_E), e um vídeo de demonstração da pipeline nesse [link](https://youtu.be/xAI52gHAf6s)

Caso não consiga acessar pelo Youtube, acesse o vídeo pelo [Drive](https://drive.google.com/drive/folders/1eSrF4gNFM-6M7MdbT_Sw4aJE51wRIi86?usp=sharing)

## Participações
## Participações
| Nome do Membro                           | Contribuição                                         | Significância da Contribuição para o Projeto (Excelente/Boa/Regular/Ruim/Nula) |
| ---------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------ |
| Álvaro Gouveia -18/0012002		                                   | Auxílio Criação dos Agentes Iniciais / Sistema de Chaveamento | Excelente | 
| Antônio Ferreira de Castro Neto - 19/0044799| Criação de novos Agentes. Melhorias de usabilidade e visual da interface. Criação do README | Excelente |
| Davi Matheus da Rocha de Oliveira - 19/0042419	         |   Criação dos Agentes Finais / Melhorias na Interface  | Excelente                                                                            |
| Francisco Emanoel Ferreira   - 17/0142329	              |  Criação da pipeline e dockerização  | Muito Boa |
|Guilherme Rogelin Vial	- 19/0014032	    | Criação dos agentes e do modelo responsável pela lógica do jogo. | Excelente |
| Liverson Furtado Severo	- 18/0022237    | Criação dos agentes e do modelo responsável pela lógica do jogo. | Excelente                                                                         |
| Matheus Filipe Faria Alves de Andrade	- 14/0155350	 |  Auxílio criação dos agentes / Correção bugs   |  Excelente   |
| Natanael Fernandes Coelho Filho	- 19/0058650	                 |  Auxílio criação dos agentes / auxilio na configuração do ci/cd   |     Excelente       |

## Outros 
* Lições Aprendidas:
   * Entendendo os alguns conceitos do Sistemas Multiagentes
   * Entendendo os princípios da sintaxe e semântica do framework MESA com a linguagem Python
 
* Percepções:
   * Por estarmos acostumados com a linguagem Python, nos adaptamos bem ao framework MESA, no entanto não conseguimos utilizar a interface gráfica do framework por falta de tempo. Mas ainda sim conseguimos entender como funciona o Sistema Multiagentes.
 
* Contribuições e Fragilidades
   * Uma fragilidade seria tempo escasso devido a trabalhos de outras matérias e euforia do fim do semestre.
  
* Trabalhos Futuros.
   * Adição de mais agentes
   * Possibilidade do usuário jogar contra com os Agentes
   * Botar um arquivo só de nomes de pessoas e na hora de mostrar os players iriam pegar tipo 6 nomes aleatorios, e também aleatoriamente cada player iria receber um atributo ai a gente colocaria esses agentes
   * Melhorar a UI.


## Fontes
- [Regras do jogo](https://pt.wikipedia.org/wiki/Pedra-papel-tesoura-lagarto-Spock)

- [Mesa](https://mesa.readthedocs.io/en/stable/)
