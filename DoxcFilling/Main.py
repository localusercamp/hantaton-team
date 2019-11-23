from docxtpl import DocxTemplate

doc_name = 'DogovorGPKh'
file_path = "/home/god/Hantaton/hantaton-team/DoxcFilling/"


doc = DocxTemplate(f"{file_path}{doc_name}.docx")
context = { 'CompanyCity' : "Ханты"}
doc.render(context)

doc.save(f"{file_path}шаблон-final.pdf")

# context = { 'director' : "И.И.Иванов"}
# doc.render(context)
# doc.save("шаблон-final.docx")
