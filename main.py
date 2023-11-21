from .util.registerDoctor import register_doctor
from .util.scheduleAppointment import schedule_appointment
from .util.listAppointments import list_appointments
from .util.cancelAppointment import cancel_appointment
from .util.generateReport import generate_report
from .util.addHours import add_hours

while True:
  print('''
  Sistema de Gerenciamento de Consultas Hospitalares")
  1. Cadastrar Médico
  2. Agendar Consulta
  3. Lista de Consultas Agendadas
  4. Cancelar Consulta
  5. Relatório de Consultas
  6. Adicionar Horários
  0. Sair''')

  escolha = input("Escolha a opção desejada: ")

  if escolha == "1":
    register_doctor()

  elif escolha == "2":
    schedule_appointment()

  elif escolha == "3":
    list_appointments()

  elif escolha == "4":
    cancel_appointment()

  elif escolha == "5":
    generate_report()

  elif escolha == "6":
    add_hours()

  elif escolha == "0":
    print('Obrigado por acessar nosso Sistema... Até logo')
    break

  else:
    print("Opção inválida. Tente novamente.")