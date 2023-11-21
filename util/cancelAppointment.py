from listAppointments import list_appointments

scheduled_appointments = []

def cancel_appointment():
    """
        Função para cancelar uma consulta agendada.
        Solicita ao usuário para escolher uma consulta da lista de consultas agendadas.
        Remove a consulta escolhida da lista de consultas agendadas.
    """
    list_appointments()
    if scheduled_appointments:
        appointmentNumber = int(input('Escolha o número da consulta a ser cancelada:')) - 1
        if 0 <= appointmentNumber < len(scheduled_appointments):
            canceledAppointment = scheduled_appointments.pop(appointmentNumber)
            print(f'Consulta do paciente {canceledAppointment[0]} com o Dr{canceledAppointment[1]} no dia {canceledAppointment[3]} às{canceledAppointment[4]} foi cancelada.')
        else:
            print('Número de consulta inválido.')
    else:
        print('Não há consultas agendadas.')
