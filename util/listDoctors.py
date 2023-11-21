doctors = []

def list_doctors():
    """
    Função para listar todos os médicos cadastrados.
    Imprime o nome e a especialidade de cada médico.
    """
    print('Médicos Cadastrados:')
    a = 0
    for i in doctors:
        print(f"{a + 1}. {doctors[a][0]} - {doctors[a][1]}")
        a += 1