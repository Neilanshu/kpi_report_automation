import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
import os
import numpy as np

# Load the dataset 
file_path = "/Users/nilanshubhandare/fraud_detection/Sales Data.xls"
df = pd.read_excel(file_path)

# To make sure the 'Date' column is properly formatted as a datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Created new columns to represent the Year and Month for easier analysis
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# KPIs
# 1. Total Sales per Category
total_sales_per_category = df.groupby('Category')['TotalSales'].sum()

# 2. Return on Marketing Spend (ROMS) per Category (we're assuming 10,000 as marketing spend here)
roms_per_category = df.groupby('Category').apply(lambda x: (x['TotalSales'].sum() / 10000) * 100)

# 3. Average Order Value (AOV) per Category
aov_per_category = df.groupby('Category').apply(lambda x: x['TotalSales'].sum() / x['QuantitySold'].sum())

# Adding a new KPI for year-over-year growth
df['Sales Growth'] = df.groupby('Category')['TotalSales'].pct_change() * 100  # This is the YoY growth in percentage
yoy_growth_per_category = df.groupby('Category')['Sales Growth'].mean()

# Let's gather all the KPIs into a nice DataFrame
kpi_df = pd.DataFrame({
    'Total Sales': total_sales_per_category,
    'ROMs (%)': roms_per_category,
    'AOV': aov_per_category,
    'YoY Growth (%)': yoy_growth_per_category
})

# Make a directory to save the results if it doesn't already exist
output_dir = "kpi_dashboard_outputs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Visualizations for the KPIs
# Total Sales per Category
plt.figure(figsize=(10, 6))
sns.barplot(x=total_sales_per_category.index, y=total_sales_per_category.values, palette="Blues_d")
plt.title('Total Sales per Category', fontsize=16)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.xlabel('Category', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'total_sales_per_category.png'))
plt.close()

# ROMS per Category
plt.figure(figsize=(10, 6))
sns.barplot(x=roms_per_category.index, y=roms_per_category.values, palette="YlGnBu")
plt.title('Return on Marketing Spend (ROMS) per Category', fontsize=16)
plt.ylabel('ROMS (%)', fontsize=12)
plt.xlabel('Category', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'roms_per_category.png'))
plt.close()

# AOV per Category
plt.figure(figsize=(10, 6))
sns.barplot(x=aov_per_category.index, y=aov_per_category.values, palette="Purples")
plt.title('Average Order Value (AOV) per Category', fontsize=16)
plt.ylabel('AOV ($)', fontsize=12)
plt.xlabel('Category', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'aov_per_category.png'))
plt.close()

# Year-over-Year Sales Growth per Category
plt.figure(figsize=(10, 6))
sns.barplot(x=yoy_growth_per_category.index, y=yoy_growth_per_category.values, palette="RdYlGn")
plt.title('Year-over-Year Sales Growth per Category', fontsize=16)
plt.ylabel('YoY Growth (%)', fontsize=12)
plt.xlabel('Category', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'yoy_growth_per_category.png'))
plt.close()

# PDF for the final KPI dashboard
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# A title for the dashboard
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, 'KPI Dashboard', ln=True, align='C')

# Add the images (graphs) to the PDF
pdf.ln(10)
pdf.set_font('Arial', '', 12)

pdf.cell(200, 10, 'Total Sales per Category:', ln=True)
pdf.image(os.path.join(output_dir, 'total_sales_per_category.png'), x=10, w=190)

pdf.ln(10)
pdf.cell(200, 10, 'Return on Marketing Spend (ROMS) per Category:', ln=True)
pdf.image(os.path.join(output_dir, 'roms_per_category.png'), x=10, w=190)

pdf.ln(10)
pdf.cell(200, 10, 'Average Order Value (AOV) per Category:', ln=True)
pdf.image(os.path.join(output_dir, 'aov_per_category.png'), x=10, w=190)

pdf.ln(10)
pdf.cell(200, 10, 'Year-over-Year Sales Growth per Category:', ln=True)
pdf.image(os.path.join(output_dir, 'yoy_growth_per_category.png'), x=10, w=190)

# Save pdf
pdf_output_path = os.path.join(output_dir, 'kpi_dashboard.pdf')
pdf.output(pdf_output_path)

# To let the user know where the dashboard was saved
print(f"Dashboard successfully saved as a PDF at: {pdf_output_path}")