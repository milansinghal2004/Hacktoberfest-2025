import sys
import argparse
import os
from pygments import lexers, util
from pygments.lexers import get_lexer_by_name, get_lexer_for_filename
from pygments.styles import get_style_by_name
from pygments.util import ClassNotFound
from PIL import Image, ImageDraw, ImageFont

class CodeToImage:
    def __init__(self, style_name="monokai", font_size=20, padding=40):
        self.style = get_style_by_name(style_name)
        self.font_size = font_size
        self.padding = padding
        self.line_height = int(font_size * 1.5)
        
        # Colors from style or defaults
        self.bg_color = self.style.background_color or "#272822"
        
        # Load font
        try:
            # Try to find a monospace font on Windows
            self.font = ImageFont.truetype("consola.ttf", self.font_size)
        except IOError:
            try:
                self.font = ImageFont.truetype("DejaVuSansMono.ttf", self.font_size)
            except IOError:
                self.font = ImageFont.load_default()

    def get_tokens(self, code, language=None, filename=None):
        try:
            if language:
                lexer = get_lexer_by_name(language)
            elif filename:
                lexer = get_lexer_for_filename(filename)
            else:
                lexer = lexers.guess_lexer(code)
        except ClassNotFound:
            lexer = lexers.get_lexer_by_name("text")
            
        return list(lexer.get_tokens(code))

    def render(self, code, output_path, language=None, filename=None):
        tokens = self.get_tokens(code, language, filename)
        
        # Calculate image size
        dummy_img = Image.new("RGB", (1, 1))
        draw = ImageDraw.Draw(dummy_img)
        
        lines = code.splitlines()
        max_width = 0
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=self.font)
            width = bbox[2] - bbox[0]
            max_width = max(max_width, width)
        
        text_height = len(lines) * self.line_height
        
        # Window dimensions
        window_width = max_width + (self.padding * 2)
        window_height = text_height + (self.padding * 2) + 40 # extra for title bar
        
        # Canvas dimensions (background gradient)
        canvas_width = window_width + 120
        canvas_height = window_height + 120
        
        # Create canvas with dynamic, subtle gradient
        canvas = Image.new("RGB", (canvas_width, canvas_height), "#1e1e1e")
        draw = ImageDraw.Draw(canvas)
        
        # Pick random base colors for the gradient (formal/dark tones)
        import random
        # Base colors (RGB) - keep them low (0-70) for that subtle "vibe"
        r1, g1, b1 = random.randint(10, 50), random.randint(10, 50), random.randint(30, 70)
        r2, g2, b2 = random.randint(0, 30), random.randint(0, 30), random.randint(10, 40)

        for i in range(canvas_height):
            ratio = i / canvas_height
            r = int(r1 + (r2 - r1) * ratio)
            g = int(g1 + (g2 - g1) * ratio)
            b = int(b1 + (b2 - b1) * ratio)
            draw.line([(0, i), (canvas_width, i)], fill=(r, g, b))

        # Draw Shadow with rounded corners
        shadow_offset = 15
        shadow_rect = [60 + shadow_offset, 60 + shadow_offset, 60 + window_width + shadow_offset, 60 + window_height + shadow_offset]
        draw.rounded_rectangle(shadow_rect, radius=12, fill=(0, 0, 0, 80)) # Mock shadow with darker color
        
        # Draw Window Frame
        window_rect = [60, 60, 60 + window_width, 60 + window_height]
        draw.rounded_rectangle(window_rect, radius=12, fill=self.bg_color)
        
        # Title Bar Buttons (macOS style)
        btn_y = 60 + 20
        btn_radius = 6
        draw.ellipse([60+20, btn_y-btn_radius, 60+20+12, btn_y+btn_radius], fill="#ff5f56") # Red
        draw.ellipse([60+45, btn_y-btn_radius, 60+45+12, btn_y+btn_radius], fill="#ffbd2e") # Yellow
        draw.ellipse([60+70, btn_y-btn_radius, 60+70+12, btn_y+btn_radius], fill="#27c93f") # Green

        # Render Text
        curr_y = 60 + 40 + self.padding
        curr_x = 60 + self.padding
        
        temp_x = curr_x
        for ttype, value in tokens:
            if value == "\n":
                curr_y += self.line_height
                temp_x = curr_x
                continue
                
            color = self.style.style_for_token(ttype)['color']
            if not color:
                color = "ffffff"
            
            # Convert hex to RGB
            color_rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            
            draw.text((temp_x, curr_y), value, font=self.font, fill=color_rgb)
            
            # Move x cursor
            bbox = draw.textbbox((0, 0), value, font=self.font)
            temp_x += (bbox[2] - bbox[0])

        canvas.save(output_path)
        print(f"Image saved to {output_path}")

def interactive_menu():
    print("\n" + "="*40)
    print("  ✨ Code-to-Image Interactive Menu ✨")
    print("="*40)
    
    code_content = ""
    filename = None
    
    choice = input("\n[1] Load from File\n[2] Paste Code Snippet\nChoice: ").strip()
    
    if choice == "1":
        file_path = input("Enter file path: ").strip()
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                code_content = f.read()
            filename = file_path
        else:
            print("Error: File not found.")
            return
    elif choice == "2":
        print("Paste your code below (Press Ctrl+D or Ctrl+Z then Enter to finish):")
        code_content = sys.stdin.read()
    else:
        print("Invalid choice.")
        return

    theme = input("Enter theme (default: monokai, try 'dracula', 'friendly', 'native'): ").strip() or "monokai"
    output = input("Enter output filename (default: code_snippet.png): ").strip() or "code_snippet.png"
    
    try:
        generator = CodeToImage(style_name=theme)
        generator.render(code_content, output, filename=filename)
        print(f"\n✅ Success! Image saved to: {output}")
    except Exception as e:
        print(f"\n❌ Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert code to a beautiful image.")
    parser.add_argument("input", nargs="?", help="Input file path")
    parser.add_argument("--code", help="Raw code snippet")
    parser.add_argument("--output", default="code_snippet.png", help="Output image path")
    parser.add_argument("--theme", default="monokai", help="Pygments theme name")
    parser.add_argument("--lang", help="Programming language for highlighting")
    
    args = parser.parse_args()
    
    # If no arguments provided, launch interactive menu
    if not args.input and not args.code:
        interactive_menu()
        return
        
    code_content = ""
    filename = None
    
    if args.input:
        if os.path.exists(args.input):
            try:
                with open(args.input, "r", encoding="utf-8") as f:
                    code_content = f.read()
                filename = args.input
            except UnicodeDecodeError:
                print(f"Error: Could not read {args.input}. It seems to be a binary file (like an image), not a text/code file.")
                sys.exit(1)
            except Exception as e:
                print(f"Error reading file: {e}")
                sys.exit(1)
        else:
            print(f"Error: File {args.input} not found.")
            sys.exit(1)
    elif args.code:
        code_content = args.code
        
    generator = CodeToImage(style_name=args.theme)
    generator.render(code_content, args.output, language=args.lang, filename=filename)

if __name__ == "__main__":
    main()
