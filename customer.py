class Customer:
    def __init__(self, first_name, last_name, email, account_id, postcode):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.postcode = postcode
        self.email = email

    def update_email(self, new_email):
        if "@" in new_email:
            self.email = new_email
        return
