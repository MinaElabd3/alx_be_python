def calculate_savings():
    # Prompt user for input
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your total monthly expenses: "))
    
    # Calculate monthly savings
    monthly_savings = monthly_income - monthly_expenses
    
    # Calculate projected annual savings with interest (assuming 5% annual interest rate)
    annual_savings_no_interest = monthly_savings * 12
    annual_interest_rate = 0.05
    projected_savings = annual_savings_no_interest + (annual_savings_no_interest * annual_interest_rate)
    
    # Print the results without decimal places
    print(f"Your monthly savings are ${monthly_savings:.0f}.")
    print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}")

# Run the function to calculate and display savings
calculate_savings()

