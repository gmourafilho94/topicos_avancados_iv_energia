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
