class Produto:
    def __init__(self, nome, categoria, prob_Conversao):
        self.nome = nome
        self.categoria = categoria
        self.prob_Conversao = prob_Conversao

    def set_nome(self, nome):
        self.nome = nome

    def set_categoria(self, categoria):
        self.categoria = categoria

    def set_prob_Conversao(self, prob_Conversao):
        self.prob_Conversao = prob_Conversao

    def get_nome(self):
        return self.nome

    def get_categoria(self):
        return self.categoria

    def get_prob_Conversao(self):
        return self.prob_Conversao

class RecomendacaoAEstrela:
    def __init__(self, produtos):
        self.produtos = produtos
    
    def recomendacao_a_estrela(self, produto_inicial, produto_final):
        """
        Implementa o algoritmo A* para recomendar o caminho ótimo de produto_inicial até produto_final
        com base na probabilidade de conversão como heurística.
        """
        import heapq

        # Constrói a lista de adjacência onde cada produto se conecta a todos os outros produtos
        # O custo pode ser definido, por exemplo, como 1 para cada transição (ou outro critério relevante)
        grafo = {}
        for produto in self.produtos:
            vizinhos = []
            for outro_produto in self.produtos:
                if outro_produto != produto:
                    # Defina o custo da transição conforme necessário; aqui usamos custo 1 como exemplo
                    vizinhos.append((outro_produto, 1))
            grafo[produto] = vizinhos

        # Função heurística: probabilidade de conversão negativa (maior probabilidade = menor custo)
        def heuristica(produto):
            return -produto.get_prob_Conversao()

        conjunto_aberto = []
        heapq.heappush(conjunto_aberto, (heuristica(produto_inicial), 0, produto_inicial, [produto_inicial]))

        conjunto_fechado = set()
        g_scores = {produto_inicial: 0}

        while conjunto_aberto:
            _, g_atual, atual, caminho = heapq.heappop(conjunto_aberto)

            if atual == produto_final:
                return [p.get_nome() for p in caminho]

            conjunto_fechado.add(atual)

            for vizinho, custo in grafo.get(atual, []):
                if vizinho in conjunto_fechado:
                    continue
                g_tentativo = g_atual + custo
                if vizinho not in g_scores or g_tentativo < g_scores[vizinho]:
                    g_scores[vizinho] = g_tentativo
                    f_score = g_tentativo + heuristica(vizinho)
                    heapq.heappush(conjunto_aberto, (f_score, g_tentativo, vizinho, caminho + [vizinho]))

        return None  # Nenhum caminho encontrado
        
        
# Produtos para loja de eletrônicos com diferentes níveis de conversão

# Produto de ALTA conversão - Fone de ouvido popular
fone_airpods = Produto(
    nome="AirPods Pro 2ª Geração",
    categoria="Áudio",
    prob_Conversao=0.85  # 85% de probabilidade de conversão (alta)
)

# Produto de MÉDIA conversão - Laptop
laptop_gaming = Produto(
    nome="Laptop Gamer ASUS ROG Strix G15",
    categoria="Computadores",
    prob_Conversao=0.45  # 45% de probabilidade de conversão (média)
)

# Produto de BAIXA conversão - Impressora especializada
impressora_3d = Produto(
    nome="Impressora 3D Creality Ender-3 S1 Pro",
    categoria="Impressão 3D",
    prob_Conversao=0.15  # 15% de probabilidade de conversão (baixa)
)

# Lista de produtos para usar no sistema de recomendação
produtos_eletronicos = [fone_airpods, laptop_gaming, impressora_3d]

# Exemplo de uso do sistema de recomendação
if __name__ == "__main__":
    # Criar instância do sistema de recomendação
    sistema_recomendacao = RecomendacaoAEstrela(produtos_eletronicos)
    
    # Exemplo: encontrar caminho do fone para a impressora
    caminho_recomendado = sistema_recomendacao.recomendacao_a_estrela(
        fone_airpods, impressora_3d
    )
    
    print("Produtos criados:")
    for produto in produtos_eletronicos:
        print(f"- {produto.get_nome()} ({produto.get_categoria()}) - Conversão: {produto.get_prob_Conversao():.0%}")
    
    if caminho_recomendado:
        print(f"\nCaminho recomendado do {fone_airpods.get_nome()} para {impressora_3d.get_nome()}:")
        print(" → ".join(caminho_recomendado))
    else:
        print("\nNenhum caminho encontrado.")
