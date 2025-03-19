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

# Fonts - smaller sizes for better text fitting
main_font = pygame.font.SysFont("Arial", 16)
title_font = pygame.font.SysFont("Arial", 28, bold=True)
subtitle_font = pygame.font.SysFont("Arial", 20, bold=True)
button_font = pygame.font.SysFont("Arial", 14, bold=True)
small_font = pygame.font.SysFont("Arial", 12)

# Helper functions to reduce redundancy

# Draw gradient background
def draw_gradient_background(color1, color2):
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = color1[0] * (1 - ratio) + color2[0] * ratio
        g = color1[1] * (1 - ratio) + color2[1] * ratio
        b = color1[2] * (1 - ratio) + color2[2] * ratio
        pygame.draw.line(SCREEN, (r, g, b), (0, y), (WIDTH, y))

# Draw header with title and optional shadow
def draw_header(title, title_color=WHITE, background_color=ROYAL_BLUE, y_pos=50, font=subtitle_font, shadow=True):
    # Draw header panel
    pygame.draw.rect(SCREEN, background_color, (50, y_pos, WIDTH-100, 70), border_radius=15)
    pygame.draw.rect(SCREEN, BLACK, (50, y_pos, WIDTH-100, 70), 2, border_radius=15)
    
    # Draw title, optionally with shadow
    if shadow:
        draw_text(title, WIDTH//2+2, y_pos+35+2, font, BLACK)  # Shadow
    draw_text(title, WIDTH//2, y_pos+35, font, title_color)

# Create a panel with optional transparency
def create_panel(width, height, x, y, color=(255, 255, 255), alpha=200, border=False, border_radius=10, border_color=BLACK):
    panel = pygame.Surface((width, height), pygame.SRCALPHA)
    
    # Handle both RGB and RGBA color formats
    if len(color) == 3:
        panel.fill((color[0], color[1], color[2], alpha))
    else:
        panel.fill(color)  # Assume RGBA format already
        
    SCREEN.blit(panel, (x, y))
    if border:
        pygame.draw.rect(SCREEN, border_color, (x, y, width, height), 2, border_radius=border_radius)
        
# Display wealth with appropriate colors
def display_wealth(wealth, x, y, show_shadow=True):
    panel_color = (144, 238, 144, 220) if wealth > 10000 else \
                 (255, 182, 193, 220) if wealth < 10000 else (255, 255, 255, 220)
    
    create_panel(300, 60, x-150, y, color=panel_color[:3], alpha=panel_color[3], border=True)
    
    # Add coin decorations
    for x_offset in [25, 275]:
        pygame.draw.circle(SCREEN, GOLD, (x-150+x_offset, y+30), 15)
        pygame.draw.circle(SCREEN, BLACK, (x-150+x_offset, y+30), 15, 1)
    
    # Display wealth with appropriate color
    wealth_color = DARK_GREEN if wealth > 10000 else DARK_RED if wealth < 10000 else BLACK
    if show_shadow:
        draw_text(f"Current Wealth: ${wealth:.2f}", x+1, y+30+1, main_font, BLACK)  # Shadow
    draw_text(f"Current Wealth: ${wealth:.2f}", x, y+30, main_font, wealth_color)

# Function to display detailed market research to help with skill-based decisions
def show_market_research(options):
    # Create attractive background for the research screen
    draw_gradient_background((50, 50, 80), (30, 30, 60))
    
    # Draw header with professional look
    draw_header("Advanced Market Research", WHITE, (70, 130, 180), 30, font=subtitle_font)
    
    # Create main research panel
    create_panel(WIDTH-60, HEIGHT-120, 30, 90, color=(240, 240, 250), alpha=230, border=True)
    
    # Market research title
    draw_text("ASSET CLASS ANALYSIS AND MARKET PREDICTIONS", WIDTH//2, 120, subtitle_font, DARK_BLUE)
    
    # Market trend indicators - these will influence investment outcomes
    market_trends = {
        "Stock Market Index Fund": random.choice(["all-time high", "strong uptrend", "stable growth", "slight decline", "bearish market"]),
        "Blue Chip Stocks": random.choice(["stable performance", "dividend increase", "modest growth", "sector rotation", "undervalued"]),
        "Real Estate Investment Trust": random.choice(["interest-rate sensitive", "yield compression", "property value gains", "occupancy growth", "dividend cuts"]),
        "Government Bonds": random.choice(["yield curve steepening", "inflation concerns", "safe haven demand", "rate hike fears", "historically low yields"]),
        "High-Yield Savings": random.choice(["competitive rates", "introductory offers ending", "rate stability", "guaranteed returns", "underperforming inflation"]),
        "Corporate Bonds": random.choice(["spread widening", "credit concerns", "yield opportunities", "rating upgrades", "liquidity issues"]),
        
        "Tech Growth Stocks": random.choice(["valuation concerns", "all-time high", "innovation breakthrough", "regulatory scrutiny", "sector dominance"]),
        "Municipal Bonds": random.choice(["tax advantage appeal", "budget concerns", "infrastructure spending", "yield opportunities", "credit downgrades"]),
        "Dividend Stocks": random.choice(["payout increases", "sustainable yields", "dividend cuts threat", "value opportunity", "sector rotation"]),
        "International Stock Funds": random.choice(["currency advantage", "emerging market growth", "geopolitical concerns", "valuation discount", "global recovery"]),
        "Health Sector ETF": random.choice(["breakthrough innovations", "regulatory changes", "pandemic resilience", "demographic tailwinds", "cost pressure"]),
        "Mid-Cap Growth Fund": random.choice(["acquisition targets", "expansion phase", "sector leadership", "valuation sweet spot", "liquidity challenges"]),
        
        "Cryptocurrency": random.choice(["extreme volatility", "institutional adoption", "regulatory crackdown", "all-time high", "technical weakness"]),
        "Emerging Markets": random.choice(["currency risks", "growth potential", "political instability", "demographic advantage", "commodity sensitivity"]),
        "Commodities": random.choice(["supply constraints", "demand surge", "inventory buildup", "price ceiling concerns", "producer discipline"]),
        "Peer-to-Peer Lending": random.choice(["default rate increase", "yield opportunity", "platform stability", "regulatory changes", "competitive returns"]),
        "Small-Cap Stocks": random.choice(["growth cycle", "interest rate sensitivity", "overlooked value", "domestic focus", "liquidity concerns"]),
        "Real Estate Development": random.choice(["cost overruns", "strong pre-sales", "supply constraints", "location premium", "regulatory hurdles"]),
        
        "Venture Capital": random.choice(["exit opportunity window", "unicorn potential", "funding round competition", "extended runways", "valuation resets"]),
        "Hedge Funds": random.choice(["strategy convergence", "fee compression", "alpha generation", "liquidity terms", "redemption cycle"]),
        "Private Equity": random.choice(["multiple expansion", "dry powder levels", "exit timing", "acquisition premiums", "leverage concerns"]),
        "Options Trading": random.choice(["volatility spike", "premium compression", "contract liquidity", "expiration clustering", "implied vs. realized spread"]),
        "Startup Incubator": random.choice(["cohort quality", "exit timeline extension", "mentor network strength", "funding ecosystem", "innovation cycle"]),
        "Specialized REITs": random.choice(["sector tailwinds", "occupancy challenges", "development pipeline", "cap rate compression", "refinancing window"])
    }
    
    # Draw market indicator legend
    y_position = 160
    pygame.draw.rect(SCREEN, LIGHT_GRAY, (50, y_position, WIDTH-100, 50), border_radius=5)
    draw_text("MARKET INDICATORS & SHORT SELLING OPPORTUNITIES", WIDTH//2, y_position+15, main_font, DARK_BLUE)
    draw_text("Note: Assets at 'all-time high' often revert to mean (80% chance) unless momentum continues", WIDTH//2, y_position+35, small_font, DARK_RED)
    
    # Draw market tips for current options
    y_position = 230
    for i, option in enumerate(options):
        if option in market_trends:
            trend = market_trends[option]
            
            # Determine market prediction and short selling advice
            prediction_text = ""
            short_sell_advice = ""
            color = BLACK
            
            if trend == "all-time high":
                prediction_text = "Prediction: 80% chance of mean reversion (decline), 20% chance of continued momentum"
                short_sell_advice = "Advanced Strategy: Consider short selling to profit from potential decline"
                color = DARK_RED
            elif any(term in trend for term in ["uptrend", "growth", "gains", "increase", "opportunity", "resilience", "advantage"]):
                prediction_text = "Prediction: Favorable outlook with positive growth potential"
                short_sell_advice = "Advanced Strategy: Long position recommended over short selling"
                color = DARK_GREEN
            elif any(term in trend for term in ["decline", "bearish", "cuts", "concerns", "fear", "pressure", "weakness", "hurdles"]):
                prediction_text = "Prediction: Challenges ahead may impact performance negatively"
                short_sell_advice = "Advanced Strategy: Short selling might outperform long positions"
                color = DARK_RED
            else:
                prediction_text = "Prediction: Mixed indicators suggest moderate volatility"
                short_sell_advice = "Advanced Strategy: Research specific catalysts before short selling"
                color = DARK_BLUE
                
            # Create panel for each option analysis
            create_panel(WIDTH-100, 90, 50, y_position, color=(255, 255, 255), alpha=200, border=True)
            
            # Option name with decorative element
            pygame.draw.circle(SCREEN, GOLD, (70, y_position+20), 8)
            draw_text(option, WIDTH//2, y_position+20, main_font, DARK_BLUE)
            
            # Current trend
            draw_text(f"Current Market Trend: {trend}", WIDTH//2, y_position+45, small_font, BLACK)
            
            # Prediction with appropriate color
            draw_text(prediction_text, WIDTH//2, y_position+65, small_font, color)
            
            # Short selling advice
            draw_text(short_sell_advice, WIDTH//2, y_position+85, small_font, ROYAL_BLUE)
            
            y_position += 100  # Space for next option
    
    # If there are more options than fit on screen, add scrolling instruction
    if len(options) > 4:
        draw_text("(Use mouse wheel to scroll for more assets)", WIDTH//2, HEIGHT-50, small_font, WHITE)
    
    # Continue button at bottom
    continue_button = Button(WIDTH//2-100, HEIGHT-40, 200, 30, "Return to Investment Selection", LIGHT_BLUE, ROYAL_BLUE, WHITE)
    continue_button.draw(SCREEN)
    
    pygame.display.update()
    
    # Wait for continue button click, with scroll support for many options
    scroll_offset = 0
    max_scroll = max(0, len(options) * 100 - 350)  # Limit scrolling based on content
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up
                    scroll_offset = max(0, scroll_offset - 30)
                    # Redraw the screen with new scroll position
                    # [Implement scrolling redraw logic here]
                elif event.button == 5:  # Scroll down
                    scroll_offset = min(max_scroll, scroll_offset + 30)
                    # Redraw the screen with new scroll position
                    # [Implement scrolling redraw logic here]
            
            mouse_pos = pygame.mouse.get_pos()
            continue_button.check_hover(mouse_pos)
            
            if continue_button.is_clicked(mouse_pos, event):
                waiting = False
            
            # Redraw button with hover effect
            continue_button.draw(SCREEN)
            pygame.display.update()
            pygame.time.delay(30)
    
# Handle common button events - quits and restart
def handle_button_events(buttons, return_on_click=None, include_restart=True, include_quit=True):
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_pos = pygame.mouse.get_pos()
            
            # Check each button
            for name, button in buttons.items():
                button.check_hover(mouse_pos)
                if button.is_clicked(mouse_pos, event):
                    if name == "quit" and include_quit:
                        pygame.quit()
                        sys.exit()
                    elif name == "restart" and include_restart:
                        return "RESTART"
                    elif return_on_click and name in return_on_click:
                        waiting = False
                        return name
                    elif name == return_on_click:
                        waiting = False
                        return True
            
            # Redraw buttons to show hover state
            for button in buttons.values():
                button.draw(SCREEN)
            pygame.display.update()
            pygame.time.delay(30)
    
    return False  # Default return if no specific return requested

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

# Display an immersive narrative welcome message that introduces the financial journey
def welcome_message():
    # Draw gradient background for a professional look
    draw_gradient_background((70, 130, 180), (25, 25, 112))  # Steel blue to midnight blue
    
    # Draw elegant title header
    pygame.draw.rect(SCREEN, GOLD, (50, 40, WIDTH-100, 70), border_radius=15)
    pygame.draw.rect(SCREEN, BLACK, (50, 40, WIDTH-100, 70), 2, border_radius=15)
    
    # Draw title with enhanced shadow effect
    title_shadow = title_font.render("FORTUNE'S PATH", True, BLACK)
    title_rect_shadow = title_shadow.get_rect(center=(WIDTH // 2 + 3, 75 + 3))
    SCREEN.blit(title_shadow, title_rect_shadow)
    
    title_surface = title_font.render("FORTUNE'S PATH", True, GOLD)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, 75))
    SCREEN.blit(title_surface, title_rect)
    
    # Subtitle with elegant font
    subtitle = "A JOURNEY TO FINANCIAL WISDOM"
    draw_text(subtitle, WIDTH // 2, 105, font=small_font, color=WHITE)
    
    # Create an ornate story scroll
    create_panel(WIDTH-100, 250, 50, 130, color=(255, 252, 240), alpha=200, border=True)
    
    # Gold decorative elements at corners of the story panel
    coin_positions = [(60, 140), (WIDTH-60, 140), (60, 370), (WIDTH-60, 370)]
    for pos in coin_positions:
        pygame.draw.circle(SCREEN, GOLD, pos, 10)
        pygame.draw.circle(SCREEN, BLACK, pos, 10, 1)
    
    # Draw story header
    pygame.draw.rect(SCREEN, (139, 69, 19), (100, 140, WIDTH-200, 30), border_radius=5)  # Brown header
    draw_text("YOUR FINANCIAL JOURNEY BEGINS", WIDTH // 2, 155, font=small_font, color=WHITE)
    
    # Narrative introduction with more engaging story elements
    story_lines = [
        "The year is 2030. After years of financial struggles, fortune smiles upon you.",
        "A distant relative, a legendary investor, has left you $10,000 in their will.",
        "",
        "But this is more than just money - it's an opportunity to prove yourself.",
        "The inheritance comes with a challenge: turn this seed capital into $30,000",
        "within a limited time, using your financial acumen and market intuition.",
        "",
        "Your relative's journal reveals that success will require mastering the delicate",
        "balance of risk and reward, understanding market patterns, and making",
        "strategic decisions even when faced with uncertainty."
    ]
    
    # Display story with proper spacing
    for i, line in enumerate(story_lines):
        draw_text(line, WIDTH // 2, 185 + (i * 20), font=small_font, color=DARK_BLUE)
    
    # Create a panel for the game mechanics
    create_panel(WIDTH-120, 120, 60, 390, color=(230, 230, 250), alpha=200, border=True)
    
    # Skill-based gameplay elements
    draw_text("YOUR FINANCIAL TOOLKIT:", WIDTH // 2, 410, font=subtitle_font, color=DARK_BLUE)
    
    skill_elements = [
        "• Market Analysis: Read economic indicators to predict investment outcomes",
        "• Risk Management: Balance high-risk/high-reward with safer positions",
        "• Strategic Timing: Know when to hold positions and when to secure profits",
        "• Adaptive Thinking: Respond to unexpected market events and opportunities"
    ]
    
    # Display skill elements
    for i, element in enumerate(skill_elements):
        draw_text(element, WIDTH // 2, 435 + (i * 18), font=small_font, color=DARK_BLUE)
    
    # Create victory/failure conditions panel
    create_panel(WIDTH-300, 60, 150, 520, color=(255, 223, 0, 120), border=True)  # Gold panel
    
    # Game objective with clearer success/failure states
    draw_text("OBJECTIVE: Grow $10,000 to $30,000", WIDTH // 2, 535, font=main_font, color=DARK_GREEN)
    draw_text("WARNING: Bankruptcy means game over", WIDTH // 2, 555, font=main_font, color=DARK_RED)
    
    # Create narrative-themed buttons
    start_button = Button(WIDTH // 2 - 130, HEIGHT - 70, 260, 50, "Begin Your Investment Saga", GOLD, LIGHT_YELLOW, BLACK)
    quit_button = Button(WIDTH - 120, HEIGHT - 40, 100, 30, "Exit", RED, LIGHT_CORAL, WHITE)
    
    # Draw buttons
    start_button.draw(SCREEN)
    quit_button.draw(SCREEN)
    
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

# Function to get the player's choice from a list of options with skill-based decision making
def get_choice(options, prompt="Choose an option:"):
    # Draw a gradient background that reflects strategic decision-making
    draw_gradient_background((230, 240, 255), (210, 230, 255))  # Professional blue gradient
    
    # Draw header with investment theme
    draw_header(prompt, title_color=WHITE, background_color=ROYAL_BLUE, y_pos=30)
    
    # Create main content panel for investment choices
    create_panel(WIDTH-60, 420, 30, 110, color=(255, 255, 255), alpha=200, border=True)
    
    # Add market context to make decisions more skill-based
    market_contexts = [
        "Market analysts are showing cautious optimism in most sectors.",
        "Economic indicators suggest moderate growth potential ahead.",
        "Investors are seeking both growth and stability in uncertain times.",
        "Technical analysis shows potential opportunities in volatile segments.",
        "Recent sector rotations have shifted momentum across markets.",
        "Industry disruption has created both risks and opportunities.",
        "Global economic policies continue influencing market trajectories.",
        "Inflation concerns are shifting investor preferences significantly."
    ]
    
    # Select random market context (could be made more strategic in future versions)
    market_context = random.choice(market_contexts)
    
    # Draw market intelligence header
    pygame.draw.rect(SCREEN, (50, 90, 160), (50, 120, WIDTH-100, 30), border_radius=5)
    draw_text("MARKET INTELLIGENCE", WIDTH//2, 135, font=small_font, color=WHITE)
    
    # Display current market context to inform decision
    draw_text(market_context, WIDTH//2, 160, font=main_font, color=DARK_BLUE)
    
    # Create and draw sentiment indicator to enhance skill-based decision making
    sentiment_indicators = {
        "Stock Market Index Fund": random.uniform(0.6, 0.9) if "Stock Market Index Fund" in options else None,
        "Blue Chip Stocks": random.uniform(0.5, 0.8) if "Blue Chip Stocks" in options else None,
        "Real Estate Investment Trust": random.uniform(0.4, 0.8) if "Real Estate Investment Trust" in options else None,
        "Government Bonds": random.uniform(0.7, 0.9) if "Government Bonds" in options else None,
        "High-Yield Savings": random.uniform(0.8, 0.95) if "High-Yield Savings" in options else None,
        "Corporate Bonds": random.uniform(0.6, 0.85) if "Corporate Bonds" in options else None,
        
        "Tech Growth Stocks": random.uniform(0.3, 0.9) if "Tech Growth Stocks" in options else None,
        "Municipal Bonds": random.uniform(0.65, 0.85) if "Municipal Bonds" in options else None,
        "Dividend Stocks": random.uniform(0.55, 0.8) if "Dividend Stocks" in options else None,
        "International Stock Funds": random.uniform(0.4, 0.75) if "International Stock Funds" in options else None,
        "Health Sector ETF": random.uniform(0.5, 0.85) if "Health Sector ETF" in options else None,
        "Mid-Cap Growth Fund": random.uniform(0.45, 0.8) if "Mid-Cap Growth Fund" in options else None,
        
        "Cryptocurrency": random.uniform(0.2, 0.9) if "Cryptocurrency" in options else None,
        "Emerging Markets": random.uniform(0.3, 0.8) if "Emerging Markets" in options else None,
        "Commodities": random.uniform(0.4, 0.75) if "Commodities" in options else None,
        "Peer-to-Peer Lending": random.uniform(0.4, 0.7) if "Peer-to-Peer Lending" in options else None,
        "Small-Cap Stocks": random.uniform(0.35, 0.85) if "Small-Cap Stocks" in options else None,
        "Real Estate Development": random.uniform(0.4, 0.75) if "Real Estate Development" in options else None,
        
        "Venture Capital": random.uniform(0.2, 0.9) if "Venture Capital" in options else None,
        "Hedge Funds": random.uniform(0.3, 0.85) if "Hedge Funds" in options else None,
        "Private Equity": random.uniform(0.25, 0.9) if "Private Equity" in options else None,
        "Options Trading": random.uniform(0.15, 0.95) if "Options Trading" in options else None,
        "Startup Incubator": random.uniform(0.2, 0.9) if "Startup Incubator" in options else None,
        "Specialized REITs": random.uniform(0.4, 0.8) if "Specialized REITs" in options else None
    }
    
    # Draw research recommendation panel
    draw_text("Expert Sentiment Analysis:", WIDTH//2, 185, font=main_font, color=DARK_BLUE)
    
    # Draw vertical separator line
    pygame.draw.line(SCREEN, LIGHT_GRAY, (WIDTH//2, 195), (WIDTH//2, 195 + 20 * len(options)), 2)
    
    # Draw analyst sentiment header
    draw_text("Bearish", WIDTH//2 - 120, 205, font=small_font, color=DARK_RED)
    draw_text("Neutral", WIDTH//2, 205, font=small_font, color=GRAY)
    draw_text("Bullish", WIDTH//2 + 120, 205, font=small_font, color=DARK_GREEN)
    
    # Create styled option buttons with sentiment indicators
    buttons = []
    for idx, option in enumerate(options):
        # Y position for this option
        y_pos = 230 + idx * 70
        
        # Create option button
        button = Button(WIDTH//2 - 150, y_pos, 300, 50, option, LIGHT_GRAY, WHITE, DARK_BLUE)
        buttons.append(button)
        button.draw(SCREEN)
        
        # Draw sentiment indicator for this option
        if option in sentiment_indicators and sentiment_indicators[option] is not None:
            sentiment = sentiment_indicators[option]
            
            # Background bar
            pygame.draw.rect(SCREEN, LIGHT_GRAY, (WIDTH//2 - 130, y_pos + 55, 260, 10), border_radius=5)
            
            # Colored indicator - protect against None values
            if sentiment is not None:
                indicator_width = int(260 * sentiment)
                
                # Color based on sentiment value
                if sentiment < 0.4:
                    color = DARK_RED
                elif sentiment < 0.6:
                    color = (218, 165, 32)  # Gold/yellow
                else:
                    color = DARK_GREEN
                
                # Only draw if sentiment is valid
                pygame.draw.rect(SCREEN, color, (WIDTH//2 - 130, y_pos + 55, indicator_width, 10), border_radius=5)
                
                # Draw marker for better visualization
                pygame.draw.circle(SCREEN, BLACK, (WIDTH//2 - 130 + indicator_width, y_pos + 60), 5)
    
    # Add skill-based research button and other controls
    research_button = Button(WIDTH//2 - 70, 480, 140, 40, "Market Research", LIGHT_BLUE, ROYAL_BLUE, WHITE)
    quit_button = Button(WIDTH-130, 530, 100, 40, "Exit Market", RED, LIGHT_CORAL, WHITE)
    restart_button = Button(30, 530, 100, 40, "New Journey", GREEN, LIGHT_GREEN, BLACK)
    
    # Draw buttons
    research_button.draw(SCREEN)
    quit_button.draw(SCREEN)
    restart_button.draw(SCREEN)
    
    pygame.display.update()  # Update the display to show the interface
    
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
            
            # Check research, quit and restart buttons
            research_button.check_hover(mouse_pos)
            quit_button.check_hover(mouse_pos)
            restart_button.check_hover(mouse_pos)
            
            if research_button.is_clicked(mouse_pos, event):
                # Show research panel with deeper analysis to enhance skill-based decision making
                show_market_research(options)
                
                # Redraw the original screen after research
                draw_gradient_background((230, 240, 255), (210, 230, 255))
                draw_header(prompt, title_color=WHITE, background_color=ROYAL_BLUE, y_pos=30)
                create_panel(WIDTH-60, 420, 30, 110, color=(255, 255, 255), alpha=200, border=True)
                pygame.draw.rect(SCREEN, (50, 90, 160), (50, 120, WIDTH-100, 30), border_radius=5)
                draw_text("MARKET INTELLIGENCE", WIDTH//2, 135, font=small_font, color=WHITE)
                draw_text(market_context, WIDTH//2, 160, font=main_font, color=DARK_BLUE)
                draw_text("Expert Sentiment Analysis:", WIDTH//2, 185, font=main_font, color=DARK_BLUE)
                pygame.draw.line(SCREEN, LIGHT_GRAY, (WIDTH//2, 195), (WIDTH//2, 195 + 20 * len(options)), 2)
                draw_text("Bearish", WIDTH//2 - 120, 205, font=small_font, color=DARK_RED)
                draw_text("Neutral", WIDTH//2, 205, font=small_font, color=GRAY)
                draw_text("Bullish", WIDTH//2 + 120, 205, font=small_font, color=DARK_GREEN)
                
                # Redraw buttons and indicators
                for idx, option in enumerate(options):
                    y_pos = 230 + idx * 70
                    buttons[idx].draw(SCREEN)
                    
                    if option in sentiment_indicators and sentiment_indicators[option] is not None:
                        sentiment = sentiment_indicators[option]
                        pygame.draw.rect(SCREEN, LIGHT_GRAY, (WIDTH//2 - 130, y_pos + 55, 260, 10), border_radius=5)
                        
                        # Protect against None values
                        if sentiment is not None:
                            indicator_width = int(260 * sentiment)
                            
                            # Color based on sentiment
                            if sentiment < 0.4:
                                color = DARK_RED
                            elif sentiment < 0.6:
                                color = (218, 165, 32)  # Gold
                            else:
                                color = DARK_GREEN
                                
                            pygame.draw.rect(SCREEN, color, (WIDTH//2 - 130, y_pos + 55, indicator_width, 10), border_radius=5)
                            pygame.draw.circle(SCREEN, BLACK, (WIDTH//2 - 130 + indicator_width, y_pos + 60), 5)
                
                research_button.draw(SCREEN)
                quit_button.draw(SCREEN)
                restart_button.draw(SCREEN)
                pygame.display.update()
            
            elif quit_button.is_clicked(mouse_pos, event):
                pygame.quit()
                sys.exit()
            elif restart_button.is_clicked(mouse_pos, event):
                return "RESTART"  # Special return value to indicate restart
        
        # Redraw buttons with hover effects
        for button in buttons:
            button.draw(SCREEN)
        
        research_button.draw(SCREEN)
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
    
    # Chapter titles with educational themes
    titles = ["Chapter 1: Building Financial Foundations", 
              "Chapter 2: Risk and Reward Balance", 
              "Chapter 3: Portfolio Diversification", 
              "Chapter 4: Advanced Market Analysis", 
              "Chapter 5: Long-term Wealth Strategy"]
    title = titles[min(journey_round-1, 4)]
    
    # Draw header with title using helper function
    draw_header(title, title_color=WHITE)
    
    # Display wealth with helper function
    display_wealth(wealth, WIDTH//2, 120)
    
    # Story narrative panel with helper function
    create_panel(WIDTH-200, 100, 100, 200, color=(255, 255, 255), alpha=180, border=True)
    
    # Dynamic narratives based on wealth and journey progress - more educational
    story_options = {
        1: [
            "Your financial advisor introduces investment fundamentals.",
            "Learning the basics of risk vs. reward in financial markets.",
            "First steps in understanding market dynamics.",
            "Beginning your path to financial literacy."
        ],
        2: {
            "success": [
                "Your early success opens doors to new investment strategies.",
                "With growing capital, you explore more sophisticated options.",
                "Your advisor suggests broadening your investment horizons.",
                "Your initial gains allow for more diverse opportunities."
            ],
            "neutral": [
                "Steady progress teaches patience in long-term investing.",
                "Balancing risk continues to be a key learning experience.",
                "Your portfolio shows the importance of perseverance.",
                "The financial journey requires both caution and courage."
            ],
            "setback": [
                "Early setbacks offer valuable lessons in market resilience.",
                "Despite challenges, your investment education continues.",
                "Learning recovery strategies after market fluctuations.",
                "Understanding that losses can be stepping stones to knowledge."
            ]
        },
        3: {
            "success": [
                "Your growing portfolio attracts attention from expert advisors.",
                "As your wealth grows, so does your financial acumen.",
                "Your success demonstrates your developing investment skill.",
                "Your wealth accumulation shows strategic thinking."
            ],
            "struggling": [
                "Diversification becomes crucial for portfolio recovery.",
                "Advanced strategies may help overcome previous setbacks.",
                "Seeking specialized advice to strengthen your position.",
                "Exploring opportunities for financial course correction."
            ]
        },
        4: {
            "expert": [
                "Your investment acumen approaches professional level!",
                "Your portfolio management skills show remarkable growth.",
                "You're developing the mindset of a seasoned investor.",
                "Your financial decisions reflect sophisticated understanding."
            ],
            "solid": [
                "Your balanced approach demonstrates sound investment principles.",
                "Consistent strategy is paying dividends in your financial journey.",
                "Your portfolio reflects thoughtful risk management.",
                "Your investment discipline continues to yield results."
            ],
            "struggling": [
                "Despite challenges, perseverance is key to investment success.",
                "Even veteran investors face market headwinds occasionally.",
                "Strategic repositioning may help recovery efforts.",
                "This challenging phase tests your investment resolve."
            ]
        }
    }
    
    # Select appropriate story based on round and performance
    if journey_round == 1:
        story = random.choice(story_options[1])
    elif journey_round == 2:
        if wealth > 12000:
            story = random.choice(story_options[2]["success"])
        elif wealth < 8000:
            story = random.choice(story_options[2]["setback"])
        else:
            story = random.choice(story_options[2]["neutral"])
    elif journey_round == 3:
        if wealth > 15000:
            story = random.choice(story_options[3]["success"])
        else:
            story = random.choice(story_options[3]["struggling"])
    else:
        if wealth > 20000:
            story = random.choice(story_options[4]["expert"])
        elif wealth > 10000:
            story = random.choice(story_options[4]["solid"])
        else:
            story = random.choice(story_options[4]["struggling"])
    
    # Draw the story narrative with word wrapping
    words = story.split()
    if len(words) > 8:  # If story is long enough to need wrapping
        first_line = " ".join(words[:8])
        second_line = " ".join(words[8:])
        draw_text(first_line, WIDTH//2, 230, main_font, DARK_BLUE)
        draw_text(second_line, WIDTH//2, 255, main_font, DARK_BLUE)
    else:
        draw_text(story, WIDTH//2, 240, main_font, DARK_BLUE)
    
    # Lesson panel - educational component
    create_panel(WIDTH-200, 50, 100, 280, color=(230, 230, 250), alpha=200, border=True)
    
    # Educational lessons based on round
    lessons = [
        "Lesson: Diversification reduces overall investment risk.",
        "Lesson: Higher potential returns typically come with higher risk.",
        "Lesson: Market timing is difficult; consistent strategy often wins.",
        "Lesson: Economic cycles affect different investments differently.",
        "Lesson: Compounding returns grow your wealth exponentially over time.",
        "Lesson: Regular portfolio rebalancing maintains your risk profile."
    ]
    
    draw_text(random.choice(lessons), WIDTH//2, 305, main_font, DARK_BLUE)
    
    # Create buttons
    buttons = {
        "continue": Button(WIDTH//2-100, HEIGHT-100, 200, 50, "Continue Journey", LIGHT_BLUE, ROYAL_BLUE, WHITE),
        "quit": Button(WIDTH-150, HEIGHT-60, 120, 40, "Quit Game", RED, LIGHT_CORAL, BLACK),
        "restart": Button(30, HEIGHT-60, 120, 40, "Restart", GREEN, LIGHT_GREEN, BLACK)
    }
    
    for button in buttons.values():
        button.draw(SCREEN)
    
    pygame.display.update()
    
    # Use helper function for button handling
    result = handle_button_events(buttons, return_on_click="continue")
    if result == "RESTART":
        return -999999  # Special code to signal restart

    # Investment pools with educational descriptions
    investment_pools = {
        "beginner": {
            "Stock Market Index Fund": ("Low-cost fund that tracks entire market. Good first investment.", 
                                      random.randint(-8, 20)),
            "Government Bonds": ("Government-backed debt securities. Very safe, modest returns.", 
                                random.randint(2, 7)),
            "Real Estate Investment Trust": ("Fund that owns income-producing properties. Steady dividends.", 
                                           random.randint(-5, 15)),
            "Blue Chip Stocks": ("Shares in established, financially sound companies.", 
                                random.randint(-10, 25)),
            "High-Yield Savings": ("Bank savings with better than average interest. Very safe.", 
                                  random.randint(1, 4)),
            "Corporate Bonds": ("Debt issued by companies. Higher yield than government bonds.", 
                               random.randint(3, 9))
        },
        
        "intermediate": {
            "Tech Growth Stocks": ("Companies with above-average growth potential in technology.", 
                                 random.randint(-20, 40)),
            "Municipal Bonds": ("Local government debt with tax advantages.", 
                              random.randint(2, 6)),
            "Dividend Stocks": ("Companies that share profits with shareholders regularly.", 
                              random.randint(-5, 15)),
            "International Stock Funds": ("Diversified exposure to global markets.", 
                                        random.randint(-15, 30)),
            "Health Sector ETF": ("Exchange-traded fund focusing on healthcare companies.", 
                                random.randint(-12, 25)),
            "Mid-Cap Growth Fund": ("Fund investing in medium-sized growing companies.", 
                                  random.randint(-10, 22))
        },
        
        "advanced": {
            "Cryptocurrency": ("Digital currency using blockchain technology. Highly volatile.", 
                             random.randint(-50, 80)),
            "Emerging Markets": ("Investments in developing economies. High risk/reward.", 
                               random.randint(-25, 45)),
            "Commodities": ("Raw materials like gold, oil, or agricultural products.", 
                          random.randint(-20, 35)),
            "Peer-to-Peer Lending": ("Direct loans to individuals for interest income.", 
                                    random.randint(-10, 20)),
            "Small-Cap Stocks": ("Shares in smaller companies with growth potential.", 
                               random.randint(-30, 50)),
            "Real Estate Development": ("Direct investment in property development projects.", 
                                      random.randint(-25, 40))
        },
        
        "expert": {
            "Venture Capital": ("Investing in early-stage companies with high potential.", 
                              random.randint(-60, 90)),
            "Hedge Funds": ("Actively managed investment pools using advanced strategies.", 
                          random.randint(-40, 60)),
            "Private Equity": ("Direct investment in private companies, not publicly traded.", 
                             random.randint(-30, 70)),
            "Options Trading": ("Contracts giving right to buy/sell assets at set prices.", 
                              random.randint(-70, 100)),
            "Startup Incubator": ("Supporting multiple early-stage companies with capital and resources.", 
                                random.randint(-50, 120)),
            "Specialized REITs": ("Real estate trusts in specific sectors like data centers.", 
                                random.randint(-20, 40))
        }
    }
    
    # Select investment pool based on journey round
    if journey_round == 1:
        pool = investment_pools["beginner"]
    elif journey_round == 2:
        pool = investment_pools["intermediate"]
    elif journey_round == 3:
        pool = investment_pools["advanced"]
    else:
        pool = investment_pools["expert"]
    
    # Select 4 random investments from the appropriate pool
    investment_names = random.sample(list(pool.keys()), 4)
    
    # Create a dictionary of just the selected investments
    options_dict = {name: pool[name] for name in investment_names}
    
    # Ask the player to choose an investment
    choice = get_choice(investment_names, f"Investment Round {journey_round}: Choose wisely!")
    if choice == "RESTART":
        return -999999  # Special code to signal restart
    
    # Get the description and growth for the chosen investment
    description, growth = options_dict[choice]
    
    # Add short selling option for advanced and expert rounds (3+)
    position_type = "long"  # Default to long position
    
    if journey_round >= 3:  # Only available in advanced rounds
        # Draw short selling decision screen
        draw_gradient_background((50, 50, 80), (30, 30, 60))  # Professional dark gradient
        
        # Header with explanation
        draw_header("Investment Position Strategy", title_color=WHITE, background_color=ROYAL_BLUE)
        
        # Create panel for explanation
        create_panel(WIDTH-100, 200, 50, 120, color=(240, 240, 250), alpha=230, border=True)
        
        # Title
        draw_text("CHOOSE YOUR POSITION STRATEGY", WIDTH//2, 140, subtitle_font, DARK_BLUE)
        
        # Explanation of short selling
        explanation = [
            "You can now choose between two investment strategies:",
            "",
            "LONG POSITION: Traditional investing - profit when prices rise, lose when prices fall.",
            "Maximum loss is limited to your investment amount.",
            "",
            "SHORT POSITION: Advanced strategy - profit when prices fall, lose when prices rise.",
            "Higher risk but can capitalize on overvalued assets or market peaks."
        ]
        
        # Draw explanation text
        for i, line in enumerate(explanation):
            draw_text(line, WIDTH//2, 170 + (i * 22), small_font, BLACK if i in [0, 2, 5] else 
                      DARK_BLUE if i in [3, 6] else GRAY)
        
        # Add market analysis that influences short selling success
        market_status = "normal"
        
        # Check if this asset is at "all-time high" based on market research
        market_trends = {
            "Stock Market Index Fund": random.choice(["all-time high", "strong uptrend", "stable growth", "slight decline", "bearish market"]),
            "Blue Chip Stocks": random.choice(["stable performance", "dividend increase", "modest growth", "sector rotation", "undervalued"]),
            "Real Estate Investment Trust": random.choice(["interest-rate sensitive", "yield compression", "property value gains", "occupancy growth", "dividend cuts"]),
            "Government Bonds": random.choice(["yield curve steepening", "inflation concerns", "safe haven demand", "rate hike fears", "historically low yields"]),
            "High-Yield Savings": random.choice(["competitive rates", "introductory offers ending", "rate stability", "guaranteed returns", "underperforming inflation"]),
            "Corporate Bonds": random.choice(["spread widening", "credit concerns", "yield opportunities", "rating upgrades", "liquidity issues"]),
            
            "Tech Growth Stocks": random.choice(["valuation concerns", "all-time high", "innovation breakthrough", "regulatory scrutiny", "sector dominance"]),
            "Municipal Bonds": random.choice(["tax advantage appeal", "budget concerns", "infrastructure spending", "yield opportunities", "credit downgrades"]),
            "Dividend Stocks": random.choice(["payout increases", "sustainable yields", "dividend cuts threat", "value opportunity", "sector rotation"]),
            "International Stock Funds": random.choice(["currency advantage", "emerging market growth", "geopolitical concerns", "valuation discount", "global recovery"]),
            "Health Sector ETF": random.choice(["breakthrough innovations", "regulatory changes", "pandemic resilience", "demographic tailwinds", "cost pressure"]),
            "Mid-Cap Growth Fund": random.choice(["acquisition targets", "expansion phase", "sector leadership", "valuation sweet spot", "liquidity challenges"]),
            
            "Cryptocurrency": random.choice(["extreme volatility", "institutional adoption", "regulatory crackdown", "all-time high", "technical weakness"]),
            "Emerging Markets": random.choice(["currency risks", "growth potential", "political instability", "demographic advantage", "commodity sensitivity"]),
            "Commodities": random.choice(["supply constraints", "demand surge", "inventory buildup", "price ceiling concerns", "producer discipline"]),
            "Peer-to-Peer Lending": random.choice(["default rate increase", "yield opportunity", "platform stability", "regulatory changes", "competitive returns"]),
            "Small-Cap Stocks": random.choice(["growth cycle", "interest rate sensitivity", "overlooked value", "domestic focus", "liquidity concerns"]),
            "Real Estate Development": random.choice(["cost overruns", "strong pre-sales", "supply constraints", "location premium", "regulatory hurdles"]),
            
            "Venture Capital": random.choice(["exit opportunity window", "unicorn potential", "funding round competition", "extended runways", "valuation resets"]),
            "Hedge Funds": random.choice(["strategy convergence", "fee compression", "alpha generation", "liquidity terms", "redemption cycle"]),
            "Private Equity": random.choice(["multiple expansion", "dry powder levels", "exit timing", "acquisition premiums", "leverage concerns"]),
            "Options Trading": random.choice(["volatility spike", "premium compression", "contract liquidity", "expiration clustering", "implied vs. realized spread"]),
            "Startup Incubator": random.choice(["cohort quality", "exit timeline extension", "mentor network strength", "funding ecosystem", "innovation cycle"]),
            "Specialized REITs": random.choice(["sector tailwinds", "occupancy challenges", "development pipeline", "cap rate compression", "refinancing window"])
        }
        
        if choice in market_trends:
            trend = market_trends[choice]
            
            # Determine if asset is at peak for short selling opportunity
            if trend == "all-time high" or "valuation concerns" in trend:
                market_status = "peak"
                draw_text(f"Market Analysis: {choice} appears to be at a market peak", 
                          WIDTH//2, 320, main_font, DARK_RED)
                draw_text("Technical indicators suggest potential for mean reversion (price decline)", 
                          WIDTH//2, 345, small_font, DARK_RED)
            elif any(term in trend for term in ["decline", "bearish", "cuts", "concerns", "fear", "pressure", "weakness", "hurdles"]):
                market_status = "declining"
                draw_text(f"Market Analysis: {choice} is showing signs of weakness", 
                          WIDTH//2, 320, main_font, DARK_RED)
                draw_text("Technical indicators suggest continued downward pressure", 
                          WIDTH//2, 345, small_font, DARK_RED)
            else:
                draw_text(f"Market Analysis: {choice} appears to be in a normal market state", 
                          WIDTH//2, 320, main_font, DARK_BLUE)
                draw_text("No clear indicators of extreme overvaluation or imminent decline", 
                          WIDTH//2, 345, small_font, DARK_BLUE)
        
        # Create buttons for position choice
        long_button = Button(WIDTH//2 - 220, 400, 200, 50, "LONG POSITION", LIGHT_BLUE, ROYAL_BLUE, WHITE)
        short_button = Button(WIDTH//2 + 20, 400, 200, 50, "SHORT POSITION", LIGHT_CORAL, DARK_RED, WHITE)
        
        # Draw info text based on market status
        if market_status == "peak":
            draw_text("SHORT SELLING SUCCESS PROBABILITY: 80%", WIDTH//2, 470, small_font, DARK_RED)
        elif market_status == "declining":
            draw_text("SHORT SELLING SUCCESS PROBABILITY: 65%", WIDTH//2, 470, small_font, DARK_RED)
        else:
            draw_text("SHORT SELLING SUCCESS PROBABILITY: 50%", WIDTH//2, 470, small_font, DARK_BLUE)
            
        # Draw educational note
        draw_text("Note: Short selling is an advanced technique with higher potential risks and rewards", 
                  WIDTH//2, 500, small_font, DARK_BLUE)
        
        # Draw buttons
        long_button.draw(SCREEN)
        short_button.draw(SCREEN)
        
        pygame.display.update()
        
        # Wait for choice
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                mouse_pos = pygame.mouse.get_pos()
                long_button.check_hover(mouse_pos)
                short_button.check_hover(mouse_pos)
                
                if long_button.is_clicked(mouse_pos, event):
                    position_type = "long"
                    waiting = False
                elif short_button.is_clicked(mouse_pos, event):
                    position_type = "short"
                    waiting = False
                
                # Redraw buttons with hover effect
                long_button.draw(SCREEN)
                short_button.draw(SCREEN)
                pygame.display.update()
                pygame.time.delay(30)
        
        # Modify growth based on short selling choice and market status
        if position_type == "short":
            # Invert growth for short position: negative becomes positive, positive becomes negative
            growth = -growth
            
            # Apply probability-based adjustment for short selling at market peaks
            if market_status == "peak" and growth > 0:  # If shorting at peak and original growth was negative
                # 80% chance of success (increased return for short)
                if random.random() < 0.8:
                    growth = growth * random.uniform(1.2, 1.5)  # Boost short returns by 20-50%
                
            elif market_status == "declining" and growth > 0:
                # 65% chance of success
                if random.random() < 0.65:
                    growth = growth * random.uniform(1.1, 1.3)  # Boost short returns by 10-30%
    
    # Display the chosen investment and explain its characteristics
    draw_gradient_background((240, 248, 255), (255, 248, 220))  # Light blue to cream background
    
    # Header for result screen
    draw_header(f"Investment: {choice}", title_color=DARK_BLUE, background_color=LIGHT_BLUE)
    
    # Create info panel
    create_panel(WIDTH-100, 300, 50, 150, color=(255, 255, 255), alpha=220, border=True)
    
    # Educational explanation
    draw_text("Investment Strategy:", WIDTH // 2, 170, font=subtitle_font, color=DARK_BLUE)
    
    # Split description into multiple lines if needed
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
        draw_text(line, WIDTH // 2, 200 + (i * 25), main_font, BLACK)
    
    y_offset = 200 + (len(lines) * 25) + 30
    
    # Educational component about the investment type
    educational_insights = {
        "beginner": [
            "Beginner investors often benefit from low-cost index funds.",
            "Diversification is key to managing investment risk.",
            "Dollar-cost averaging reduces timing risk for new investors.",
            "Starting with blue-chip stocks provides stability for beginners."
        ],
        "intermediate": [
            "Asset allocation becomes more important as portfolios grow.",
            "Dividend stocks can provide income while growing capital.",
            "International exposure helps reduce geographic concentration risk.",
            "Sector ETFs allow targeted investment in growing industries."
        ],
        "advanced": [
            "Alternative investments can reduce correlation with stock markets.",
            "Emerging markets offer growth potential but with higher volatility.",
            "Commodities often move opposite to stocks during market stress.",
            "Higher risk investments should be balanced with stable assets."
        ],
        "expert": [
            "Professional investors maintain strict risk management systems.",
            "Private investments can offer returns uncorrelated with public markets.",
            "Derivatives can be used to hedge risk or enhance returns.",
            "Complex strategies require constant monitoring and adjustment."
        ]
    }
    
    # Select insight based on round
    if journey_round == 1:
        insight = random.choice(educational_insights["beginner"])
    elif journey_round == 2:
        insight = random.choice(educational_insights["intermediate"])
    elif journey_round == 3:
        insight = random.choice(educational_insights["advanced"])
    else:
        insight = random.choice(educational_insights["expert"])
    
    # Draw educational insight
    create_panel(WIDTH-150, 60, 75, y_offset, color=(230, 230, 250), alpha=200, border=True)
    draw_text("Financial Insight:", WIDTH // 2, y_offset + 15, main_font, DARK_BLUE)
    draw_text(insight, WIDTH // 2, y_offset + 40, small_font, DARK_BLUE)
    
    y_offset += 70
    
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
    
    # Create story narrative panel for investment details
    create_panel(WIDTH-200, 80, 100, y_offset + 30, color=(255, 248, 220), alpha=200, border=True)
    
    draw_text(f"Previous wealth: ${old_wealth:.2f}", WIDTH // 2, y_offset + 45)
    draw_text(f"New wealth: ${wealth:.2f}", WIDTH // 2, y_offset + 75, 
              color=DARK_GREEN if wealth > old_wealth else DARK_RED if wealth < old_wealth else BLACK)
    
    # Add a market event that might affect the investment
    # Define market events with educational descriptions
    market_events = {
        # Negative events with educational element
        "recession": {
            "event": "Economic recession hits! Market values decline.",
            "impact": -10,
            "lesson": "Recessions affect different investments differently. Diversification is crucial."
        },
        "interest_rates": {
            "event": "Interest rates rise, affecting investment returns.",
            "impact": -5,
            "lesson": "Rate changes impact bonds, real estate, and growth stocks in different ways."
        },
        "inflation": {
            "event": "Inflation increases, affecting purchasing power.",
            "impact": -8,
            "lesson": "Some assets like real estate and commodities can be inflation hedges."
        },
        "trade_tensions": {
            "event": "Global trade tensions affect markets.",
            "impact": -7,
            "lesson": "International events demonstrate why geographic diversification matters."
        },
        "bankruptcy": {
            "event": "Major company bankruptcy shakes investor confidence.",
            "impact": -12,
            "lesson": "Company-specific risk can be mitigated through diversification."
        },
        "political": {
            "event": "Political instability creates market uncertainty.",
            "impact": -9,
            "lesson": "Political events create volatility but rarely affect long-term performance."
        },
        "regulatory": {
            "event": "Regulatory changes impact business operations.",
            "impact": -6,
            "lesson": "Regulatory risk affects different sectors in different ways."
        },
        "currency": {
            "event": "Currency devaluation affects international investments.",
            "impact": -11,
            "lesson": "Currency hedging can protect international investments."
        },
        "disaster": {
            "event": "Natural disaster disrupts supply chains.",
            "impact": -8,
            "lesson": "Unexpected events highlight the importance of emergency reserves."
        },
        "cyber": {
            "event": "Cyber attack on financial institutions creates panic.",
            "impact": -10,
            "lesson": "Modern risks require modern risk management strategies."
        },
        "bubble": {
            "event": "Market speculation bubble bursts!",
            "impact": -15,
            "lesson": "Market euphoria often precedes significant corrections."
        },
        "housing": {
            "event": "Housing market crash affects broader economy.",
            "impact": -13,
            "lesson": "Real estate cycles can impact multiple investment sectors."
        },
        "oil": {
            "event": "Oil price shock impacts energy sector.",
            "impact": -9,
            "lesson": "Commodity price risks affect multiple industries."
        },
        "strikes": {
            "event": "Labor strikes disrupt production in key industries.",
            "impact": -7,
            "lesson": "Labor relations can significantly impact company performance."
        },
        "banking": {
            "event": "Banking crisis leads to credit squeeze.",
            "impact": -14,
            "lesson": "Financial system health affects availability of capital for all."
        },
        "agriculture": {
            "event": "Agricultural shortage leads to price inflation.",
            "impact": -6,
            "lesson": "Food production challenges can drive broader inflation trends."
        },
        "consumer": {
            "event": "Consumer confidence falls to historic lows.",
            "impact": -8,
            "lesson": "Consumer sentiment drives approximately 70% of economic activity."
        },
        "fraud": {
            "event": "Corporate fraud scandal rocks major corporation.",
            "impact": -11,
            "lesson": "Corporate governance is crucial for long-term investment success."
        },
        "tech_correction": {
            "event": "Tech sector correction after years of growth.",
            "impact": -12,
            "lesson": "High-growth sectors often experience higher volatility."
        },
        "healthcare": {
            "event": "Healthcare costs surge, affecting corporate profits.",
            "impact": -7,
            "lesson": "Healthcare expenses impact both consumers and companies' bottom lines."
        },
        
        # Positive events with educational element
        "tech_breakthrough": {
            "event": "New technology breakthrough boosts the economy!",
            "impact": 15,
            "lesson": "Innovation drives productivity and economic expansion."
        },
        "stimulus": {
            "event": "Government stimulus package helps the economy.",
            "impact": 8,
            "lesson": "Fiscal policy can significantly impact short-term economic conditions."
        },
        "tax_cuts": {
            "event": "Tax cuts benefit businesses and investors.",
            "impact": 12,
            "lesson": "Tax policy affects corporate earnings and investor returns."
        },
        "jobs": {
            "event": "Strong jobs report improves economic outlook.",
            "impact": 6,
            "lesson": "Employment metrics are leading indicators of economic health."
        },
        "trade_agreement": {
            "event": "New trade agreement opens international markets.",
            "impact": 11,
            "lesson": "Reduced trade barriers can create new investment opportunities."
        },
        "central_bank": {
            "event": "Central bank policy supports market growth.",
            "impact": 9,
            "lesson": "Monetary policy directly affects borrowing costs and asset prices."
        },
        "renewable": {
            "event": "Innovation in renewable energy creates new opportunities.",
            "impact": 13,
            "lesson": "Sustainability trends are reshaping industry and investment landscapes."
        },
        "productivity": {
            "event": "Productivity gains reported across multiple sectors.",
            "impact": 7,
            "lesson": "Productivity growth drives long-term economic prosperity."
        },
        "spending": {
            "event": "Consumer spending surges in holiday season.",
            "impact": 10,
            "lesson": "Consumer spending patterns can indicate economic confidence."
        },
        "medical": {
            "event": "Medical breakthrough promises new treatment options.",
            "impact": 14,
            "lesson": "Healthcare innovation can create significant investment opportunities."
        },
        "infrastructure": {
            "event": "Infrastructure bill passes, boosting construction sector.",
            "impact": 12,
            "lesson": "Government spending on infrastructure can stimulate economic growth."
        },
        "corporate": {
            "event": "Record corporate profits reported this quarter.",
            "impact": 15, 
            "lesson": "Corporate earnings drive stock market returns over time."
        },
        "unemployment": {
            "event": "Unemployment reaches historic low.",
            "impact": 8,
            "lesson": "Low unemployment typically leads to wage growth and inflation."
        },
        "housing_rebound": {
            "event": "Housing market rebounds with strong sales.",
            "impact": 9,
            "lesson": "Real estate often leads economic recoveries due to wealth effect."
        },
        "new_market": {
            "event": "New market opens for domestic products.",
            "impact": 11,
            "lesson": "Market expansion creates growth opportunities for businesses."
        },
        "tech_product": {
            "event": "Tech company announces revolutionary product.",
            "impact": 16,
            "lesson": "Disruptive innovation can create new industry leaders."
        },
        "resource": {
            "event": "Mining company discovers valuable resource deposit.",
            "impact": 13,
            "lesson": "Resource discoveries can shift supply-demand dynamics."
        },
        "merger": {
            "event": "Merger creates powerful new market leader.",
            "impact": 10,
            "lesson": "Consolidation can create economies of scale and market influence."
        },
        "foreign_investment": {
            "event": "Foreign investment flows into domestic markets.",
            "impact": 8,
            "lesson": "Capital flows affect currency values and asset prices."
        },
        "agricultural": {
            "event": "Agricultural surplus leads to economic stability.",
            "impact": 7,
            "lesson": "Food security contributes to economic and social stability."
        }
    }
    
    # 30% chance of a market event occurring
    if random.random() < 0.3:
        # Create event panel
        create_panel(WIDTH-100, 200, 50, y_offset + 110, color=(255, 240, 240), alpha=220, border=True)
        
        # Group events by category for story progression
        negative_events = ["recession", "interest_rates", "inflation", "trade_tensions", 
                          "bankruptcy", "political", "regulatory", "currency", "disaster", 
                          "cyber", "bubble", "housing", "oil", "strikes", "banking", 
                          "agriculture", "consumer", "fraud", "tech_correction", "healthcare"]
        
        positive_events = ["tech_breakthrough", "stimulus", "tax_cuts", "jobs", 
                          "trade_agreement", "central_bank", "renewable", "productivity", 
                          "spending", "medical", "infrastructure", "corporate", "unemployment", 
                          "housing_rebound", "new_market", "tech_product", "resource", 
                          "merger", "foreign_investment", "agricultural"]
        
        # Choose event based on player's wealth trend for more narrative continuity
        if wealth > old_wealth * 1.1:  # Player doing well - mix of events, slightly more negative for balance
            event_category = random.choices([negative_events, positive_events], weights=[0.6, 0.4])[0]
        elif wealth < old_wealth * 0.9:  # Player struggling - more positive events for balance
            event_category = random.choices([negative_events, positive_events], weights=[0.3, 0.7])[0]
        else:  # Neutral performance - balanced odds
            event_category = random.choices([negative_events, positive_events], weights=[0.5, 0.5])[0]
            
        # Select a random event from the chosen category
        event_key = random.choice(event_category)
        event_data = market_events[event_key]
        
        # Extract event details
        event_text = event_data["event"]
        impact = event_data["impact"]
        lesson = event_data["lesson"]
        
        # Display event information
        draw_text("BREAKING NEWS:", WIDTH // 2, y_offset + 125, color=RED, font=subtitle_font)
        draw_text(event_text, WIDTH // 2, y_offset + 155)
        
        # Calculate impact on wealth
        old_wealth = wealth
        wealth += wealth * (impact / 100)
        
        # Display impact on wealth
        impact_color = DARK_GREEN if impact > 0 else DARK_RED
        draw_text(f"Impact on your wealth: {impact}%", WIDTH // 2, y_offset + 185, color=impact_color)
        draw_text(f"Updated wealth: ${wealth:.2f}", WIDTH // 2, y_offset + 215, 
                 color=DARK_GREEN if wealth > old_wealth else DARK_RED)
        
        # Create educational insight panel
        create_panel(WIDTH-150, 60, 75, y_offset + 240, color=(230, 230, 250), alpha=200, border=True)
        
        # Display educational lesson
        draw_text("Financial Insight:", WIDTH // 2, y_offset + 255, main_font, DARK_BLUE)
        draw_text(lesson, WIDTH // 2, y_offset + 275, small_font, DARK_BLUE)
        
        # Add this event to the investment history
        investment_history.append(f"Market Event: {event_text} - Impact: {impact}%")
        
        # Store the impact for skill tracking
        market_impact = impact
    else:
        # No market event
        market_impact = 0
    
    # Create continue button using skill-based prompt based on performance
    if wealth > old_wealth * 1.2:  # Over 20% gain
        continue_text = "Celebrate Success & Continue"
    elif wealth > old_wealth:  # Any gain
        continue_text = "Continue Building Wealth"
    elif wealth > old_wealth * 0.9:  # Small loss
        continue_text = "Regroup & Continue"
    else:  # Big loss
        continue_text = "Learn from Loss & Continue"
    
    # Continue button and buttons panel
    create_panel(WIDTH-200, 60, 100, HEIGHT-90, color=(245, 245, 245), alpha=180, border=True)
    continue_button = Button(WIDTH // 2 - 120, HEIGHT - 80, 240, 50, continue_text, LIGHT_GREEN, GREEN)
    continue_button.draw(SCREEN)
    
    pygame.display.update()
    
    # Wait for player to continue with improved button handling
    buttons = {"continue": continue_button}
    handle_button_events(buttons, return_on_click="continue")
    
    # Record this investment in the history with the market impact
    total_growth = growth + market_impact
    
    # Create a more educational and narrative investment history entry
    if total_growth > 15:
        quality = "excellent"
    elif total_growth > 5:
        quality = "good"
    elif total_growth > -5:
        quality = "modest"
    elif total_growth > -15:
        quality = "disappointing"
    else:
        quality = "disastrous"
        
    investment_history.append(f"Round {journey_round}: {choice} - {quality} growth of {total_growth}%")
    
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
    draw_header("Financial Wisdom", title_color=GOLD, font=title_font)
    
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
    
    # Use helper function for button events
    result = handle_button_events(buttons, return_on_click="continue")
    if result == "RESTART":
        return "RESTART"
    
    return "CONTINUE"

# Function to show decision screen and handle player choices with skill-based narrative elements
def show_decision_screen(wealth, journey_round):
    # Setup screen
    draw_gradient_background((255, 250, 205), (255, 228, 225))
    
    # Draw header with title
    draw_header("Strategic Decision Point", title_color=WHITE)
    
    # Display wealth with appropriate colors
    display_wealth(wealth, WIDTH//2, 120)
    
    # Narrative panel - larger for more story content
    create_panel(WIDTH-100, 150, 50, 180, color=(255, 255, 255), alpha=180)
    
    # Dynamic story narratives based on journey progress and wealth
    story_options = {
        1: {
            "high": [
                "Your early investments have performed exceptionally well, attracting the attention of a senior financial advisor.",
                "Your financial mentor is impressed with your intuition and suggests you're ready for more complex strategies."
            ],
            "medium": [
                "Your cautious approach has kept your portfolio stable, though your advisor sees untapped potential.",
                "Your investment journey shows promise, but your advisor suggests more calculated risks might be needed."
            ],
            "low": [
                "Despite early setbacks, your financial mentor sees determination in your investment approach.",
                "The market has been challenging, but your advisor believes valuable lessons have been learned."
            ]
        },
        2: {
            "high": [
                "Word of your investment success has spread. A prestigious firm has offered specialized opportunities.",
                "Your growing reputation as a savvy investor has opened doors to exclusive investment circles."
            ],
            "medium": [
                "Your balanced portfolio shows maturity in your investment thinking. New paths are emerging.",
                "Your consistent approach has built a foundation for more strategic investment decisions."
            ],
            "low": [
                "Recovery strategies have become crucial. Your advisor suggests focusing on fundamental analysis.",
                "The challenging market has tested your resolve. Your next moves will be defining moments."
            ]
        },
        3: {
            "high": [
                "Financial publications have taken note of your exceptional returns. New mentors seek you out.",
                "Your investment insight has captured attention of industry veterans. Elite opportunities await."
            ],
            "medium": [
                "Your methodical approach demonstrates growing expertise in market analysis and timing.",
                "Your portfolio diversification strategies show increasing sophistication in risk management."
            ],
            "low": [
                "Despite market headwinds, your persistence shows the mindset needed for long-term success.",
                "Your resilience in the face of volatility demonstrates the temperament of a seasoned investor."
            ]
        },
        4: {
            "high": [
                "Your investment mastery has become legendary. Financial institutions compete for your insights.",
                "Few have achieved your level of market understanding. Your strategies are studied by others."
            ],
            "medium": [
                "Your disciplined approach has weathered multiple market cycles, showing true investing wisdom.",
                "Your balanced risk management has built a resilient portfolio that others seek to emulate."
            ],
            "low": [
                "The path to investment mastery is often marked by challenges that forge deeper understanding.",
                "Even the greatest investors faced defining moments where persistence determined their legacy."
            ]
        }
    }
    
    # Select appropriate narrative based on journey round and wealth
    wealth_ratio = wealth / 10000  # Compare to starting wealth
    
    if journey_round <= 4:
        if wealth_ratio > 1.5:
            narrative = random.choice(story_options[min(journey_round, 4)]["high"])
        elif wealth_ratio > 0.8:
            narrative = random.choice(story_options[min(journey_round, 4)]["medium"])
        else:
            narrative = random.choice(story_options[min(journey_round, 4)]["low"])
    else:
        # For very advanced rounds
        if wealth_ratio > 2:
            narrative = "Your investment legacy continues to grow. Few have mastered the markets as you have."
        elif wealth_ratio > 1:
            narrative = "Your journey exemplifies the balanced approach of a true market strategist."
        else:
            narrative = "Even in challenging times, your persistence defines the heart of a true investor."
    
    # Format and display narrative with word wrapping
    words = narrative.split()
    if len(words) > 10:  # If narrative is long enough to need wrapping
        first_line = " ".join(words[:10])
        second_line = " ".join(words[10:])
        draw_text(first_line, WIDTH//2, 210, main_font, DARK_BLUE)
        draw_text(second_line, WIDTH//2, 235, main_font, DARK_BLUE)
    else:
        draw_text(narrative, WIDTH//2, 220, main_font, DARK_BLUE)
    
    # Add skill-based decision context
    skill_challenges = [
        "Market analysts predict volatility ahead. How will you position your portfolio?",
        "Economic indicators are mixed. Where do you see the best opportunities?",
        "Sector rotations are occurring rapidly. How will you adapt your strategy?",
        "Interest rate changes are expected. How will you adjust your investments?",
        "Global events are shifting market sentiment. What's your strategic response?",
        "New technologies are disrupting traditional industries. How will you capitalize?",
        "Investor psychology is driving market movements. What's your contrarian play?",
        "Regulatory changes are affecting key sectors. How will you navigate the shift?"
    ]
    
    # Display the skill challenge
    challenge = random.choice(skill_challenges)
    draw_text(challenge, WIDTH//2, 270, main_font, DARK_BLUE)
    
    # Add skill-based risk-reward indicator
    create_panel(WIDTH-200, 50, 100, 320, color=(240, 248, 255), alpha=200, border=True)
    
    draw_text("Risk-Reward Analysis:", WIDTH//2, 335, main_font, DARK_BLUE)
    
    # Risk-reward indicators to help player make a skill-based decision
    risk_metrics = [
        f"Market Volatility: {random.choice(['High', 'Moderate', 'Low'])}",
        f"Economic Outlook: {random.choice(['Strong', 'Stable', 'Uncertain', 'Weak'])}",
        f"Interest Rate Trend: {random.choice(['Rising', 'Stable', 'Falling'])}",
        f"Investor Sentiment: {random.choice(['Bullish', 'Neutral', 'Bearish'])}",
    ]
    
    # Display risk metrics
    for i, metric in enumerate(risk_metrics):
        draw_text(metric, WIDTH//2, 360 + i*25, small_font, DARK_BLUE)
    
    # Create buttons with more strategic options
    buttons = {
        "strategic": Button(WIDTH//4-150, 440, 280, 60, "Strategic Market Positioning", LIGHT_BLUE, ROYAL_BLUE, WHITE),
        "secure": Button(3*WIDTH//4-130, 440, 260, 60, "Secure Gains & Reassess", LIGHT_CORAL, DARK_RED, WHITE),
        "tips": Button(WIDTH//2-80, 510, 160, 40, "Investment Analysis", LIGHT_GREEN, GREEN, DARK_GREEN),
        "quit": Button(WIDTH-150, HEIGHT-60, 120, 40, "Exit Market", RED, LIGHT_CORAL, BLACK),
        "restart": Button(30, HEIGHT-60, 120, 40, "New Journey", GREEN, LIGHT_GREEN, BLACK)
    }
    
    for button in buttons.values():
        button.draw(SCREEN)
    
    pygame.display.update()
    
    # Handle player decision using helper function
    decision = handle_button_events(buttons, return_on_click=list(buttons.keys()))
    
    # Map strategic decisions to the original options for compatibility
    if decision == "strategic":
        return "continue"
    elif decision == "secure":
        return "stop"
    elif decision == "tips":
        # Show investment tips then return to decision screen
        show_investment_tips()
        return show_decision_screen(wealth, journey_round)
    else:
        return decision

# Game over screen when player loses all money
def show_game_over():
    # Dramatic red-to-black gradient
    draw_gradient_background((180, 0, 0), (0, 0, 0))
    
    # Draw header with title
    draw_header("FINANCIAL RUIN!", title_color=RED, background_color=DARK_RED, y_pos=80, font=title_font)
    
    # Message panel
    create_panel(WIDTH-100, 200, 50, 200, color=(0, 0, 0), alpha=180)
    
    # Shorter dramatic message
    draw_text("You've lost everything!", 
             WIDTH//2, 250, subtitle_font, RED)
    draw_text("Your financial journey ends in disaster.", 
             WIDTH//2, 290, main_font, LIGHT_CORAL)
    draw_text("In finance, there are no second chances.", 
             WIDTH//2, 330, main_font, LIGHT_CORAL)
    
    # Create buttons
    buttons = {
        "restart": Button(WIDTH//2-200, 420, 180, 50, "Try Again", GREEN, LIGHT_GREEN),
        "quit": Button(WIDTH//2+20, 420, 180, 50, "Give Up", RED, LIGHT_CORAL)
    }
    
    # Draw buttons initially
    for button in buttons.values():
        button.draw(SCREEN)
    pygame.display.update()
    
    # Use helper function to handle button events
    result = handle_button_events(buttons, return_on_click="restart")
    return "restart" if result else "restart"  # Always return restart as fallback

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
        draw_text("Thank you for playing! Wouldd you like to start a new journey?", 
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
