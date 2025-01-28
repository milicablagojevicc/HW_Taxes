#Create a tax calculator
def calculate_net_salary():
    try:
        # Read gross salary input
        gross_salary = float(input("Enter the gross salary: "))

        # Read number of children input
        num_children = int(input("Enter the number of children: "))

        # Validate inputs
        if gross_salary < 0:
            raise ValueError("Gross salary cannot be negative.")
        if num_children < 0:
            raise ValueError("Number of children cannot be negative.")

        # Determine base tax rate based on gross salary
        if gross_salary < 1000:
            tax_rate = 10  # 10%
        elif gross_salary < 2000:
            tax_rate = 12  # 12%
        elif gross_salary < 4000:
            tax_rate = 14  # 14%
        else:
            tax_rate = 18  # 18%

        # Calculate child tax cut based on gross salary
        if gross_salary < 2000:
            child_tax_cut = 1 * num_children  # 1% per child
        else:
            child_tax_cut = 0.5 * num_children  # 0.5% per child

        # Adjust the effective tax rate
        effective_tax_rate = max(tax_rate - child_tax_cut, 0)  # Tax rate cannot be negative

        # Calculate net salary
        net_salary = gross_salary * (1 - effective_tax_rate / 100)

        # Print the net salary
        print(f"Net salary: {net_salary:.2f}")

    except ValueError as e:
        print(f"Invalid input: {e}")


# Call the function
calculate_net_salary()