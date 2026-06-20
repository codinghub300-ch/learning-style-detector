from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

questions = [
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

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/quiz")
def quiz():
  return render_template("quiz.html", questions=questions)

@app.route("/result", methods=["POST"])
def result():
  answers = request.json

scores = {
    "Processing": {"Active": 0, "Reflective": 0},
    "Perception": {"Sensing": 0, "Intuitive": 0},
    "Input": {"Visual": 0, "Verbal": 0},
    "Understanding": {"Sequential": 0, "Global": 0}
}

for i, answer in enumerate(answers):
    _, dim, style = questions[i]["options"][answer]
    scores[dim][style] += 1

final_result = {}

for dim, values in scores.items():
    styles = list(values.keys())

    if values[styles[0]] > values[styles[1]]:
        final_result[dim] = styles[0]
    elif values[styles[1]] > values[styles[0]]:
        final_result[dim] = styles[1]
    else:
        final_result[dim] = "Balanced"

return jsonify(final_result)


if __name__ == "main":
  app.run(debug=True)

