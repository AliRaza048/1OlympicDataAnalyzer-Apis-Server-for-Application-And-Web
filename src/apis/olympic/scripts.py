import json
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table

def json_to_pdf(json_file, pdf_file):
    # Load JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Convert JSON to DataFrame
    df = pd.DataFrame(data)
    df.to_csv(pdf_file)

# Example usage
json_file = 'dataset.json'
pdf_file = 'dataset.csv'
json_to_pdf(json_file, pdf_file)
