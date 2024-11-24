# Análise de Algoritmos para o Problema do Troco

## Descrição do Projeto
Este projeto implementa e analisa diferentes abordagens algorítmicas para resolver o problema do troco, comparando o desempenho entre implementações recursiva, com memorização e iterativa.

### Autores
- João Renan
- Pedro Coimbra
- Carlos Egerr

### Instituição
Centro Universitário do Estado do Pará (CESUPA)  
Disciplina: Análise e Projeto de Algoritmos  
Professor: Isaac Elgrably

## Sobre o Projeto
O código implementa três diferentes abordagens para resolver o problema do troco:
1. **Abordagem Recursiva**: Implementação básica usando recursão
2. **Abordagem com Memorização**: Utiliza programação dinâmica com memorização
3. **Abordagem Iterativa**: Solução iterativa utilizando programação dinâmica

### Funcionalidades
- Análise de desempenho para valores de 5 até 1000
- Comparação de tempo de execução entre as diferentes abordagens
- Visualização gráfica dos resultados usando matplotlib
- Escala logarítmica para melhor visualização das diferenças de desempenho

### Configurações de Teste
- Conjunto de moedas disponíveis: [1, 2, 5]
- Valores testados: [5, 10, 20, 100, 500, 1000]
- A abordagem recursiva é limitada a valores até 20 para evitar estouro de pilha

## Como Executar
1. Certifique-se de ter Python instalado com as bibliotecas necessárias:
```bash
pip install matplotlib
```

2. Execute o script principal:
```python
python nome_do_arquivo.py
```

## Resultados
O programa gera um gráfico que mostra:
- Tempo de execução para cada abordagem
- Escala logarítmica no eixo Y para melhor visualização
- Comparação clara entre os diferentes métodos
- Marcadores para cada ponto de dados

## Observações
- A implementação recursiva é limitada a valores pequenos devido à limitação de pilha do Python
- Para valores maiores que 20, apenas as abordagens com memorização e iterativa são utilizadas
- O gráfico utiliza escala logarítmica para melhor visualização das diferenças de desempenho

## Análise de Complexidade
- Recursivo: O(2^n)
- Memorizado: O(n)
- Iterativo: O(n)

## Conclusões
A análise demonstra que:
1. A abordagem recursiva tem desempenho exponencial e só é viável para valores pequenos
2. A memorização melhora significativamente o desempenho
3. A solução iterativa apresenta o melhor desempenho geral

---
Projeto desenvolvido como parte da disciplina de Análise e Projeto de Algoritmos no CESUPA, 2024.
