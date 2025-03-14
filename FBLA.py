Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
import random
import time

# Setup turtle screen
screen = turtle.Screen()
screen.title("Investment Simulator")
screen.bgcolor("white")

# Create a turtle for drawing
drawer = turtle.Turtle()
drawer.speed(0)
drawer.hideturtle()

def draw_text(text, x, y, size=15, color="black"):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.color(color)
    drawer.write(text, align="center", font=("Times New Roman", size, "normal"))
    
#clears the screen to make way for a new one
def clear_screen():
    drawer.clear()
    screen.clearscreen()
    
# Function to print the welcome message at the start of the game
def welcome_message():
    """Display the initial welcome message and instructions."""
    clear_screen()
    screen.bgcolor("lightblue")
    draw_text("Welcome to the Investment Simulator!", 0, 100, size=24, color="darkblue")
    time.sleep(2)
    draw_text("Your goal is to make smart investments and grow your wealth.", 0, 60)
    time.sleep(2)
    draw_text("Each decision will affect your wealth, and random events may change everything.", 0, 20)
    time.sleep(2)
    draw_text("Let's get started!\n", 0, -40)
    time.sleep(2)
    clear_screen()

#Function to ask the user their choice(1,2,3, or 4)
def get_choice(options, prompt="Choose an option: "):
    """Get a valid choice from the user using simple input selection."""
    clear_screen()
    screen.bgcolor("lightyellow")
    draw_text(prompt, 0, 130, size=20, color="brown")

    for idx, option in enumerate(options, 1):
        draw_text(f"{idx}) {option}", 0, 100 - idx*30)

    choice = turtle.textinput("Your Choice", "Enter the number of your choice: ")

    if choice.isdigit() and 1 <= int(choice) <= len(options):
        return options[int(choice) - 1]
    else:
        turtle.textinput("Invalid Choice", "Please select a valid option.")
        return get_choice(options, prompt)

# Stimulates the stock market for the user(if chosen)
def stock_market():
    """Simulate stock market investment."""
    clear_screen()     
    screen.bgcolor("lightgreen")
    draw_text("You are in the Stock Market!", 0, 100, size=24, color="darkgreen")
    time.sleep(1)
    draw_text("Risky choice but high return", 0, 50, size=18, color="green")
    time.sleep(1.5)
    options = ["Technology stocks", "Real estate stocks", "Renewable energy stocks", "Biotech stocks"]
    choice = get_choice(options, "Which sector would you like to invest in?")

    # Different options for stock market investments
    investments = {
        "Technology stocks": 15,  
        "Real estate stocks": 7,  
        "Renewable energy stocks": 10,  
        "Biotech stocks": 20
    }

    growth = investments[choice]
    clear_screen()
    screen.bgcolor("lightyellow")
    draw_text(f"You chose {choice}. Let's see how it goes...", 0, 60)
    time.sleep(2)

    # Random events for investement choices
    event = random.choice(['boom', 'crash'])
    if event == 'boom':
        growth *= 1.5
        draw_text("The market boomed, and your investment grew by more!", 0, 20)
    elif event == 'crash':
        growth *= 0.5
        draw_text("The market crashed, and your investment lost some value.", 0, 20)

    time.sleep(2)
    return growth

# Function to stimulate the bond market(if chosen by the user)
def bond_market():
    """Simulate bond market investment."""
    clear_screen()
    screen.bgcolor("lightgrey")
    draw_text("You are in the Bond Market!", 0, 100, size=24, color="black")
    time.sleep(1)

    # Options for bond investment(different types of bonds to invest in)
    options = ["Government bonds", "Corporate bonds", "Municipal bonds", "High-yield bonds"]
    choice = get_choice(options, "Which bond would you like to invest in?")

    investments = {
        "Government bonds": 3,  
        "Corporate bonds": 5,  
        "Municipal bonds": 4,  
        "High-yield bonds": 8
    }

    growth = investments[choice]
    clear_screen()
    screen.bgcolor("lightyellow")
    draw_text(f"You chose {choice}. Let's see how it goes...", 0, 60)
    time.sleep(2)

    event = random.choice(['stable', 'recession'])
    if event == 'stable':
        growth += 2
        draw_text("The bond market is stable, and your returns grew!", 0, 20)
    elif event == 'recession':
        growth -= 1
        draw_text("The recession hit, and your returns decreased.", 0, 20)

    time.sleep(2)
    return growth

# Displays if "savings accounts" is selected
def savings_account():
    """Simulate savings account investment."""
    clear_screen()
    screen.bgcolor("lightblue")
    draw_text("You chose a savings account!", 0, 100, size=24, color="darkblue")
    time.sleep(1)
    draw_text("Your returns will be low, but it's a safe investment.", 0, 60)
    time.sleep(2)
    return 1  # Very low but safe returns

def emergency_fund():
    """Simulate emergency fund investment."""
    clear_screen()
    screen.bgcolor("lightcoral")
    draw_text("You decided to build an emergency fund!", 0, 100, size=24, color="darkred")
    time.sleep(1)
    draw_text("It’s not a big return, but it’s safe.", 0, 60)
    time.sleep(2)
    return 2  # Low, guaranteed returns

# Function to simulate a random event
def random_event():
    """Generate a random event that affects wealth."""
    clear_screen()
    events = [
        "You inherited $5,000!",
        "A natural disaster caused a loss of $3,000.",
        "You discovered a great opportunity and gained $2,000.",
        "You lost $4,000 in a bad business venture."
    ]
    event = random.choice(events)
    draw_text(f"Event: {event}", 0, 100, size=20, color="darkgreen")

    # Extract the amount from the event string, removing any non-numeric characters (like '!' or ',')
    amount_str = event.split('$')[1].split()[0]
    amount_str = amount_str.replace(',', '').replace('!', '').replace('.', '')  # Remove commas, exclamation mark, and period
    time.sleep(2)
    return int(amount_str)

# Displays the summary and investment records based on your choices
def display_summary(total_wealth, investment_history):
    """Display final summary of wealth and investments."""
    clear_screen()
    draw_text(f"Your total wealth: ${total_wealth}", 0, 100, size=24, color="darkblue")
    draw_text("Investment History:", 0, 60, size=20)

    for i, investment in enumerate(investment_history, 1):
        draw_text(f"{i}. {investment}", 0, 60 - i*20)

    if total_wealth >= 100000:
        draw_text("Congratulations! You’re a millionaire!", 0, -20, size=24, color="darkgreen")
    else:
        draw_text("Better luck next time!", 0, -40, size=24, color="darkred")

    time.sleep(2)

def final_path(wealth, investment_history):
    """Path when the user decides not to invest further."""
    draw_text("You've decided to stop investing.", 0, 100, size=24, color="darkblue")
    draw_text("Here's a summary of your wealth and investment history:", 0, 60, size=20)
    display_summary(wealth, investment_history)

    # Ask if they want to play again or exit
    choice = turtle.textinput("Play Again?", "Enter 'y' to restart the game or 'n' to exit: ").lower()

    if choice == 'y':
        main()  # Restart the game
    else:
        draw_text("Thank you for playing! Goodbye!", 0, -75, size=24, color="darkblue")
        time.sleep(2)
        turtle.bye()  # Exit the game

def main():
    """Main function to run the investment game."""
    welcome_message()

    wealth = 10000 # Starting wealth of $10000
    investment_history = []

    options = ["Stock Market", "Bond Market", "Savings Account", "Emergency Fund"] # Options to choose from
    choice = get_choice(options, "Where would you like to invest your money?")

    if choice == "Stock Market":
        growth = stock_market()
        investment_history.append(f"Stock Market - Growth: {growth}%")
        wealth += wealth * (growth / 100)
    elif choice == "Bond Market":
        growth = bond_market()
        investment_history.append(f"Bond Market - Growth: {growth}%")
        wealth += wealth * (growth / 100)
    elif choice == "Savings Account":
        growth = savings_account()
        investment_history.append(f"Savings Account - Growth: {growth}%")
        wealth += wealth * (growth / 100)
    elif choice == "Emergency Fund":
        growth = emergency_fund()
...         investment_history.append(f"Emergency Fund - Growth: {growth}%")
...         wealth += wealth * (growth / 100)
... 
...     wealth += random_event()
... 
...     while True:
...         choice = turtle.textinput("Continue Investing?", "Enter 'y' to continue or 'n' to stop investing: ").lower()
... 
...         if choice == 'n':
...             final_path(wealth, investment_history)
...             break
...         else:
...             options = ["Stock Market", "Bond Market", "Savings Account", "Emergency Fund"]
...             choice = get_choice(options, "Where would you like to invest next?")
... 
...             if choice == "Stock Market":
...                 growth = stock_market()
...                 investment_history.append(f"Stock Market - Growth: {growth}%")
...                 wealth += wealth * (growth / 100)
...             elif choice == "Bond Market":
...                 growth = bond_market()
...                 investment_history.append(f"Bond Market - Growth: {growth}%")
...                 wealth += wealth * (growth / 100)
...             elif choice == "Savings Account":
...                 growth = savings_account()
...                 investment_history.append(f"Savings Account - Growth: {growth}%")
...                 wealth += wealth * (growth / 100)
...             elif choice == "Emergency Fund":
...                 growth = emergency_fund()
...                 investment_history.append(f"Emergency Fund - Growth: {growth}%")
...                 wealth += wealth * (growth / 100)
... 
...             wealth += random_event()
... 
... if __name__ == "__main__":
...     main()
