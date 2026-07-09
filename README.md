# 🧠 Sinapse // Projeto final Programação Orientada a Objetos

O **Sinapse** é um sistema desktop desenvolvido em **Python** com **CustomTkinter**, criado para auxiliar estudantes no acompanhamento de hábitos saudáveis e na identificação do risco de desenvolvimento da **Síndrome de Burnout** por meio de um modelo de Inteligência Artificial.

O sistema reúne funcionalidades de cadastro, gerenciamento de usuários, incentivo à criação de hábitos, registro de atividades e previsão do nível de risco de burnout, oferecendo uma interface moderna e intuitiva.

## ✨ Funcionalidades

- Cadastro e autenticação de usuários;
- Coleta de informações pessoais, acadêmicas e comportamentais;
- Predição do risco de burnout utilizando um modelo de **Random Forest**;
- Escolha e acompanhamento de hábitos saudáveis:
  - Dormir cedo;
  - Atividade física;
  - Leitura;
  - Meditação;
- Ferramentas auxiliares para cada hábito:
  - Cálculo do tempo de sono;
  - Cálculo do IMC;
  - Média de páginas lidas por dia;
  - Tempo de meditação;
- Exibição de recomendações personalizadas conforme o nível de risco;
- Registro de atividades realizadas pelo usuário;
- Sistema de conquistas;
- Área informativa sobre a Síndrome de Burnout;
- Painel administrativo para moderadores e desenvolvedores, permitindo gerenciamento de usuários e configurações do sistema.

---

## 🧠 Inteligência Artificial

A previsão do risco de burnout é realizada utilizando um modelo de **Random Forest**, treinado a partir do conjunto de dados **Student Mental Health Burnout Dataset**.

Durante o cadastro, o usuário responde perguntas relacionadas a fatores como:

- idade;
- gênero;
- ano acadêmico;
- horas de estudo;
- pressão das provas;
- desempenho acadêmico;
- níveis de estresse, ansiedade e depressão;
- horas de sono;
- atividade física;
- suporte social;
- tempo de tela;
- uso da internet;
- estresse financeiro;
- expectativa familiar.

Essas informações são utilizadas para classificar o usuário em um dos níveis de risco:

- 🟢 Baixo (Low)
- 🟡 Médio (Medium)
- 🔴 Alto (High)

Após a previsão, o sistema apresenta orientações e incentiva a adoção de hábitos saudáveis para melhorar a qualidade de vida.

---

## 🛠️ Tecnologias utilizadas

- Python
- CustomTkinter
- Pandas
- Scikit-learn
- Random Forest Classifier
- CSV para persistência de dados

---

## 🏛️ Arquitetura

O projeto foi desenvolvido seguindo os princípios da **Programação Orientada a Objetos (POO)**, utilizando:

- encapsulamento;
- herança;
- polimorfismo;
- classes abstratas;
- mixins.

A interface gráfica foi organizada em diversas telas independentes, facilitando a manutenção e expansão do sistema.

---

## 📁 Estrutura geral

```text
interface.py          # Interface gráfica
lib.py                # Regras de negócio
usuarios.csv          # Banco de dados dos usuários
senha_sistema.csv     # Senha administrativa
student_mental_health_burnout_1M.csv
```

---

## 🎯 Objetivo

O principal objetivo do **Sinapse** é promover hábitos saudáveis e conscientizar estudantes sobre fatores que contribuem para o burnout, utilizando técnicas de Inteligência Artificial para fornecer uma estimativa de risco e incentivar mudanças positivas na rotina.

Mais do que realizar uma previsão, o sistema busca incentivar o autocuidado, acompanhar a evolução dos usuários e oferecer ferramentas que contribuam para uma melhor saúde física e mental.

<img width="8192" height="4078" alt="User Management System Flow-2026-07-09-163251" src="https://github.com/user-attachments/assets/8f981932-7712-44be-870b-4f14447a96f7" />
