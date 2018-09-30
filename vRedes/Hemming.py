Mensagem = input()


class Redes:
    def HemmingCode(Mensagem):
        def QuantidadeDeBitsParaAdicionar(Mensagem):
            for r in range(len(Mensagem)):
                if 2 ** r >= (len(Mensagem) + r + 1):
                    return r

        def Tabela(qtBits, Mensagem):
            tamanho = len(Mensagem) + qtBits
            return tamanho

        def Desconhecidos(tamanhoDaTabela):
            X = list()

            for i in range(tamanhoDaTabela):
                local = 2 ** i
                if local < tamanhoDaTabela:
                    X.append(2 ** i)
            return X

        def TabelaComDesconhecidos(PosicoesDesconhecidas, Mensagem):
            NovaMensagem = list(range(1, tamanhoTabela + 1))

            contador = 0
            for item in PosicoesDesconhecidas:
                contador += 1
                NovaMensagem[item - 1] = {'P' + str(contador): 'x'}

            cont = 1
            for item in NovaMensagem:
                if str(item).isnumeric():
                    NovaMensagem[item - 1] = {'M' + str(cont): Mensagem[cont - 1]}
                    cont += 1

            return NovaMensagem

        def Descript(QuantidadeDeBitsParaAdd, index):
            for i in range(QuantidadeDeBitsParaAdd):
                for j in range(QuantidadeDeBitsParaAdd):
                    if PosicoesDesconhecidas[i] + PosicoesDesconhecidas[j] == index and (i != j):
                        return [i + 1, j + 1]

        def Descript3desconhecidos(QuantidadeDeBitsParaAdd, index):
            for k in range(QuantidadeDeBitsParaAdd):
                for i in range(QuantidadeDeBitsParaAdd):
                    for j in range(QuantidadeDeBitsParaAdd):
                        if PosicoesDesconhecidas[i] + PosicoesDesconhecidas[j] + PosicoesDesconhecidas[k] == index and (
                                i != j != k):
                            return [i + 1, j + 1, k + 1]

        def acharValorDosM(TabelaGeral, bitsParaAdd):
            cont = contador = 0
            TabelaFinal = list()
            for item in TabelaGeral:
                cont += 1
                for key in item:
                    if item[key] == 'x':
                        continue
                    else:
                        contador += 1
                        index = cont

                        auxiliar = dict()

                        if Descript(bitsParaAdd, index) is None:
                            auxiliar['M' + str(contador)] = 'P' + str(
                                Descript3desconhecidos(bitsParaAdd, index)[0]), 'P' + str(
                                Descript3desconhecidos(bitsParaAdd, index)[1]), 'P' + str(
                                Descript3desconhecidos(bitsParaAdd, index)[2])
                        else:
                            auxiliar['M' + str(contador)] = 'P' + str(Descript(bitsParaAdd, index)[0]), 'P' + str(
                                Descript(bitsParaAdd, index)[1])

                        TabelaFinal.append(auxiliar)

            return TabelaFinal

        def ValoresDeP(TabelaFinal):
            ValoresDeP = dict()

            for dicionario in TabelaFinal:
                valores = str(dicionario.values())

                if 'P1' in valores:
                    chave = str(dicionario.keys()).strip("dict_keys(['").strip("'])")
                    # print(chave)
                    for item in TabelaGeral:
                        if chave in item:
                            if 'P1' not in ValoresDeP:
                                ValoresDeP['P1'] = item[chave]
                            else:
                                ValoresDeP['P1'] += item[chave]
                if 'P2' in valores:
                    chave = str(dicionario.keys()).strip("dict_keys(['").strip("'])")
                    # print(chave)
                    for item in TabelaGeral:
                        if chave in item:
                            if 'P2' not in ValoresDeP:
                                ValoresDeP['P2'] = item[chave]
                            else:
                                ValoresDeP['P2'] += item[chave]
                if 'P3' in valores:
                    chave = str(dicionario.keys()).strip("dict_keys(['").strip("'])")
                    # print(chave)
                    for item in TabelaGeral:
                        if chave in item:
                            if 'P3' not in ValoresDeP:
                                ValoresDeP['P3'] = item[chave]
                            else:
                                ValoresDeP['P3'] += item[chave]
                if 'P4' in valores:
                    chave = str(dicionario.keys()).strip("dict_keys(['").strip("'])")
                    # print(chave)
                    for item in TabelaGeral:
                        if chave in item:
                            if 'P4' not in ValoresDeP:
                                ValoresDeP['P4'] = item[chave]
                            else:
                                ValoresDeP['P4'] += item[chave]
            return ValoresDeP

        def Final(valoresDeP):
            for item in valoresDeP:
                for dicionario in TabelaGeral:
                    if item in dicionario:
                        cont = 0
                        for num in valoresDeP[item]:
                            cont += int(num)
                            if cont % 2 == 0:
                                valoresDeP[item] = 0
                            else:
                                valoresDeP[item] = 1
                        dicionario[item] = valoresDeP[item]
            return TabelaGeral

        bitsParaAdd = QuantidadeDeBitsParaAdicionar(Mensagem)
        tamanhoTabela = Tabela(bitsParaAdd, Mensagem)
        PosicoesDesconhecidas = Desconhecidos(tamanhoTabela)
        TabelaGeral = TabelaComDesconhecidos(PosicoesDesconhecidas, Mensagem)
        TabelaFinal = acharValorDosM(TabelaGeral, bitsParaAdd)
        valoresDeP = ValoresDeP(TabelaFinal)
        TabelaGeral = Final(valoresDeP)

        MensagemFinal = str()
        for item in TabelaGeral:
            valores = str(item.values()).strip("dict_values(['").strip("'])")
            MensagemFinal += valores

        return MensagemFinal


msg = Redes.HemmingCode(Mensagem)
print(msg)
