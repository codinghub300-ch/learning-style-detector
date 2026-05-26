# Learning Style Detection Game 

# Initialize scores
scores = {
    "Active": 0,
    "Reflective": 0,
    "Sensing": 0,
    "Intuitive": 0,
    "Visual": 0,
    "Verbal": 0,
    "Sequential": 0,
    "Global": 0
}

print("🎮 Welcome to the Learning Style Detector Game!\nChoose the answer that best matches you:\n")

questions = [
    {
        "text": "1. When learning something new, I prefer to...",
        "options": {
            "a": ("Try it out and learn while doing.", "Active"),
            "b": ("Think about it and understand the idea first.", "Reflective")
        }
    },
    {
        "text": "2. I prefer information that is...",
        "options": {
            "a": ("Detailed and based on facts.", "Sensing"),
            "b": ("Conceptual and based on ideas.", "Intuitive")
        }
    },
    {
        "text": "3. I remember things better when I...",
        "options": {
            "a": ("See diagrams, charts, and pictures.", "Visual"),
            "b": ("Hear explanations or read text.", "Verbal")
        }
    },
    {
        "text": "4. I understand things better when...",
        "options": {
            "a": ("They are presented step by step.", "Sequential"),
            "b": ("I see the big picture first.", "Global")
        }
    }
]

# Ask questions
for q in questions:
    print(q["text"])
    for key, (desc, _) in q["options"].items():
        print(f"  {key}) {desc}")
    
    while True:
        answer = input("Your choice (a/b): ").strip().lower()
        if answer in q["options"]:
            style = q["options"][answer][1]
            scores[style] += 1
            break
        else:
            print("❌ Invalid choice. Please enter 'a' or 'b'.")

print("\n🧠 Your detected learning style is:")

# Show the result
dimensions = [
    ("Active", "Reflective"),
    ("Sensing", "Intuitive"),
    ("Visual", "Verbal"),
    ("Sequential", "Global")
]

for a, b in dimensions:
    if scores[a] > scores[b]:
        print(f"- {a}")
    elif scores[b] > scores[a]:
        print(f"- {b}")
    else:
        print(f"- {a} / {b} (Balanced)")

print("\n✅ Thanks for playing!")
