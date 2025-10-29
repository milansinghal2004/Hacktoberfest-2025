from pyfiglet import Figlet
import random

# Get all available fonts
fonts = Figlet().getFonts()

# Ask user if they want a specific font or a random one
choice = input("Do you want to choose a font? (y/n): ").strip().lower()

if choice == "y":
    chosen_font = input("Enter font name: ").strip()
    if chosen_font not in fonts:
        print("Invalid font name. Using a random font instead.")
        chosen_font = random.choice(fonts)
else:
    chosen_font = random.choice(fonts)

# Create Figlet object with chosen font
f = Figlet(font=chosen_font)

# Get user text and render it
text = input("Input: ")
print(f.renderText(text))
