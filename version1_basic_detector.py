def main():
    print("🔬 Welcome to the Learning Lab Adventure!")
    print("You'll go through a short simulation, and based on your choices, we'll detect your learning style.\n")

    # المتغيرات لحساب النقاط
    scores = {
        "Active": 0,
        "Reflective": 0,
        "Visual": 0,
        "Verbal": 0,
        "Sensing": 0,
        "Intuitive": 0,
        "Sequential": 0,
        "Global": 0
    }

    print("1️⃣ You enter the lab. Do you:")
    print("A. Start pressing buttons to see what happens?")
    print("B. Read the manual and observe others first?")
    q1 = input("Your choice (A/B): ").strip().upper()
    if q1 == "A":
        scores["Active"] += 1
    else:
        scores["Reflective"] += 1

    print("\n2️⃣ You need to understand how a machine works. Do you prefer:")
    print("A. A diagram or a video demonstration?")
    print("B. A detailed written or spoken explanation?")
    q2 = input("Your choice (A/B): ").strip().upper()
    if q2 == "A":
        scores["Visual"] += 1
    else:
        scores["Verbal"] += 1

    print("\n3️⃣ While solving a puzzle, do you:")
    print("A. Prefer facts and concrete clues?")
    print("B. Prefer to guess and look for patterns?")
    q3 = input("Your choice (A/B): ").strip().upper()
    if q3 == "A":
        scores["Sensing"] += 1
    else:
        scores["Intuitive"] += 1

    print("\n4️⃣ You need to complete a complex task. Do you:")
    print("A. Follow a step-by-step approach?")
    print("B. Explore everything freely and connect ideas?")
    q4 = input("Your choice (A/B): ").strip().upper()
    if q4 == "A":
        scores["Sequential"] += 1
    else:
        scores["Global"] += 1

    print("\n🔍 Analyzing your choices...")
    final_style = []
    final_style.append("Active" if scores["Active"] >= scores["Reflective"] else "Reflective")
    final_style.append("Sensing" if scores["Sensing"] >= scores["Intuitive"] else "Intuitive")
    final_style.append("Visual" if scores["Visual"] >= scores["Verbal"] else "Verbal")
    final_style.append("Sequential" if scores["Sequential"] >= scores["Global"] else "Global")

    print("\n🎓 Your Learning Style Profile is:")
    for style in final_style:
        print(f"✔️ {style}")

main()
