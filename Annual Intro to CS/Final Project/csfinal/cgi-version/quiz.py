#!/usr/bin/env python3
import cgi, cgitb, os
cgitb.enable()

BASE = "/~swaldman80"
STATIC = f"{BASE}/static"

ANSWERS = {
    'q1': '2009',
    'q2': 'Java',
    'q3': 'The Aether',
    'q4': 'The Ender Dragon',
    'q5': 'Obsidian',
    'q6': 'Notch',
    'q7': 'Eyes of Ender',
}

QUESTIONS = [
    {'key': 'q1', 'text': 'In what year was Minecraft first released?',          'options': ['2007', '2009', '2011', '2013']},
    {'key': 'q2', 'text': 'What programming language is Minecraft written in?',   'options': ['Python', 'C++', 'Java', 'Netlogo']},
    {'key': 'q3', 'text': 'Which of these is NOT a dimension in Minecraft?',      'options': ['The Overworld', 'The Nether', 'The Aether', 'The End']},
    {'key': 'q4', 'text': "What is the name of Minecraft's 'final' boss?",       'options': ['The Wither', 'The Elder Guardian', 'The Ender Dragon', 'The Ravager']},
    {'key': 'q5', 'text': 'What material do you need to craft a Nether portal?',  'options': ['Obsidian', 'Crying Obsidian', 'Blackstone', 'Bedrock']},
    {'key': 'q6', 'text': 'Who created Minecraft?',                               'options': ['Jeb_', 'Notch', 'Dinnerbone', 'Dream']},
    {'key': 'q7', 'text': 'Which item is required to activate an End Portal?',    'options': ['Ender Pearls', 'Eyes of Ender', 'Blaze Rods', 'Obsidian']},
]

MSGS = ['Better luck next time!', 'Not bad — keep playing!', 'Pretty good!', 'Pretty good!', 'Nice work!', 'Almost perfect!', 'You know your stuff!', 'Perfect score!']

form = cgi.FieldStorage()

def page_head():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Minecraft Quiz</title>
    <link href="https://fonts.googleapis.com/css2?family=VT323&display=swap" rel="stylesheet">
    <style>
        * {{
            font-family: 'VT323', sans-serif;
            font-stretch: 150%;
            color: #ffffff;
        }}

        body {{
            text-align: center;
        }}

        .navbar {{
            position: sticky;
            top: 0;
            z-index: 40;
            border: 5px solid #51515187;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 2rem;
            height: 72px;
            background-color: #0000002c;
            margin-bottom: 20px;
        }}

        .content_wrappers {{
            border: 5px solid #51515187;
            background-color: #0000002c;
            border-radius: 5px;
            margin-bottom: 20px;
            text-align: center;
            padding: 2rem;
            width: 35%;
        }}

        .home-button {{
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .home-button h1 {{
            color: #ffffffcc;
            font-size: 2rem;
            font-weight: 600;
            margin: 0;
            padding: 0.5rem;
        }}

        .home-button img {{
            object-fit: contain;
        }}

        .links a {{
            color: #ffffffcc;
            text-decoration: none;
            font-size: 1.5rem;
            padding: .5rem .75rem;
            border-radius: 4px;
        }}

        .links a:hover {{
            color: #ffffff;
        }}

        .content {{
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}

        .wrapper {{
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .question {{
            background: #0000004a;
            border: 2px solid #51515187;
            border-radius: 5px;
            padding: 1.25rem 1.5rem;
            margin-bottom: 1rem;
            text-align: left;
        }}

        .question p {{
            font-size: 1.3rem;
            margin: 0 0 0.75rem;
        }}

        .opt {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin: 0.3rem 0;
            font-size: 1.2rem;
            color: #ccc;
            cursor: pointer;
        }}

        .opt:hover {{
            color: #fff;
        }}

        .opt input {{
            width: 16px;
            height: 16px;
            cursor: pointer;
        }}

        .submit-btn {{
            background: #0000004a;
            border: 2px solid #ffffff88;
            border-radius: 5px;
            padding: 0.75rem 2rem;
            font-family: 'VT323', monospace;
            font-size: 1.5rem;
            color: #fff;
            cursor: pointer;
            margin-top: 1rem;
            width: 100%;
        }}

        .submit-btn:hover {{
            background: #ffffff18;
        }}

        .correct-q {{
            border-color: #4caf50 !important;
        }}

        .wrong-q {{
            border-color: #f44336 !important;
        }}

        .correct-ans {{
            color: #4caf50;
            font-weight: bold;
        }}

        .wrong-ans {{
            color: #f44336;
            text-decoration: line-through;
        }}

        .result {{
            background: #0000004a;
            border: 2px solid #51515187;
            border-radius: 5px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            text-align: center;
        }}

        .result .score {{
            font-size: 3rem;
        }}

        .result .msg {{
            font-size: 1.3rem;
            color: #ccc;
        }}

        .back-btn {{
            background: #0000004a;
            border: 2px solid #ffffff88;
            border-radius: 5px;
            padding: 0.75rem 2rem;
            font-family: 'VT323', monospace;
            font-size: 1.5rem;
            color: #fff;
            text-decoration: none;
            display: block;
            margin-top: 1rem;
            text-align: center;
        }}

        .back-btn:hover {{
            background: #ffffff18;
        }}
    </style>
</head>
<body background="{STATIC}/Dirt.png">
    <div class="navbar">
        <a href="{BASE}/index.html" class="home-button">
            <img src="{STATIC}/image.png" width="48px" height="48px" alt="website logo">
            <h1>Farm Discovery</h1>
        </a>
        <div class="links">
            <a href="{BASE}/index.html">About</a>
            <a href="{BASE}/quiz.py">Play the Quiz</a>
            <a href="{BASE}/farms.py">Farms</a>
            <a href="{BASE}/add.py">Add a Farm</a>
        </div>
    </div>
    <div class="content">
"""

print("Content-Type: text/html\n")
print(page_head())

if os.environ.get("REQUEST_METHOD") == "POST":
    score = 0
    results = []
    for q in QUESTIONS:
        user_ans = form.getvalue(q['key'], '')
        correct_ans = ANSWERS[q['key']]
        is_correct = user_ans == correct_ans
        if is_correct:
            score += 1
        results.append((q, user_ans, correct_ans, is_correct))

    print(f"""
            <div class="content_wrappers">
                <div class="result">
                    <div class="score">{score} / {len(QUESTIONS)}</div>
                    <div class="msg">{MSGS[score]}</div>
                </div>
""")
    for i, (q, user_ans, correct_ans, is_correct) in enumerate(results):
        cls = "correct-q" if is_correct else "wrong-q"
        print(f'                <div class="question {cls}">')
        print(f'                    <p>{i+1}. {q["text"]}</p>')
        for opt in q['options']:
            if opt == correct_ans:
                print(f'                    <div class="opt"><span class="correct-ans">&#10003; {opt}</span></div>')
            elif opt == user_ans:
                print(f'                    <div class="opt"><span class="wrong-ans">&#10007; {opt}</span></div>')
            else:
                print(f'                    <div class="opt"><span>{opt}</span></div>')
        print('                </div>')

    print(f'                <a href="{BASE}/quiz.py" class="back-btn">Try Again</a>')
    print('            </div>')

else:
    print(f'            <form class="content_wrappers" method="post" action="{BASE}/quiz.py">')
    print("                <h1>Think you're a true Minecraft fan? Take on this quiz to find out.</h1>")

    for i, q in enumerate(QUESTIONS):
        print(f'                <div class="question">')
        print(f'                    <p>{i+1}. {q["text"]}</p>')
        for opt in q['options']:
            print(f'                    <label class="opt"><input type="radio" name="{q["key"]}" value="{opt}"> {opt}</label>')
        print('                </div>')

    print('                <button type="submit" class="submit-btn">Submit</button>')
    print('            </form>')

print('        </div>\n</body>\n</html>')
