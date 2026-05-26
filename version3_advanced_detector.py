from datetime import datetime
import games

# Multiple questions per dimension
questions = [
    # Processing: Active vs Reflective
    {
        "text": "When learning something new, I prefer to...",
        "options": {
            "a": ("Try it out and learn while doing.", "Processing", "Active"),
            "b": ("Think about it and understand the idea first.", "Processing", "Reflective")
        }
    },
    {
        "text": "I like learning in group activities more than studying alone.",
        "options": {
            "a": ("Yes, I enjoy learning with others.", "Processing", "Active"),
            "b": ("No, I prefer to study alone and reflect.", "Processing", "Reflective")
        }
    },
    {
        "text": "I often understand better when I explain things to others.",
        "options": {
            "a": ("Yes, I understand better this way.", "Processing", "Active"),
            "b": ("No, I prefer to analyze it myself.", "Processing", "Reflective")
        }
    },

    # Perception: Sensing vs Intuitive
    {
        "text": "I prefer learning material that...",
        "options": {
            "a": ("Is practical and fact-based.", "Perception", "Sensing"),
            "b": ("Focuses on theories and concepts.", "Perception", "Intuitive")
        }
    },
    {
        "text": "I trust information more when it's from real-world experience.",
        "options": {
            "a": ("Yes, real data is key.", "Perception", "Sensing"),
            "b": ("No, abstract reasoning matters more.", "Perception", "Intuitive")
        }
    },
    {
        "text": "I enjoy solving problems by...",
        "options": {
            "a": ("Applying known techniques.", "Perception", "Sensing"),
            "b": ("Exploring new ideas and methods.", "Perception", "Intuitive")
        }
    },

    # Input: Visual vs Verbal
    {
        "text": "When studying, I prefer...",
        "options": {
            "a": ("Diagrams and pictures.", "Input", "Visual"),
            "b": ("Reading and listening to explanations.", "Input", "Verbal")
        }
    },
    {
        "text": "I remember content better when I...",
        "options": {
            "a": ("See it visually.", "Input", "Visual"),
            "b": ("Read or hear it.", "Input", "Verbal")
        }
    },
    {
        "text": "During presentations, I prefer...",
        "options": {
            "a": ("Slides with images or charts.", "Input", "Visual"),
            "b": ("Clear verbal explanations.", "Input", "Verbal")
        }
    },

    # Understanding: Sequential vs Global
    {
        "text": "I prefer instructions that are...",
        "options": {
            "a": ("Step-by-step.", "Understanding", "Sequential"),
            "b": ("Big picture first, then details.", "Understanding", "Global")
        }
    },
    {
        "text": "I understand better when...",
        "options": {
            "a": ("Information is given in logical order.", "Understanding", "Sequential"),
            "b": ("I can explore freely and connect ideas later.", "Understanding", "Global")
        }
    },
    {
        "text": "In solving problems, I prefer...",
        "options": {
            "a": ("Following structured methods.", "Understanding", "Sequential"),
            "b": ("Jumping around to see relationships.", "Understanding", "Global")
        }
    }
]

# Score tracker
scores = {
    "Processing": {"Active": 0, "Reflective": 0},
    "Perception": {"Sensing": 0, "Intuitive": 0},
    "Input": {"Visual": 0, "Verbal": 0},
    "Understanding": {"Sequential": 0, "Global": 0}
}

def ask_questions():
    print("🎮 Welcome to the Learning Style Detector Game!\nChoose what matches you best:\n")
    for q in questions:
        print(q["text"])
        for key, (desc, _, _) in q["options"].items():
            print(f"  {key}) {desc}")
        while True:
            ans = input("Your choice (a/b): ").strip().lower()
            if ans in q["options"]:
                _, dim, style = q["options"][ans]
                scores[dim][style] += 1
                break
            else:
                print("❌ Invalid choice. Enter 'a' or 'b'.")

def get_result():
    result = {}
    for dim, dim_scores in scores.items():
        a, b = dim_scores.values()
        keys = list(dim_scores.keys())
        if a > b:
            result[dim] = keys[0]
        elif b > a:
            result[dim] = keys[1]
        else:
            result[dim] = "Balanced"
    return result

def launch_games(styles):
    print("\n🎮 Launching personalized learning games:\n")
    game_log = []
    for dim, style in styles.items():
        if style == "Balanced":
            print(f"\n👉 [{dim}] → Balanced (No specific game, both styles apply)")
            game_log.append(f"[{dim}] - Balanced: no game launched.")
            continue

        game_func = {
            ("Active", "Processing"): games.active_game,
            ("Reflective", "Processing"): games.reflective_game,
            ("Sensing", "Perception"): games.sensing_game,
            ("Intuitive", "Perception"): games.intuitive_game,
            ("Visual", "Input"): games.visual_game,
            ("Verbal", "Input"): games.verbal_game,
            ("Sequential", "Understanding"): games.sequential_game,
            ("Global", "Understanding"): games.global_game
        }.get((style, dim), lambda: print("🕹️ Default game not found."))

        print(f"\n👉 [{dim}] → {style} Game:")
        game_func()
        game_log.append(f"[{dim}] - {style}: game played.")
    return game_log

def export_report(result):
    now = datetime.now()
    filename = f"learning_style_report_{now.strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("🎓 Learning Style Report\n")
        f.write("=============================\n")
        f.write(f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("Your Detected Styles:\n")
        for dim, style in result.items():
            f.write(f" - {dim}: {style}\n")
        f.write("\nThanks for participating!\n")
    print(f"\n📁 Report saved as: {filename}")

def main():
    while True:
        ask_questions()
        result = get_result()
        print("\n🎯 Your Learning Style Profile:")
        for dim, style in result.items():
            print(f" - {dim}: {style}")
        export_report(result)

        # Launch personalized games
        game_log = launch_games(result)

        # Ask if the user wants to play again
        again = input("\n🔁 Do you want to take the test again? (y/n): ").strip().lower()
        if again != 'y':
            print("\n👋 Thanks for playing! See you next time.")
            break

        # Reset scores for the next round
        for dim in scores:
            for style in scores[dim]:
                scores[dim][style] = 0



if __name__ == "__main__":
    main()
