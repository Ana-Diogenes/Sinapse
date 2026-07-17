import abc
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import random
from datetime import datetime
import csv
import ast

class DadosFactuais:
    '''
    Informações mais basicas do usuario
    
    Attributes:
        idade (int): idade
        genero (str): genero
        ano_academico (int): ano que a pessoa está na escola ou faculdade
    '''
    def __init__(self,idade,genero,ano_academico):  
        self.__idade = idade
        self.__genero = genero
        self.__ano_academico = ano_academico 
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        if type(valor) == int:
            self.__idade = valor
            return True
        return False

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, valor):
        if type(valor) == str:
            self.__genero = valor
            return True
        return False

    @property
    def ano_academico(self):
        return self.__ano_academico

    @ano_academico.setter
    def ano_academico(self, valor):
        if type(valor) == int:
            self.__ano_academico = valor
            return True
        return False

class Caracterizacao:
    """Informacoes sobre o usuario necessarias para prever seu nivel de burnout

        Attributes:
            dados_factuais (DadosFactuais): Informações mais basicas do usuario
            horas_estudo_dia (float): tempo que o usuario passa estudando
            pressao_provas (float): pressao antes de provas avaliada em uma escala de 0-10
            performance_academica (float): performance academica avaliada em uma escala de 0-10
            nivel_estresse (float): nivel de estresse avaliado em uma escala de 0-10
            nivel_ansiedade (float): nivel de ansiedade avaliado em uma escala de 0-10
            nivel_depressao (float): nivel de depressao avaliado em uma escala de 0-10
            horas_sono (float): horas de sono diarias
            atividade_fisica (float): nivel de atividade fisica avaliada em uma escala de 0-10
            suporte_social (float): nivel de suporte que o usuario tem das pessoas do seu convivio avaliado em uma escala de 0-10
            tempo_tela (float): horas que o usuario passa em telas
            uso_internet (float): horas que o usuario passa na internet
            estresse_financeiro (float): nivel de estresse financeiro avaliado em uma escala de 0-10
            expectativa_familiar (float): nivel de espectativa que a familia tem no usuario avaliado em uma escala de 0-10
    """
    def __init__(self,dados_factuais,horas_estudo_dia,pressao_provas,performance_academica,nivel_estresse,nivel_ansiedade,nivel_depressao,horas_sono,atividade_fisica,suporte_social,tempo_tela,uso_internet,estresse_financeiro,expectativa_familiar):        
        self.dados_factuais = dados_factuais
        self.__horas_estudo_dia = horas_estudo_dia
        self.__pressao_provas = pressao_provas
        self.__performance_academica = performance_academica
        self.__nivel_estresse = nivel_estresse
        self.__nivel_ansiedade = nivel_ansiedade
        self.__nivel_depressao = nivel_depressao
        self.__horas_sono = horas_sono
        self.__atividade_fisica = atividade_fisica
        self.__suporte_social = suporte_social
        self.__tempo_tela = tempo_tela
        self.__uso_internet = uso_internet
        self.__estresse_financeiro = estresse_financeiro
        self.__expectativa_familiar = expectativa_familiar
    
    @property
    def horas_estudo_dia(self):
        return self.__horas_estudo_dia

    @horas_estudo_dia.setter
    def horas_estudo_dia(self, valor):
        if type(valor) == float:
            self.__horas_estudo_dia = valor
            return True
        return False

    @property
    def pressao_provas(self):
        return self.__pressao_provas

    @pressao_provas.setter
    def pressao_provas(self, valor):
        if type(valor) == float:
            self.__pressao_provas = valor
            return True
        return False

    @property
    def performance_academica(self):
        return self.__performance_academica

    @performance_academica.setter
    def performance_academica(self, valor):
        if type(valor) == float:
            self.__performance_academica = valor
            return True
        return False

    @property
    def nivel_estresse(self):
        return self.__nivel_estresse

    @nivel_estresse.setter
    def nivel_estresse(self, valor):
        if type(valor) == float:
            self.__nivel_estresse = valor
            return True
        return False

    @property
    def nivel_ansiedade(self):
        return self.__nivel_ansiedade

    @nivel_ansiedade.setter
    def nivel_ansiedade(self, valor):
        if type(valor) == float:
            self.__nivel_ansiedade = valor
            return True
        return False

    @property
    def nivel_depressao(self):
        return self.__nivel_depressao

    @nivel_depressao.setter
    def nivel_depressao(self, valor):
        if type(valor) == float:
            self.__nivel_depressao = valor
            return True
        return False

    @property
    def horas_sono(self):
        return self.__horas_sono

    @horas_sono.setter
    def horas_sono(self, valor):
        if type(valor) == float:
            self.__horas_sono = valor
            return True
        return False

    @property
    def atividade_fisica(self):
        return self.__atividade_fisica

    @atividade_fisica.setter
    def atividade_fisica(self, valor):
        if type(valor) == float:
            self.__atividade_fisica = valor
            return True
        return False

    @property
    def suporte_social(self):
        return self.__suporte_social

    @suporte_social.setter
    def suporte_social(self, valor):
        if type(valor) == float:
            self.__suporte_social = valor
            return True
        return False

    @property
    def tempo_tela(self):
        return self.__tempo_tela

    @tempo_tela.setter
    def tempo_tela(self, valor):
        if type(valor) == float:
            self.__tempo_tela = valor
            return True
        return False

    @property
    def uso_internet(self):
        return self.__uso_internet

    @uso_internet.setter
    def uso_internet(self, valor):
        if type(valor) == float:
            self.__uso_internet = valor
            return True
        return False

    @property
    def estresse_financeiro(self):
        return self.__estresse_financeiro
    
    @estresse_financeiro.setter
    def estresse_financeiro(self, valor):
        if type(valor) == float:
            self.__estresse_financeiro = valor
            return True
        return False

    @property
    def expectativa_familiar(self):
        return self.__expectativa_familiar

    @expectativa_familiar.setter
    def expectativa_familiar(self, valor):
        if type(valor) == float:
            self.__expectativa_familiar = valor
            return True
        return False
    def __str__(self):
        return str([self.dados_factuais.idade,self.dados_factuais.genero,self.dados_factuais.ano_academico,self.horas_estudo_dia,self.pressao_provas,self.performance_academica,self.nivel_estresse,self.nivel_ansiedade,self.nivel_depressao,self.horas_sono,self.atividade_fisica,self.suporte_social,self.tempo_tela,self.uso_internet,self.estresse_financeiro,self.expectativa_familiar])

class ModeloIA():
    """
    Classe que preve o nível de risco do usuario
    """    
    def prever(self,dados):  
        tabela = pd.read_csv("student_mental_health_burnout_1M.csv")
        tradutor = LabelEncoder() 
        tabela['gender'] = tradutor.fit_transform(tabela['gender'])
        x = tabela.drop(['burnout_score','mental_health_index','risk_level','dropout_risk'], axis=1)
        y = tabela ['risk_level']
        ia_arvore = RandomForestClassifier()
        ia_arvore.fit(x,y)
        previsao = pd.DataFrame([{'age': dados.dados_factuais.idade,'gender': dados.dados_factuais.genero,'academic_year': dados.dados_factuais.ano_academico,'study_hours_per_day': dados.horas_estudo_dia,'exam_pressure': dados.pressao_provas,'academic_performance': dados.performance_academica,'stress_level': dados.nivel_estresse,'anxiety_score': dados.nivel_ansiedade,'depression_score': dados.nivel_depressao,'sleep_hours': dados.horas_sono,'physical_activity': dados.atividade_fisica,'social_support': dados.suporte_social,'screen_time': dados.tempo_tela,'internet_usage': dados.uso_internet,'financial_stress': dados.estresse_financeiro,'family_expectation': dados.expectativa_familiar}])
        previsao['gender'] = tradutor.transform(previsao['gender'])
        nova_previsao = ia_arvore.predict(previsao)
        return nova_previsao

class Habito (abc.ABC):
    """Habito do ususario

    Attributes:
        nome (str): nome do habito
    """    
    nome = 'Habito'
    
    @abc.abstractmethod
    def motivar (self):
        pass
    
class DormirCedo(Habito):
    """
    Habito dormir cedo

    Attributes:
        nome (str): nome do habito
    """
    nome = 'dormir cedo'
    def motivar(self):
        return random.choice(["Dormir cedo hoje é investir em uma versao mais forte de você amanha.","Seu corpo precisa de descanso tanto quanto sua mente precisa de foco.","Quem dorme cedo nao perde tempo — ganha energia.","A disciplina de hoje é o sucesso de amanha começando no seu sono.","Desligar agora é escolher acordar melhor depois.","Nao é sobre dormir menos, é sobre viver melhor.","A noite bem dormida é o primeiro passo de um dia produtivo.","Seu futuro agradece cada hora de sono que você respeita hoje."])
    
    def calular_sono(self,inicio,fim):
        t1 = datetime.strptime(inicio,"%H:%M")
        t2 = datetime.strptime(fim,"%H:%M")
        if t2 < t1:
            t2 = t2.replace(day=2)
        return t2 - t1

class AtividadeFisica (Habito):
    """
    Habito praticar atividade fisica

    Attributes:
        nome (str): nome do habito
    """
    nome = 'atividade fisica'
    def motivar(self):
        return random.choice(["Seu corpo pode até pedir para parar, mas sua mente decide continuar.","Um treino hoje é um passo a menos em direçao à sua melhor versao.","Disciplina vence a motivaçao quando a vontade acaba.","Você nao treina só o corpo, treina a mente também.","O esforço de hoje é o resultado de amanha.","Nao espere sentir vontade, crie o hábito.","Cada gota de suor te aproxima do seu objetivo.","O limite começa onde sua determinaçao acaba.","Treinar é investir em você mesmo.","Você é mais forte do que a desculpa que tentou te parar."])
    def calcular_IMC(self,peso,altura):
        return peso/(altura**2)

class Leitura (Habito):
    """
    Habito leitura

    Attributes:
        nome (str): nome do habito
    """
    nome = 'leitura'
    def motivar(self):
        return random.choice(["Quem lê vive mil vidas em uma só.", "Ler é treinar a mente para enxergar o mundo de outra forma.", "Um livro por dia afasta a ignorância para sempre.", "A leitura abre portas que a realidade ainda nao mostrou.", "Quem lê nunca está sozinho.", "Cada página lida é um passo no seu crescimento.", "Livros sao academias para a mente.", "Ler hoje é pensar melhor amanha.", "A leitura transforma curiosidade em conhecimento.", "Quanto mais você lê, mais você entende o mundo."])
    def calcular_media(self,paginas,dias):
        return paginas/dias
    
class Meditacao (Habito):
    """
    Habito meditar

    Attributes:
        nome (str): nome do habito
    """
    nome = 'meditacao'
    def motivar(self):
        return random.choice(["Respire fundo e permita que sua mente encontre a calma.", "Cada respiraçao é uma oportunidade de recomeçar.", "O silêncio interior é uma fonte inesgotável de força.", "Você nao precisa controlar tudo; apenas esteja presente.", "A paz que você procura já existe dentro de você.", "Deixe os pensamentos passarem como nuvens no céu.", "Seu bem-estar começa com um momento de atençao plena.", "Respire tranquilidade, expire preocupações.", "A serenidade cresce quando você desacelera."])
    def calcular_tempo_meditacao(self,inicio,fim):
        t1 = datetime.strptime(inicio,"%H:%M")
        t2 = datetime.strptime(fim,"%H:%M")
        if t2 < t1:
            t2 = t2.replace(day=2)
        return t2 - t1

class AtividadeMixin:
    '''
    Registra atividade do usuario
    '''
    def registrar_atividade(self,atividade):
        return f'{self.nome} - {atividade}'

class Conquista:
    '''
    Registra conquistas do usuario
    
    Attributes:
        nome(str): nome da conquista
    '''
    
    def __init__(self,nome):
        self.nome = nome

class Usuario (AtividadeMixin):
    """
    Usuario do sistema

        Attributes:
            nome (str): nome
            senha (str): senha
            caracterizacao (Caracterizacao): informacoes do usuario
            sistema (Sistema): sistema em que o usuario está
            novo (bool, optional): diz se o usuario é novo no sistema, por padrão é True.
        """    
    def __init__(self,nome, senha, caracterizacao,sistema,novo = True):    
        self.sistema = sistema
        self.nome = nome
        self.__senha = senha
        self.caracteristicas= caracterizacao
        self.atividades = []
        self.habitos = []
        self.conquistas = []
        self.atividades.append(self.registrar_atividade('criou conta'))
        if novo == True:
            sistema.__add__(self)
        
    def listar_habitos(self):
        lista = []
        for h in self.habitos:
            lista.append(h.nome)
        return str(lista)
    
    def listar_conquistas(self):
        lista = []
        for c in self.conquistas:
            lista.append(c.nome)
        return str(lista)
        
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self,nova_senha):
        if len(nova_senha) >=8:
            self.__senha = nova_senha

    def prever(self):
        self.atividades.append(self.registrar_atividade('fez previsao com RandomForest'))
        self.adicionar_conquista('Usuario de IA')
        self.sistema.atualizar_sistema(self)
        return ModeloIA().prever(self.caracteristicas)

    def adicionar_conquista(self, conquista):
        self.conquistas.append(Conquista(conquista))
        self.atividades.append(self.registrar_atividade(f'obteve a conquista {conquista}'))
        self.sistema.atualizar_sistema(self)
    
    def adicionar_habito(self,habito):
        self.habitos.append(habito)
        self.atividades.append(self.registrar_atividade(f'adiquiriu o habito {habito.nome}'))
        self.adicionar_conquista('Melhores Habitos')
        self.sistema.atualizar_sistema(self)
    def atualizar_caracterizacao(self, caracterizacao):
        self.caracteristicas = caracterizacao
        self.atividades.append(self.registrar_atividade("atualizou a caracterizacao"))
        self.adicionar_conquista('Voce mudou')
        self.sistema.atualizar_sistema(self)    
    
class Sistema:
    """
    Sistema que armazena os usuarios
    
    attributes:
        senha(str): senha do sistema
        usuarios(list): lista de usuarios do sistema
    """
    def __init__(self):
        with open('usuarios.csv', "r", newline='') as lista_usuarios:
            users = list(csv.reader(lista_usuarios, delimiter=","))
        self.usuarios = users

    def atualizar_sistema(self, usuario):
        lista_nova = []
        with open('usuarios.csv', "r", newline='') as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                if linha[0].lower() != usuario.nome.lower():
                    lista_nova.append(linha)
                else:
                    lista_nova.append([usuario.nome, usuario.senha, str(usuario.caracteristicas), str(usuario.atividades), usuario.listar_habitos(), usuario.listar_conquistas()])
        with open('usuarios.csv', 'w', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(lista_nova)
            
    def procurar_usuario(self,nome,senha):
        for user in self.usuarios:
            if user[0] == nome and user[1]==senha:
                lista = ast.literal_eval(user[2])
                usuario = Usuario(user[0],user[1],Caracterizacao(DadosFactuais(lista[0],lista[1],lista[2]),float(lista[3]),float(lista[4]),float(lista[5]),float(lista[6]),float(lista[7]),float(lista[8]),float(lista[9]),float(lista[10]),float(lista[11]),float(lista[12]),float(lista[13]),float(lista[14]),float(lista[15])),self,False)
                usuario.atividades = ast.literal_eval(user[3])
                for h in ast.literal_eval(user[4]):
                    if h == "dormir cedo":
                        usuario.habitos.append(DormirCedo())
                    elif h == "atividade fisica":
                        usuario.habitos.append(AtividadeFisica())
                    elif h == "leitura":
                        usuario.habitos.append(Leitura())
                    elif h == "meditacao":
                        usuario.habitos.append(Meditacao())
                conquistas = ast.literal_eval(user[5])
                usuario.conquistas = []
                for c_nome in conquistas:
                    usuario.conquistas.append(Conquista(c_nome))
                return usuario
        return False
            
    def __add__(self, usuario):
        with open('usuarios.csv', "a", newline='') as usuarios:
            escritor = csv.writer(usuarios)
            escritor.writerow([usuario.nome, usuario.senha, str(usuario.caracteristicas), str(usuario.atividades), usuario.listar_habitos(), usuario.listar_conquistas()])
        self.usuarios.append([usuario.nome, usuario.senha, str(usuario.caracteristicas), str(usuario.atividades), usuario.listar_habitos(), usuario.listar_conquistas()])
        return self
    
    def __sub__(self, usuario):
        lista_nova = []
        achou = False
        with open('usuarios.csv', "r", newline='') as usuarios:
            lista_usuarios = csv.reader(usuarios, delimiter=",")
            for linha in lista_usuarios:
                if (linha[0]).lower() != (usuario).lower():
                    lista_nova.append(linha)
                elif (linha[0]).lower() == (usuario).lower():
                    achou = True
        if achou == False:
            return self
        with open('usuarios.csv', 'w', newline='') as users:
            escritor = csv.writer(users)
            escritor.writerows(lista_nova)
        self.usuarios = lista_nova
        return self

class Dev(Usuario):
    """
    Tem acesso as informações do sistema e pode modifica-lo

    Attributes:
        senha_dev(str): atributo da classe, compartilhado por todos os devs
        sistema(Sistema): sistema que o dev acessa
    """    
    __senha_dev = 'DevDoSistema'
    
    def listar_usuarios(self):
        return self.sistema.usuarios
    
    def excluir_usuario(self,usuario):
        self.sistema = self.sistema - usuario
        return self.sistema
    
    @property
    def senha_dev(self):
        return Dev.__senha_dev
    
    @senha_dev.setter
    def senha_dev(self,nova_senha):
        if len(nova_senha) >=8:
            Dev.senha_dev = nova_senha
            
class Mod(Usuario):
    """
    Tem acesso ao nome dos usuarios do sistema

    Attributes:
        senha_mod(str): atributo da classe, compartilhado por todos os mods
        sistema(Sistema): sistema que o mod acessa
    """
    __senha_mod = 'ModDoSistema'
        
    def listar_usuarios(self):
        nomes_usuarios = []
        for user in self.sistema.usuarios:
            nomes_usuarios.append(user[0])
        return nomes_usuarios

    @property
    def senha_mod(self):
        return Mod.__senha_mod
    
    @senha_mod.setter
    def senha(self,nova_senha):
        if len(nova_senha) >=8:
            Mod.__senha_mod = nova_senha

class InterfaceMostrarDados(abc.ABC):
    """
    Interface abstrata para mostrar de dados do usuário no terminal
    """
    
    @abc.abstractmethod
    def mostrar(self,usuario):
        pass
    
class MostrarCaracterização(InterfaceMostrarDados):
    """
    Imprime a caracterização completa do usuario
    """
    def mostrar(self, usuario):
        c = usuario.caracteristicas
        d = c.dados_factuais

        print("=" * 50)
        print("          CARACTERIZAÇÃO DO USUÁRIO")
        print("=" * 50)
        print(f"Idade:                 {d.idade}")
        print(f"Gênero:                {d.genero}")
        print(f"Ano acadêmico:         {d.ano_academico}")
        print(f"Horas de estudo:       {c.horas_estudo_dia}")
        print(f"Pressão nas provas:    {c.pressao_provas}")
        print(f"Performance:           {c.performance_academica}")
        print(f"Nível de estresse:     {c.nivel_estresse}")
        print(f"Nível de ansiedade:    {c.nivel_ansiedade}")
        print(f"Nível de depressão:    {c.nivel_depressao}")
        print(f"Horas de sono:         {c.horas_sono}")
        print(f"Atividade física:      {c.atividade_fisica}")
        print(f"Suporte social:        {c.suporte_social}")
        print(f"Tempo de tela:         {c.tempo_tela}")
        print(f"Uso da internet:       {c.uso_internet}")
        print(f"Estresse financeiro:   {c.estresse_financeiro}")
        print(f"Expectativa familiar:  {c.expectativa_familiar}")
        print("=" * 50)

class MostrarUsuario(InterfaceMostrarDados):
    """
    Imprime um resumo das informações do usuario
    """
    def mostrar(self, usuario):
        print("=" * 50)
        print("         INFORMAÇÕES DO USUÁRIO")
        print("=" * 50)
        print(f"Nome:                  {usuario.nome}")
        print(f"Hábitos:               {usuario.listar_habitos()}")
        print(f"Quantidade conquistas: {len(usuario.conquistas)}")
        print("=" * 50)