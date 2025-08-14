# ----------------------------------------------------
# A classe pai, Estudante, que estava faltando
# ----------------------------------------------------
class Estudante:
    """Classe base para representar um estudante com informações básicas."""

    def __init__(self, nome, ra):
        """
        Inicializa um estudante.
        
        Args:
            nome (str): Nome completo do estudante.
            ra (str): Registro Acadêmico.
        """
        self.nome = nome
        self.ra = ra

    def exibir_informacoes(self):
        """Exibe informações básicas do estudante."""
        print(f"Nome: {self.nome} | RA: {self.ra}")

    def verificar_ra(self, ra_digitado):
        """
        Verifica se o RA informado pertence ao estudante.
        
        Args:
            ra_digitado (str): RA a ser verificado.
            
        Returns:
            bool: True se o RA corresponder, False caso contrário.
        """
        return ra_digitado.upper().strip() == self.ra


# ----------------------------------------------------
# A classe filha, EstudanteADS, que herda de Estudante
# ----------------------------------------------------
class EstudanteADS(Estudante):
    """
    Classe filha que herda de Estudante e adiciona informações específicas
    do curso de Análise e Desenvolvimento de Sistemas (ADS).
    """

    def __init__(self, nome, ra, semestre, universidade, campus):
        """
        Inicializa um estudante de ADS.
        
        Args:
            nome (str): Nome completo do estudante.
            ra (str): Registro Acadêmico.
            semestre (int): Semestre atual.
            universidade (str): Nome da universidade.
            campus (str): Campus de estudo.
        """
        super().__init__(nome, ra)  # Chama o construtor da classe pai
        self.semestre = semestre
        self.universidade = universidade
        self.campus = campus

    def exibir_informacoes(self):
        """Exibe informações completas do estudante ADS com formatação visual."""
        linha = "=" * 65
        print(f"\n{linha}")
        print("🎓 ESTUDANTE ENCONTRADO")
        print(f"{linha}")
        print(f"📋 Nome Completo: {self.nome}")
        print(f"🆔 Registro Acadêmico: {self.ra}")
        print(f"📚 Semestre: {self.semestre}º")
        print(f"🏫 Universidade: {self.universidade}")
        print(f"🏢 Campus: {self.campus}")
        print(f"💻 Curso: Análise e Desenvolvimento de Sistemas")
        print(f"{linha}")


# ----------------------------------------------------
# A classe SistemaConsultaRA para gerenciar o sistema
# ----------------------------------------------------
class SistemaConsultaRA:
    """Sistema principal para consulta de RAs com interface interativa."""

    def __init__(self):
        """Inicializa o sistema com dados dos estudantes."""
        self.alunos = [
            EstudanteADS("Igor Ferreira Mazzarino Sansão", "G991559", 4, "UNIP", "Sorocaba"),
            EstudanteADS("Caio Silva", "R072762", 4, "UNIP", "Sorocaba"),
            EstudanteADS("Ryan Celestino", "R074587", 4, "UNIP", "Sorocaba"),
            EstudanteADS("Matheus Rocha", "G986BE9", 4, "UNIP", "Sorocaba"),
        ]

    def iniciar_sistema(self):
        """Inicia o loop principal do sistema de consulta."""
        print("Bem-vindo ao Sistema de Consulta de RA.")
        while True:
            ra_input = input("Por favor, digite o RA a ser consultado (ou 'sair' para encerrar): ").strip()
            
            if ra_input.lower() == 'sair':
                print("Sistema encerrado. Até mais!")
                break
            
            self.consultar_ra(ra_input)

    def consultar_ra(self, ra_digitado):
        """
        Busca e exibe as informações do estudante com o RA fornecido.
        
        Args:
            ra_digitado (str): O RA a ser pesquisado.
        """
        aluno_encontrado = None
        for aluno in self.alunos:
            if aluno.verificar_ra(ra_digitado):
                aluno_encontrado = aluno
                break  # Para o loop assim que encontrar o aluno
        
        if aluno_encontrado:
            aluno_encontrado.exibir_informacoes()
        else:
            print("❗ RA não encontrado. Por favor, verifique o número e tente novamente.")


# ----------------------------------------------------
# Bloco principal para iniciar a aplicação
# ----------------------------------------------------
if __name__ == "__main__":
    sistema = SistemaConsultaRA()
    sistema.iniciar_sistema()