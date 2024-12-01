from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Top 10 Economic Indicators with Public Data Links', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Data to be added to the PDF
data = {
    "Gross Domestic Product (GDP)": [
        "World Bank GDP Data: https://data.worldbank.org/indicator/NY.GDP.MKTP.CD",
        "FRED GDP Data: https://fred.stlouisfed.org/series/GDP/"
    ],
    "Unemployment Rate": [
        "Bureau of Labor Statistics Unemployment Data: https://www.bls.gov/data/",
        "Google Public Data Explorer - Unemployment: https://www.google.com/publicdata/explore?ds=z1ebjpgk2654c1_"
    ],
    "Consumer Price Index (CPI)": [
        "Bureau of Labor Statistics CPI Data: https://www.bls.gov/cpi/data.htm",
        "FRED CPI Data: https://fred.stlouisfed.org/series/CPALTT01USM657N"
    ],
    "Producer Price Index (PPI)": [
        "Bureau of Labor Statistics PPI Data: https://www.bls.gov/data/"
    ],
    "Retail Sales": [
        "FRED Retail Sales Data: https://fred.stlouisfed.org/series/GDP/"
    ],
    "Industrial Production": [
        "FRED Industrial Production Data: https://fred.stlouisfed.org/series/GDP/"
    ],
    "Housing Starts": [
        "FRED Housing Starts Data: https://fred.stlouisfed.org/series/GDP/"
    ],
    "Trade Balance": [
        "FRED Trade Balance Data: https://fred.stlouisfed.org/series/GDP/"
    ],
    "Consumer Confidence Index (CCI)": [
        "FRED CCI Data: https://fred.stlouisfed.org/series/GDP/"
    ],
    "Stock Market Indices": [
        "FRED Stock Market Indices Data: https://fred.stlouisfed.org/series/GDP/"
    ]
}

for indicator, links in data.items():
    pdf.chapter_title(indicator)
    for link in links:
        pdf.chapter_body(link)

pdf.output('economic_indicators.pdf')

print("PDF created successfully!")
