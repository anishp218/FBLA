import pygame
import random
import sys

# Initialize      
pygame.init()

# Constants
WIDTH, HEIGHT = 900, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Investment Story Game")

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
small_font = pygame.font.SysFont("Times New Roman", 16)

# Market news that affects sectors
market_news = [
    {"headline": "Technology center explodes in Silicon Valley!", "tech": -15, "real_estate": -5, "energy": 0, "biotech": -10, "bonds": 5},
    {"headline": "New breakthrough in cancer treatment!", "tech": 0, "real_estate": 0, "energy": 0, "biotech": 20, "bonds": 0},
    {"headline": "Housing market crashes nationwide!", "tech": -5, "real_estate": -25, "energy": -5, "biotech": -5, "bonds": 10},
    {"headline": "Oil pipeline ruptures, causing major spill!", "tech": 0, "real_estate": -5, "energy": -20, "biotech": 0, "bonds": 0},
    {"headline": "New renewable energy tax credits approved!", "tech": 5, "real_estate": 0, "energy": 15, "biotech": 0, "bonds": 0},
    {"headline": "Fed raises interest rates!", "tech": -10, "real_estate": -15, "energy": -5, "biotech": -10, "bonds": 15},
    {"headline": "Major tech company releases revolutionary AI!", "tech": 25, "real_estate": 0, "energy": 0, "biotech": 5, "bonds": -5},
    {"headline": "Pandemic causes global lockdowns!", "tech": 10, "real_estate": -20, "energy": -15, "biotech": 30, "bonds": 10},
    {"headline": "Solar energy efficiency doubles with new technology!", "tech": 10, "real_estate": 0, "energy": 20, "biotech": 0, "bonds": -5},
    {"headline": "Housing construction booms in major cities!", "tech": 0, "real_estate": 25, "energy": 5, "biotech": 0, "bonds": -5},
    {"headline": "Government increases infrastructure spending!", "tech": 5, "real_estate": 15, "energy": 10, "biotech": 0, "bonds": -10},
    {"headline": "Major political unrest in oil-producing regions!", "tech": -5, "real_estate": -10, "energy": -25, "biotech": -5, "bonds": 15}
]

# Portfolio to track investments
portfolio = {
    "tech": {"long": 0, "short": 0},
    "real_estate": {"long": 0, "short": 0},
    "energy": {"long": 0, "short": 0},
    "biotech": {"long": 0, "short": 0},
    "government": {"long": 0, "short": 0},
    "corporate": {"long": 0, "short": 0},
    "municipal": {"long": 0, "short": 0},
    "high_yield": {"long": 0, "short": 0},
    "savings": {"amount": 0},
    "emergency": {"amount": 0}
}

# Current market news
current_news = None

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

# Function to add navigation buttons to screens
def add_navigation_buttons(screen, show_back=True):
    # Quit button - top-right corner
    quit_button = Button(WIDTH - 110, 20, 90, 40, "Quit", RED, LIGHT_CORAL, WHITE)
    quit_button.draw(screen)
    
    # Restart button - top-right second position
    restart_button = Button(WIDTH - 210, 20, 90, 40, "Restart", BLUE, LIGHT_BLUE, WHITE)
    restart_button.draw(screen)
    
    # Back button (if needed) - top-left corner
    back_button = None
    if show_back:
        back_button = Button(20, 20, 90, 40, "Back", GRAY, LIGHT_GRAY)
        back_button.draw(screen)
    
    return quit_button, restart_button, back_button

# Handle navigation button clicks
def handle_navigation(quit_button, restart_button, back_button, mouse_pos, event):
    if quit_button.is_clicked(mouse_pos, event):
        pygame.quit()
        sys.exit()
    elif restart_button.is_clicked(mouse_pos, event):
        return "restart"
    elif back_button and back_button.is_clicked(mouse_pos, event):
        return "back"
    return None

# Function to draw text on screen
def draw_text(text, x, y, font=main_font, color=BLACK):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    SCREEN.blit(text_surface, text_rect)

# Function to draw multi-line text
def draw_multiline_text(text, x, y, font=main_font, color=BLACK, line_height=30, max_width=700):
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        temp_line = ' '.join(current_line + [word])
        temp_surface = font.render(temp_line, True, color)
        
        if temp_surface.get_width() > max_width:
            lines.append(' '.join(current_line))
            current_line = [word]
        else:
            current_line.append(word)
    
    if current_line:
        lines.append(' '.join(current_line))
    
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(x, y + i * line_height))
        SCREEN.blit(text_surface, text_rect)

# Welcome screen with instructions
def show_instructions():
    SCREEN.fill(LIGHT_BLUE)
    draw_text("Welcome to the Investment Story Game!", WIDTH // 2, 60, font=title_font, color=DARK_BLUE)
    
    instructions = [
        "• You've inherited $10,000 from a distant relative.",
        "• Your goal is to grow your wealth through smart investing.",
        "• You can invest in stocks, bonds, savings accounts, or emergency funds.",
        "• Use the Market Research button to get hints about market trends.",
        "• You can either buy (go long) or short sell investments:",
        "  - BUYING (LONG): You profit when prices go up.",
        "  - SHORT SELLING: You profit when prices go down.",
        "• Each investment decision will affect your wealth.",
        "• Random events may dramatically change your financial situation.",
        "• Your goal is to reach $100,000 without going bankrupt.",
        "• If your wealth falls below $0, you lose the game."
    ]
    
    y_pos = 130
    for instruction in instructions:
        text_surface = main_font.render(instruction, True, BLACK)
        text_rect = text_surface.get_rect(topleft=(100, y_pos))
        SCREEN.blit(text_surface, text_rect)
        y_pos += 35
    
    # Add start button
    start_button = Button(WIDTH // 2 - 100, 600, 200, 50, "Start Game", GREEN, LIGHT_GREEN)
    start_button.draw(SCREEN)
    
    # Add navigation buttons (no back button on first screen)
    quit_button, restart_button, _ = add_navigation_buttons(SCREEN, show_back=False)
    
    pygame.display.update()
    
    # Wait for user to click start
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            start_button.check_hover(mouse_pos)
            quit_button.check_hover(mouse_pos)
            restart_button.check_hover(mouse_pos)
            
            if start_button.is_clicked(mouse_pos, event):
                return
            
            # Handle navigation buttons
            action = handle_navigation(quit_button, restart_button, None, mouse_pos, event)
            if action == "restart":
                return
        
        start_button.draw(SCREEN)
        quit_button.draw(SCREEN)
        restart_button.draw(SCREEN)
        pygame.display.update()
        pygame.time.delay(30)

# Function to display options and get user choice
def get_choice(options, prompt="What will you do:", previous_screen=None):
    SCREEN.fill(LIGHT_YELLOW)
    draw_text(prompt, WIDTH // 2, 100, font=title_font, color=BROWN)
    
    buttons = []
    for idx, option in enumerate(options):
        y_pos = 150 + idx * 60
        button = Button(WIDTH // 2 - 150, y_pos, 300, 50, option, WHITE, LIGHT_GRAY)
        buttons.append(button)
        button.draw(SCREEN)
    
    # Add navigation buttons
    quit_button, restart_button, back_button = add_navigation_buttons(SCREEN)
    
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
            
            quit_button.check_hover(mouse_pos)
            restart_button.check_hover(mouse_pos)
            back_button.check_hover(mouse_pos)
            
            # Handle navigation buttons
            action = handle_navigation(quit_button, restart_button, back_button, mouse_pos, event)
            if action == "restart":
                return "restart"
            elif action == "back" and previous_screen:
                return "back"
        
        # Redraw buttons with hover effects
        for button in buttons:
            button.draw(SCREEN)
        
        quit_button.draw(SCREEN)
        restart_button.draw(SCREEN)
        back_button.draw(SCREEN)
        
        pygame.display.update()
        pygame.time.delay(30)

# Market research screen
def market_research(wealth):
    global current_news
    
    SCREEN.fill(LIGHT_GREY)
    draw_text("Market Research", WIDTH // 2, 60, font=title_font, color=DARK_BLUE)
    draw_text(f"Current Wealth: ${wealth:.2f}", WIDTH // 2, 100)
    
    # Generate or display current news
    if not current_news:
        current_news = random.choice(market_news)
    
    draw_text("BREAKING NEWS:", WIDTH // 2, 150, color=DARK_RED, font=title_font)
    draw_multiline_text(current_news["headline"], WIDTH // 2, 200, color=DARK_RED)
    
    # Display sector impacts
    draw_text("Market Impacts:", WIDTH // 2, 250, font=title_font)
    
    impact_info = [
        f"Technology: {'▲' if current_news['tech'] > 0 else '▼' if current_news['tech'] < 0 else '◆'}",
        f"Real Estate: {'▲' if current_news['real_estate'] > 0 else '▼' if current_news['real_estate'] < 0 else '◆'}",
        f"Energy: {'▲' if current_news['energy'] > 0 else '▼' if current_news['energy'] < 0 else '◆'}",
        f"Biotech: {'▲' if current_news['biotech'] > 0 else '▼' if current_news['biotech'] < 0 else '◆'}",
        f"Bonds: {'▲' if current_news['bonds'] > 0 else '▼' if current_news['bonds'] < 0 else '◆'}"
    ]
    
    y_pos = 300
    for info in impact_info:
        draw_text(info, WIDTH // 2, y_pos)
        y_pos += 40
    
    # Add tips for investment strategy
    draw_text("Investment Tip:", WIDTH // 2, 500, font=title_font)
    
    # Generate a tip based on the current news
    if any(value > 10 for key, value in current_news.items() if key != "headline"):
        tip = "Consider going LONG on sectors with ▲ and SHORT on sectors with ▼"
    elif any(value < -10 for key, value in current_news.items() if key != "headline"):
        tip = "Consider going SHORT on sectors with ▼ and LONG on sectors with ▲"
    else:
        tip = "Market changes are subtle. Consider safer investments like bonds or savings."
    
    draw_multiline_text(tip, WIDTH // 2, 540)
    
    # Add back button
    back_button = Button(WIDTH // 2 - 100, 600, 200, 50, "Back to Main Menu", LIGHT_CORAL, RED, WHITE)
    back_button.draw(SCREEN)
    
    # Add navigation buttons
    quit_button, restart_button, nav_back_button = add_navigation_buttons(SCREEN)
    
    pygame.display.update()
    
    # Wait for user to click back
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            back_button.check_hover(mouse_pos)
            quit_button.check_hover(mouse_pos)
            restart_button.check_hover(mouse_pos)
            nav_back_button.check_hover(mouse_pos)
            
            if back_button.is_clicked(mouse_pos, event):
                return
            
            # Handle navigation buttons
            action = handle_navigation(quit_button, restart_button, nav_back_button, mouse_pos, event)
            if action == "restart":
                return "restart"
            elif action == "back":
                return
        
        back_button.draw(SCREEN)
        quit_button.draw(SCREEN)
        restart_button.draw(SCREEN)
        nav_back_button.draw(SCREEN)
        pygame.display.update()
        pygame.time.delay(30)

# Get investment amount
def get_investment_amount(wealth, investment_type):
    SCREEN.fill(LIGHT_YELLOW)
    draw_text(f"How much would you like to invest in {investment_type}?", WIDTH // 2, 100, font=title_font)
    draw_text(f"Current wealth: ${wealth:.2f}", WIDTH // 2, 150)
    
    # Add input box for amount
    input_rect = pygame.Rect(WIDTH // 2 - 150, 200, 300, 50)
    input_color = LIGHT_GRAY
    input_active = True
    input_text = ""
    
    # Add buttons for different percentages
    percentage_buttons = []
    percentages = ["25%", "50%", "75%", "100%"]
    
    for i, percentage in enumerate(percentages):
        x_pos = 150 + i * 200
        button = Button(x_pos, 280, 100, 40, percentage, WHITE, LIGHT_GRAY)
        percentage_buttons.append(button)
    
    # Add confirm button
    confirm_button = Button(WIDTH // 2 - 100, 350, 200, 50, "Confirm", GREEN, LIGHT_GREEN)
    
    # Add navigation buttons
    quit_button, restart_button, back_button = add_navigation_buttons(SCREEN)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            
            # Check navigation button hover
            quit_button.check_hover(mouse_pos)
            restart_button.check_hover(mouse_pos)
            back_button.check_hover(mouse_pos)
            
            # Handle navigation button clicks
            action = handle_navigation(quit_button, restart_button, back_button, mouse_pos, event)
            if action == "restart":
                return "restart"
            elif action == "back":
                return "back"
            
            # Handle text input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        amount = float(input_text)
                        if 0 < amount <= wealth:
                            return amount
                        else:
                            input_text = "Invalid amount"
                    except ValueError:
                        input_text = "Invalid input"
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if event.unicode.isdigit() or event.unicode == '.':
                        input_text += event.unicode
            
            # Handle button clicks
            for i, button in enumerate(percentage_buttons):
                button.check_hover(mouse_pos)
                if button.is_clicked(mouse_pos, event):
                    percentage = int(percentages[i].strip('%'))
                    input_text = str(round(wealth * percentage / 100, 2))
            
            # Handle confirm button
            confirm_button.check_hover(mouse_pos)
            if confirm_button.is_clicked(mouse_pos, event):
                try:
                    amount = float(input_text)
                    if 0 < amount <= wealth:
                        return amount
                    else:
                        input_text = "Invalid amount"
                except ValueError:
                    input_text = "Invalid input"
        
        SCREEN.fill(LIGHT_YELLOW)
        draw_text(f"How much would you like to invest in {investment_type}?", WIDTH // 2, 100, font=title_font)
        draw_text(f"Current wealth: ${wealth:.2f}", WIDTH // 2, 150)
        
        # Draw input box
        pygame.draw.rect(SCREEN, input_color, input_rect, border_radius=5)
        pygame.draw.rect(SCREEN, BLACK, input_rect, 2, border_radius=5)
        
        # Render input text
        text_surface = main_font.render(input_text, True, BLACK)
        text_rect = text_surface.get_rect(center=input_rect.center)
        SCREEN.blit(text_surface, text_rect)
        
        # Draw percentage buttons
        for button in percentage_buttons:
            button.draw(SCREEN)
        
        # Draw confirm button
        confirm_button.draw(SCREEN)
        
        # Draw navigation buttons
        quit_button.draw(SCREEN)
        restart_button.draw(SCREEN)
        back_button.draw(SCREEN)
        
        draw_text("Enter amount or select a percentage of your wealth", WIDTH // 2, 450)
        
        pygame.display.update()
        pygame.time.delay(30)

# Get position type (long or short)
def get_position_type(sector):
    SCREEN.fill(LIGHT_YELLOW)
    draw_text(f"How would you like to invest in {sector}?", WIDTH // 2, 100, font=title_font, color=BROWN)
    
    # Create buttons for long and short
    long_button = Button(WIDTH // 2 - 250, 200, 200, 80, "BUY (LONG)", GREEN, LIGHT_GREEN)
    short_button = Button(WIDTH // 2 + 50, 200, 200, 80, "SHORT SELL", RED, LIGHT_CORAL)
    
    # Add explanations
    explanations = [
        "BUY (LONG): You profit when the asset's value increases.",
        "You're betting the market will go UP.",
        "",
        "SHORT SELL: You profit when the asset's value decreases.",
        "You're betting the market will go DOWN."
    ]
    
    y_pos = 320
    for explanation in explanations:
        text_surface = main_font.render(explanation, True, BLACK)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y_pos))
        SCREEN.blit(text_surface, text_rect)
        y_pos += 30
    
    long_button.draw(SCREEN)
    short_button.draw(SCREEN)
    
    # Add navigation buttons
    quit_button, restart_button, back_button = add_navigation_buttons(SCREEN)
    
    pygame.display.update()
    
    # Wait for user selection
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            
            long_button.check_hover(mouse_pos)
            short_button.check_hover(mouse_pos)
            quit_button.check_hover(mouse_pos)
            restart_button.check_hover(mouse_pos)
            back_button.check_hover(mouse_pos)
            
            if long_button.is_clicked(mouse_pos, event):
                return "long"
            elif short_button.is_clicked(mouse_pos, event):
                return "short"
            
            # Handle navigation button clicks
            action = handle_navigation(quit_button, restart_button, back_button, mouse_pos, event)
            if action == "restart":
                return "restart"
            elif action == "back":
                return "back"
        
        # Redraw buttons with hover effects
        long_button.draw(SCREEN)
        short_button.draw(SCREEN)
        quit_button.draw(SCREEN)
        restart_button.draw(SCREEN)
        back_button.draw(SCREEN)
        
        pygame.display.update()
        pygame.time.delay(30)

# Stock market simulation
def stock_market(wealth):
    global current_news
    SCREEN.fill(LIGHT_GREEN)
    draw_text("Stock Market Investment", WIDTH // 2, 100, font=title_font, color=DARK_GREEN)
    draw_text(f"Current Wealth: ${wealth:.2f}", WIDTH // 2, 150)
    
    # Add navigation buttons
    quit_button, restart_button, back_button = add_navigation_buttons(SCREEN)
    
    pygame.display.update()
    pygame.time.delay(1500)
    
    # Choose sector
    options = ["Technology Stocks", "Real Estate Stocks", "Renewable Energy Stocks", "Biotech Stocks"]
    choice = get_choice(options, "Which sector would you like to invest in?", "main")
    
    # Check for navigation choices
    if choice == "restart":
        return "restart"
    elif choice == "back":
        return wealth
    
    # Map choices to portfolio keys
    sector_mapping = {
        "Technology Stocks": "tech",
        "Real Estate Stocks": "real_estate",
        "Renewable Energy Stocks": "energy",
        "Biotech Stocks": "biotech"
    }
    
    sector = sector_mapping[choice]
    
    # Choose position type (long or short)
    position = get_position_type(choice)
    if position == "restart":
        return "restart"
    elif position == "back":
        return wealth
    
    # Get investment amount
    investment_amount = get_investment_amount(wealth, choice)
    if investment_amount == "restart":
        return "restart"
    elif investment_amount == "back":
        return wealth
    
    # Update portfolio and wealth
    portfolio[sector][position] += investment_amount
    remaining_wealth = wealth - investment_amount
    
    # Base growth rates
    base_growth_rates = {
        "tech": 15,
        "real_estate": 7,
        "energy": 10,
        "biotech": 20
    }
    
    # Adjust growth based on current news
    news_impact = 0
    if sector == "tech":
        news_impact = current_news["tech"]
    elif sector == "real_estate":
        news_impact = current_news["real_estate"]
    elif sector == "energy":
        news_impact = current_news["energy"]
    elif sector == "biotech":
        news_impact = current_news["biotech"]
    
    base_growth = base_growth_rates[sector]
    adjusted_growth = base_growth + news_impact
    
    # Random event multiplier (market volatility)
    volatility = random.uniform(0.7, 1.3)
    final_growth = adjusted_growth * volatility
    
    # Calculate return based on position type
    if position == "long":
        return_amount = investment_amount * (1 + final_growth / 100)
    else:  # short position
        return_amount = investment_amount * (1 - final_growth / 100)
    
    # Display result
    SCREEN.fill(LIGHT_YELLOW)
    draw_text(f"Investment Result for {choice}", WIDTH // 2, 100, font=title_font)
    
    if position == "long":
        growth_text = f"Market growth: {final_growth:.2f}%"
    else:
        growth_text = f"Market change: {final_growth:.2f}%"
    
    draw_text(growth_text, WIDTH // 2, 150)
    
    profit = return_amount - investment_amount
    profit_color = GREEN if profit >= 0 else RED
    
    draw_text(f"Investment: ${investment_amount:.2f}", WIDTH // 2, 200)
    draw_text(f"Return: ${return_amount:.2f}", WIDTH // 2, 250)
    draw_text(f"Profit/Loss: ${profit:.2f}", WIDTH // 2, 300, color=profit_color)
    
    # Continue button
    continue_button = Button(WIDTH // 2 - 100, 400, 200, 50, "Continue", BLUE, LIGHT_BLUE, WHITE)
    continue_button.draw(SCREEN)
    
    # Add navigation buttons
    quit_button, restart_button, back_button = add_navigation_buttons(SCREEN)
    
    pygame.display.update()
    
    # Wait for user to continue
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            continue_button.check_hover(mouse_pos)
            quit_button.check_hover(mouse_pos)
            restart_button.check_hover(mouse_pos)
            back_button.check_hover(mouse_pos)
            
            if continue_button.is_clicked(mouse_pos, event):
                # Update the news after the transaction is complete
                current_news = random.choice(market_news)
                return remaining_wealth + return_amount
            
            # Handle navigation button clicks
            action = handle_navigation(quit_button, restart_button, back_button, mouse_pos, event)
            if action == "restart":
                return "restart"
            elif action == "back":
                return wealth  # Return original wealth if going back
        
        continue_button.draw(SCREEN)
        quit_button.draw(SCREEN)
        restart_button.draw(SCREEN)
        back_button.draw(SCREEN)
        pygame.display.update()
        pygame.time.delay(30)

# Bond market simulation
def bond_market(wealth):
    global current_news
    SCREEN.fill(LIGHT_GREY)
    draw_text("Bond Market Investment", WIDTH // 2, 100, font=title_font, color=BLACK)
    draw_text(f"Current Wealth: ${wealth:.2f}", WIDTH // 2, 150)
    
    # Add navigation buttons
    quit_button, restart_button, back_button = add_navigation_buttons(SCREEN)
    
    pygame.display.update()
    pygame.time.delay(1000)
    
    # Choose bond type
    options = ["Government Bonds", "Corporate Bonds", "Municipal Bonds", "High-Yield Bonds"]
    choice = get_choice(options, "Which bonds would you like to invest in?", "main")
    
    # Check for navigation choices
    if choice == "restart":
        return "restart"
    elif choice == "back":
        return wealth
    
    # Map choices to portfolio keys
    bond_mapping = {
        "Government Bonds": "government",
        "Corporate Bonds": "corporate",
        "Municipal Bonds": "municipal",
        "High-Yield Bonds": "high_yield"
    }
    
    bond_type = bond_mapping[choice]
    
    # Choose position type (long or short)
    position = get_position_type(choice)
    if position == "restart":
        return "restart"
    elif position == "back":
        return wealth
    
    # Get investment amount
    # Get investment amount
    investment_amount = get_investment_amount(wealth, choice)
    if investment_amount == "restart":
        return "restart"
    elif investment_amount == "back":
        return wealth
    
    # Update portfolio and wealth
    portfolio[bond_type][position] += investment_amount
    remaining_wealth = wealth - investment_amount
    
    # Base yield rates for bonds
    base_yield_rates = {
        "government": 3,
        "corporate": 5,
        "municipal": 4,
        "high_yield": 8
    }
    
    # Adjust yield based on current news
    news_impact = current_news["bonds"]
    
    base_yield = base_yield_rates[bond_type]
    adjusted_yield = base_yield + news_impact
    
    # Random event multiplier (less volatility for bonds)
    volatility = random.uniform(0.9, 1.1)
    final_yield = adjusted_yield * volatility
    
    # Calculate return based on position type
    if position == "long":
        return_amount = investment_amount * (1 + final_yield / 100)
    else:  # short position
        return_amount = investment_amount * (1 - final_yield / 100)
    
    # Display result
    SCREEN.fill(LIGHT_YELLOW)
    draw_text(f"Investment Result for {choice}", WIDTH // 2, 100, font=title_font)
    
    if position == "long":
        yield_text = f"Bond yield: {final_yield:.2f}%"
    else:
        yield_text = f"Bond market change: {final_yield:.2f}%"
    
    draw_text(yield_text, WIDTH // 2, 150)
    
    profit = return_amount - investment_amount
    profit_color = GREEN if profit >= 0 else RED
    
    draw_text(f"Investment: ${investment_amount:.2f}", WIDTH // 2, 200)
    draw_text(f"Return: ${return_amount:.2f}", WIDTH // 2, 250)
    draw_text(f"Profit/Loss: ${profit:.2f}", WIDTH // 2, 300, color=profit_color)
    
    # Continue button
    continue_button = Button(WIDTH // 2 - 100, 400, 200, 50, "Continue", BLUE, LIGHT_BLUE, WHITE)
    continue_button.draw(SCREEN)
    
    # Add navigation buttons
    quit_button, restart_button, back_button = add_navigation_buttons(SCREEN)
    
    pygame.display.update()
    
    # Wait for user to continue
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            continue_button.check_hover(mouse_pos)
            quit_button.check_hover(mouse_pos)
            restart_button.check_hover(mouse_pos)
            back_button.check_hover(mouse_pos)
            
            if continue_button.is_clicked(mouse_pos, event):
                # Update the news after the transaction is complete
                current_news = random.choice(market_news)
                return remaining_wealth + return_amount
            
            # Handle navigation button clicks
            action = handle_navigation(quit_button, restart_button, back_button, mouse_pos, event)
            if action == "restart":
                return "restart"
            elif action == "back":
                return wealth  # Return original wealth if going back
        
        continue_button.draw(SCREEN)
        quit_button.draw(SCREEN)
        restart_button.draw(SCREEN)
        back_button.draw(SCREEN)
        pygame.display.update()
        pygame.time.delay(30)

# Savings account simulation
def savings_account(wealth):
    SCREEN.fill(LIGHT_BLUE)
    draw_text("Savings Account", WIDTH // 2, 100, font=title_font, color=DARK_BLUE)
    draw_text(f"Current Wealth: ${wealth:.2f}", WIDTH // 2, 150)
    
    # Add navigation buttons
    quit_button, restart_button, back_button = add_navigation_buttons(SCREEN)
    
    pygame.display.update()
    pygame.time.delay(1000)
    
    # Display savings information
    draw_text("Savings accounts offer a safe, low-yield investment option.", WIDTH // 2, 200)
    draw_text("Current interest rate: 2.5% per year", WIDTH // 2, 250)
    draw_text("Time frame: 3 months (0.625% return)", WIDTH // 2, 300)
    
    # Get investment amount
    investment_amount = get_investment_amount(wealth, "a Savings Account")
    if investment_amount == "restart":
        return "restart"
    elif investment_amount == "back":
        return wealth
    
    # Update portfolio and wealth
    portfolio["savings"]["amount"] += investment_amount
    remaining_wealth = wealth - investment_amount
    
    # Calculate return (3 month period)
    interest_rate = 0.025 / 4  # 2.5% annual rate for a quarter
    return_amount = investment_amount * (1 + interest_rate)
    
    # Display result
    SCREEN.fill(LIGHT_YELLOW)
    draw_text("Savings Account Result", WIDTH // 2, 100, font=title_font)
    
    draw_text("Interest rate: 0.625% (3 months)", WIDTH // 2, 150)
    
    profit = return_amount - investment_amount
    
    draw_text(f"Investment: ${investment_amount:.2f}", WIDTH // 2, 200)
    draw_text(f"Return after 3 months: ${return_amount:.2f}", WIDTH // 2, 250)
    draw_text(f"Interest earned: ${profit:.2f}", WIDTH // 2, 300, color=GREEN)
    
    # Continue button
    continue_button = Button(WIDTH // 2 - 100, 400, 200, 50, "Continue", BLUE, LIGHT_BLUE, WHITE)
    continue_button.draw(SCREEN)
    
    # Add navigation buttons
    quit_button, restart_button, back_button = add_navigation_buttons(SCREEN)
    
    pygame.display.update()
    
    # Wait for user to continue
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            continue_button.check_hover(mouse_pos)
            quit_button.check_hover(mouse_pos)
            restart_button.check_hover(mouse_pos)
            back_button.check_hover(mouse_pos)
            
            if continue_button.is_clicked(mouse_pos, event):
                return remaining_wealth + return_amount
            
            # Handle navigation button clicks
            action = handle_navigation(quit_button, restart_button, back_button, mouse_pos, event)
            if action == "restart":
                return "restart"
            elif action == "back":
                return wealth  # Return original wealth if going back
        
        continue_button.draw(SCREEN)
        quit_button.draw(SCREEN)
        restart_button.draw(SCREEN)
        back_button.draw(SCREEN)
        pygame.display.update()
        pygame.time.delay(30)

# Emergency fund simulation
def emergency_fund(wealth):
    SCREEN.fill(LIGHT_BLUE)
    draw_text("Emergency Fund", WIDTH // 2, 100, font=title_font, color=DARK_BLUE)
    draw_text(f"Current Wealth: ${wealth:.2f}", WIDTH // 2, 150)
    
    # Add navigation buttons
    quit_button, restart_button, back_button = add_navigation_buttons(SCREEN)
    
    pygame.display.update()
    pygame.time.delay(1000)
    
    # Display emergency fund information
    draw_text("Emergency funds provide financial security for unexpected events.", WIDTH // 2, 200)
    draw_text("Money in emergency funds is completely safe from market fluctuations.", WIDTH // 2, 250)
    draw_text("It earns a small interest of 1% per year.", WIDTH // 2, 300)
    draw_text("Having emergency funds may help you avoid costly loans during crisis.", WIDTH // 2, 350)
    
    # Get investment amount
    investment_amount = get_investment_amount(wealth, "your Emergency Fund")
    if investment_amount == "restart":
        return "restart"
    elif investment_amount == "back":
        return wealth
    
    # Update portfolio and wealth
    portfolio["emergency"]["amount"] += investment_amount
    remaining_wealth = wealth - investment_amount
    
    # Calculate return (3 month period)
    interest_rate = 0.01 / 4  # 1% annual rate for a quarter
    return_amount = investment_amount * (1 + interest_rate)
    
    # Display result
    SCREEN.fill(LIGHT_YELLOW)
    draw_text("Emergency Fund Result", WIDTH // 2, 100, font=title_font)
    
    draw_text("Interest rate: 0.25% (3 months)", WIDTH // 2, 150)
    
    profit = return_amount - investment_amount
    
    draw_text(f"Amount saved: ${investment_amount:.2f}", WIDTH // 2, 200)
    draw_text(f"Value after 3 months: ${return_amount:.2f}", WIDTH // 2, 250)
    draw_text(f"Interest earned: ${profit:.2f}", WIDTH // 2, 300, color=GREEN)
    
    # Continue button
    continue_button = Button(WIDTH // 2 - 100, 400, 200, 50, "Continue", BLUE, LIGHT_BLUE, WHITE)
    continue_button.draw(SCREEN)
    
    # Add navigation buttons
    quit_button, restart_button, back_button = add_navigation_buttons(SCREEN)
    
    pygame.display.update()
    
    # Wait for user to continue
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            continue_button.check_hover(mouse_pos)
            quit_button.check_hover(mouse_pos)
            restart_button.check_hover(mouse_pos)
            back_button.check_hover(mouse_pos)
            
            if continue_button.is_clicked(mouse_pos, event):
                return remaining_wealth + return_amount
            
            # Handle navigation button clicks
            action = handle_navigation(quit_button, restart_button, back_button, mouse_pos, event)
            if action == "restart":
                return "restart"
            elif action == "back":
                return wealth  # Return original wealth if going back
        
        continue_button.draw(SCREEN)
        quit_button.draw(SCREEN)
        restart_button.draw(SCREEN)
        back_button.draw(SCREEN)
        pygame.display.update()
        pygame.time.delay(30)

# Random event simulation
def random_event(wealth):
    SCREEN.fill(LIGHT_CORAL)
    draw_text("RANDOM LIFE EVENT!", WIDTH // 2, 100, font=title_font, color=DARK_RED)
    
    # List of possible events with their financial impacts
    events = [
        {"description": "You got sick and had to pay medical bills.", "impact": -2000},
        {"description": "Your car broke down and needs repairs.", "impact": -1500},
        {"description": "You received a tax refund!", "impact": 1000},
        {"description": "You won a small lottery prize!", "impact": 2000},
        {"description": "A distant relative left you some money in their will.", "impact": 3000},
        {"description": "You had to replace your laptop after it stopped working.", "impact": -800},
        {"description": "Your apartment was flooded and insurance didn't cover everything.", "impact": -3000},
        {"description": "You received a performance bonus at work!", "impact": 1500},
        {"description": "You had unexpected home repairs.", "impact": -1200},
        {"description": "You found $100 in an old jacket!", "impact": 100}
    ]
    
    # Select a random event
    event = random.choice(events)
    
    # Check if user has emergency funds
    has_emergency = portfolio["emergency"]["amount"] > 0
    
    # If the event is negative and there are emergency funds, use them
    modified_impact = event["impact"]
    emergency_used = 0
    
    if event["impact"] < 0 and has_emergency:
        available_emergency = portfolio["emergency"]["amount"]
        if abs(event["impact"]) <= available_emergency:
            emergency_used = abs(event["impact"])
            modified_impact = 0
        else:
            emergency_used = available_emergency
            modified_impact = event["impact"] + available_emergency
    
    # Update emergency fund if used
    if emergency_used > 0:
        portfolio["emergency"]["amount"] -= emergency_used
    
    # Display event information
    draw_text(event["description"], WIDTH // 2, 200, font=title_font)
    
    if event["impact"] < 0:
        impact_color = RED
        impact_text = f"Financial Impact: -${abs(event['impact']):.2f}"
    else:
        impact_color = GREEN
        impact_text = f"Financial Impact: +${event['impact']:.2f}"
    
    draw_text(impact_text, WIDTH // 2, 250, color=impact_color)
    
    if emergency_used > 0:
        draw_text(f"Emergency Fund Used: ${emergency_used:.2f}", WIDTH // 2, 300, color=BLUE)
        draw_text(f"Actual Financial Impact: ${modified_impact:.2f}", WIDTH // 2, 350, color=impact_color if modified_impact != 0 else GREEN)
    
    # Update wealth
    new_wealth = wealth + modified_impact
    
    draw_text(f"Previous Wealth: ${wealth:.2f}", WIDTH // 2, 400)
    draw_text(f"New Wealth: ${new_wealth:.2f}", WIDTH // 2, 450)
    
    # Continue button
    continue_button = Button(WIDTH // 2 - 100, 550, 200, 50, "Continue", BLUE, LIGHT_BLUE, WHITE)
    continue_button.draw(SCREEN)
    
    # Add navigation buttons
    quit_button, restart_button, _ = add_navigation_buttons(SCREEN, show_back=False)
    
    pygame.display.update()
    
    # Wait for user to continue
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            continue_button.check_hover(mouse_pos)
            quit_button.check_hover(mouse_pos)
            restart_button.check_hover(mouse_pos)
            
            if continue_button.is_clicked(mouse_pos, event):
                return new_wealth
            
            # Handle navigation button clicks
            action = handle_navigation(quit_button, restart_button, None, mouse_pos, event)
            if action == "restart":
                return "restart"
        
        continue_button.draw(SCREEN)
        quit_button.draw(SCREEN)
        restart_button.draw(SCREEN)
        pygame.display.update()
        pygame.time.delay(30)

# Portfolio display
def show_portfolio(wealth):
    SCREEN.fill(LIGHT_GREY)
    draw_text("Your Investment Portfolio", WIDTH // 2, 60, font=title_font, color=DARK_BLUE)
    draw_text(f"Current Wealth: ${wealth:.2f}", WIDTH // 2, 100)
    
    # Calculate total invested amount
    total_investment = 0
    for sector, positions in portfolio.items():
        if sector in ["savings", "emergency"]:
            total_investment += positions["amount"]
        else:
            total_investment += positions["long"] + positions["short"]
    
    draw_text(f"Total Invested: ${total_investment:.2f}", WIDTH // 2, 130)
    
    # Display stock investments
    y_pos = 180
    stocks = ["tech", "real_estate", "energy", "biotech"]
    draw_text("Stock Investments:", WIDTH // 2, y_pos, font=title_font)
    y_pos += 40
    
    for stock in stocks:
        stock_name = {
            "tech": "Technology",
            "real_estate": "Real Estate",
            "energy": "Energy",
            "biotech": "Biotech"
        }[stock]
        
        long_amount = portfolio[stock]["long"]
        short_amount = portfolio[stock]["short"]
        
        if long_amount > 0 or short_amount > 0:
            draw_text(f"{stock_name}:", WIDTH // 2 - 200, y_pos, font=main_font, color=DARK_BLUE)
            if long_amount > 0:
                draw_text(f"LONG: ${long_amount:.2f}", WIDTH // 2, y_pos, font=main_font)
            if short_amount > 0:
                draw_text(f"SHORT: ${short_amount:.2f}", WIDTH // 2 + 200, y_pos, font=main_font)
            y_pos += 30
    
    y_pos += 20
    # Display bond investments
    bonds = ["government", "corporate", "municipal", "high_yield"]
    draw_text("Bond Investments:", WIDTH // 2, y_pos, font=title_font)
    y_pos += 40
    
    for bond in bonds:
        bond_name = {
            "government": "Government",
            "corporate": "Corporate",
            "municipal": "Municipal",
            "high_yield": "High-Yield"
        }[bond]
        
        long_amount = portfolio[bond]["long"]
        short_amount = portfolio[bond]["short"]
        
        if long_amount > 0 or short_amount > 0:
            draw_text(f"{bond_name}:", WIDTH // 2 - 200, y_pos, font=main_font, color=DARK_BLUE)
            if long_amount > 0:
                draw_text(f"LONG: ${long_amount:.2f}", WIDTH // 2, y_pos, font=main_font)
            if short_amount > 0:
                draw_text(f"SHORT: ${short_amount:.2f}", WIDTH // 2 + 200, y_pos, font=main_font)
            y_pos += 30
    
    y_pos += 20
    # Display other investments
    draw_text("Other Funds:", WIDTH // 2, y_pos, font=title_font)
    y_pos += 40
    
    savings = portfolio["savings"]["amount"]
    emergency = portfolio["emergency"]["amount"]
    
    if savings > 0:
        draw_text(f"Savings Account: ${savings:.2f}", WIDTH // 2, y_pos, font=main_font)
        y_pos += 30
    
    if emergency > 0:
        draw_text(f"Emergency Fund: ${emergency:.2f}", WIDTH // 2, y_pos, font=main_font)
    
    # Back button
    back_button = Button(WIDTH // 2 - 100, 600, 200, 50, "Back to Main Menu", BLUE, LIGHT_BLUE, WHITE)
    back_button.draw(SCREEN)
    
    # Add navigation buttons
    quit_button, restart_button, _ = add_navigation_buttons(SCREEN, show_back=False)
    
    pygame.display.update()
    
    # Wait for user to continue
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            back_button.check_hover(mouse_pos)
            quit_button.check_hover(mouse_pos)
            restart_button.check_hover(mouse_pos)
            
            if back_button.is_clicked(mouse_pos, event):
                return wealth
            
            # Handle navigation button clicks
            action = handle_navigation(quit_button, restart_button, None, mouse_pos, event)
            if action == "restart":
                return "restart"
        
        back_button.draw(SCREEN)
        quit_button.draw(SCREEN)
        restart_button.draw(SCREEN)
        pygame.display.update()
        pygame.time.delay(30)

# Game over screen
def game_over(wealth, success=False):
    if success:
        SCREEN.fill(LIGHT_GREEN)
        draw_text("CONGRATULATIONS!", WIDTH // 2, 150, font=title_font, color=DARK_GREEN)
        draw_text("You've reached your financial goal of $100,000!", WIDTH // 2, 220, font=title_font)
        draw_text(f"Final Wealth: ${wealth:.2f}", WIDTH // 2, 290, font=title_font)
        message = "You're on your way to financial independence!"
    else:
        SCREEN.fill(LIGHT_CORAL)
        draw_text("GAME OVER", WIDTH // 2, 150, font=title_font, color=DARK_RED)
        draw_text("Unfortunately, you've gone bankrupt!", WIDTH // 2, 220, font=title_font)
        draw_text(f"Final Wealth: ${wealth:.2f}", WIDTH // 2, 290, font=title_font)
        message = "Better luck next time!"
    
    draw_text(message, WIDTH // 2, 360, font=title_font)
    
    # Restart button
    restart_button = Button(WIDTH // 2 - 100, 450, 200, 50, "Restart Game", GREEN, LIGHT_GREEN)
    
    # Quit button
    quit_button = Button(WIDTH // 2 - 100, 520, 200, 50, "Quit Game", RED, LIGHT_CORAL, WHITE)
    
    pygame.display.update()
    
    # Wait for user action
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            restart_button.check_hover(mouse_pos)
            quit_button.check_hover(mouse_pos)
            
            if restart_button.is_clicked(mouse_pos, event):
                return True  # Restart
            elif quit_button.is_clicked(mouse_pos, event):
                pygame.quit()
                sys.exit()
        
        restart_button.draw(SCREEN)
        quit_button.draw(SCREEN)
        pygame.display.update()
        pygame.time.delay(30)

# Main game loop
def main():
    global portfolio, current_news
    
    # Reset game state
    portfolio = {
        "tech": {"long": 0, "short": 0},
        "real_estate": {"long": 0, "short": 0},
        "energy": {"long": 0, "short": 0},
        "biotech": {"long": 0, "short": 0},
        "government": {"long": 0, "short": 0},
        "corporate": {"long": 0, "short": 0},
        "municipal": {"long": 0, "short": 0},
        "high_yield": {"long": 0, "short": 0},
        "savings": {"amount": 0},
        "emergency": {"amount": 0}
    }
    
    current_news = random.choice(market_news)
    
    # Initial wealth
    wealth = 10000
    
    # Show game instructions
    show_instructions()
    
    # Game running flag
    running = True
    turn_counter = 0
    
    while running:
        # Check win/lose conditions
        if wealth >= 100000:
            if game_over(wealth, success=True):
                main()  # Restart game
            else:
                return
        elif wealth <= 0:
            if game_over(wealth, success=False):
                main()  # Restart game
            else:
                return
        
        # Main menu
        SCREEN.fill(LIGHT_BLUE)
        draw_text("Investment Story Game", WIDTH // 2, 60, font=title_font, color=DARK_BLUE)
        draw_text(f"Current Wealth: ${wealth:.2f}", WIDTH // 2, 120, font=title_font)
        draw_text(f"Turn: {turn_counter}", WIDTH // 2, 160)
        
        # Main menu options
        options = [
            "Invest in Stocks",
            "Invest in Bonds",
            "Open a Savings Account",
            "Create Emergency Fund",
            "Check Portfolio",
            "Market Research"
        ]
        
        buttons = []
        for idx, option in enumerate(options):
            y_pos = 220 + idx * 60
            button = Button(WIDTH // 2 - 150, y_pos, 300, 50, option, WHITE, LIGHT_GRAY)
            buttons.append(button)
            button.draw(SCREEN)
        
        # Random event chance (10%)
        random_event_chance = random.random() < 0.1
        if random_event_chance and turn_counter > 0:
            draw_text("Random Life Event Incoming!", WIDTH // 2, 600, color=RED, font=title_font)
        
        # Add navigation buttons
        quit_button, restart_button, _ = add_navigation_buttons(SCREEN, show_back=False)
        
        pygame.display.update()
        
        # Wait for selection
        selection_made = False
        while not selection_made:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                mouse_pos = pygame.mouse.get_pos()
                
                for idx, button in enumerate(buttons):
                    button.check_hover(mouse_pos)
                    if button.is_clicked(mouse_pos, event):
                        selection = options[idx]
                        selection_made = True
                
                quit_button.check_hover(mouse_pos)
                restart_button.check_hover(mouse_pos)
                
                # Handle navigation button clicks
                action = handle_navigation(quit_button, restart_button, None, mouse_pos, event)
                if action == "restart":
                    main()  # Restart game
                    return
            
            # Redraw buttons with hover effects
            for button in buttons:
                button.draw(SCREEN)
            
            quit_button.draw(SCREEN)
            restart_button.draw(SCREEN)
            pygame.display.update()
            pygame.time.delay(30)
        
        # Handle selection
        result = None
        
        if selection == "Invest in Stocks":
            result = stock_market(wealth)
        elif selection == "Invest in Bonds":
            result = bond_market(wealth)
        elif selection == "Open a Savings Account":
            result = savings_account(wealth)
        elif selection == "Create Emergency Fund":
            result = emergency_fund(wealth)
        elif selection == "Check Portfolio":
            result = show_portfolio(wealth)
        elif selection == "Market Research":
            result = market_research(wealth)
            if result is None:
                result = wealth  # No change to wealth
        
        # Handle restart option from sub-menus
        if result == "restart":
            main()
            return
        
        # Update wealth
        if isinstance(result, (int, float)):
            wealth = result
        
        # Trigger random event if rolled
        if random_event_chance and turn_counter > 0:
            result = random_event(wealth)
            if result == "restart":
                main()
                return
            wealth = result
        
        # Increment turn counter for non-informational actions
        if selection not in ["Check Portfolio", "Market Research"]:
            turn_counter += 1

# Start the game
if __name__ == "__main__":
    main()
