from listDoctors import list_doctors

doctors = []
scheduled_appointments = []

def add_hours():
    print('Gestão de Médicos - Adicionar Novos Horários')
    list_doctors()

    if doctors:
        choose_doctor = int(input('Escolha o número do médico: ')) - 1
        if 0 <= choose_doctor < len(doctors):
            choosenDoctor = doctors[choose_doctor]
            newHours = input('Digite os novos horários (separados por barra / ): ').split('/')
            choosenDoctor[2].extend(newHours)
            print('Novos horários adicionados com sucesso.')
        else:
            print('Número de médico inválido.')
    else:
        print('Não há médicos cadastrados.')