﻿#!/usr/bin/python


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

__CHANNEL_USERNAME__ = "CPMOneOwner"
__GROUP_USERNAME__   = "CPMOneShop"

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
    brand_name = figlet_format('CPMOne2', font='drpepper')
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text, end=None)
    console.print("[bold green]♕ CPMOne[/bold green]: Car Parking Multiplayer 2 Hacking Tool.")
    console.print(f"[bold green]♕ Telegram[/bold green]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue] or [bold blue]@{__GROUP_USERNAME__}[/bold blue].")
    console.print("[bold red]<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>[/bold red]")
    console.print("[bold yellow]BY:CPMOne[/bold yellow]: THIS IS MY PERSONAL USE ONLY", end="\n\n")

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        WalletData = data.get('WalletData')
        PlayerStorage = data.get('PlayerStorage')
        if 'Money' in WalletData and 'LocalID' in PlayerStorage and 'Brakes' in PlayerStorage:
            console.print("[bold][red]<<<<<<<<<<<<<<<<[/red][ PLAYER DETAILS ][red]>>>>>>>>>>>>>>>>[/red][/bold]")
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
    console.print("[bold][red]<<<<<<<<<<<<<<<<<<<<<[/red][ KEYS ][red]>>>>>>>>>>>>>>>>>>>>>[/red][/bold]")
    console.print(f"[bold green]Access Key [/bold green]: { data.get('access_key') }.")
    console.print(f"[bold green]Telegram ID[/bold green]: { data.get('telegram_id') }.")
    console.print(f"[bold green]Balance    [/bold green]: { (data.get('coins') if not data.get('is_unlimited') else 'Lifetime') }.")

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
            load_key_data(cpm)
            console.print("[bold][red]<<<<<<<<<<<<<<<<<<<[/red][ SERVICES ][red]>>>>>>>>>>>>>>>>>>>[/red][/bold]")
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
            console.print("[bold][red](01):[/red] [green]Account Delete[/green]         [red][FREE][/red]")
            console.print("[bold][red](02):[/red] [green]Account Register[/green]       [red][FREE][/red]")
            console.print("[bold][red](03):[/red] [green]Increase Money[/green]         [red][4.000K][/red]")
            console.print("[bold][red](04):[/red] [green]Change ID[/green]              [red][2.500K][/red]")
            console.print("[bold][red](05):[/red] [green]Change Name[/green]            [red][1.000K][/red]")
            console.print("[bold][red](06):[/red] [green]Complete Missions[/green]      [red][6.000K][/red]")
            console.print("[bold][red](07):[/red] [green]Delete Friends[/green]         [red][2.000K][/red]")
            console.print("[bold][red](08):[/red] [green]King Rank[/green]              [red][6.000K][/red]")
            console.print("[bold][red](09):[/red] [green]Maximize Drag Wins[/green]     [red][6.000K][/red]")
            console.print("[bold][red](10):[/red] [green]Unlock Slots[/green]           [red][7.000K][/red]")
            console.print("[bold][red](11):[/red] [green]Unlock Apartments[/green]      [red][10.000K][/red]")
            console.print("[bold][red](12):[/red] [green]Unlock Brakes[/green]          [red][5.000K][/red]")
            console.print("[bold][red](13):[/red] [green]Unlock Wheels[/green]          [red][6.000K][/red]")
            console.print("[bold][red](14):[/red] [green]Unlock Clothes[/green]         [red][9.000K][/red]")
            console.print("[bold][red](15):[/red] [green]Unlock Cars[/green]            [red][10.000K][/red]")
            console.print("[bold][red](0) :[/red] [red]Exit[/red]", end="\n\n")
            console.print("[bold][red]<<<<<<<<<<<<<<<<<<<<<[/red][ CPM2 ][red]>>>>>>>>>>>>>>>>>>>>>[/red][/bold]")
            service = IntPrompt.ask(f"[bold][?] Select a Service [red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            if service == 0: # Exit
                console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
            elif service == 1: # Account Delete
                console.print("[bold cyan][!] After deleting your account there is no going back !!.[/bold cyan]")
                answ = Prompt.ask("[bold cyan][?] Do You want to Delete this Account ?![/bold cyan]", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    console.print("[bold cyan][%] Deleting Your Account[/bold cyan]: [bold green]SUCCESSFUL.[/bold green].")
                    console.print("==================================")
                    console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                else: continue
            elif service == 2: # Account Register
                console.print("[bold cyan][!] Registring new Account.[/bold cyan]")
                acc2_email = prompt_valid_value("[bold][?] Account Email[/bold]", "Email", password=False)
                acc2_password = prompt_valid_value("[bold][?] Account Password[/bold]", "Password", password=False)
                console.print("[bold cyan][%] Creating new Account[/bold cyan]: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>")
                    console.print(f"[bold red]! INFO[/bold red]: In order to tweak this account with CPMNuker")
                    console.print("you most sign-in to the game using this account.")
                    sleep(2)
                    continue
                elif status == 105:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] This email is already exists !.[/bold yellow]")
                    sleep(2)
                    continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue 
            elif service == 3: # Increase Money
                console.print("[bold cyan][!] Insert how much money do you want.[/bold cyan]")
                amount = IntPrompt.ask("[bold][?] Amount[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if amount > 0 and amount <= 500000000:
                    if cpm.set_player_money(amount):
                        console.print("[bold green]SUCCESSFUL.[/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED.[/bold red]")
                        console.print("[bold yellow][!] Please try again.[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please use valid values.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                console.print("[bold cyan][!] Enter your new ID.[/bold cyan]")
                new_id = Prompt.ask("[bold][?] ID[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if len(new_id) >= 2 and len(new_id) <= 50 and (' ' in new_id) == False:
                    if cpm.set_player_id(new_id.upper()):
                        console.print("[bold green]SUCCESSFUL.[/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED.[/bold red]")
                        console.print("[bold yellow][!] Please try again.[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please use valid ID.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                console.print("[bold cyan][!] Enter your new Name.[/bold cyan]")
                new_name = Prompt.ask("[bold][?] Name[/bold]")
                console.print("[bold cyan][%] Saving your data[/bold cyan]: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 30:
                    if cpm.set_player_name(new_name):
                        console.print("[bold green]SUCCESSFUL.[/bold green]")
                        console.print("==================================")
                        answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                        else: continue
                    else:
                        console.print("[bold red]FAILED.[/bold red]")
                        console.print("[bold yellow][!] Please try again.[/bold yellow]")
                        sleep(2)
                        continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please use valid values.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 6: # Complete Missions
                console.print("[bold cyan][%] Completing all missions[/bold cyan]: ", end=None)
                if cpm.complete_missions():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 7: # Delete Friends
                console.print("[bold cyan][%] Deleting Friends[/bold cyan]: ", end=None)
                if cpm.delete_player_friends():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 8: # King Rank
                console.print("[bold red][!] Note:[/bold red]: if the king rank doesn't appear in game, logout and login few times.")
                console.print("[bold red][!] Note:[/bold red]: please don't do King Rank on same account twice !!.", end="\n\n")
                sleep(2)
                console.print("[bold cyan][%] Upgrading Rank[/bold cyan]: ", end=None)
                if cpm.set_player_rank():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 9: # Maximize Drag Wins
                console.print("[bold cyan][%] Maximizing drag wins[/bold cyan]: ", end=None)
                if cpm.maximize_drag_wins():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 10: # Unlock Slots
                console.print("[bold cyan][%] Unlocking all slots[/bold cyan]: ", end=None)
                if cpm.unlock_slots():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 11: # Unlock Apartments
                console.print("[bold cyan][%] Unlocking All apartments[/bold cyan]: ", end=None)
                if cpm.unlock_apartments():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 12: # Unlock Brakes
                console.print("[bold cyan][%] Unlocking Brakes[/bold cyan]: ", end=None)
                if cpm.unlock_brakes():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 13: # Unlock Wheels
                console.print("[bold cyan][%] Unlocking Wheels[/bold cyan]: ", end=None)
                if cpm.unlock_wheels():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 14: # Unlock Clothes
                console.print("[bold cyan][%] Unlocking Clothes[/bold cyan]: ", end=None)
                if cpm.unlock_clothes():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            elif service == 15: # Unlock Cars
                console.print("[bold cyan][%] Unlocking Cars[/bold cyan]: ", end=None)
                if cpm.unlock_cars():
                    console.print("[bold green]SUCCESSFUL.[/bold green]")
                    console.print("==================================")
                    answ = Prompt.ask("[bold cyan][?] Do You want to Exit ?[/bold cyan]", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold yellow][!] Thank You for using our tool, please join our telegram channel[/bold yellow]: [bold blue]@{__CHANNEL_USERNAME__}[/bold blue].")
                    else: continue
                else:
                    console.print("[bold red]FAILED.[/bold red]")
                    console.print("[bold yellow][!] Please try again.[/bold yellow]")
                    sleep(2)
                    continue
            else: continue
            break
        break
