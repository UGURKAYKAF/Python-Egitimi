class Logistic:
    def __init__(self, Company_name, foundation_year, founder_name, company_slogan, inventory_space):
        self.company_name = Company_name
        self.foundation_year = foundation_year
        self.founder_name = founder_name
        self.company_slogan = company_slogan
        self.inventory_space = inventory_space

    def print_report(self):
        print(f"""The company name is {self.company_name} abd was founded in {self.foundation_year}.
        The founder of the company is {self.founder_name}.
        Company slogan: {self.company_slogan}.
        Inventory space of the company: {self.inventory_space}""")

    def update_inventory_space(self, new_storage_space):
        self.inventory_space = new_storage_space
        print(f"Inventory space has been changed to {self.inventory_space}")


logistic_company = Logistic("LogCom", 1990, "laura McCartey", "There is no place we cannot reach.", 2500)

logistic_company.update_inventory_space(3000)
logistic_company.print_report()

class Trading:
    def __init__(self, company_name, foundation_year, founder_name, company_slogan, sales ,expenses, revenue):
        self.company_name = company_name
        self.foundation_year = foundation_year
        self.founder_name = founder_name
        self.company_slogan = company_slogan
        self.sales = sales 
        self.expenses = expenses
        self.revenue = revenue

    def print_report(self):
        print(f"""The company name is {self.company_name} and was founded in {self.foundation_year}.
        The dounder of the company is {self.founder_name}.
        Company slofan: {self.company_slogan}.
        Total sales: {self.sales}.
        Total expenses: {self.expenses}.
        Total revenue: {self.revenue}""")

    def update_sales_and_expenses(self, new_sales, new_expenses):
        self.sales += new_sales
        self.expenses += new_expenses
        print("sales and expenses are updated!")

    def calculate_revenue(self):
        self.revenue = self.sales - self.expenses
        print(f"The Revenue of the compant is: {self.revenue}")


trading_company = Trading('Tracom',2005,'Chong Wu', 'We revolutionize trading.', 5000,2000,3000)
trading_company.update_sales_and_expenses(100,50)
trading_company.calculate_revenue()
trading_company.print_report()
