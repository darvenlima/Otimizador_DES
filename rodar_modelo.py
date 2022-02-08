
import subprocess
import random
import math
import time
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
#from tf.optimizers.Adam import Adam
from keras.callbacks import EarlyStopping

from analise_restricoes import analise_das_restricoes




def avaliar_resposta(Pop,resposta_meta,FO,model,media_score,media_MSE,linguagem,max_ou_min,nome_codigo_simulacao,nome_arquivo_entrada,nome_arquivo_saida, dados_de_entrada, dados_de_saida, restricoes):
    reposta_real = 0
    CREATE_NO_WINDOW = 0x08000000
    """altera os valores de entrada no arquivo de entrada e roda a simulação"""
    print("\n entrada \n")
    metamodelo_promisor = 0
    print(Pop)
    arquivo_entrada = open(nome_arquivo_entrada, 'w')
    for j in range(0, len(Pop)):
        arquivo_entrada.write(str(Pop[j]))
        arquivo_entrada.write(" ")
    arquivo_entrada.close()
    """analisa qual linguagem de programação está sendo usada"""
    #if media_score < 0.7:
    #    Z = 3.29
    #else:
    #    Z = 1.96
    #Z = 1.96
    if media_score > 0:
        ta = tf.TensorArray(tf.float32, size=0, dynamic_size=True, clear_after_read=False)
        x_meta = np.array(Pop)
        ta = ta.write(0,Pop)
        print(f"x_metamodelo: {ta.stack()}")
        valor_predito = model.predict(ta.stack())
        print(f"valor predito: {valor_predito}")
        resposta_meta.append(valor_predito[0][0])
        if max_ou_min == 0:
            valor_com_marguem = valor_predito - 1.96*media_MSE
            print(f"valor predito com margem: {valor_com_marguem} --- FO: {FO}")
            #if valor_com_marguem <= FO:
            metamodelo_promisor = 1
            print(f"valor pre: {valor_predito} margem: {media_MSE} valor_com_marguem: {valor_com_marguem} FO: {FO}")
            if linguagem == 0:
                subprocess.run(["C:/Program Files (x86)/Rockwell Software/Arena/siman.exe","C:/Users/darve/Desktop/Trabalho-Estoque-New.p"],creationflags=CREATE_NO_WINDOW)
            else:
                subprocess.run("python " + nome_codigo_simulacao,creationflags=CREATE_NO_WINDOW)

                    #subprocess.run("gcc -c " + nome_codigo_simulacao,creationflags=CREATE_NO_WINDOW)
                    #subprocess.run("Rscript " + nome_codigo_simulacao,creationflags=CREATE_NO_WINDOW)
            """
            else:
                valor_predito = float(valor_predito)
                valor_predito = round(valor_predito, 4)
                Pop.append(valor_predito)
            """
        else:
            valor_com_marguem = valor_predito + 1.96*media_MSE
            print(f"valor predito com margem: {valor_com_marguem} --- FO: {FO}")
            #if valor_com_marguem >= FO:
            metamodelo_promisor = 1
            print(f"valor pre: {valor_predito} margem: {media_MSE} valor_com_marguem: {valor_com_marguem} FO: {FO}")
            if linguagem == 0:
                subprocess.run(["C:/Program Files (x86)/Rockwell Software/Arena/siman.exe","C:/Users/darve/Desktop/Trabalho-Estoque-New.p"],creationflags=CREATE_NO_WINDOW)
            else:
                subprocess.run("python " + nome_codigo_simulacao, creationflags=CREATE_NO_WINDOW)

            """
            else:
                valor_predito = float(valor_predito)
                valor_predito = round(valor_predito, 4)
                Pop.append(valor_predito)
            """
    else:
        metamodelo_promisor = 1
        if linguagem == 0:
            subprocess.run(["C:/Program Files (x86)/Rockwell Software/Arena/siman.exe","C:/Users/darve/Desktop/Trabalho-Estoque-New.p"],creationflags=CREATE_NO_WINDOW)
        else:
            subprocess.run("python " + nome_codigo_simulacao, creationflags=CREATE_NO_WINDOW)

    if metamodelo_promisor == 1:
        """pega o valor de saída e avalia a solução"""
        arquivo_saida = open(nome_arquivo_saida, 'r')
        resultado = arquivo_saida.read()
        resultado = resultado.split(" ")
        #print(dados_de_saida)
        arquivo_saida.close()



        """armazena a solução na lista Pop"""

        for l in range(0,len(dados_de_saida)):
            if dados_de_saida[l] == "funcao objetivo":
                funcao_objetivo = l

        reposta_real = float(resultado[funcao_objetivo])
        reposta_real = round(reposta_real, 4)

        """colocar teste para verificar viabilidade"""
        if analise_das_restricoes(0,dados_de_entrada, Pop, dados_de_saida, resultado, restricoes) == True:
            print("\n solucao viavel\n")
            print("\n resultados \n")
            print(resultado)
            for j in range(0,len(dados_de_saida)):
                if dados_de_saida[j] == "funcao objetivo":
                    funcao_objetivo = j
            print("\n funcao objetivo\n")
            print(float(resultado[funcao_objetivo]))
            Pop.append(float(resultado[funcao_objetivo]))
            Pop[len(Pop)-1] = round(Pop[len(Pop)-1], 4)
        else:
            for j in range(0,len(dados_de_saida)):
                if dados_de_saida[j] == "funcao objetivo":
                    funcao_objetivo = j
            print("\n funcao objetivo\n")
            print(float(resultado[funcao_objetivo]))
            if max_ou_min == 0:
                Pop.append(10000000)
            else:
                Pop.append(-10000000)


    return Pop[len(Pop)-1],reposta_real
