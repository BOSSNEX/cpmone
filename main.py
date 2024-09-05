#!/usr/bin/python

# Copyright (C) Anasov <me@anasov.ly> - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Anasov <me@anasov.ly>, 05, May, 2024.

#############################################
# DO NOT BUY THIS TOOL FROM ANY SCAMMER !!! #
# OFFICIAL SELLER IS 'ANAS' AT TELEGRAM !!! #
#############################################

import random
import requests
from time import sleep
import os, signal, sys
from pyfiglet import figlet_format
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
from cpmnuker import CPMNuker

__CHANNEL_USERNAME__ = "CPMNuker"
__GROUP_USERNAME__   = "CPMNukerChat"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name = figlet_format('CPMNuker2', font='drpepper')
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text, end=None)
    console.print("[bold green]♕ CPMNuker[/bold green]: Car Parking Multiplayer 2 Hacking Tool.")
    console.print(f"[bold green]♕ Telegram[/bold green]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue] or [bold blue]@{__GROUP_USERNAME__}[/bold blue].")
    console.print("[bold red]==================================================[/bold red]")
    console.print("[bold yellow]! Note[/bold yellow]: Logout from the game before using this tool !.", end="\n\n")

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        WalletData = data.get('WalletData')
        PlayerStorage = data.get('PlayerStorage')
        if 'Money' in WalletData and 'LocalID' in PlayerStorage and 'Brakes' in PlayerStorage:
            console.print("[bold][red]================[/red][ PLAYER DETAILS ][red]================[/red][/bold]")
            console.print(f"[bold green]Name   [/bold green]: { (PlayerStorage.get('Name') if 'Name' in PlayerStorage else 'UNDEFINED') }.")
            console.print(f"[bold green]ID     [/bold green]: { (PlayerStorage.get('LocalID') if 'LocalID' in PlayerStorage else 'UNDEFINED') }.")
            console.print(f"[bold green]Money  [/bold green]: { (WalletData.get('Money') if 'Money' in WalletData else 'UNDEFINED') }.")
            console.print(f"[bold green]Coins  [/bold green]: { (WalletData.get('Coins') if 'Coins' in WalletData else 'UNDEFINED') }.")
        else:
            console.print("[bold red]! ERROR[/bold red]: new accounts most be signed-in to the game at least once !.")
            exit(1)
    else:
        console.print("[bold red]! ERROR[/bold red]: seems like your login is not properly set !.")
        exit(1)
    
def load_key_data(cpm):
    data = cpm.get_key_data()
    console.print("[bold][red]==================================================[/red][/bold]")
    console.print(f"[bold green]Access Key [/bold green]: { data.get('access_key') }.")
    console.print(f"[bold green]Telegram ID[/bold green]: { data.get('telegram_id') }.")
    console.print(f"[bold green]Balance    [/bold green]: { (data.get('coins') if not data.get('is_unlimited') else 'Unlimited') }.")

def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    console.print("[bold][red]==================================================[/red][/bold]")
    console.print(f"[bold][green]Location[/bold][/green]: {data.get('city')}, {data.get('regionName')}, {data.get('countryCode')}")
    console.print(f"[bold][green]ISP[/bold][/green]     : {data.get('isp')}")
    console.print("[bold][red]===================[/red][ SERVICES ][red]===================[/red][/bold]")

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(f"{tag} cannot be empty or just spaces. Please try again.")
        else:
            return value

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] Account Email[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] Account Password[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] Access Key[/bold]", "Access Key", password=False)
        console.print("[bold cyan][%] Trying to Login[/bold cyan]: ", end=None)
        cpm = CPMNuker(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                console.print("[bold red]ACCOUNT NOT FOUND[/bold red].")
                sleep(2)
                continue
            elif login_response == 101:
                console.print("[bold red]WRONG PASSWORD[/bold red].")
                sleep(2)
                continue
            elif login_response == 103:
                console.print("[bold red]INVALID ACCESS KEY[/bold red].")
                sleep(2)
                continue
            else:
                console.print("[bold red]TRY AGAIN[/bold red].")
                console.print("[bold yellow]! Note[/bold yellow]: make sure you filled out the fields !.")
                sleep(2)
                continue
        else:
            console.print("[bold green]SUCCESSFUL[/bold green].")
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_details(cpm, key_data)
            load_client_details()
            choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "0"]
            console.print("[cyan](1):[/cyan] [red]Change Name[/red]", end="\n\n")
            console.print("[cyan](2):[/cyan] [red]Change ID[/red]", end="\n\n")
            console.print("[cyan](3):[/cyan] [red]Insert Money[/red]", end="\n\n")
            console.print("[cyan](4):[/cyan] [red]Insert Slot[/red]", end="\n\n")
            console.print("[cyan](5):[/cyan] [red]Unlock All Houses[/red]", end="\n\n")
            console.print("[cyan](6):[/cyan] [red]Insert King Rank[/red]", end="\n\n")
            console.print("[cyan](7):[/cyan] [red]Set All Levels[/red]", end="\n\n")
            console.print("[cyan](8):[/cyan] [red]Unlock All Wheels[/red]", end="\n\n")
            console.print("[cyan](9):[/cyan] [red]Unlock All Equipaments Female[/red]", end="\n\n")
            console.print("[cyan](10):[/cyan] [red]Unlock All Equipaments Male[/red]", end="\n\n")
            console.print("[cyan](11):[/cyan] [red]Unlock All Brakes[/red]", end="\n\n")
            console.print("[cyan](12):[/cyan] [red]Unlock All Calipers[/red]", end="\n\n")
            console.print("[cyan](13):[/cyan] [red]Unlock All Paint[/red]", end="\n\n")
            console.print("[cyan](14):[/cyan] [red]Unlock Car[/red]", end="\n\n")
            console.print("[cyan](15):[/cyan] [red]Unlock All Animations[/red]", end="\n\n")
            console.print("[cyan](16):[/cyan] [red]Set Crash V1[/red]", end="\n\n")
            console.print("[cyan](17):[/cyan] [red]Set Fix V1[/red]", end="\n\n")
            console.print("[cyan](0):[/cyan] [red]Exit[/red]", end="\n\n")
            service = IntPrompt.ask(f"[bold][?] Select a Service [red][1-13 or 0][/red][/bold]", choices=choices, show_choices=False)
            if service == 1:
                new_name = prompt_valid_value("[bold][?] New Name[/bold]", "Name", min_length=1, max_length=15)
                success = cpm.set_player_name(new_name)
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
                        continue
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]: Failed to Change Name.")
            elif service == 2:
                new_id = prompt_valid_value("[bold][?] New ID[/bold]", "ID", min_length=1, max_length=10)
                success = cpm.set_player_id(new_id)
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
                        continue
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]: Failed to Change ID.")
            elif service == 3:
                money = prompt_valid_number("[bold][?] Insert Money (0-50000000)[/bold]", "Amount", 0, 50000000)
                success = cpm.insert_money(money)
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
                        continue
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]: Failed to Insert Money.")
            elif service == 4:
                slots = prompt_valid_number("[bold][?] Number of Slots to Insert (1-20)[/bold]", "Amount", 1, 20)
                success = cpm.insert_slots(slots)
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
                        continue
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]: Failed to Insert Slots.")
            elif service == 5:
                success = cpm.unlock_all_houses()
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
                        continue
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]: Failed to Unlock All Houses.")
            elif service == 6:
                success = cpm.set_player_king_rank()
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
                        continue
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]: Failed to Insert King Rank.")
            elif service == 7:
                success = cpm.set_player_all_levels()
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
                        continue
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]: Failed to Set All Levels.")
            elif service == 8:
                success = cpm.unlock_all_wheels()
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
                        continue
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]: Failed to Unlock All Wheels.")
            elif service == 9:
                success = cpm.unlock_equip_female()
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
                        continue
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]: Failed to Unlock All Equipaments Female.")
            elif service == 10:
                success = cpm.unlock_equip_male()
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
                        continue
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]: Failed to Unlock All Equipaments Male.")
            elif service == 11:
                success = cpm.unlock_all_brakes()
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
                        continue
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]: Failed to Unlock All Brakes.")
            elif service == 12:
                success = cpm.unlock_all_calipers()
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
                        continue
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]: Failed to Unlock All Calipers.")
            elif service == 13:
                success = cpm.unlock_all_paint()
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
                        continue
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]: Failed to Unlock All Paint.")
            elif service == 14:
                valid_car_slots = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 38, 44, 64, 76, 80, 81, 82, 98, 100, 101, 102, 103, 104, 105, 106, 107, 118, 120, 126, 127, 128, 131, 132, 134, 135, 138, 139, 140, 141, 143, 144, 147, 148, 150, 152, 153]
                car = prompt_valid_choice("[bold][?] Number Corresponding to Available Car Slot (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 38, 44, 64, 76, 80, 81, 82, 98, 100, 101, 102, 103, 104, 105, 106, 107, 118, 120, 126, 127, 128, 131, 132, 134, 135, 138, 139, 140, 141, 143, 144, 147, 148, 150, 152 and 153)[/bold]", valid_car_slots)
                success = cpm.unlock_all_car(car)
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
                        continue
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]: Failed to Unlock Car.")
            elif service == 15:
                success = cpm.unlock_all_animations()
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
                        continue
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]: Failed to Unlock All Animations.")
            elif service == 16:
                success = cpm.set_crash_acc_v1()
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
                        continue
                    else:
                        break
                else:
                    console.print("[bold red]FAILED[/bold red]: Failed to Set Crash V1.")
            elif service == 17:
                success = cpm.set_fix_acc_v1()
                if success:
                    console.print("[bold green]SUCCESSFUL[/bold green].")
                    choice = IntPrompt.ask("[bold][?] Choose an option [red][1: Return to Menu / 0: Exit][/red][/bold]", choices=["1", "0"], show_choices=False)
                    if choice == 1:
