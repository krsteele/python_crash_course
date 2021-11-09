class Employee:
    """Representation of employee"""

    def __init__(self, first, last, salary):
        """Instantiate employee with first name, last name and annual salary."""
        self.first_name = first
        self.last_name = last
        self.annual_salary = salary

    def give_raise(self, salary_bump=5000):
        """Add a raise to the annual_salary attribute."""
        self.annual_salary += salary_bump

    