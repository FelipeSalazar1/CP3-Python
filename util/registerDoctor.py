doctors = []
def register_doctor():
    """
        Função para registrar um novo médico.
        Solicita ao usuário o nome, a especialidade e os horários disponíveis do médico.
        Adiciona o novo médico à lista de médicos.
    """
    name = input('Nome do médico: ')
    speciality = input(f'Olá Dr.{name}, qual a sua especialidade? ')
    hours = input('Quais os seus horários disponíveis? (separados por barra / ): ').split('/')
    doctor = [name, speciality, hours]
    doctors.append(doctor)
    print(f'Médico {name} cadastrado com sucesso.')