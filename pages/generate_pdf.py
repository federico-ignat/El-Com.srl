from reportlab.lib.pagesize import A4
from reportlab.lib.pdfgen import canvas

pdf = canva.Canvas("ELCOM_Report.pdf", pagesize=A4)

# Pagina 1 
pdf.setFont("Helvatica-Bold", 22)
pdf.drawString(100, 750, "EL.COM GROUP")
pdf.drawString(100, 710, "Documentazione Aziendale")
pdf.showPage()

# Pagina 2
pdf.setFont("helvatica-bold", 18)
pdf.drawString(50, 800, "Chi e EL.COM")

pdf.setFont("Helvatica", 12)

text = pdf.beginText(50, 760)
text.textLine("EL.COM produce cablaggi elettrici.")
text.textLine("e sistemi di connessione.")
text.textLine("Opera in numerosi settori industriali.")
pdf.drawText(text)

pdf.showPage()

# Pagina 3 
pdf.setFont("Helvatica-Bold", 18)
pdf.drawString(50, 800, "Settori")

pdf.setFont("Helvatica", 12)

text = pdf.beginText(50, 760)
text.textLine("- Automotive")
text.textLine("- Aerospace")
text.textLine("- Militare")
text.textLine("- Agricolo")
pdf.drawText(text)

pdf.save()
