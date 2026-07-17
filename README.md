![Python](https://img.shields.io/badge/Python-3.11-blue)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-GUI-green)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![POO](https://img.shields.io/badge/OOP-Project-red)
![Status](https://img.shields.io/badge/status-concluded-success)

# 🧠 Sinapse // Projeto Final Programação Orientada a Objetos

> **Sistema inteligente para monitoramento de hábitos e predição do risco de Burnout utilizando Inteligência Artificial.**

O **Sinapse** é uma aplicação desktop desenvolvida em **Python** que auxilia estudantes a desenvolver hábitos saudáveis enquanto realiza uma estimativa do nível de risco de Burnout por meio de um modelo de **Machine Learning**.

Além da predição, o sistema permite acompanhar hábitos, registrar atividades, visualizar conquistas e acessar conteúdos educativos sobre saúde mental.

---

## ✨ Funcionalidades

- 👤 Cadastro e autenticação de usuários
- 📋 Coleta de informações pessoais e acadêmicas
- 🤖 Predição do risco de Burnout utilizando **Random Forest**
- 💤 Gerenciamento de hábitos saudáveis
  - Dormir cedo
  - Atividade física
  - Leitura
  - Meditação
- 📈 Registro de atividades realizadas
- 🏆 Sistema de conquistas
- 📚 Informações educativas sobre Síndrome de Burnout
- 🛠️ Área administrativa para desenvolvedores e moderadores

---

## 🧩 Tecnologias Utilizadas

- Python 3
- CustomTkinter
- Pandas
- Scikit-learn
- CSV
- Programação Orientada a Objetos (POO)

---

## 🏗️ Arquitetura do Projeto

O sistema foi desenvolvido seguindo conceitos de **Programação Orientada a Objetos**, utilizando:

- Encapsulamento
- Herança
- Polimorfismo
- Classes Abstratas (ABC)
- Mixins
- Properties
- Separação entre interface gráfica e regras de negócio

Principais classes:

```
Sistema
│
├── Usuario
│   ├── Dev
│   └── Mod
│
├── Caracterizacao
│
├── DadosFactuais
│
├── ModeloIA
│
└── Habito
    ├── DormirCedo
    ├── AtividadeFisica
    ├── Leitura
    └── Meditacao
```

---

## 🧠 Inteligência Artificial

O sistema utiliza um modelo de classificação baseado em **Random Forest**, treinado com um conjunto de dados contendo informações relacionadas à saúde mental de estudantes.

A predição considera fatores como:

- idade;
- gênero;
- ano acadêmico;
- horas de estudo;
- pressão em provas;
- desempenho acadêmico;
- nível de estresse;
- ansiedade;
- depressão;
- horas de sono;
- atividade física;
- suporte social;
- tempo de tela;
- uso da internet;
- estresse financeiro;
- expectativa familiar.

Ao final, o modelo classifica o usuário em um dos níveis de risco:

- 🟢 Low
- 🟡 Medium
- 🔴 High

---

## 💻 Interface

A interface foi construída utilizando **CustomTkinter**, proporcionando uma experiência moderna e intuitiva.

O sistema possui telas para:

- Tela inicial
- Login
- Cadastro
- Caracterização do usuário
- Tela principal
- Resultado da IA
- Hábitos
- Atividades
- Conquistas
- Informações sobre Burnout
- Área administrativa

---

## 📂 Estrutura do Projeto

```
Sinapse/
│
├── interface.py
├── lib.py
├── usuarios.csv
├── student_mental_health_burnout_1M.csv
│
└── README.md
```

---


## 🎯 Objetivos

O projeto busca:

- incentivar hábitos saudáveis;
- conscientizar sobre saúde mental;
- auxiliar na identificação de fatores associados ao Burnout;
- aplicar conceitos de Inteligência Artificial e Programação Orientada a Objetos em uma aplicação real.

---

## 📚 Conceitos Aplicados

- Programação Orientada a Objetos
- Interface Gráfica
- Machine Learning
- Engenharia de Software
- Manipulação de arquivos CSV
- Estruturas de Dados
- Tratamento de exceções
- Persistência de dados

---

<img width="1127" height="727" alt="Captura de tela 2026-07-16 152716" src="https://github.com/user-attachments/assets/d76366c5-6dfe-48b1-a3ef-2cb3aa1c93df" />

---

<img width="8192" height="3558" alt="Diagrama-de-clases-sinapse-2026-07-17-092812" src="https://github.com/user-attachments/assets/b945c106-9c0c-4f90-b2d7-7b39fdd7dfaf" />

