from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph, Spacer, Frame, PageTemplate
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def add_background(canvas, doc, bg_image_path):
    canvas.saveState()
    width, height = letter
    canvas.drawImage(bg_image_path, 0, 0, width=width, height=height)
    canvas.restoreState()

def create_pdf(file_path, logo_path, bg_image_path, tabelle, contenitori):
    pdf = SimpleDocTemplate(file_path, pagesize=letter)
    
    # Definisci il frame e il template della pagina
    frame = Frame(0, 0, letter[0], letter[1], leftPadding=0, bottomPadding=0, rightPadding=0, topPadding=0)
    template = PageTemplate(id='background', frames=frame, onPage=lambda canv, doc: add_background(canv, doc, bg_image_path))
    pdf.addPageTemplates([template])
    
    elements = []

    # Aggiungi il logo
    logo = Image(logo_path, width=2*inch, height=2*inch)
    elements.append(logo)

    # Aggiungi un po' di spazio
    elements.append(Spacer(1, 12))

    styles = getSampleStyleSheet()
    
    # Aggiungi il titolo principale
    title = Paragraph("Prezzario Mediterranea Olives", styles['Title'])
    elements.append(title)

    # Itera sulle tabelle e aggiungile al PDF
    for idx, (descrizione, data) in enumerate(zip(contenitori, tabelle)):
        # Aggiungi il sottotitolo della tabella
        subtitle = Paragraph(f"{descrizione}", styles['Heading2'])
        elements.append(subtitle)
        
        # Aggiungi la tabella
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(table)
        
        # Aggiungi un po' di spazio tra le tabelle
        elements.append(Spacer(1, 12))

    # Costruisci il PDF
    pdf.build(elements)

# Percorso del logo
logo_path = "02_logo.png"

# Percorso dell'immagine di sfondo
bg_image_path = "background.png"  # Sostituisci con il percorso della tua immagine di sfondo

# Dati delle tabelle estratti dalle immagini
tabelle = [
    [
        ['Articolo', 'Descrizione', 'Peso', 'Prezzo'],
        ['OLIVE VERDI S.S. MAMMOTH', 'kg 13.00', '€ 67.70'],
        ['OLIVE VERDI INTERE', 'kg 13.00', '€ 62.40'],
        ['OLIVE VERDI SNOCC.', 'kg 10.00', '€ 60.00'],
        ['OLIVE VERDI RONDELLE', 'kg 10.00', '€ 58.60'],
        ['KALAMATA INTERE', 'kg 13.00', '€ 76.50'],
        ['KALAMATA SNOCC.', 'kg 10.00', '€ 71.50'],
        ['KALAMATA RONDELLE', 'kg 10.00', '€ 67.40'],
        ['VERDI FARCITI AGLIO', 'kg 10.00', '€ 73.40'],
        ['VERDI FARCITI CETRIOLO', 'kg 10.00', '€ 73.40'],
        ['VERDI FARCITI PIRI PIRI', 'kg 10.00', '€ 74.80'],
        ['VERDI FARCITI JALAPENOS', 'kg 10.00', '€ 74.80'],
        ['VERDI FARCITI PEPERONE', 'kg 10.00', '€ 74.10'],
        ['VERDI FARCITI MANDORLA', 'kg 10.00', '€ 76.90'],
    ],
    [
        ['Articolo', 'Descrizione', 'Peso', 'Prezzo'],
        ['OLIVE VERDI S.S. MAMMOTH', 'kg 1.900', '€ 12.40'],
        ['OLIVE VERDI INTERE', 'kg 1.900', '€ 11.80'],
        ['OLIVE VERDI SNOCC.', 'kg 1.800', '€ 13.80'],
        ['OLIVE VERDI RONDELLE', 'kg 1.800', '€ 13.50'],
        ['KALAMATA INTERE', 'kg 1.800', '€ 14.70'],
        ['KALAMATA SNOCC.', 'kg 1.800', '€ 14.70'],
        ['KALAMATA RONDELLE', 'kg 1.800', '€ 14.60'],
        ['VERDI FARCITI AGLIO', 'kg 1.900', '€ 16.00'],
        ['VERDI FARCITI CETRIOLO', 'kg 1.900', '€ 16.00'],
        ['VERDI FARCITI PIRI PIRI', 'kg 1.900', '€ 16.30'],
        ['VERDI FARCITI JALAPENOS', 'kg 1.900', '€ 16.30'],
        ['VERDI FARCITI PEPERONE', 'kg 1.900', '€ 16.20'],
        ['VERDI FARCITI MANDORLA', 'kg 1.900', '€ 16.70'],
    ],
    [
        ['Articolo', 'Descrizione', 'Peso', 'Prezzo'],
        ['OLIVE VERDI S.S. MAMMOTH', 'kg 3.00', '€ 19.20'],
        ['OLIVE VERDI INTERE', 'kg 3.00', '€ 18.00'],
        ['OLIVE VERDI SNOCC.', 'kg 3.00', '€ 21.20'],
        ['OLIVE VERDI RONDELLE', 'kg 3.00', '€ 20.00'],
        ['KALAMATA INTERE', 'kg 3.00', '€ 22.20'],
        ['KALAMATA SNOCC.', 'kg 3.00', '€ 22.40'],
        ['KALAMATA RONDELLE', 'kg 3.00', '€ 23.20'],
        ['VERDI FARCITI AGLIO', 'kg 3.00', '€ 25.10'],
        ['VERDI FARCITI CETRIOLO', 'kg 3.00', '€ 25.10'],
        ['VERDI FARCITI PIRI PIRI', 'kg 3.00', '€ 25.10'],
        ['VERDI FARCITI JALAPENOS', 'kg 3.00', '€ 25.60'],
        ['VERDI FARCITI PEPERONE', 'kg 3.00', '€ 25.35'],
        ['VERDI FARCITI MANDORLA', 'kg 3.00', '€ 26.20'],
    ],
    [
        ['Articolo', 'Descrizione', 'Peso', 'Prezzo'],
        ['OLIVE VERDI S.S. MAMMOTH', 'kg 5.00', '€ 28.00'],
        ['OLIVE VERDI INTERE', 'kg 5.00', '€ 26.00'],
        ['OLIVE VERDI SNOCC.', 'kg 4.50', '€ 29.20'],
        ['OLIVE VERDI RONDELLE', 'kg 4.50', '€ 31.60'],
        ['KALAMATA INTERE', 'kg 5.00', '€ 31.30'],
        ['KALAMATA SNOCC.', 'kg 4.50', '€ 32.00'],
        ['KALAMATA RONDELLE', 'kg 5.00', '€ 31.30'],
        ['VERDI FARCITI AGLIO', 'kg 5.00', '€ 37.70'],
        ['VERDI FARCITI CETRIOLO', 'kg 5.00', '€ 37.70'],
        ['VERDI FARCITI PIRI PIRI', 'kg 5.00', '€ 38.40'],
        ['VERDI FARCITI JALAPENOS', 'kg 5.00', '€ 38.40'],
        ['VERDI FARCITI PEPERONE', 'kg 5.00', '€ 38.00'],
        ['VERDI FARCITI MANDORLA', 'kg 5.00', '€ 39.50'],
    ],
    [
        ['Articolo', 'Descrizione', 'Peso', 'Prezzo'],
        ['OLIVE VERDI INTERE', 'GR.285', '€ 2.40'],
        ['OLIVE VERDI SNOCC.', 'GR.250', '€ 2.65'],
        ['OLIVE VERDI RONDELLE', 'GR.250', '€ 2.60'],
        ['KALAMATA INTERE', 'GR.285', '€ 2.50'],
        ['KALAMATA SNOCC.', 'GR.250', '€ 2.65'],
        ['KALAMATA RONDELLE', 'GR.250', '€ 2.60'],
        ['VERDI FARCITI AGLIO', 'GR. 285', '€ 3.00'],
        ['VERDI FARCITI CETRIOLO', 'GR. 285', '€ 3.00'],
        ['VERDI FARCITI PIRI PIRI', 'GR. 285', '€ 3.00'],
        ['VERDI FARCITI JALAPENOS', 'GR. 285', '€ 3.00'],
        ['VERDI FARCITI PEPERONE', 'GR. 285', '€ 3.00'],
        ['VERDI FARCITI MANDORLA', 'GR. 285', '€ 3.10'],
    ],
    [
        ['Articolo', 'Descrizione', 'Peso', 'Prezzo'],
        ['OLIVE VERDI S.S. MAMMOTH', 'kg 0.900', '€ 6.30'],
        ['OLIVE VERDI INTERE', 'kg 0.900', '€ 5.90'],
        ['OLIVE VERDI SNOCC.', 'kg 0.800', '€ 6.80'],
        ['OLIVE VERDI RONDELLE', 'kg 0.800', '€ 7.80'],
        ['KALAMATA INTERE', 'kg 0.800', '€ 7.80'],
        ['KALAMATA SNOCC.', 'kg 0.800', '€ 7.80'],
        ['KALAMATA RONDELLE', 'kg 0.800', '€ 8.10'],
        ['VERDI FARCITI AGLIO', 'kg 0.900', '€ 8.10'],
        ['VERDI FARCITI CETRIOLO', 'kg 0.900', '€ 8.10'],
        ['VERDI FARCITI PIRI PIRI', 'kg 0.900', '€ 8.25'],
        ['VERDI FARCITI JALAPENOS', 'kg 0.900', '€ 8.25'],
        ['VERDI FARCITI PEPERONE', 'kg 0.900', '€ 8.20'],
        ['VERDI FARCITI MANDORLA', 'kg 0.900', '€ 8.50'],
    ]
]

# Elenco dei contenitori
contenitori = [
    "Latta da 20.00 Kg",
    "Boccioni da 3.0 Kg",
    "Boccioni da 5.0 Kg",
    "Latta da 10.00 Kg",
    "Vasetti in Vetro GR. 480",
    "Boccioni da 1.5 Kg"
]

# Specifica il percorso del file PDF da creare
create_pdf("prezziario_mediterranea_olives.pdf", logo_path, bg_image_path, tabelle, contenitori)
