import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('ClassePrimaire.xlsx')

# Select the active worksheet
sheet = workbook.active

# Write "A" in cell C4
sheet['C5'] = 'bonjour'

# Save the workbook
workbook.save('ClassePrimaire.xlsx')
