# Lambda functions for tax bands
personal_allowance = lambda income: min(income, 12570) * 0
basic_rate = lambda income: max(0, min(income, 50270) - 12570) * 0.20
higher_rate = lambda income: max(0, min(income, 125140) - 50270) * 0.40
additional_rate = lambda income: max(0, income - 125140) * 0.45


# Rule engine to calculate total tax
def calculate_tax(income):
    tax_personal_allowance = personal_allowance(income)
    tax_basic_rate = basic_rate(income)
    tax_higher_rate = higher_rate(income)
    tax_additional_rate = additional_rate(income)

    total_tax = (
            tax_personal_allowance +
            tax_basic_rate +
            tax_higher_rate +
            tax_additional_rate
    )

    return total_tax


# Test cases
def test_tax_calculation():
    # Test personal allowance
    result = calculate_tax(10000)
    print(f"Test 1: Income = £10,000, Tax = £{result}")
    assert result == 0, "Test case 1 failed"

    # Test basic rate
    result = calculate_tax(30000)
    print(f"Test 2: Income = £30,000, Tax = £{result}")
    assert result == 3486, "Test case 2 failed"

    # Test higher rate
    result = calculate_tax(60000)
    print(f"Test 3: Income = £60,000, Tax = £{result}")
    assert result == 11486, "Test case 3 failed"

    # Test additional rate
    result = calculate_tax(150000)
    print(f"Test 4: Income = £150,000, Tax = £{result}")
    assert result == 53186, "Test case 4 failed"

    print("All test cases passed!")


# Run tests
test_tax_calculation()