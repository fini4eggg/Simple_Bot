import time

from SimpleRobot import InfoBot
from SimpleRobot import FuckOffBot
from telegrambot import Telegrambot


#infoBot = SimpleRobot("это инфо-бот", "getInfo")
#helloBot = SimpleRobot("это привет-бот", "sayHello")
botInfo = InfoBot('Инфо бот', 'info')
botFuck = FuckOffBot('Блять, отъебись', 'fuck')
robots = [botInfo, botFuck]
last_message_id = 0

while True:
    # 1 обращаемся к телеграм за поседними сообщениями


    bot = Telegrambot()
    messages = bot.get_messages_as_json(last_message_id + 1)

    # 2 обработка ответа от телеграм

    for message in messages:
        # TODO
        last_message_id = max(last_message_id, message["update_id"])

        text = message["message"]["text"]
        chat_id = message["message"]["chat"]["id"]
        user = message["message"]["chat"]["first_name"]

        for robot in robots:

            if text.lower() == robot.get_command():
                answer = f"{user}, и тебе привет, это робот {robot.get_name()}"
                result = bot.post_message_to_user(chat_id, answer)
                print(result)
        # 3 отправить ответ в телеграм



    time.sleep(1)