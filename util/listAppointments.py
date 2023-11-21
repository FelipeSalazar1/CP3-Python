scheduled_appointments = []

def list_appointments():
    """
        Função para listar todas as consultas agendadas.
        Imprime o nome do paciente, o nome do médico, a especialidade do médico, a data e o horário de cada consulta.
    """
    if not scheduled_appointments:
        print('Não há consultas agendadas.')
        return

    print('Lista de Consultas Agendadas:')
    for i, appointment in enumerate(scheduled_appointments, start=1):
        print(f"{i}. Paciente: {appointment[0]}, Médico: {appointment[1]}, "
              f"Especialidade: {appointment[2]}, Data: {appointment[3]}, "
              f"Horário: {appointment[4]}")
    print('Fim da lista de consultas agendadas.')