# kpi_report_automation

## Introduction
The KPI Report Automation project automates the generation and delivery of Key Performance Indicator (KPI) reports for a business using sales data. It calculates KPIs such as Total Sales, Return on Marketing Spend (ROMS), and Average Order Value (AOV) for each product category. The script also generates data visualizations and exports the results in multiple formats. The entire process is automated using cron jobs, ensuring that the reports are generated and updated regularly without manual intervention.

## Features
- Automatically generates KPI reports based on sales data.
- Computes key business KPIs like Total Sales, ROMS, AOV, and YoY Growth.
- Generates charts and visualizations for better insights.
- Export reports in multiple formats: PDF and PNG.
- Automates the report generation using cron jobs.
- Easy integration with your existing sales data and workflows.

## Technologies Used
- **Python**: The main programming language used for automation and analysis.
- **pandas**: Data manipulation and analysis library.
- **matplotlib**: Library for creating visualizations and charts.
- **openpyxl**: Used to read and write Excel files.
- **crontab**: For scheduling automated execution of scripts on a regular basis.
- **Git**: Version control system for tracking changes to the project.

## Installation
To set up the project on your local machine, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Neilanshu/kpi_report_automation.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd kpi_report_automation
    ```

3. **Create a virtual environment (optional but recommended)**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Ensure you have your sales data file (`Sales Data.xls`) in the project directory**.

## Usage
To run the automation script manually, use the following command:

```bash
python kpi_report_automation.py
```

Automating with Cron Jobs

You can set up a cron job to run the script automatically at regular intervals. For example, to run the script at 2 AM every day:
1.	Open the crontab editor:
 ```bash
crontab -e
```
2.	Add the following line to run the script daily:
 ```bash
0 2 * * * /path/to/python /path/to/kpi_report_automation.py
```
This will automatically execute the script and generate the reports every day at 2 AM.

Output
	•	Reports: The script generates a detailed KPI report which is saved in the following formats:
	•	kpi_dashboard.pdf (PDF version of the report)
	•	Graphical outputs saved as images (PNG):
	•	total_sales_per_category.png
	•	roms_per_category.png
	•	aov_per_category.png
	•	yoy_growth_per_category.png
	•	Logs: Logs of the execution process can be tracked if necessary.

Acknowledgments
	•	pandas: Used for data manipulation and analysis.
	•	matplotlib: Used for generating charts and visualizations.
	•	openpyxl: Used to handle Excel file reading and writing.
	•	crontab: For automating script execution.
