from calendar import c
from portfolio_data import companies
#---> TEST command: 
#---> python3 portfolio/portfolio_review.py

def calculate_investment(company):
    invested_amount = round(float(company["quantity"]) * float(company["avg_price"]), 2)
    return invested_amount

def display_investment(company):
    print(f"{company['name']}:",calculate_investment(company),"$")

def calculate_total_investment():
    total = 0.0
    for company in companies:
        total += calculate_investment(company)
    return total

def display_total_investment():
    print("Total invested:",calculate_total_investment(),"$")

def display_portfolio():
    for company in companies:
        display_investment(company)
    display_total_investment()

def update_portfolio():
    companies.append({
        "name":"Micron", 
        "ticker":"MU", 
        "quantity": 2, 
        "avg_price": 165
        })
    companies.append({
        "name":"SpaceX", 
        "ticker":"SPCX", 
        "quantity": 5, 
        "avg_price": 100
        })

def main():
    while True:
        decision = input("\nType D to DISPLAY, U to UPDATE, S to SEARCH or Q to EXIT:\n")
        if decision == "D":
            print("\n----------FULL PORTFOLIO----------")
            display_portfolio()
        elif decision == "U":
            print("\n----------UPDATING PORTFOLIO----------")
            update_portfolio()
            print("Portfolio updated.\n")
        elif decision == "S":
            search_input = input("Type company name or T to display total investment:\n")
            if search_input == "T":
                print("\n----------TOTAL INVESTMENT----------")
                display_total_investment()
            else:
                valid_company = False
                for company in companies:
                    if  company["name"] == search_input:
                        valid_company = True
                        print("\n----------SPECIFIC INVESTMENT----------")
                        display_investment(company)
                if not valid_company:
                    print("Company not found. Please try again.\n")
        elif decision == "Q":
            break
        else:
            print("Please enter one of the following: D, U, S, Q:\n")

if __name__ == "__main__":
    main()
