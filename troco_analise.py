import matplotlib.pyplot as plt
import time
import sys

# Implementação recursiva
def troco_recursivo(moedas, valor):
    """Implementação recursiva para o problema do troco."""
    if valor == 0:
        return 0
    if valor < 0:
        return float('inf')
    
    minimo_moedas = float('inf')
    for moeda in moedas:
        num_moedas = 1 + troco_recursivo(moedas, valor - moeda)
        minimo_moedas = min(minimo_moedas, num_moedas)
    
    return minimo_moedas if minimo_moedas != float('inf') else -1

# Implementação com memorização
def troco_memorizado(moedas, valor, memo):
    """Implementação com memorização para o problema do troco."""
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

# Implementação iterativa usando programação dinâmica
def troco_iterativo(moedas, valor):
    """Implementação iterativa para o problema do troco."""
    dp = [float('inf')] * (valor + 1)
    dp[0] = 0
    
    for i in range(1, valor + 1):
        for moeda in moedas:
            if i - moeda >= 0:
                dp[i] = min(dp[i], dp[i - moeda] + 1)
    
    return dp[valor] if dp[valor] != float('inf') else -1

# Análise de desempenho e visualização
def analisar_e_visualizar_ate_5000():
    moedas = [1, 2, 5]
    valores = list(range(1, 5001))  # Valores de 1 a 5000
    tempos_recursivo = []
    tempos_memorizado = []
    tempos_iterativo = []
    
    # Inicializar memoização compartilhada
    memo = {}
    
    total_valores = len(valores)
    
    print("Iniciando análise de desempenho...")
    for idx, valor in enumerate(valores, 1):
        # Feedback de progresso a cada 500 valores
        if idx % 500 == 0 or idx == total_valores:
            print(f"Processando valor {idx} de {total_valores} ({(idx/total_valores)*100:.1f}%)")
        
        # Desempenho recursivo
        if valor <= 20:  # Apenas testar recursivo para valores pequenos
            try:
                inicio = time.perf_counter()
                troco_recursivo(moedas, valor)
                tempo = time.perf_counter() - inicio
                tempos_recursivo.append(tempo)
            except RecursionError:
                tempos_recursivo.append(float('inf'))
        else:
            tempos_recursivo.append(None)  # Ignorar valores grandes

        # Desempenho memorizado
        try:
            inicio = time.perf_counter()
            troco_memorizado(moedas, valor, memo)
            tempo = time.perf_counter() - inicio
            tempos_memorizado.append(tempo)
        except RecursionError:
            tempos_memorizado.append(float('inf'))

        # Desempenho iterativo
        inicio = time.perf_counter()
        troco_iterativo(moedas, valor)
        tempo = time.perf_counter() - inicio
        tempos_iterativo.append(tempo)
    
    print("Análise concluída. Preparando gráfico...")
    
    # Preparar dados para plotagem
    valores_recursivo = [val for val, t in zip(valores, tempos_recursivo) if t is not None]
    tempos_recursivo_filtrado = [t for t in tempos_recursivo if t is not None]
    
    # Plotando resultados
    plt.figure(figsize=(16, 10))

    # Plot para recursivo (valores pequenos)
    if valores_recursivo and tempos_recursivo_filtrado:
        plt.plot(
            valores_recursivo, tempos_recursivo_filtrado, 
            label='Recursivo (valores pequenos)', marker='o', linestyle='-', markersize=4, color='blue'
        )
    
    # Plot para memorizado
    plt.plot(
        valores, tempos_memorizado, 
        label='Memorizado', marker='x', linestyle='-', markersize=4, color='green'
    )
    
    # Plot para iterativo
    plt.plot(
        valores, tempos_iterativo, 
        label='Iterativo', marker='s', linestyle='-', markersize=4, color='red'
    )
    
    plt.yscale('log')  # Escala logarítmica para melhor visualização
    plt.xlabel('Valor', fontsize=16)
    plt.ylabel('Tempo (s)', fontsize=16)
    plt.title('Desempenho dos Algoritmos para o Problema do Troco (Valores de 1 a 5000)', fontsize=20)
    plt.legend(fontsize=14)
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.tight_layout()
    plt.savefig('grafico_desempenho_atualizado_5000.png')  # Salvar gráfico como imagem
    plt.show()

    # Informar se algum valor memorizado causou RecursionError
    if any(t == float('inf') for t in tempos_memorizado):
        print("Aviso: Alguns valores na implementação memorizada excederam a profundidade máxima de recursão.")

# Executar análise e visualização
if __name__ == "__main__":
    analisar_e_visualizar_ate_5000()
