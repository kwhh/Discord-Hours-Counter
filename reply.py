import discord
import asyncio
import os
from tqdm import tqdm
from colorama import Fore, Style

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

async def send_hourly_count(token, channel_id, start_hour):
    client = discord.Client()

    @client.event
    async def on_ready():
        clear_screen()
        print(f"{Fore.CYAN}{Style.BRIGHT}")
        print(f"██╗  ██╗ ██████╗ ██╗   ██╗██████╗      ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗███████╗██████╗  ")
        print(f"{Fore.WHITE}{Style.BRIGHT}██║  ██║██╔═══██╗██║   ██║██╔══██╗    ██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗")
        print(f"{Fore.CYAN}{Style.BRIGHT}███████║██║   ██║██║   ██║██████╔╝    ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝")
        print(f"{Fore.WHITE}{Style.BRIGHT}██╔══██║██║   ██║██║   ██║██╔══██╗    ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗")
        print(f"{Fore.CYAN}{Style.BRIGHT}██║  ██║╚██████╔╝╚██████╔╝██║  ██║    ╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║")
        print(f"{Fore.WHITE}{Style.BRIGHT}╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝")
        print(f"{Fore.CYAN}                    ┍━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{Fore.WHITE}                       More > https://github.com/kwhh")
        print(f"{Fore.CYAN}                           Logged in as {client.user} ")
        print(f"{Fore.WHITE}                    ┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙")

        channel = client.get_channel(channel_id)
        if channel is None:
            await client.close()
            return

        channel_name = channel.name if isinstance(channel, discord.TextChannel) else "Unknown"
        print(f"{Fore.CYAN}STARTED AUTO COUNTER IN ({channel_name})")

        current_hour = start_hour

        while current_hour <= 250:
            try:
                await channel.send(str(current_hour))
                current_hour += 1
            except discord.HTTPException:
                break

            await asyncio.sleep(3600)

        clear_screen()
        print(f"{Fore.CYAN}Hourly messages completed.")
        await client.close()

    try:
        await client.start(token, bot=False)
    except discord.LoginFailure:
        pass

async def main():
    token = input(f"{Fore.CYAN}{Style.BRIGHT}Enter your token: ").strip()
    channel_id = int(input(f"{Fore.WHITE}{Style.BRIGHT}Enter the channel ID: ").strip())
    start_hour = int(input(f"{Fore.CYAN}{Style.BRIGHT}Enter the starting hour (0-200): ").strip())

    for _ in tqdm(range(10), desc="Loading", ncols=80):
        await asyncio.sleep(0.1)

    clear_screen()
    await send_hourly_count(token, channel_id, start_hour)
    clear_screen()
    print(f"{Fore.CYAN}All messages completed.")

asyncio.run(main())
