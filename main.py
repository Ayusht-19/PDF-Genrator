from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm",format="A4")
df = pd.read_csv("topics.csv")

for index,row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times",style="B", size=20)
    pdf.cell(w=0,h=12,txt=row["Topic"],align="l")
    pdf.line(x1=10,y1=20,x2=200,y2=20)

pdf.output("output.pdf")