from rich import print
import random
usr = input("Enter any from \n 1. rock  2. paper  3. scissors \n")
ai = random.choice(["rock", "paper", "scissors"])
print("[bold green]You chose:[/bold green]", usr)
print("[bold blue]AI chose:[/bold blue]", ai)
if usr == "rock" and ai == "scissors":
    print("[bold green]You win![/bold green]")
elif usr == "paper" and ai == "rock":
    print("[bold green]You win![/bold green]")
elif usr == "scissors" and ai == "paper":
    print("[bold green]You win![/bold green]")
elif ai == "rock" and usr == "scissors":
    print("[bold red]You lose![/bold red]")
elif ai == "paper" and usr == "rock":
    print("[bold red]You lose![/bold red]")
elif ai == "scissors" and usr == "paper":
    print("[bold red]You lose![/bold red]")
elif usr == ai:
    print("[bold yellow]It's a tie![/bold yellow]")
else :
    print("[bold red]Invalid input! Please choose Rock, Paper, or Scissors.[/bold red]")