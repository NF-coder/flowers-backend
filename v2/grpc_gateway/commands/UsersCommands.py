class UsersCommands():
    def __init__(self, client) -> None:
        self.client = client
    
    def find_unconfirmed_suppliers(self):
        return self.client.configure_command(
            functionName="find_unconfirmed_suppliers",
            className="Users"
        )
    
    def approve_supplier_request(self):
        return self.client.configure_command(
            functionName="confirm_supplier_by_id",
            className="Users"
        )
    
    def find_unconfirmed_suppliers(self):
        return self.client.configure_command(
            functionName="find_unconfirmed_suppliers",
            className="Users"
        )

    def add_new_user(self):
        return self.client.configure_command(
            functionName="add_new_user",
            className="Users"
        )

    def get_user_by_id(self):
        return self.client.configure_command(
            functionName="get_info_by_id",
            className="Users"
        )