class BuscaLocal:
    def __init__(self, mochila):
        self.mochila = mochila
        
    def melhor_aprimorante(self):
        """
        Método que encontra o melhor aprimorante para a mochila percorrendo
        toda vizinhança da mochila. A vizinhança é explorada pelo método SWAP.

        Retorna: nova mochila com melhor solução encontrada ou a própria mochila se não houver melhoria.
        """
        melhor_mochila = self.mochila.clone()
        melhor_valor = melhor_mochila.get_profit()
        itens = melhor_mochila.get_items()
        n = len(itens)

        encontrou_melhora = False

        # Indices dos itens dentro e fora da mochila
        dentro = [i for i in range(n) if itens[i] == 1]
        fora = [j for j in range(n) if itens[j] == 0]

        for i in dentro:
            for j in fora:
                vizinho = self.mochila.clone()
                vizinho.remove_item(i)
                vizinho.add_item(j)
                if vizinho.is_valid():
                    valor_vizinho = vizinho.get_profit()
                    if valor_vizinho > melhor_valor:
                        melhor_valor = valor_vizinho
                        melhor_mochila = vizinho
                        encontrou_melhora = True

        if encontrou_melhora:
            return melhor_mochila
        else:
            return self.mochila