class Security:
    def __init__(self,bot_name,bot_id):
        self.bot_name = bot_name
        self.bot_id = bot_id

secure = Security("Darling",420)

print(secure.bot_name)
print(secure.bot_id)