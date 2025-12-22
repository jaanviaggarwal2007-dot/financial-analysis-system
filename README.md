# Financial Analysis System

# Python & MySQL–Based Independent Project

Author: Jaanvi Aggarwal,
Country: Nepal,
Academic Interest: Economics & Finance,
Tools: Python 3.8+, MySQL 8.0+, VS Code.

# Project Overview

This project is a Financial Statement Analysis System built independently using Python and MySQL.
It is designed to simulate, in a simplified but realistic way, how financial analysts store, process, and analyze company-level financial data.

The system allows users to:

Create and store company records
Input financial statement data for multiple periods
Maintain a structured relational database
Calculate key financial ratios related to profitability, liquidity, and growth
Compare companies operating in very different economic contexts

This project was built to deepen my understanding of applied finance, databases, and analytical reasoning beyond textbook theory.

# Motivation

I wanted to explore finance not just conceptually, but computationally.

Rather than relying on pre-built tools, I chose to:
Design the database schema myself
Write the Python logic from scratch
Manually test the system using real-world-style financial data

The goal was learning through building.

# Technology Stack

Programming Language: Python 3.8+
Database: MySQL 8.0+
Connector: mysql-connector-python
Modules Used:mysql.connector, csv, datetime
Development Environment: VS Code
Platform: GitHub

# Database Structure

The system uses a relational database named finance_db with two main tables:

# Companies Table

Stores basic company information such as:

Company ID
Company Name
Industry

# Financial Statements Table

Stores period-wise financial data including:

Revenue
Net Income
Assets
Liabilities
Reporting Period

This structure allows one-to-many relationships between companies and their financial records.

# System Workflow

Financial data is entered manually or imported via CSV
Python processes and validates the input
Data is stored in a MySQL relational database
Stored data is queried to compute financial ratios
Results are displayed through a menu-driven interface

This mirrors the logical flow used in basic financial analysis pipelines.

# Case Studies Used

To test the system meaningfully, I applied it to two contrasting case studies:

- Nepali Hydropower Startup

Capital-intensive infrastructure business
Focus on asset structure and long-term liabilities
Emphasis on stable profitability and sustainability

- Indian Tech Unicorn

High-growth, scalable business model
Focus on margins and revenue growth
Used to study efficiency at scale

These two cases allowed me to compare financial behavior across very different economic and industry contexts.

# Key Metrics Calculated

Net Profit Margin
Assets-to-Liabilities Ratio
Revenue Growth Rate
Net Income Growth

The calculations are intentionally simplified but conceptually aligned with real-world financial analysis.

# Project Documentation

This repository includes two supporting PDFs:

project_summary_one_page_Jaanvi_Aggarwal.pdf
→ A one-page, friendly summary of the project, methodology, and case studies

project_report_Jaanvi_Aggarwal.pdf
→ A detailed project report including system design, workflow, tables, and outputs

# Limitations

This project is educational and has known limitations:

No duplicate company validation
Limited input error handling
No enforced foreign-key constraints
No automated data sourcing

These limitations were intentional to keep the system transparent and beginner-friendly.

# Future Improvements

Planned enhancements include:
Stronger input validation
Data visualization (charts & trends)
API-based financial data import
Expanded multi-period and valuation analysis

# Final Note

This project represents my first serious attempt to bridge finance and programming through hands-on work.
It reflects my interest in analytical thinking, systems design, and applied economics, and serves as a foundation I plan to build on in future settings.


