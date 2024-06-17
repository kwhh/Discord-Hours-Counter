import discord
import asyncio
import os
from colorama import Fore, Style
from tqdm import tqdm

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class MyClient(discord.Client):
    async def on_ready(self):
        clear_screen()
        print(f"""{Fore.CYAN}{Style.BRIGHT}
 █████╗ ██╗   ██╗████████╗ ██████╗     ██████╗ ███████╗██████╗ ██╗  ██╗   ██╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗    ██╔══██╗██╔════╝██╔══██╗██║  ╚██╗ ██╔╝
███████║██║   ██║   ██║   ██║   ██║    ██████╔╝█████╗  ██████╔╝██║   ╚████╔╝ 
██╔══██║██║   ██║   ██║   ██║   ██║    ██╔══██╗██╔══╝  ██╔═══╝ ██║    ╚██╔╝  
██║  ██║╚██████╔╝   ██║   ╚██████╔╝    ██║  ██║███████╗██║     ███████╗██║   
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝     ╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚═╝   
""")
        print(f"{Fore.WHITE}                    ┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{Fore.CYAN}                       More > https://github.com/kwhh")
        print(f"{Fore.RED}                           Logged in as {self.user} ")
        print(f"{Fore.WHITE}                    ┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙")

    async def on_message(self, message):
        if self.user in message.mentions and message.author != self.user:
            await message.reply(CUSTOM_MESSAGE, mention_author=True)

async def main():
    global TOKEN, CUSTOM_MESSAGE

    TOKEN = input(f"{Fore.BLUE}{Style.BRIGHT}Enter your token: ").strip()
    clear_screen()

    for _ in tqdm(range(10), desc="Loading", ncols=80):
        await asyncio.sleep(0.1)
    CUSTOM_MESSAGE = input(f"{Fore.BLUE}{Style.BRIGHT}Enter the Reply message: ").strip()
    clear_screen()

    intents = discord.Intents.default()
    intents.messages = True
    client = MyClient(intents=intents)

    try:
        await client.start(TOKEN, bot=False)
    except discord.LoginFailure:
        print(f"Invalid token: {TOKEN}.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await client.close()

asyncio.run(main())
