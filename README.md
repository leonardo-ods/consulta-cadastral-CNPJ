# Consulta Situação Cadastral de CNPJ

Este é um programa simples em Python que realiza a consulta da situação cadastral de CNPJs usando uma **API pública**. Criado para facilitar a rotina do setor financeiro, o sistema permite verificar rapidamente se um CNPJ está **ativo** e **apto para emissão de notas fiscais**, com uma interface gráfica intuitiva desenvolvida com **Tkinter**.

💬 Criado com foco na praticidade e na automação de rotinas do dia a dia.

## 💡 Funcionalidades

- Consulta a situação cadastral de um CNPJ;
- Interface gráfica simples e direta;
- Respeita o limite de 5 consultas por minuto da API;
- Exibe mensagens amigáveis para o usuário em caso de erro ou espera;
- Pode ser convertido em executável (.exe) com PyInstaller para facilitar o uso por equipes não técnicas.

## 🖥️ Tela do programa

![image](https://github.com/user-attachments/assets/9fa8d47e-c511-4d06-986a-c4bd03a040c1)
![image](https://github.com/user-attachments/assets/30b2ae18-2f3b-4e1d-ac35-ef31ceaadb3b)
![image](https://github.com/user-attachments/assets/3bf7d980-b87b-4005-9ec9-f0f9a232117e)

*Interface gráfica simples com Tkinter*

## 📄 Bibliotecas utilizadas

- requests
- tkinter (já incluído na instalação padrão do Python)
- re (biblioteca padrão)
- time (biblioteca padrão)

## 🔐 Sobre a API utilizada
Esta aplicação usa a API pública do CNPJA.com para obter os dados cadastrais. A API permite até 5 consultas por minuto, por isso o programa já controla esse limite internamente.
