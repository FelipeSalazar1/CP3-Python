from listDoctors import list_doctors

doctors = []
scheduled_appointments = []

def schedule_appointment():
    """
        Função para agendar uma nova consulta.
        Solicita ao usuário o nome do paciente, o médico, a data e o horário da consulta.
        Adiciona a nova consulta à lista de consultas agendadas.
    """
    print('Agendamento de Consultas')
    list_doctors()

    if doctors:
        choose_doctor = int(input('Escolha o número do médico: ')) - 1
        if 0 <= choose_doctor < len(doctors):
            choosenDoctor = doctors[choose_doctor]
            print(f'Horários disponíveis do Dr.{choosenDoctor[0]}: {choosenDoctor[2]}')
            appointmentHour = input('Escolha o horário da consulta: ')
            appointmentPacient = input('Digite o nome do paciente: ')
            appointmentDate = input('Digite a data da consulta: ')
            appointment = [appointmentPacient, choosenDoctor[0], choosenDoctor[1], appointmentDate, appointmentHour]
            scheduled_appointments.append(appointment)
            print('Consulta agendada com sucesso.')
        else:
            print('Número de médico inválido.')
    else:
        print('Não há médicos cadastrados.')