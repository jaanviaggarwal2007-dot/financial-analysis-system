# Finance_db.py

import mysql.connector

def connect_db():
    """Connect to MySQL database"""
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",      # Change if needed
            password="localhost1234",      # Change if needed  
            database="finance_db"
        )
        return db
    except:
        print("Error connecting to database")
        return None

def show_menu():
    """Display main menu"""
    print("\n" + "="*40)
    print("FINANCIAL ANALYSIS SYSTEM")
    print("="*40)
    print("1. Add Company")
    print("2. Add Financial Statement")
    print("3. View Companies")
    print("4. View Financial Data")
    print("5. Calculate Ratios")
    print("6. Exit")
    print("="*40)

def add_company(db):
    """Add a new company"""
    print("\n--- ADD NEW COMPANY ---")
    name = input("Company Name: ")
    industry = input("Industry: ")
    
    cursor = db.cursor()
    sql = "INSERT INTO companies (name, industry) VALUES (%s, %s)"
    cursor.execute(sql, (name, industry))
    db.commit()
    print(f"Company '{name}' added successfully!")

def add_statement(db):
    """Add financial statement data"""
    print("\n--- ADD FINANCIAL STATEMENT ---")
    
    # Show companies first
    view_companies(db)
    
    company_id = input("Enter Company ID: ")
    stmt_type = input("Statement Type (Income/Balance): ")
    period = input("Period (YYYY-MM-DD): ")
    revenue = float(input("Revenue: ") or 0)
    net_income = float(input("Net Income: ") or 0)
    assets = float(input("Total Assets: ") or 0)
    liabilities = float(input("Total Liabilities: ") or 0)
    
    cursor = db.cursor()
    sql = """INSERT INTO statements 
             (company_id, type, period, revenue, net_income, assets, liabilities) 
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (company_id, stmt_type, period, revenue, net_income, assets, liabilities))
    db.commit()
    print("Financial statement added!")

def view_companies(db):
    """Show all companies"""
    cursor = db.cursor()
    cursor.execute("SELECT * FROM companies")
    companies = cursor.fetchall()
    
    print("\n--- COMPANIES ---")
    for company in companies:
        print(f"ID: {company[0]}, Name: {company[1]}, Industry: {company[2]}")

def view_financial_data(db):
    """View financial statements"""
    print("\n--- FINANCIAL DATA ---")
    
    view_companies(db)
    company_id = input("Enter Company ID to view: ")
    
    cursor = db.cursor()
    sql = """SELECT s.period, s.type, s.revenue, s.net_income, s.assets, s.liabilities 
             FROM statements s 
             WHERE company_id = %s 
             ORDER BY period DESC"""
    cursor.execute(sql, (company_id,))
    statements = cursor.fetchall()
    
    for stmt in statements:
        print(f"\nPeriod: {stmt[0]} | Type: {stmt[1]}")
        print(f"  Revenue: ${stmt[2]:,.2f}")
        print(f"  Net Income: ${stmt[3]:,.2f}")
        print(f"  Assets: ${stmt[4]:,.2f}")
        print(f"  Liabilities: ${stmt[5]:,.2f}")

def calculate_ratios(db):
    """Calculate and display financial ratios"""
    print("\n--- FINANCIAL RATIOS ---")
    
    view_companies(db)
    company_id = input("Enter Company ID: ")
    period = input("Enter Period (YYYY-MM-DD): ")
    
    cursor = db.cursor()
    sql = "SELECT revenue, net_income, assets, liabilities FROM statements WHERE company_id = %s AND period = %s"
    cursor.execute(sql, (company_id, period))
    data = cursor.fetchone()
    
    if not data:
        print("No data found for this period!")
        return
    
    revenue, net_income, assets, liabilities = data
    
    print(f"\nFinancial Ratios for Period: {period}")
    print("=" * 30)
    
    # Profitability Ratios
    if revenue > 0:
        net_margin = (net_income / revenue) * 100
        print(f"Net Profit Margin: {net_margin:.1f}%")
    
    # Liquidity Ratio (Current Ratio approximation)
    if liabilities > 0:
        current_ratio = assets / liabilities
        print(f"Assets to Liabilities Ratio: {current_ratio:.2f}")
    
    # Growth Calculation (compare with previous period)
    sql_prev = """SELECT revenue, net_income 
                  FROM statements 
                  WHERE company_id = %s AND period < %s 
                  ORDER BY period DESC LIMIT 1"""
    cursor.execute(sql_prev, (company_id, period))
    prev_data = cursor.fetchone()
    
    if prev_data:
        prev_revenue, prev_net_income = prev_data
        if prev_revenue > 0:
            revenue_growth = ((revenue - prev_revenue) / prev_revenue) * 100
            print(f"Revenue Growth: {revenue_growth:.1f}%")
        
        if prev_net_income > 0:
            income_growth = ((net_income - prev_net_income) / prev_net_income) * 100
            print(f"Net Income Growth: {income_growth:.1f}%")

def import_csv_data(db):
    """Simple CSV import function"""
    print("\n--- IMPORT CSV DATA ---")
    print("Please format your CSV as: company_name,industry,period,revenue,net_income,assets,liabilities")
    filename = input("Enter CSV filename: ")
    
    try:
        cursor = db.cursor()
        
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 7:
                    # Add company if needed
                    company_name, industry, period, revenue, net_income, assets, liabilities = data
                    
                    # Check if company exists
                    cursor.execute("SELECT id FROM companies WHERE name = %s", (company_name,))
                    result = cursor.fetchone()
                    
                    if not result:
                        # Add new company
                        cursor.execute("INSERT INTO companies (name, industry) VALUES (%s, %s)", 
                                       (company_name, industry))
                        company_id = cursor.lastrowid
                    else:
                        company_id = result[0]
                    
                    # Add financial statement
                    sql = """INSERT INTO statements 
                             (company_id, type, period, revenue, net_income, assets, liabilities) 
                             VALUES (%s, 'Income', %s, %s, %s, %s, %s)"""
                    cursor.execute(sql, (company_id, period, float(revenue), float(net_income), 
                                         float(assets), float(liabilities)))
        
        db.commit()
        print("CSV data imported successfully!")
        
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main program function"""
    print("Welcome to Simple Financial Analysis System!")
    
    # Connect to database
    db = connect_db()
    if not db:
        return
    
    # Main program loop
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_company(db)
        elif choice == '2':
            add_statement(db)
        elif choice == '3':
            view_companies(db)
        elif choice == '4':
            view_financial_data(db)
        elif choice == '5':
            calculate_ratios(db)
        elif choice == '6':
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Please try again.")
        
        input("\nPress Enter to continue...")
    
    db.close()

if __name__ == "__main__":
    main()
