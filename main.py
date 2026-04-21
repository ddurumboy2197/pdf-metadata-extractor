class TelegramBot:
    def __init__(self):
        self.messages = []

    def send_message(self, user_id, message):
        self.messages.append((user_id, message))

    def get_messages(self):
        return self.messages

class BotSimulator:
    def __init__(self):
        self.bot = TelegramBot()

    def start(self):
        while True:
            user_input = input("Botga yozing: ")
            if user_input.lower() == "quit":
                break
            user_id = input("Foydalanuvchi ID: ")
            self.bot.send_message(user_id, user_input)

    def get_bot_messages(self):
        return self.bot.get_messages()

def main():
    simulator = BotSimulator()
    simulator.start()
    print("Botga yuborilgan xabarlarni ko'rish uchun quyidagi funksiyani bosing:")
    print("get_bot_messages()")

def get_bot_messages():
    simulator = BotSimulator()
    return simulator.get_bot_messages()

if __name__ == "__main__":
    main()
```

Kodni ishga tushirish uchun quyidagicha amal qiling:

1. Kodni yozing va saqlang.
2. Terminalda kodni ishga tushiring.
3. Botga yuborilgan xabarlarni ko'rish uchun `get_bot_messages()` funksiyasini bosing.
