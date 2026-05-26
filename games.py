import webbrowser
import time

def open_link(style_name, url):
    print(f"\n🔗 Opening a {style_name} learning style game in your browser...")
    try:
        time.sleep(0.5)  # Short delay for UX, optional
        webbrowser.open(url)  # Opens in default browser (works on all systems)
    except Exception as e:
        print(f"⚠️ Could not open the game automatically. Error: {e}")
        print(f"➡️ Please open this link manually: {url}")
def active_game():
    open_link("Active", "https://www.mission-us.org/")  # Example link

def reflective_game():
    open_link("Reflective", "https://www.logiclike.com/")

def sensing_game():
    open_link("Sensing", "https://www.brainpop.com/games/")

def intuitive_game():
    open_link("Intuitive", "https://www.ncase.me/trust/")

def visual_game():
    open_link("Visual", "https://www.crazygames.com/game/color-pixel-art-classic")

def verbal_game():
    open_link("Verbal", "https://www.freerice.com/")

def sequential_game():
    open_link("Sequential", "https://www.coolmathgames.com/0-sudoku")

def global_game():
    open_link("Global", "https://www.sporcle.com/")

global_game()