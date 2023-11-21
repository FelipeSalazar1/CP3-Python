scheduled_appointments = []

def generate_report():
    """
        Função para gerar um relatório de todas as consultas agendadas.
        Imprime o nome do paciente, o nome do médico, a especialidade do médico, a data e o horário de cada consulta.
    """
    option = input('Deseja visualizar o relatório por (1) dia, (2) médico ou (3) paciente? ')
    if option == '1':
        day = input('Digite o dia: ')
        dayAppointments = [appointment for appointment in scheduled_appointments if appointment[3] == day]
        if dayAppointments:
            print(f'Relatório de Consultas no dia {day}:')
            for appointment in dayAppointments:
                print(f"Paciente: {appointment[0]}, Médico: {appointment[1]}, Data: {appointment[3]}, Horário: {appointment[4]}")
        else:
            print('Não há consultas neste dia.')
    elif option == '2':
        doctor = input('Digite o nome do médico: ')
        doctorAppointments = [appointment for appointment in scheduled_appointments if appointment[1] == doctor]
        if doctorAppointments:
            print(f'Relatório de Consultas do Dr.{doctor}:')
            for appointment in doctorAppointments:
                print(f"Paciente: {appointment[0]}, Data: {appointment[3]}, Horário: {appointment[4]}")
        else:
            print('Este médico não tem consultas agendadas.')
    elif option == '3':
        pacient = input('Digite o nome do paciente: ')
        pacient_consults = [appointment for appointment in scheduled_appointments if appointment[0] == pacient]
        if pacient_consults:
            print(f'Relatório de Consultas do paciente {pacient}:')
            for appointment in pacient_consults:
                print(f"Médico: {appointment[1]}, Data: {appointment[3]}, Horário: {appointment[4]}")
        else:
            print('Este paciente não tem consultas agendadas.')
    else:
        print('Opção inválida.')