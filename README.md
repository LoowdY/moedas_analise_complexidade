# Análise Comparativa de Algoritmos do Problema do Troco
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7.1-green.svg)](https://matplotlib.org/)

## 📚 Sumário
1. [Sobre o Projeto](#sobre-o-projeto)
2. [Estrutura do Código](#estrutura-do-código)
3. [Implementações](#implementações)
4. [Análise de Complexidade](#análise-de-complexidade)
5. [Metodologia de Teste](#metodologia-de-teste)
6. [Resultados](#resultados)
7. [Como Executar](#como-executar)
8. [Contribuidores](#contribuidores)

## 🎯 Sobre o Projeto

### Descrição
Implementação e análise comparativa de três diferentes abordagens para resolver o problema do troco: recursiva, com memorização e iterativa. O projeto realiza uma análise de desempenho detalhada para valores de 1 a 5000.

### Autores
- João Renan
- Pedro Coimbra
- Carlos Egerr

### Instituição
**CESUPA - Centro Universitário do Estado do Pará**
- Disciplina: Análise e Projeto de Algoritmos
- Professor: Isaac Elgrably

## 🏗️ Estrutura do Código

### Arquivos Principais
```
projeto/
│
├── troco_analise.py         # Arquivo principal com implementações
├── requirements.txt         # Dependências do projeto
└── grafico_desempenho_atualizado_5000.png  # Gráfico gerado
```

### Dependências
```python
matplotlib==3.7.1
time
sys
```

## 💻 Implementações

### 1. Implementação Recursiva
```python
def troco_recursivo(moedas, valor):
    if valor == 0:
        return 0
    if valor < 0:
        return float('inf')
    
    minimo_moedas = float('inf')
    for moeda in moedas:
        num_moedas = 1 + troco_recursivo(moedas, valor - moeda)
        minimo_moedas = min(minimo_moedas, num_moedas)
    
    return minimo_moedas if minimo_moedas != float('inf') else -1
```

#### Características:
- Abordagem força-bruta
- Recalcula subproblemas múltiplas vezes
- Limitada a valores ≤ 20 devido ao limite de recursão
- Ideal para entendimento inicial do problema

### 2. Implementação com Memorização
```python
def troco_memorizado(moedas, valor, memo):
    if valor in memo:
        return memo[valor]
    if valor == 0:
        return 0
    if valor < 0:
        return float('inf')
    
    minimo_moedas = float('inf')
    for moeda in moedas:
        num_moedas = 1 + troco_memorizado(moedas, valor - moeda, memo)
        minimo_moedas = min(minimo_moedas, num_moedas)
    
    memo[valor] = minimo_moedas if minimo_moedas != float('inf') else -1
    return memo[valor]
```

#### Características:
- Utiliza dicionário para armazenar resultados já calculados
- Reduz significativamente recálculos
- Ainda sujeita a limites de recursão
- Equilibra tempo e uso de memória

### 3. Implementação Iterativa
```python
def troco_iterativo(moedas, valor):
    dp = [float('inf')] * (valor + 1)
    dp[0] = 0
    
    for i in range(1, valor + 1):
        for moeda in moedas:
            if i - moeda >= 0:
                dp[i] = min(dp[i], dp[i - moeda] + 1)
    
    return dp[valor] if dp[valor] != float('inf') else -1
```

#### Características:
- Programação dinâmica bottom-up
- Não tem limitações de recursão
- Uso eficiente de memória
- Melhor performance para valores grandes

## 📊 Análise de Complexidade

### Complexidade Temporal

| Implementação | Melhor Caso | Caso Médio | Pior Caso |
|--------------|-------------|------------|-----------|
| Recursiva    | O(1)        | O(2^n)     | O(2^n)    |
| Memorizada   | O(1)        | O(n*m)     | O(n*m)    |
| Iterativa    | O(n*m)      | O(n*m)     | O(n*m)    |

Onde:
- n = valor do troco
- m = número de moedas disponíveis

### Complexidade Espacial

| Implementação | Complexidade |
|--------------|--------------|
| Recursiva    | O(n)         |
| Memorizada   | O(n)         |
| Iterativa    | O(n)         |

## 🔬 Metodologia de Teste

### Configuração dos Testes
- **Range de valores**: 1 a 5000
- **Conjunto de moedas**: [1, 2, 5]
- **Medição**: `time.perf_counter()`
- **Limitações**:
  - Recursivo: testado até valor 20
  - Memorizado: compartilha cache entre execuções
  - Iterativo: sem limitações

### Métricas Coletadas
1. Tempo de execução (segundos)
2. Ocorrência de RecursionError
3. Progress tracking a cada 500 valores

## 📈 Resultados

### Visualização
O script gera um gráfico detalhado (`grafico_desempenho_atualizado_5000.png`) com:
- Escala logarítmica no eixo Y
- Marcadores distintos para cada implementação:
  - Recursivo: círculos azuis
  - Memorizado: 'x' verdes
  - Iterativo: quadrados vermelhos
- Grid para facilitar leitura

### Análise de Resultados
1. **Algoritmo Recursivo**
   - Viável apenas para valores pequenos
   - Crescimento exponencial do tempo

2. **Algoritmo Memorizado**
   - Performance intermediária
   - Benefício significativo da cache

3. **Algoritmo Iterativo**
   - Melhor performance geral
   - Crescimento linear do tempo

## 🚀 Como Executar

### Requisitos
- Python 3.7+
- Matplotlib 3.7.1

### Instalação
```bash
# Clonar repositório
git clone [url-do-repositorio]

# Instalar dependências
pip install -r requirements.txt
```

### Execução
```bash
python troco_analise.py
```

## 👥 Contribuidores
- João Renan - Implementação e Documentação
- Pedro Coimbra - Análise e Testes
- Carlos Egerr - Visualização e Relatório

## 📝 Notas Adicionais

### Limitações Conhecidas
1. Recursão limitada por padrão do Python
2. Uso de memória cresce com o valor do troco
3. Cache compartilhado pode afetar medições

### Melhorias Futuras
1. Implementar testes unitários
2. Adicionar mais denominações de moedas
3. Otimizar uso de memória
4. Implementar versões paralelas
5. Adicionar análise de espaço utilizado

---

© 2024 CESUPA - Desenvolvido como projeto da disciplina de Análise e Projeto de Algoritmos.
