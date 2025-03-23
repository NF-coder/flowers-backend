class AuthCommands():
    def __init__(self, client) -> None:
        self.client = client
    
    def add_auth_by_email(self):
        return self.client.configure_command(
            functionName="add_auth_method",
            className="EmailAuth"
        )