import requests
import re
import tkinter as tk
from tkinter import messagebox
import time

# Variáveis globais para controle do limite de consultas
consultas_realizadas = 0
inicio_periodo = None

def consultar_cnpj():
    global consultas_realizadas, inicio_periodo

    # Controle de tempo e limite de consultas por minuto (limitação da API)
    agora = time.time()
    
    if inicio_periodo is None or agora - inicio_periodo > 60:
        inicio_periodo = agora
        consultas_realizadas = 0
    
    if consultas_realizadas >= 5:
        tempo_restante = int(60 - (agora - inicio_periodo))
        messagebox.showerror("Erro", f"ERRO AO CONSULTAR, AGUARDE {tempo_restante} SEGUNDOS PARA TENTAR NOVAMENTE")
        return

    # Obtém o CNPJ digitado
    cnpj_input = cnpj_entry.get()
    
    # Remove caracteres não numéricos do CNPJ usando regex
    cnpj = re.sub(r'\D', '', cnpj_input)
    
    if not cnpj or len(cnpj) != 14:
        messagebox.showerror("Erro", "Digite um CNPJ válido!")
        return
    
    url = f"https://open.cnpja.com/office/{cnpj}"
    
    try:
        # Faz a requisição para o endpoint
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            consultas_realizadas += 1
            dados = resposta.json()
            
            # Verifica o status geral da empresa
            status_geral = dados.get("status", {}).get("text", "Não informado")
            resultado = f"Status geral: {status_geral}\n\n"
            
            # Verifica os registros estaduais
            registros = dados.get("registrations", [])
            if registros:
                for reg in registros:
                    status_texto = reg.get("status", {}).get("text", "Não informado")
                    resultado += f"Situação Cadastral: {status_texto}\n"
            else:
                resultado += "Não há informações sobre registros estaduais."
            
            # Exibe o resultado em uma janela pop-up
            messagebox.showinfo("Resultado da Consulta", resultado)
        else:
            messagebox.showerror("Erro", f"Erro ao consultar o CNPJ. Status code: {resposta.status_code}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função para sair
def sair():
    app.destroy()

# Criação da janela principal
app = tk.Tk()
app.title("Consulta de CNPJ")
app.geometry("400x200")

# Campo de entrada para o CNPJ
tk.Label(app, text="Digite o CNPJ:", font=("Arial", 12)).pack(pady=10)
cnpj_entry = tk.Entry(app, font=("Arial", 12), width=30)
cnpj_entry.pack(pady=5)

# Botão para consultar
consultar_button = tk.Button(app, text="Consultar", font=("Arial", 12), command=consultar_cnpj)
consultar_button.pack(pady=10)

# Botão para sair
sair_button = tk.Button(app, text="Sair", font=("Arial", 12), command=sair)
sair_button.pack(pady=10)

# Inicia o loop da aplicação
app.mainloop()
