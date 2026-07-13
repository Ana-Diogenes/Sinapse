# 🧠 Sinapse // Projeto Final Programação Orientada a Objetos

O **Sinapse** é um sistema desktop desenvolvido em **Python** com **CustomTkinter**, criado para auxiliar estudantes no acompanhamento de hábitos saudáveis e na conscientização sobre fatores relacionados à **Síndrome de Burnout**.

O sistema utiliza **Inteligência Artificial** para estimar o nível de risco de burnout a partir de informações acadêmicas, comportamentais e emocionais fornecidas pelo usuário. Além da previsão, a aplicação incentiva a adoção de hábitos saudáveis, registra a evolução do usuário e oferece ferramentas para promover o bem-estar físico e mental.

---

## ✨ Funcionalidades

- Cadastro e autenticação de usuários;
- Coleta de informações pessoais, acadêmicas e comportamentais;
- Predição do nível de risco de burnout utilizando Inteligência Artificial;
- Registro do histórico de atividades do usuário;
- Sistema de conquistas;
- Escolha e acompanhamento de hábitos saudáveis;
- Mensagens motivacionais personalizadas para cada hábito;
- Ferramentas auxiliares para promoção da saúde e bem-estar;
- Persistência de dados em arquivos CSV;
- Diferentes níveis de acesso (Usuário, Moderador e Desenvolvedor).

---

## 🧠 Inteligência Artificial

A previsão é realizada por um modelo de **Random Forest**, treinado a partir do conjunto de dados **Student Mental Health Burnout Dataset**.

Durante o cadastro, o usuário informa dados como:

- Idade;
- Gênero;
- Ano acadêmico;
- Horas de estudo por dia;
- Pressão durante provas;
- Desempenho acadêmico;
- Nível de estresse;
- Nível de ansiedade;
- Nível de depressão;
- Horas de sono;
- Nível de atividade física;
- Suporte social;
- Tempo de tela;
- Tempo de uso da internet;
- Estresse financeiro;
- Expectativa familiar.

Essas informações são processadas pelo modelo para classificar o usuário em um dos níveis de risco de burnout.

---

## 💪 Hábitos Saudáveis

O sistema permite que o usuário adicione hábitos saudáveis ao seu perfil. Cada hábito possui mensagens motivacionais e ferramentas específicas para auxiliar no acompanhamento.

### 😴 Dormir Cedo

- Mensagens motivacionais;
- Cálculo automático do tempo de sono.

### 🏃 Atividade Física

- Mensagens motivacionais;
- Cálculo do Índice de Massa Corporal (IMC).

### 📚 Leitura

- Mensagens motivacionais;
- Cálculo da média de páginas lidas por dia.

### 🧘 Meditação

- Mensagens motivacionais;
- Cálculo do tempo de meditação.

---

## 🏆 Sistema de Conquistas

O Sinapse recompensa automaticamente ações realizadas pelo usuário, incentivando sua participação no sistema.

Entre as conquistas disponíveis estão:

- **Usuário de IA** — obtida ao realizar a previsão de burnout;
- **Melhores Hábitos** — obtida ao adicionar novos hábitos saudáveis.

---

## 👥 Perfis de Usuário

O sistema possui três níveis de acesso:

### Usuário

- Realiza a previsão de burnout;
- Adiciona hábitos;
- Visualiza suas atividades e conquistas.

### Moderador

Além das funcionalidades do usuário:

- Pode visualizar os nomes dos usuários cadastrados no sistema.

### Desenvolvedor

Além das funcionalidades do usuário:

- Pode visualizar todos os dados cadastrados;
- Pode remover usuários do sistema.

---

## 🏗️ Arquitetura do Projeto

O projeto foi desenvolvido seguindo os princípios da **Programação Orientada a Objetos (POO)**.

Os principais conceitos utilizados são:

- Encapsulamento;
- Herança;
- Polimorfismo;
- Classes Abstratas (ABC);
- Mixins;
- Sobrecarga de operadores (`+` e `-`);
- Propriedades (`@property`);
- Separação entre regras de negócio e interface gráfica.

---

## 🛠️ Tecnologias Utilizadas

- Python
- CustomTkinter
- Pandas
- Scikit-learn
- Random Forest Classifier
- CSV
- Datetime
- AST

---

## 📂 Estrutura Geral

```text
📦 projeto
├── interface.py                      # Interface gráfica
├── lib.py                            # Regras de negócio
├── usuarios.csv                      # Banco de dados dos usuários
├── student_mental_health_burnout_1M.csv
└── README.md
```

---

## 🎯 Objetivo

O **Sinapse** busca incentivar o autocuidado e auxiliar estudantes na identificação de fatores relacionados ao burnout por meio da aplicação de técnicas de Inteligência Artificial.

Além de fornecer uma estimativa de risco, o sistema incentiva mudanças positivas na rotina por meio da adoção de hábitos saudáveis, do acompanhamento das atividades realizadas e de um sistema de conquistas, promovendo uma experiência interativa e educativa.

<img width="8192" height="2855" alt="User Management System Flow-2026-07-13-180155" src="https://github.com/user-attachments/assets/6de08edf-4958-49fc-bd30-3e58dc44d9af" />
