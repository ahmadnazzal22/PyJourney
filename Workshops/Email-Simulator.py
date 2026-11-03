class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def get_balance(self):
        balance = 0

        for item in self.ledger:
            balance += item['amount']

        return balance

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False

        self.ledger.append({
            'amount': -amount,
            'description': description
        })

        return True

    def transfer(self, amount, another_category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f'Transfer to {another_category.name}')
        another_category.deposit(amount, f'Transfer from {self.name}')

        return True

    def __str__(self):
        title = self.name.center(30, '*')
        output = title + '\n'

        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"

            output += f"{description:<23}{amount:>7}\n"

        output += f"Total: {self.get_balance():.2f}"

        return output


def create_spend_chart(categories):
    total_withdrawals = 0
    withdrawals = []

    for category in categories:
        category_total = 0

        for item in category.ledger:
            if item['amount'] < 0:
                category_total += abs(item['amount'])

        withdrawals.append(category_total)
        total_withdrawals += category_total

    percentages = []

    for amount in withdrawals:
        if total_withdrawals == 0:
            percentage = 0
        else:
            percentage = int((amount / total_withdrawals) * 100)

        percentage = (percentage // 10) * 10
        percentages.append(percentage)

    chart = "Percentage spent by category\n"

    for level in range(100, -1, -10):
        chart += f"{level:>3}|"

        for percentage in percentages:
            if percentage >= level:
                chart += " o "
            else:
                chart += "   "

        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_name_length = max(len(category.name) for category in categories)

    for i in range(max_name_length):
        chart += "     "

        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "

        if i < max_name_length - 1:
            chart += "\n"

    return chart
