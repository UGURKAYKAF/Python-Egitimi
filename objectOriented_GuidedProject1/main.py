class HealthInsurance:
    def __init__(self, company_name, foundation_year, founder_name, company_slogan, num_of_employee, num_of_clients):
        self.company_name = company_name
        self.foundation_year = foundation_year 
        self.founder_name = founder_name
        self.company_slogan = company_slogan
        self.num_of_employee = num_of_employee
        self.num_of_clients = num_of_clients

    def print_report(self):
        print(f"""The company {self.company_name} was founded in {self.foundation_year}. 
        The founder of the company is {self.founder_name}. 
        Company slogan: {self.company_slogan}. 
        Number of employees: {self.num_of_employee}. 
        Number of clients: {self.num_of_clients}""")

    def sup_heath_insurance(self, age, chronic_disease, income):
        if age >= 60 and chronic_disease == True and income < 6000:
            print("We are sorry! You are not eligible for supplemantal health insurance.")
        elif age < 60 and income>= 6000 or chronic_disease == False:
            print("Congratulations! You can get supplemental health insurance.")
        
    def update_num_clients(self, new_number):
        self.num_of_clients = new_number
        print(f"Number of clients has been changed to {self.num_of_clients}!")



HI_company = HealthInsurance('Healthy', 2012, 'Bob Mayer', 'We care for you', 3500,13230)
HI_company.sup_heath_insurance(45, False, 5000)
HI_company.update_num_clients(13231)
HI_company.print_report()

        