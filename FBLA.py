import pygame, random, sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FORTUNE'S PATH: A JOURNEY TO FINANCIAL WISDOM")

# Colors
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
RED, GREEN, BLUE = (255, 0, 0), (0, 255, 0), (0, 0, 255)
LIGHT_BLUE, LIGHT_GREEN = (173, 216, 230), (144, 238, 144)
LIGHT_YELLOW, LIGHT_CORAL = (255, 255, 224), (240, 128, 128)
DARK_GREEN, DARK_BLUE, DARK_RED = (0, 100, 0), (0, 0, 139), (139, 0, 0)
BROWN, GRAY, LIGHT_GRAY = (165, 42, 42), (128, 128, 128), (200, 200, 200)
GOLD, ROYAL_BLUE, DEEP_PURPLE = (255, 215, 0), (65, 105, 225), (72, 61, 139)

# Fonts - even smaller to fit text better in all boxes
main_font = pygame.font.SysFont("Arial", 18)
title_font = pygame.font.SysFont("Arial", 32, bold=True)
subtitle_font = pygame.font.SysFont("Arial", 24, bold=True)
button_font = pygame.font.SysFont("Arial", 16, bold=True)
small_font = pygame.font.SysFont("Arial", 14)

# Draw gradient background
def draw_gradient_background(color1, color2):
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = color1[0] * (1 - ratio) + color2[0] * ratio
        g = color1[1] * (1 - ratio) + color2[1] * ratio
        b = color1[2] * (1 - ratio) + color2[2] * ratio
        pygame.draw.line(SCREEN, (r, g, b), (0, y), (WIDTH, y))

# Button class defines the properties and behaviors of clickable buttons in the game
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=BLACK):
        self.rect = pygame.Rect(x, y, width, height)  # Define the button's rectangular shape (position and size)
        self.text = text  # The text displayed on the button
        self.color = color  # The color of the button in normal state
        self.hover_color = hover_color  # The color when the mouse hovers over the button
        self.text_color = text_color  # Color of the text on the button
        self.is_hovered = False  # This will keep track of whether the button is being hovered over by the mouse
        
    def draw(self, surface):
        # Draw the button with the appropriate color based on hover state
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=10)  # Draw the button with rounded corners
        pygame.draw.rect(surface, BLACK, self.rect, 2, border_radius=10)  # Border for the button
        
        # Render the text on the button and center it within the button
        text_surface = button_font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)  # Display the text on the button
        
    def check_hover(self, pos):
        # Check if the mouse is hovering over the button
        self.is_hovered = self.rect.collidepoint(pos)  # Updates hover status based on mouse position
        return self.is_hovered
        
    def is_clicked(self, pos, event):
        # Check if the button has been clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)  # Returns True if the click happens within the button's area
        return False

# Function to draw text on the screen, used throughout the game for displaying messages
def draw_text(text, x, y, font=main_font, color=BLACK):
    text_surface = font.render(text, True, color)  # Create the text surface with the desired font and color
    text_rect = text_surface.get_rect(center=(x, y))  # Position the text at the specified (x, y) coordinates
    SCREEN.blit(text_surface, text_rect)  # Blit (draw) the text onto the screen

# Display a welcome message when the game starts
def welcome_message():
    # Draw gradient background for a professional look
    draw_gradient_background(ROYAL_BLUE, DEEP_PURPLE)
    
    # Draw decorative header
    pygame.draw.rect(SCREEN, GOLD, (50, 50, WIDTH-100, 70), border_radius=15)
    pygame.draw.rect(SCREEN, BLACK, (50, 50, WIDTH-100, 70), 2, border_radius=15)
    
    # Draw title with shadow effect for better visibility
    title_shadow = title_font.render("FORTUNE'S PATH", True, BLACK)
    title_rect_shadow = title_shadow.get_rect(center=(WIDTH // 2 + 2, 85 + 2))
    SCREEN.blit(title_shadow, title_rect_shadow)
    
    title_surface = title_font.render("FORTUNE'S PATH", True, GOLD)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, 85))
    SCREEN.blit(title_surface, title_rect)
    
    # Create a semi-transparent panel for story text
    panel = pygame.Surface((WIDTH-100, 220), pygame.SRCALPHA)
    panel.fill((255, 255, 255, 180))  # White with 70% opacity
    SCREEN.blit(panel, (50, 150))
    
    # Story introduction text - very concise to fit properly
    draw_text("2030: You inherited $10,000 from a distant relative.", 
              WIDTH // 2, 170, font=main_font, color=BLACK)
    draw_text("Your chance to build wealth for your future.", 
              WIDTH // 2, 200, font=main_font, color=BLACK)
    draw_text("Each investment has risks and rewards.", 
              WIDTH // 2, 230, font=main_font, color=BLACK)
    draw_text("Your path to financial wisdom begins now!", 
              WIDTH // 2, 260, font=main_font, color=BLACK)
    
    # Create a panel for the game objective
    objective_panel = pygame.Surface((WIDTH-100, 100), pygame.SRCALPHA)
    objective_panel.fill((255, 223, 0, 120))  # Gold with opacity
    SCREEN.blit(objective_panel, (50, 380))
    pygame.draw.rect(SCREEN, BLACK, (50, 380, WIDTH-100, 100), 2, border_radius=10)
    
    # Game objective text with warning - shorter text to fit better
    draw_text("YOUR MISSION:", WIDTH // 2, 400, font=subtitle_font, color=DARK_BLUE)
    draw_text("Reach $30,000 to win the game!", 
              WIDTH // 2, 430, font=main_font, color=DARK_GREEN)
    draw_text("Lose all money = GAME OVER!", 
              WIDTH // 2, 460, font=main_font, color=DARK_RED)
    
    # Create start button
    start_button = Button(WIDTH // 2 - 100, 510, 200, 50, "Begin Your Journey", GOLD, LIGHT_YELLOW, BLACK)
    quit_button = Button(WIDTH // 2 - 100, 570, 200, 40, "Quit Game", RED, LIGHT_CORAL, BLACK)
    
    pygame.display.update()  # Update the display to show the message
    
    # Wait for player to click
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            start_button.check_hover(mouse_pos)
            quit_button.check_hover(mouse_pos)
            
            if start_button.is_clicked(mouse_pos, event):
                waiting = False
            elif quit_button.is_clicked(mouse_pos, event):
                pygame.quit()
                sys.exit()
            
            # Redraw buttons to show hover state
            start_button.draw(SCREEN)
            quit_button.draw(SCREEN)
            pygame.display.update()
            pygame.time.delay(30)

# Function to get the player's choice from a list of options
def get_choice(options, prompt="Choose an option:"):
    # Draw a nice gradient background
    draw_gradient_background((240, 248, 255), (176, 224, 230))  # Light blue gradient
    
    # Draw header panel
    pygame.draw.rect(SCREEN, ROYAL_BLUE, (50, 50, WIDTH-100, 70), border_radius=15)
    pygame.draw.rect(SCREEN, BLACK, (50, 50, WIDTH-100, 70), 2, border_radius=15)
    
    # Draw title with shadow effect
    prompt_shadow = subtitle_font.render(prompt, True, BLACK)
    prompt_rect_shadow = prompt_shadow.get_rect(center=(WIDTH // 2 + 2, 85 + 2))
    SCREEN.blit(prompt_shadow, prompt_rect_shadow)
    
    prompt_surface = subtitle_font.render(prompt, True, WHITE)
    prompt_rect = prompt_surface.get_rect(center=(WIDTH // 2, 85))
    SCREEN.blit(prompt_surface, prompt_rect)
    
    # Create semi-transparent panel for choices
    panel = pygame.Surface((WIDTH-100, 350), pygame.SRCALPHA)
    panel.fill((255, 255, 255, 200))  # White with 80% opacity
    SCREEN.blit(panel, (50, 140))
    
    # Add decorative elements
    for i in range(4):
        pygame.draw.circle(SCREEN, GOLD, (50, 140 + i*90), 8)
        pygame.draw.circle(SCREEN, GOLD, (WIDTH-50, 140 + i*90), 8)
    
    buttons = []  # A list to store the button objects that will represent each option
    
    # Draw explanatory text based on options type
    if "Stock Market" in options:
        draw_text("You review your investment options carefully:", WIDTH // 2, 160, font=main_font, color=DARK_BLUE)
    elif "Tech Startup" in options:
        draw_text("With more experience, you consider these opportunities:", WIDTH // 2, 160, font=main_font, color=DARK_BLUE)
    elif "Cryptocurrency" in options:
        draw_text("As your portfolio grows, you look at advanced options:", WIDTH // 2, 160, font=main_font, color=DARK_BLUE)
    elif "Venture Capital" in options:
        draw_text("Your financial advisor presents these alternatives:", WIDTH // 2, 160, font=main_font, color=DARK_BLUE)
    
    # Create styled option buttons
    for idx, option in enumerate(options):
        y_pos = 200 + idx * 60  # Space out each button vertically
        button = Button(WIDTH // 2 - 150, y_pos, 300, 50, option, LIGHT_GRAY, WHITE, DARK_BLUE)  # Create a new button for each option
        buttons.append(button)  # Add the button to the list
        button.draw(SCREEN)  # Draw the button on the screen
    
    # Add quit and restart buttons at the bottom
    quit_button = Button(WIDTH-150, HEIGHT-60, 120, 40, "Quit Game", RED, LIGHT_CORAL, BLACK)
    restart_button = Button(30, HEIGHT-60, 120, 40, "Restart", GREEN, LIGHT_GREEN, BLACK)
    
    quit_button.draw(SCREEN)
    restart_button.draw(SCREEN)
    
    pygame.display.update()  # Update the display to show the buttons
    
    # Loop to wait for the player to make a choice
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Exit the game if the player closes the window
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()  # Get the current mouse position on the screen
            
            # Check option buttons
            for idx, button in enumerate(buttons):
                button.check_hover(mouse_pos)  # Check if the mouse is hovering over any button
                if button.is_clicked(mouse_pos, event):  # Check if a button is clicked
                    return options[idx]  # Return the option associated with the clicked button
            
            # Check quit and restart buttons
            quit_button.check_hover(mouse_pos)
            restart_button.check_hover(mouse_pos)
            
            if quit_button.is_clicked(mouse_pos, event):
                pygame.quit()
                sys.exit()
            elif restart_button.is_clicked(mouse_pos, event):
                return "RESTART"  # Special return value to indicate restart
        
        # Redraw buttons with hover effects
        for button in buttons:
            button.draw(SCREEN)
        
        quit_button.draw(SCREEN)
        restart_button.draw(SCREEN)
        
        pygame.display.update()  # Update the display to reflect any changes
        pygame.time.delay(30)  # Small delay to prevent high CPU usage

# This function simulates the player's journey and their investments
def journey_progress(wealth, investment_history, journey_round=1):
    # Draw gradient background based on journey round
    gradient_colors = [
        ((173, 216, 230), (240, 255, 240)),  # Round 1: Light blue to green
        ((240, 255, 240), (255, 250, 205)),  # Round 2: Light green to yellow
        ((255, 250, 205), (230, 230, 250)),  # Round 3: Light yellow to lavender
        ((230, 230, 250), (255, 228, 225))   # Round 4+: Lavender to rose
    ]
    color_index = min(journey_round-1, 3)
    draw_gradient_background(*gradient_colors[color_index])
    
    # Draw header and title
    pygame.draw.rect(SCREEN, ROYAL_BLUE, (50, 30, WIDTH-100, 70), border_radius=15)
    pygame.draw.rect(SCREEN, BLACK, (50, 30, WIDTH-100, 70), 2, border_radius=15)
    
    # Chapter titles
    titles = ["Chapter 1: First Steps", "Chapter 2: Growing Knowledge", 
              "Chapter 3: Expanding Horizons", "Chapter 4: Mastering the Market", 
              "Chapter 5: Financial Freedom"]
    title = titles[min(journey_round-1, 4)]
    
    # Draw title with shadow
    draw_text(title, WIDTH//2+2, 65+2, subtitle_font, BLACK)  # Shadow
    draw_text(title, WIDTH//2, 65, subtitle_font, WHITE)      # Text
    
    # Wealth display panel with color based on performance
    panel_color = (144, 238, 144, 220) if wealth > 10000 else \
                 (255, 182, 193, 220) if wealth < 10000 else (255, 255, 255, 220)
    
    wealth_panel = pygame.Surface((300, 60), pygame.SRCALPHA)
    wealth_panel.fill(panel_color)
    SCREEN.blit(wealth_panel, (WIDTH//2 - 150, 120))
    pygame.draw.rect(SCREEN, BLACK, (WIDTH//2 - 150, 120, 300, 60), 2, border_radius=10)
    
    # Gold coins decoration
    for x_offset in [25, 275]:
        pygame.draw.circle(SCREEN, GOLD, (WIDTH//2 - 150 + x_offset, 150), 15)
        pygame.draw.circle(SCREEN, BLACK, (WIDTH//2 - 150 + x_offset, 150), 15, 1)
    
    # Display wealth amount
    wealth_color = DARK_GREEN if wealth > 10000 else DARK_RED if wealth < 10000 else BLACK
    draw_text(f"Current Wealth: ${wealth:.2f}", WIDTH//2+1, 150+1, main_font, BLACK)  # Shadow
    draw_text(f"Current Wealth: ${wealth:.2f}", WIDTH//2, 150, main_font, wealth_color)
    
    # Story narrative panel
    story_panel = pygame.Surface((WIDTH-200, 80), pygame.SRCALPHA)
    story_panel.fill((255, 255, 255, 180))
    SCREEN.blit(story_panel, (100, 200))
    
    # Shorter narratives that fit better in the UI
    if journey_round == 1:
        story = "Your advisor suggests these beginner options:"
    elif journey_round == 2:
        if wealth > 12000:
            story = "Success! New investment possibilities await."
        elif wealth < 8000:
            story = "Setback, but you're determined to recover."
        else:
            story = "Time to explore new opportunities."
    elif journey_round == 3:
        story = "Your growing wealth attracts attention." if wealth > 15000 else \
               "Seek diverse investments to grow your portfolio."
    else:
        if wealth > 20000:
            story = "Your investment skills are becoming legendary!"
        elif wealth > 10000:
            story = "Your balanced approach is paying off."
        else:
            story = "Despite challenges, you press forward."
    
    draw_text(story, WIDTH//2, 240, main_font, DARK_BLUE)
    
    # Create buttons
    quit_button = Button(WIDTH-150, HEIGHT-60, 120, 40, "Quit Game", RED, LIGHT_CORAL, BLACK)
    restart_button = Button(30, HEIGHT-60, 120, 40, "Restart", GREEN, LIGHT_GREEN, BLACK)
    continue_button = Button(WIDTH//2-100, HEIGHT-100, 200, 50, "Continue Journey", LIGHT_BLUE, ROYAL_BLUE, WHITE)
    
    for button in [quit_button, restart_button, continue_button]:
        button.draw(SCREEN)
    
    pygame.display.update()
    
    # Wait for player decision
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            for button in [continue_button, quit_button, restart_button]:
                button.check_hover(mouse_pos)
                
            if continue_button.is_clicked(mouse_pos, event):
                waiting = False
            elif quit_button.is_clicked(mouse_pos, event):
                pygame.quit()
                sys.exit()
            elif restart_button.is_clicked(mouse_pos, event):
                return -999999  # Special code to signal restart
            
            for button in [continue_button, quit_button, restart_button]:
                button.draw(SCREEN)
            pygame.display.update()
            pygame.time.delay(30)

    # Present the player with investment options based on the round
    if journey_round == 1:
        # First round - basic investment options
        options = ["Stock Market", "Bond Market", "Real Estate", "Savings Fund"]
        choice = get_choice(options, "Where will you begin your investment journey?")
        
        # Investment details with shorter descriptions
        investment_details = {
            "Stock Market": ("Risky but potentially rewarding. High returns or losses.", 
                             random.randint(-5, 25)),
            "Bond Market": ("Low risk, steady but modest growth.", 
                            random.randint(3, 8)),
            "Real Estate": ("Medium risk, property values fluctuate.", 
                            random.randint(0, 15)),
            "Savings Fund": ("Very safe but slow growth.", 
                             random.randint(1, 5))
        }
    
    elif journey_round == 2:
        # Second round - intermediate investment options
        options = ["Tech Startup", "Government Bonds", "Rental Property", "Index Fund"]
        choice = get_choice(options, "Where will you invest next?")
        
        investment_details = {
            "Tech Startup": ("High risk with big potential. Many startups fail.", 
                             random.randint(-20, 50)),
            "Government Bonds": ("Very low risk, guaranteed modest returns.", 
                                 random.randint(2, 6)),
            "Rental Property": ("Steady income plus property growth.", 
                                random.randint(5, 15)),
            "Index Fund": ("Diversified market investment.", 
                          random.randint(-2, 18))
        }
    
    elif journey_round == 3:
        # Third round - advanced investment options
        options = ["Cryptocurrency", "Foreign Markets", "Gold & Precious Metals", "Peer-to-Peer Lending"]
        choice = get_choice(options, "Time for a more advanced investment strategy!")
        
        investment_details = {
            "Cryptocurrency": ("Extremely volatile. Big gains or losses.", 
                               random.randint(-40, 80)),
            "Foreign Markets": ("International diversity for your portfolio.", 
                                random.randint(-10, 25)),
            "Gold & Precious Metals": ("Safe haven during economic uncertainty.", 
                                       random.randint(-5, 15)),
            "Peer-to-Peer Lending": ("Direct loans for interest income.", 
                                     random.randint(0, 20))
        }
    
    else:
        # Later rounds - mix of different options
        options = ["Venture Capital", "ETFs", "Municipal Bonds", "Dividend Stocks"]
        choice = get_choice(options, "Choose your next investment wisely!")
        
        investment_details = {
            "Venture Capital": ("Funding early-stage companies with potential.", 
                                random.randint(-30, 60)),
            "ETFs": ("Diversified funds tracking market indexes.", 
                     random.randint(-5, 20)),
            "Municipal Bonds": ("Government securities with tax benefits.", 
                                random.randint(2, 7)),
            "Dividend Stocks": ("Companies that share profits regularly.", 
                                random.randint(0, 15))
        }
    
    description, growth = investment_details[choice]  # Get the description and growth rate for the chosen investment
    
    # Display the chosen investment and explain its characteristics
    SCREEN.fill(LIGHT_YELLOW)  # Change the background to a lighter color to show the result
    draw_text(f"You chose: {choice}", WIDTH // 2, 100, font=title_font, color=DARK_BLUE)
    
    # Split long descriptions into multiple lines
    words = description.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line + " " + word) > 50:  # Limit line length
            lines.append(current_line)
            current_line = word
        else:
            current_line += " " + word if current_line else word
    
    if current_line:
        lines.append(current_line)
    
    # Display each line of the description
    for i, line in enumerate(lines):
        draw_text(line, WIDTH // 2, 150 + (i * 30))
    
    y_offset = 150 + (len(lines) * 30) + 20
    
    # Draw the investment growth/loss
    if growth > 0:
        draw_text(f"Your investment grew by {growth}%!", WIDTH // 2, y_offset, color=DARK_GREEN)
    elif growth == 0:
        draw_text("Your investment broke even - no gain or loss.", WIDTH // 2, y_offset, color=BROWN)
    else:
        draw_text(f"Your investment decreased by {abs(growth)}%!", WIDTH // 2, y_offset, color=DARK_RED)
    
    # Calculate and display new wealth
    old_wealth = wealth
    wealth += wealth * (growth / 100)
    
    draw_text(f"Previous wealth: ${old_wealth:.2f}", WIDTH // 2, y_offset + 40)
    draw_text(f"New wealth: ${wealth:.2f}", WIDTH // 2, y_offset + 70, 
              color=DARK_GREEN if wealth > old_wealth else DARK_RED if wealth < old_wealth else BLACK)
    
    # Add a market event that might affect the investment
    market_events = [
        ("Economic recession hits! Market values decline.", -10),
        ("New technology breakthrough boosts the economy!", 15),
        ("Interest rates rise, affecting investment returns.", -5),
        ("Government stimulus package helps the economy.", 8),
        ("Inflation increases, affecting purchasing power.", -8),
        ("Tax cuts benefit businesses and investors.", 12),
        ("Global trade tensions affect markets.", -7),
        ("Strong jobs report improves economic outlook.", 6)
    ]
    
    # 30% chance of a market event occurring
    if random.random() < 0.3:
        event, impact = random.choice(market_events)
        draw_text("BREAKING NEWS:", WIDTH // 2, y_offset + 110, color=RED)
        draw_text(event, WIDTH // 2, y_offset + 140)
        
        old_wealth = wealth
        wealth += wealth * (impact / 100)
        
        draw_text(f"Impact on your wealth: {impact}%", WIDTH // 2, y_offset + 170, 
                 color=DARK_GREEN if impact > 0 else DARK_RED)
        draw_text(f"Updated wealth: ${wealth:.2f}", WIDTH // 2, y_offset + 200, 
                 color=DARK_GREEN if wealth > old_wealth else DARK_RED)
        
        # Add this event to the investment history
        investment_history.append(f"Market Event: {event} - Impact: {impact}%")
    
    # Continue button
    continue_button = Button(WIDTH // 2 - 100, HEIGHT - 80, 200, 50, "Continue", LIGHT_GREEN, GREEN)
    continue_button.draw(SCREEN)
    
    pygame.display.update()
    
    # Wait for the player to continue
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            continue_button.check_hover(mouse_pos)
            
            if continue_button.is_clicked(mouse_pos, event):
                waiting = False
            
            continue_button.draw(SCREEN)
            pygame.display.update()
            pygame.time.delay(30)
    
    # Record this investment in the history
    # We need to check if there was a market event that added an impact
    market_impact = 0
    # Since we've already used the variable name in the market event section,
    # we're using a different name here to avoid any confusion
    if random.random() < 0.3:  # This matches the probability in the market event section
        _, market_impact = random.choice(market_events)
    
    total_growth = growth + market_impact
    investment_history.append(f"Round {journey_round}: {choice} - Growth: {total_growth}%")
    
    return wealth

# Function to provide investment tips and educational content
def show_investment_tips():
    tips = [
        "Diversification: Don't put all your eggs in one basket.",
        "Higher returns come with higher risks.",
        "Long-term investments often beat short-term trades.",
        "Compound interest is the eighth wonder of the world.",
        "Research before investing - knowledge reduces risk.",
        "Regular investing beats market timing.",
        "Know your risk tolerance before investing.",
        "Keep emergency funds in liquid, safe accounts.",
        "Consider tax implications of investments.",
        "Reinvest dividends to accelerate growth."
    ]
    
    quotes = [
        "The best investment you can make is in yourself. - Warren Buffett",
        "Be fearful when others are greedy. - Warren Buffett",
        "Money is a terrible master but an excellent servant. - P.T. Barnum",
        "Financial freedom is for those who learn and work for it. - Kiyosaki",
        "Know the value, not just the price. - Philip Fisher"
    ]
    
    # Setup screen
    draw_gradient_background((230, 230, 250), (240, 255, 255))
    
    # Draw header with title
    pygame.draw.rect(SCREEN, ROYAL_BLUE, (50, 30, WIDTH-100, 70), border_radius=15)
    pygame.draw.rect(SCREEN, BLACK, (50, 30, WIDTH-100, 70), 2, border_radius=15)
    draw_text("Financial Wisdom", WIDTH//2+2, 65+2, title_font, BLACK)  # Shadow
    draw_text("Financial Wisdom", WIDTH//2, 65, title_font, GOLD)
    
    # Create book decoration
    pygame.draw.rect(SCREEN, BROWN, (WIDTH//2-175, 110, 350, 40), border_radius=5)
    pygame.draw.rect(SCREEN, LIGHT_YELLOW, (WIDTH//2-175, 150, 350, 300))
    pygame.draw.rect(SCREEN, BLACK, (WIDTH//2-175, 110, 350, 340), 2)
    draw_text("Investment Guide", WIDTH//2, 130, subtitle_font, GOLD)
    
    # Display 3 random tips
    selected_tips = random.sample(tips, 3)
    for i, tip in enumerate(selected_tips):
        # Tip box
        pygame.draw.rect(SCREEN, WHITE, (WIDTH//2-160, 170+(i*90), 320, 70), border_radius=10)
        pygame.draw.rect(SCREEN, BLACK, (WIDTH//2-160, 170+(i*90), 320, 70), 1, border_radius=10)
        
        # Star bullet
        star_x, star_y = WIDTH//2-150, 205+(i*90)
        pygame.draw.polygon(SCREEN, GOLD, [
            (star_x, star_y), 
            (star_x+5, star_y-10), 
            (star_x+10, star_y), 
            (star_x+5, star_y+10)
        ])
        
        # Handle text wrapping
        words = tip.split()
        if len(words) > 7:  # Reduce max words per line
            first_line = " ".join(words[:7])
            second_line = " ".join(words[7:])
            draw_text(first_line, WIDTH//2-10, 185+(i*90), main_font, DARK_BLUE)
            draw_text(second_line, WIDTH//2-10, 215+(i*90), main_font, DARK_BLUE)
        else:
            draw_text(tip, WIDTH//2-10, 205+(i*90), main_font, DARK_BLUE)
    
    # Motivational quote
    draw_text(random.choice(quotes), WIDTH//2, HEIGHT-130, small_font, DARK_BLUE)
    
    # Buttons
    buttons = {
        "continue": Button(WIDTH//2-100, HEIGHT-80, 200, 50, "Continue Journey", LIGHT_BLUE, ROYAL_BLUE, WHITE),
        "quit": Button(WIDTH-150, HEIGHT-60, 120, 40, "Quit Game", RED, LIGHT_CORAL, BLACK),
        "restart": Button(30, HEIGHT-60, 120, 40, "Restart", GREEN, LIGHT_GREEN, BLACK)
    }
    
    for button in buttons.values():
        button.draw(SCREEN)
    
    pygame.display.update()
    
    # Wait for player action
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            for button_name, button in buttons.items():
                button.check_hover(mouse_pos)
                if button.is_clicked(mouse_pos, event):
                    if button_name == "continue":
                        waiting = False
                    elif button_name == "quit":
                        pygame.quit()
                        sys.exit()
                    elif button_name == "restart":
                        return "RESTART"
            
            for button in buttons.values():
                button.draw(SCREEN)
            pygame.display.update()
            pygame.time.delay(30)
            
    return "CONTINUE"

# Function to show decision screen and handle player choices
def show_decision_screen(wealth, journey_round):
    # Setup screen
    draw_gradient_background((255, 250, 205), (255, 228, 225))
    
    # Draw header with title
    pygame.draw.rect(SCREEN, ROYAL_BLUE, (50, 30, WIDTH-100, 70), border_radius=15)
    pygame.draw.rect(SCREEN, BLACK, (50, 30, WIDTH-100, 70), 2, border_radius=15)
    draw_text("Decision Point", WIDTH//2+2, 65+2, subtitle_font, BLACK)  # Shadow
    draw_text("Decision Point", WIDTH//2, 65, subtitle_font, WHITE)
    
    # Wealth display with color based on performance
    panel_color = (144, 238, 144, 220) if wealth > 10000 else \
                 (255, 182, 193, 220) if wealth < 10000 else (255, 255, 255, 220)
    
    wealth_panel = pygame.Surface((300, 60), pygame.SRCALPHA)
    wealth_panel.fill(panel_color)
    SCREEN.blit(wealth_panel, (WIDTH//2-150, 120))
    pygame.draw.rect(SCREEN, BLACK, (WIDTH//2-150, 120, 300, 60), 2, border_radius=10)
    
    # Add coin decorations
    for x_offset in [25, 275]:
        pygame.draw.circle(SCREEN, GOLD, (WIDTH//2-150+x_offset, 150), 15)
        pygame.draw.circle(SCREEN, BLACK, (WIDTH//2-150+x_offset, 150), 15, 1)
    
    # Display wealth amount
    wealth_color = DARK_GREEN if wealth > 10000 else DARK_RED if wealth < 10000 else BLACK
    draw_text(f"Current Wealth: ${wealth:.2f}", WIDTH//2+1, 150+1, main_font, BLACK)  # Shadow
    draw_text(f"Current Wealth: ${wealth:.2f}", WIDTH//2, 150, main_font, wealth_color)
    
    # Narrative panel
    story_panel = pygame.Surface((WIDTH-100, 120), pygame.SRCALPHA)
    story_panel.fill((255, 255, 255, 180))
    SCREEN.blit(story_panel, (50, 200))
    
    # Shorter narratives for decision screen
    if wealth > 20000:
        narrative = "Remarkable success! Financial experts are taking notice."
        narrative2 = "Continue growing your fortune or secure what you've earned?"
    elif wealth > 12000:
        narrative = "Wise choices! Your portfolio is growing steadily."
        narrative2 = "Continue investing or take your profits now?"
    elif wealth > 8000:
        narrative = "Ups and downs, but you're still in the game."
        narrative2 = "Keep investing or stop here with what you have?"
    else:
        narrative = "Challenging market. Sometimes persistence is key."
        narrative2 = "Push forward or secure what remains of your capital?"
    
    draw_text(narrative, WIDTH//2, 230, main_font, DARK_BLUE)
    draw_text(narrative2, WIDTH//2, 270, main_font, DARK_BLUE)
    
    # Decorative elements
    for i in range(2):
        pygame.draw.circle(SCREEN, GOLD, (70, 230+i*40), 5)
        pygame.draw.circle(SCREEN, GOLD, (WIDTH-70, 230+i*40), 5)
    
    # Create buttons
    buttons = {
        "continue": Button(WIDTH//4-120, 350, 240, 60, "Continue Journey", LIGHT_GREEN, GREEN, DARK_GREEN),
        "stop": Button(3*WIDTH//4-120, 350, 240, 60, "Secure Wealth & Exit", LIGHT_CORAL, RED, DARK_RED),
        "quit": Button(WIDTH-150, HEIGHT-60, 120, 40, "Quit Game", RED, LIGHT_CORAL, BLACK),
        "restart": Button(30, HEIGHT-60, 120, 40, "Restart", GREEN, LIGHT_GREEN, BLACK)
    }
    
    for button in buttons.values():
        button.draw(SCREEN)
    
    pygame.display.update()
    
    # Handle player decision
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            for button_name, button in buttons.items():
                button.check_hover(mouse_pos)
                if button.is_clicked(mouse_pos, event):
                    return button_name
            
            for button in buttons.values():
                button.draw(SCREEN)
            pygame.display.update()
            pygame.time.delay(30)

# Game over screen when player loses all money
def show_game_over():
    # Dramatic red-to-black gradient
    draw_gradient_background((180, 0, 0), (0, 0, 0))
    
    # Header
    pygame.draw.rect(SCREEN, DARK_RED, (50, 80, WIDTH-100, 70), border_radius=15)
    pygame.draw.rect(SCREEN, BLACK, (50, 80, WIDTH-100, 70), 2, border_radius=15)
    
    # Title with shadow
    draw_text("FINANCIAL RUIN!", WIDTH//2+3, 115+3, title_font, BLACK)  # Shadow
    draw_text("FINANCIAL RUIN!", WIDTH//2, 115, title_font, RED)
    
    # Message panel
    panel = pygame.Surface((WIDTH-100, 200), pygame.SRCALPHA)
    panel.fill((0, 0, 0, 180))
    SCREEN.blit(panel, (50, 200))
    
    # Shorter dramatic message
    draw_text("You've lost everything!", 
             WIDTH//2, 250, subtitle_font, RED)
    draw_text("Your financial journey ends in disaster.", 
             WIDTH//2, 290, main_font, LIGHT_CORAL)
    draw_text("In finance, there are no second chances.", 
             WIDTH//2, 330, main_font, LIGHT_CORAL)
    
    # Buttons
    restart_button = Button(WIDTH//2-200, 420, 180, 50, "Try Again", GREEN, LIGHT_GREEN)
    quit_button = Button(WIDTH//2+20, 420, 180, 50, "Give Up", RED, LIGHT_CORAL)
    
    restart_button.draw(SCREEN)
    quit_button.draw(SCREEN)
    pygame.display.update()
    
    # Wait for decision
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
                pygame.quit()
                sys.exit()
            
            restart_button.draw(SCREEN)
            quit_button.draw(SCREEN)
            pygame.display.update()

# Main function where the game starts and runs
def main():
    welcome_message()
    
    # Main game loop for multiple playthroughs
    while True:
        wealth = 10000
        investment_history = []
        journey_round = 1
        
        # Show tips before starting
        show_investment_tips()
        
        # First investment round
        wealth = journey_progress(wealth, investment_history, journey_round)
        
        # Main game loop
        continue_journey = True
        while continue_journey:
            journey_round += 1
            
            # Occasionally show tips (20% chance)
            if random.random() < 0.2:
                show_investment_tips()
            
            # Show decision screen
            decision = show_decision_screen(wealth, journey_round)
            
            if decision == "continue":
                wealth = journey_progress(wealth, investment_history, journey_round)
                # Check for bankruptcy
                if wealth <= 0:
                    show_game_over()
                    continue_journey = False
            elif decision == "stop":
                continue_journey = False
            elif decision == "restart":
                continue_journey = False
                journey_round = 0
                wealth = 10000
                investment_history = []
            elif decision == "quit":
                pygame.quit()
                sys.exit()
        
        # End of the game: Show the final wealth and the player's investment history
        # Draw a gradient background based on performance
        if wealth >= 20000:
            # Success - gold to light green gradient
            draw_gradient_background((255, 223, 0), (144, 238, 144))
        elif wealth > 10000:
            # Positive - light blue to light green
            draw_gradient_background((173, 216, 230), (144, 238, 144))
        elif wealth > 5000:
            # Neutral - light yellow to white
            draw_gradient_background((255, 255, 224), (255, 255, 255))
        else:
            # Loss - light coral to white
            draw_gradient_background((240, 128, 128), (255, 255, 255))
        
        # Draw decorative header
        pygame.draw.rect(SCREEN, ROYAL_BLUE, (50, 30, WIDTH-100, 70), border_radius=15)
        pygame.draw.rect(SCREEN, BLACK, (50, 30, WIDTH-100, 70), 2, border_radius=15)
        
        # Draw title with shadow effect
        title_shadow = title_font.render("Journey Complete", True, BLACK)
        title_rect_shadow = title_shadow.get_rect(center=(WIDTH // 2 + 2, 65 + 2))
        SCREEN.blit(title_shadow, title_rect_shadow)
        
        title_surface = title_font.render("Journey Complete", True, GOLD)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, 65))
        SCREEN.blit(title_surface, title_rect)
        
        # Shorter messages based on performance
        if wealth >= 30000:
            message = "Tripled your investment! Amazing!"
            color = DARK_GREEN
            story = "Your financial skills are legendary! Future Wall Street star?"
        elif wealth >= 20000:
            message = "Doubled your investment! Great job!"
            color = DARK_GREEN
            story = "Shrewd decisions have paid off. A financial prodigy!"
        elif wealth > 10000:
            message = "Investment profit! Good job!"
            color = DARK_BLUE
            story = "Careful investing yielded positive returns."
        elif wealth == 10000:
            message = "Broke even - no gain or loss."
            color = BLUE
            story = "Played it safe and protected your capital."
        elif wealth > 5000:
            message = "Lost some money, but kept most."
            color = BROWN
            story = "Challenging markets, but preserved capital well."
        elif wealth > 0:
            message = "Significant investment losses."
            color = DARK_RED
            story = "Investing carries risks. Better luck next time!"
        else:
            message = "Lost all investment capital."
            color = DARK_RED
            story = "Market was brutal. Every loss teaches a lesson!"
        
        # Draw wealth amount with decorative elements
        wealth_panel = pygame.Surface((350, 70), pygame.SRCALPHA)
        if wealth > 10000:
            wealth_panel.fill((144, 238, 144, 220))  # Light green with opacity
        elif wealth < 10000:
            wealth_panel.fill((255, 182, 193, 220))  # Light pink with opacity
        else:
            wealth_panel.fill((255, 255, 255, 220))  # White with opacity
        
        SCREEN.blit(wealth_panel, (WIDTH//2 - 175, 110))
        pygame.draw.rect(SCREEN, BLACK, (WIDTH//2 - 175, 110, 350, 70), 2, border_radius=10)
        
        # Add gold coins decoration
        pygame.draw.circle(SCREEN, GOLD, (WIDTH//2 - 175 + 25, 110 + 35), 20)
        pygame.draw.circle(SCREEN, BLACK, (WIDTH//2 - 175 + 25, 110 + 35), 20, 1)
        pygame.draw.circle(SCREEN, GOLD, (WIDTH//2 + 175 - 25, 110 + 35), 20)
        pygame.draw.circle(SCREEN, BLACK, (WIDTH//2 + 175 - 25, 110 + 35), 20, 1)
        
        # Draw wealth with shadow
        wealth_text = f"Final Wealth: ${wealth:.2f}"
        draw_text(wealth_text, WIDTH // 2, 145, font=subtitle_font, color=color)
        
        # Create a panel for the performance message
        message_panel = pygame.Surface((WIDTH-150, 50), pygame.SRCALPHA)
        message_panel.fill((255, 255, 255, 180))  # White with opacity
        SCREEN.blit(message_panel, (75, 190))
        
        # Draw performance message and story
        draw_text(message, WIDTH // 2, 215, font=main_font, color=color)
        draw_text(story, WIDTH // 2, 245, font=main_font, color=DARK_BLUE)
        
        # Create a scroll for investment history
        history_panel = pygame.Surface((WIDTH-200, 180), pygame.SRCALPHA)
        history_panel.fill((255, 255, 255, 180))  # White with opacity
        SCREEN.blit(history_panel, (100, 270))
        
        # Add decorative elements to history panel
        pygame.draw.rect(SCREEN, BROWN, (100, 270, WIDTH-200, 30), border_radius=5)  # Top bar
        pygame.draw.rect(SCREEN, BLACK, (100, 270, WIDTH-200, 180), 2, border_radius=10)  # Border
        
        # Draw history title
        history_title = subtitle_font.render("Investment History", True, WHITE)
        history_title_rect = history_title.get_rect(center=(WIDTH // 2, 285))
        SCREEN.blit(history_title, history_title_rect)
        
        # Show each investment decision the player made
        y_offset = 320
        for i, investment in enumerate(investment_history):
            # Alternate row colors for better readability
            if i % 2 == 0:
                row_panel = pygame.Surface((WIDTH-220, 25), pygame.SRCALPHA)
                row_panel.fill((240, 240, 240, 150))  # Light gray with opacity
                SCREEN.blit(row_panel, (110, y_offset - 10))
            
            draw_text(investment, WIDTH // 2, y_offset, font=small_font, color=BLACK)
            y_offset += 25
            
            # If we're running out of space, stop listing investments
            if y_offset > 430:
                draw_text("... and more decisions", WIDTH // 2, y_offset, font=small_font, color=GRAY)
                break
        
        # Create a panel for the final message
        final_panel = pygame.Surface((WIDTH-100, 60), pygame.SRCALPHA)
        final_panel.fill((230, 230, 250, 200))  # Lavender with opacity
        SCREEN.blit(final_panel, (50, HEIGHT - 130))
        
        # Draw final message with decorative elements
        draw_text("Thank you for playing! Would you like to start a new journey?", 
                 WIDTH // 2, HEIGHT - 110, font=main_font, color=DARK_BLUE)
        
        # Add decorative stars
        for i in range(5):
            x_pos = 100 + i * (WIDTH - 200) / 4
            pygame.draw.polygon(SCREEN, GOLD, [
                (x_pos, HEIGHT - 85),  # Top
                (x_pos + 5, HEIGHT - 75),  # Right
                (x_pos, HEIGHT - 65),  # Bottom
                (x_pos - 5, HEIGHT - 75)   # Left
            ])
        
        # Buttons for restarting or quitting
        restart_button = Button(WIDTH // 4 - 100, HEIGHT - 60, 200, 50, "New Journey", GREEN, LIGHT_GREEN, DARK_GREEN)
        quit_button = Button(3 * WIDTH // 4 - 100, HEIGHT - 60, 200, 50, "Exit Game", RED, LIGHT_CORAL, DARK_RED)
        
        restart_button.draw(SCREEN)  # Draw the restart button
        quit_button.draw(SCREEN)  # Draw the quit button
        
        pygame.display.update()  # Update the screen with the final options
        
        # Wait for the player's final decision
        waiting_for_decision = True
        while waiting_for_decision:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                mouse_pos = pygame.mouse.get_pos()  # Get mouse position
                
                # Check for clicks on the restart or quit buttons
                restart_button.check_hover(mouse_pos)
                quit_button.check_hover(mouse_pos)
                
                if restart_button.is_clicked(mouse_pos, event):
                    waiting_for_decision = False  # Continue to a new game
                    break
                elif quit_button.is_clicked(mouse_pos, event):
                    pygame.quit()  # Exit the game
                    sys.exit()
                
                # Redraw buttons with updated hover states
                restart_button.draw(SCREEN)
                quit_button.draw(SCREEN)
                pygame.display.update()
                pygame.time.delay(30)

# Entry point of the program
if __name__ == "__main__":
    main()  # Start the game
