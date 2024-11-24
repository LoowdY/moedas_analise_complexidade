# Ajustar a análise para incluir valores até 1000
def analisar_e_visualizar_ate_1000():
    moedas = [1, 2, 5]
    valores = [5, 10, 20, 100, 500, 1000]
    tempos_recursivo = []
    tempos_memorizado = []
    tempos_iterativo = []

    for valor in valores:
        if valor <= 20:  # Apenas testar recursivo para valores pequenos
            # Desempenho recursivo
            inicio = time.time()
            try:
                troco_recursivo(moedas, valor)
            except RecursionError:
                tempos_recursivo.append(float('inf'))
            else:
                tempos_recursivo.append(time.time() - inicio)
        else:
            tempos_recursivo.append(None)  # Ignorar valores grandes

        # Desempenho memorizado
        inicio = time.time()
        troco_memorizado(moedas, valor, {})
        tempos_memorizado.append(time.time() - inicio)

        # Desempenho iterativo
        inicio = time.time()
        troco_iterativo(moedas, valor)
        tempos_iterativo.append(time.time() - inicio)

    # Plotando resultados
    plt.figure(figsize=(10, 6))
    if any(t is not None for t in tempos_recursivo):
        plt.plot(
            valores[:3], [t for t in tempos_recursivo if t is not None], 
            label='Recursivo (valores pequenos)', marker='o'
        )
    plt.plot(valores, tempos_memorizado, label='Memorizado', marker='o')
    plt.plot(valores, tempos_iterativo, label='Iterativo', marker='o')
    plt.yscale('log')  # Escala logarítmica para melhor visualização
    plt.xlabel('Valor')
    plt.ylabel('Tempo (s)')
    plt.title('Desempenho dos Algoritmos para o Problema do Troco')
    plt.legend()
    plt.grid()
    plt.show()

# Executar análise e visualização para até 1000
analisar_e_visualizar_ate_1000()
