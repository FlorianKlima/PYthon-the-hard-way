medicine = 'Coughussin'
dosage = 5
duration = 4.5

instructions = '{} - Take {} ML every {} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{2} - Take {1} ML every {0} hours'.format(duration, dosage, medicine)
print(instructions)

instructions = '{medicine} - Take {dosage} ML every {duration} hours'.format(medicine='Sneezergen', dosage=10, duration=6)
print(instructions)
