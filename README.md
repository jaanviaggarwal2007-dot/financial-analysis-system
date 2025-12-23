# Financial Statement Analysis System

- Python • MySQL • Applied Finance

# Overview

This project is an independently built financial statement analysis system designed to practice how analysts evaluate companies using real financial data rather than isolated formulas. The goal was not to create a polished product, but to understand how financial metrics behave across different business models when computed through the same analytical framework.

The system allows users to store company financial statements in a database, calculate core financial ratios, and compare performance across multiple periods. It was built as a learning tool at the intersection of finance, programming, and structured analysis.

# Why I Built This

Most finance learning at the school level focuses on memorizing ratios or solving individual problems. I wanted to understand what happens when the same ratios are applied consistently across very different companies — and what they actually signal about risk, stability, and growth.

Rather than conducting one-off calculations, I designed a reusable analytical engine that mirrors how financial analysts work:

- persistent data storage
- standardized metric definitions
- multi-period comparison
- interpretation rather than “right answers”

This project reflects my interest in finance as a discipline of context, synthesis, and judgment, not memorization.

# System Architecture & Workflow

Input → Processing → Storage → Metrics → Interpretation

- Financial data is entered manually or imported via CSV
- Python processes and validates inputs
- Data is stored in a MySQL relational database
- Financial ratios are calculated programmatically
- Results are compared across periods and interpreted by context

# Key Features

- Company and industry data storage
- Income statement and balance sheet inputs
- Automated calculation of:
   - Profitability ratios
   - Liquidity ratios
   - Growth metrics
- Multi-period comparison
- Menu-driven command-line interface
- CSV import support for real company data

# Case Studies (Same Code, Different Contexts)

To test whether a single analytical system could hold across contrasting realities, I applied the same code and metric definitions to two very different companies:

1. Nepali Hydropower Startup

- Capital-intensive
- Long development cycles
- Stable but delayed cash flows

2. Indian Technology Unicorn
   
- Asset-light
- Rapid revenue growth
- High margins with volatility

Using identical ratios across both forced a key realization:
financial ratios are not answers — they are signals whose meaning changes with business model, scale, and constraints.

A short comparative analysis memo applying this system to both case studies is included in the repository.

# Technical Stack

- Language: Python 3.8+
- Database: MySQL 8.0+
- Libraries: mysql-connector-python, datetime, csv
- Platform: GitHub

# How to Run

1. Create the MySQL database using database_setup.sql
2. Update database credentials in Finance_db.py
3. (Optional) Import sample CSV data
4. Run:
         - python Finance_db.py
5. Use the menu to add companies, input data, and calculate ratios

# Outputs (Sample)

- Net Profit Margin
- Assets-to-Liabilities Ratio
- Revenue Growth
- Net Income Growth

Outputs are displayed clearly for each period to support comparison and interpretation.

# Limitations

- No duplicate company prevention
- Limited input validation
- Simplified ratio set (educational focus)

These were conscious trade-offs to keep the system readable and extensible while learning core concepts.

# Reflection

This project taught me that analytical rigor comes from consistency and interpretation, not complexity. By forcing myself to use the same system across different contexts, I learned to read numbers as structured signals shaped by industry realities — a mindset I now bring to economics and finance more broadly.

# Included Documents

- One-page project summary
- Full project report
- Comparative case study memo
- Reflective note: “Ratios Are Signals”

# Author

- Jaanvi Aggarwal
Independent student project exploring finance through systems, data, and context.
