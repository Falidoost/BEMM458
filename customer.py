class Customer:
    def __init__(self, first_name, last_name, email, account_id, postcode):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.postcode = postcode
        self.email = email

    def __str__(self):
        customer_str = (f"Customer: {self.first_name} {self.last_name}\n" +
                        f"Account ID: {self.account_id}\n" +
                        f"Postcode: {self.postcode}\n" +
                        f"Email: {self.email}\n ")
        
        return customer_str
