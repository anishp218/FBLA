import pygame
import random
import sys

# Initialize      
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Investment Simulator")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)
LIGHT_YELLOW = (255, 255, 224)
LIGHT_GREY = (211, 211, 211)
LIGHT_CORAL = (240, 128, 128)
DARK_GREEN = (0, 100, 0)
DARK_BLUE = (0, 0, 139)
DARK_RED = (139, 0, 0)
BROWN = (165, 42, 42)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
main_font = pygame.font.SysFont("Times New Roman", 24)
title_font = pygame.font.SysFont("Times New Roman", 36)
button_font = pygame.font.SysFont("Times New Roman", 20)

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False
        
    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=10)  # Border
        
        text_surface = button_font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered
        
    def is_clicked(self, pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False

# Function to draw text on screen
def draw_text(text, x, y, font=main_font, color=BLACK):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    SCREEN.blit(text_surface, text_rect)

# Welcome screen
def welcome_message():
    SCREEN.fill(LIGHT_BLUE)
    draw_text("Welcome to the Investment Simulator!", WIDTH // 2, 100, font=title_font, color=DARK_BLUE)
    draw_text("Your goal is to make smart investments and grow your wealth.", WIDTH // 2, 170)
    draw_text("Each decision will affect your wealth, and random events may change everything.", WIDTH // 2, 210)
    draw_text("Let's get started!", WIDTH // 2, 250)
    
    pygame.display.update()
    pygame.time.delay(3000)  # Wait for 3 seconds

# Function to display options and get user choice
def get_choice(options, prompt="Choose an option:"):
    SCREEN.fill(LIGHT_YELLOW)
    draw_text(prompt, WIDTH // 2, 100, font=title_font, color=BROWN)
    
    buttons = []
    for idx, option in enumerate(options):
        y_pos = 150 + idx * 60
        button = Button(WIDTH // 2 - 150, y_pos, 300, 50, option, WHITE, LIGHT_GRAY)
        buttons.append(button)
        button.draw(SCREEN)
    
    pygame.display.update()
    
    # Wait for user selection
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            
            for idx, button in enumerate(buttons):
                button.check_hover(mouse_pos)
                if button.is_clicked(mouse_pos, event):
                    return options[idx]
        
        # Redraw buttons with hover effects
        for button in buttons:
            button.draw(SCREEN)
        
        pygame.display.update()
        pygame.time.delay(30)  # Small delay to prevent high CPU usage

# Stock market simulation
def stock_market():
    SCREEN.fill(LIGHT_GREEN)
    draw_text("You are in the Stock Market!", WIDTH // 2, 100, font=title_font, color=DARK_GREEN)
    draw_text("Risky choice but high return", WIDTH // 2, 150, color=GREEN)
    pygame.display.update()
    pygame.time.delay(1500)
    
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
    
    SCREEN.fill(LIGHT_YELLOW)
    draw_text(f"You chose {choice}. Let's see how it goes...", WIDTH // 2, 100)
    pygame.display.update()
    pygame.time.delay(2000)
    
    # Random events for investment choices
    event = random.choice(['boom', 'crash'])
    if event == 'boom':
        growth *= 1.5
        draw_text("The market boomed, and your investment grew by more!", WIDTH // 2, 150)
    elif event == 'crash':
        growth *= 0.5
        draw_text("The market crashed, and your investment lost some value.", WIDTH // 2, 150)
    
    pygame.display.update()
    pygame.time.delay(2000)
    return growth

# Bond market simulation
def bond_market():
    SCREEN.fill(LIGHT_GREY)
    draw_text("You are in the Bond Market!", WIDTH // 2, 100, font=title_font, color=BLACK)
    pygame.display.update()
    pygame.time.delay(1000)
    
    # Options for bond investment
    options = ["Government bonds", "Corporate bonds", "Municipal bonds", "High-yield bonds"]
    choice = get_choice(options, "Which bond would you like to invest in?")
    
    investments = {
        "Government bonds": 3,  
        "Corporate bonds": 5,  
        "Municipal bonds": 4,  
        "High-yield bonds": 8
    }
    
    growth = investments[choice]
    
    SCREEN.fill(LIGHT_YELLOW)
    draw_text(f"You chose {choice}. Let's see how it goes...", WIDTH // 2, 100)
    pygame.display.update()
    pygame.time.delay(2000)
    
    event = random.choice(['stable', 'recession'])
    if event == 'stable':
        growth += 2
        draw_text("The bond market is stable, and your returns grew!", WIDTH // 2, 150)
    elif event == 'recession':
        growth -= 1
        draw_text("The recession hit, and your returns decreased.", WIDTH // 2, 150)
    
    pygame.display.update()
    pygame.time.delay(2000)
    return growth

# Savings account simulation
def savings_account():
    SCREEN.fill(LIGHT_BLUE)
    draw_text("You chose a savings account!", WIDTH // 2, 100, font=title_font, color=DARK_BLUE)
    draw_text("Your returns will be low, but it's a safe investment.", WIDTH // 2, 150)
    pygame.display.update()
    pygame.time.delay(2000)
    return 1  # Very low but safe returns

# Emergency fund simulation
def emergency_fund():
    SCREEN.fill(LIGHT_CORAL)
    draw_text("You decided to build an emergency fund!", WIDTH // 2, 100, font=title_font, color=DARK_RED)
    draw_text("It's not a big return, but it's safe.", WIDTH // 2, 150)
    pygame.display.update()
    pygame.time.delay(2000)
    return 2  # Low, guaranteed returns

# Function to simulate a random event
def random_event():
    SCREEN.fill(WHITE)
    events = [
        "You inherited $10,000!",
        "A natural disaster caused a loss of $30,000.",
        "You discovered a great opportunity and gained $20,000.",
        "You lost $4,000 in a bad business venture.",
        "You got hacked and lost $60,000.",
        "You started a succesful company and gained $50,000",
        "You spent a lot of money on starting a company but it was unsuccesful and you lost $50,000.",
        "You won a lawsuit and gained $25,000.",
        "You lost a lawsuit and lost $25,000.",
        "You sold a large plot of land for $50,000!",
        "You created a revolutionary technology and gained $100,000!",
        "You had a surgical procedure and lost $80,000.",
        "The value of your home skyrocketed and you gained $50,000!",
        "Your car broke down and you had to get it repaired for $10,000.",
        "You got scammed and lost $50,000.",
        "You won the loterry and gained $100,000.",
        "Your house burned down and you lost $100,000.",
        "Your savings account was comprimised and you lost $100,000.",
        "You found a rare coin collection and gained $5,000.",
        "Your bike got stolen, and replacing it cost $3,000.",
        "You received a big bonus at work and gained $12,000.",
        "Your phone broke, and replacing it cost $4,000.",
        "You sold antique furniture and gained $8,000.",
        "You had a minor car accident and lost $15,000.",
        "You got a tax refund and gained $10,000.",
        "Your pet needed emergency surgery, costing you $7,000.",
        "You overpaid your taxes and lost $3,000.",
        "You won a local lottery and gained $7,500.",
        "You dropped your laptop, and repairs cost $2,500.",
        "You did some side work and earned $9,000.",
        "Your fridge broke down, and replacing it cost $3,500.",
        "You found cash in an old wallet and gained $1,000.",
        "You missed a rent payment and lost $6,000.",
        "You helped a friend move and got $500 as thanks.",
        "Your rare collectibles sold for $12,000 online.",
        "You got a parking ticket and lost $500.",
        "You accidentally subscribed to an expensive service and lost $1,200.",
        "You won a charity raffle and gained $15,000.",
        "You had to replace your AC system for $8,000.",
        "You got a raise and you gained $25,000.",
        "You treated yourself to a luxury vacation, costing $20,000.",
        "You sold a classic car and earned $30,000.",
        "Your friend paid you back a long-standing debt of $5,000.",
        "You lost your wallet on a trip and had to replace everything for $2,000.",
        "You bought an expensive ring for a loved one, spending $10,000.",
        "You received an inheritance of $50,000.",
        "You had a major health procedure, and medical bills cost $100,000.",
        "Your home suffered severe water damage, costing $80,000 in repairs.",
        "You were sued and lost $60,000 in damages.",
        "Your car engine failed, and replacement cost $15,000.",
        "You invested in a failing startup and lost $40,000.",
        "A tree fell on your house, causing $25,000 in damage.",
        "You were the victim of identity theft and lost $70,000.",
        "You had to replace your roof after a storm, costing $30,000.",
        "You got audited and owed $20,000 in back taxes."
        
    ]
    event = random.choice(events)
    draw_text("Random Event:", WIDTH // 2, 80, font=title_font, color=DARK_GREEN)
    draw_text(event, WIDTH // 2, 130, color=DARK_GREEN)
    
    # Extract the amount from the event string
    amount_str = event.split('$')[1].split()[0]
    amount_str = amount_str.replace(',', '').replace('!', '').replace('.', '')
    amount = int(amount_str)
    
    # Determine if it's a gain or loss
    if "loss" in event or "lost" in event:
        amount = -amount
    
    pygame.display.update()
    pygame.time.delay(2000)
    return amount

# Display summary of wealth and investments
def display_summary(total_wealth, investment_history):
    SCREEN.fill(WHITE)
    draw_text(f"Your total wealth: ${total_wealth:.2f}", WIDTH // 2, 80, font=title_font, color=DARK_BLUE)
    draw_text("Investment History:", WIDTH // 2, 130, font=main_font)
    
    y_offset = 170
    for i, investment in enumerate(investment_history, 1):
        draw_text(f"{i}. {investment}", WIDTH // 2, y_offset, font=main_font)
        y_offset += 30
    
    if total_wealth >= 100000:
        draw_text("Congratulations! You're a millionaire!", WIDTH // 2, y_offset + 30, font=title_font, color=DARK_GREEN)
    else:
        draw_text("Better luck next time!", WIDTH // 2, y_offset + 30, font=title_font, color=DARK_RED)
    
    # Add restart and quit buttons
    restart_button = Button(WIDTH // 4 - 100, HEIGHT - 80, 200, 50, "Restart Game", GREEN, LIGHT_GREEN)
    quit_button = Button(3 * WIDTH // 4 - 100, HEIGHT - 80, 200, 50, "Quit Game", RED, LIGHT_CORAL)
    
    restart_button.draw(SCREEN)
    quit_button.draw(SCREEN)
    
    pygame.display.update()
    
    # Wait for user decision
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            
            restart_button.check_hover(mouse_pos)
            quit_button.check_hover(mouse_pos)
            
            if restart_button.is_clicked(mouse_pos, event):
                return "restart"
            elif quit_button.is_clicked(mouse_pos, event):
                return "quit"
        
        restart_button.draw(SCREEN)
        quit_button.draw(SCREEN)
        pygame.display.update()
        pygame.time.delay(30)

# Final path when user decides to stop investing
def final_path(wealth, investment_history):
    SCREEN.fill(WHITE)
    draw_text("You've decided to stop investing.", WIDTH // 2, 80, font=title_font, color=DARK_BLUE)
    draw_text("Here's a summary of your wealth and investment history:", WIDTH // 2, 130)
    pygame.display.update()
    pygame.time.delay(2000)
    
    result = display_summary(wealth, investment_history)
    return result

# Main function to run the investment game
def main():
    welcome_message()
    
    wealth = 10000  # Starting wealth of $10000
    investment_history = []
    
    options = ["Stock Market", "Bond Market", "Savings Account", "Emergency Fund"]
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
        investment_history.append(f"Emergency Fund - Growth: {growth}%")
        wealth += wealth * (growth / 100)
    
    wealth += random_event()
    
    continue_investing = True
    while continue_investing:

        # lose if wealth goes below 0 - if you go bankrupt
        if wealth <= 0:
            SCREEN.fill(LIGHT_CORAL)
            draw_text("Game Over!", WIDTH // 2, 100, font=title_font, color=DARK_RED)
            draw_text("Your wealth has fallen below $0.", WIDTH // 2, 150)
            draw_text("You've gone bankrupt!", WIDTH // 2, 200)
            
            # Add restart and quit buttons
            restart_button = Button(WIDTH // 4 - 100, HEIGHT - 150, 200, 50, "Try Again", GREEN, LIGHT_GREEN)
            quit_button = Button(3 * WIDTH // 4 - 100, HEIGHT - 150, 200, 50, "Quit Game", RED, LIGHT_CORAL)
            
            restart_button.draw(SCREEN)
            quit_button.draw(SCREEN)
            
            pygame.display.update()
            
            # Wait for user decision
            decision_made = False
            while not decision_made:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    mouse_pos = pygame.mouse.get_pos()
                    
                    restart_button.check_hover(mouse_pos)
                    quit_button.check_hover(mouse_pos)
                    
                    if restart_button.is_clicked(mouse_pos, event):
                        return main()  # Restart the game
                    elif quit_button.is_clicked(mouse_pos, event):
                        pygame.quit()
                        sys.exit()
                
                restart_button.draw(SCREEN)
                quit_button.draw(SCREEN)
                pygame.display.update()
                pygame.time.delay(30)
            
            continue_investing = False  # This line won't be reached due to the return above, but added for clarity
        # Create buttons for continue or stop investing
        SCREEN.fill(LIGHT_YELLOW)
        draw_text("Would you like to continue investing?", WIDTH // 2, 100, font=title_font, color=BROWN)
        draw_text(f"Current Wealth: ${wealth:.2f}", WIDTH // 2, 150, font=main_font)
        
        continue_button = Button(WIDTH // 4 - 100, 250, 200, 50, "Yes, Continue", GREEN, LIGHT_GREEN)
        stop_button = Button(3 * WIDTH // 4 - 100, 250, 200, 50, "No, Stop Investing", RED, LIGHT_CORAL)
        
        continue_button.draw(SCREEN)
        stop_button.draw(SCREEN)
        
        pygame.display.update()
        
        # Wait for user decision
        decision_made = False
        while not decision_made:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                mouse_pos = pygame.mouse.get_pos()
                
                continue_button.check_hover(mouse_pos)
                stop_button.check_hover(mouse_pos)
                
                if continue_button.is_clicked(mouse_pos, event):
                    decision_made = True
                    # Continue investing
                elif stop_button.is_clicked(mouse_pos, event):
                    decision_made = True
                    continue_investing = False
            
            continue_button.draw(SCREEN)
            stop_button.draw(SCREEN)
            pygame.display.update()
            pygame.time.delay(30)
        
        if continue_investing:
            options = ["Stock Market", "Bond Market", "Savings Account", "Emergency Fund"]
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
                investment_history.append(f"Emergency Fund - Growth: {growth}%")
                wealth += wealth * (growth / 100)
            
            # Add random event after each investment round
            event_change = random_event()
            wealth += event_change
            if event_change > 0:
                investment_history.append(f"Random Event: Gained ${event_change}")
            else:
                investment_history.append(f"Random Event: Lost ${abs(event_change)}")
    
    # Final path when user stops investing
    result = final_path(wealth, investment_history)
    
    if result == "restart":
        main()  # Restart the game
    elif result == "quit":
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()
        
