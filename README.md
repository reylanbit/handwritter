# Handwritter ✍️

Este projeto automatiza a criação de PDFs que simulam redações escritas à mão. Ele foi desenvolvido para facilitar a conversão de textos digitais em documentos com aparência manuscrita, ideal para tarefas escolares ou documentos que exigem um toque pessoal.

## ✨ Características

- **Simulação de Caneta Realista:** Utiliza um tom de azul esférico (#112266) com leve transparência para imitar a pressão da tinta no papel.
- **Papel Pautado:** Gera automaticamente um fundo com linhas azuis claras, simulando uma folha de caderno A4.
- **Escrita Humana:** Implementa um sistema de *jitter* (pequenas variações aleatórias na posição das letras) para evitar a perfeição artificial das fontes digitais.
- **Alinhamento Inteligente:** O texto é sincronizado com as linhas da pauta e inclui indentação automática de parágrafos.
- **Download Automático:** O script baixa a fonte necessária (Caveat) diretamente se ela não estiver presente.

## 🚀 Como usar

### Pré-requisitos

Você precisará do Python instalado em sua máquina.

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/reylanbit/handwritter.git
   cd handwritter
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Execução

Basta rodar o script principal:
```bash
python handwriter.py
```

O arquivo `redacao_manuscrita.pdf` será gerado na raiz do projeto.

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [ReportLab](https://www.reportlab.com/) - Para geração de PDFs.
- [Requests](https://requests.readthedocs.io/) - Para download de recursos externos.

---
Desenvolvido com foco em realismo e facilidade de uso.
