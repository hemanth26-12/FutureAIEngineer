class Assistant:
    def reply(self):
        print("Hello User")

class AI_Assistant(Assistant):
    def reply(self):
        print("Hello Hemanth")
        super().reply()
a1 = AI_Assistant()
a1.reply()