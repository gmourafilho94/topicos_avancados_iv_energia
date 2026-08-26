# Topicos Avançados IV 2026.2

## Consumo energético como problemática mundial para TIC.

- Abordagens: 
  * Consumo de energia é métrica para poder verificar impacto do algoritmo para dentro do produto;
  * Como metrificar esse consumo;
  * Sabendo que `Energia = Potência/tempo`, o tempo em `ms` e potência em `J`, quanto menor o "user_time" do algoritmo ⬇️ menor o consumo ⬇️ menor impacto;
  * Como melhorar algoritmos para poder diminuir o seu "user_time"
## Aulas

### Aula 1

Aprender sobre o impacto e o porquê de estudar e aprimorar o tempo de execução

### Aula_2

Métodos de metrificação e o porquê que a metrificação deve vir direto da aplicação e não física. Para testes utilizamos um algoritmo de definir se um número é primo ou não, aumentando o número para verificar a incrementação de tempo e o consumo energético dessa incrementação. Utilza-se RAPL (Running Average Power Limit) por meio de `perf` no Linux OS para poder verificar rodando direto em conjunto com a aplicação. 

```
18,50;Joules;power/energy-pkg/;1001759924;100,00;;
0,48;Joules;power/energy-cores/;1001759409;100,00;;
1796000;ns;user_time;1796000;100,00;;
```

Assim variando/melhorando o algoritmo e fixando os valores de teste acharíamos o impacto. Montagem de csv esta dentro da `./aula_2`


### Aula_3

Ordenação e consumo de energia. A complexidade do algoritmo pode ser expressada em duas grandezas: 
* Complexidade -> número de operação (complexidade de tempo)
* Quantidade de memória utilizada

> Dica é verificar a quantidade de "fors" no algoritmo para verificar o O(n) da solução

A atividade consistiu em criar dois algoritmos de ordenação e fazer tabulação de suas performances. Para facilitar o processso de construcao dos arrays e criacao dos csvs foram criados tres scripts [medicao](./aula_3/medicao.sh) e [implementacao](./aula_3/implementacao.sh), [criacao](./aula_3/criacao_lista.sh) fazendo com que o processo seja mais automatizado.  
