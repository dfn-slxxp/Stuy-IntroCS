from django.shortcuts import render

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
    {'key': 'q4', 'text': "What is the name of Minecraft's 'final' boss?",          'options': ['The Wither', 'The Elder Guardian', 'The Ender Dragon', 'The Ravager']},
    {'key': 'q5', 'text': 'What material do you need to craft a Nether portal?',  'options': ['Obsidian', 'Crying Obsidian', 'Blackstone', 'Bedrock']},
    {'key': 'q6', 'text': 'Who created Minecraft?',                               'options': ['Jeb_', 'Notch', 'Dinnerbone', 'Dream']},
    {'key': 'q7', 'text': 'Which item is required to activate an End Portal?',    'options': ['Ender Pearls', 'Eyes of Ender', 'Blaze Rods', 'Obsidian']},
]

MSGS = ['Better luck next time!', 'Not bad — keep playing!', 'Pretty good!', 'Pretty good!', 'Nice work!', 'Almost perfect!', 'You know your stuff!', 'Perfect score!']

def render_quiz(request):
    if request.method == 'POST':
        questions = []
        score = 0
        for q in QUESTIONS:
            user_ans = request.POST.get(q['key'], '')
            correct_ans = ANSWERS[q['key']]
            is_correct = user_ans == correct_ans
            if is_correct:
                score += 1
            questions.append({
                'text': q['text'],
                'options': q['options'],
                'user_answer': user_ans,
                'correct_answer': correct_ans,
                'correct': is_correct,
            })
        return render(request, 'quiz_results.html', {
            'score': score,
            'total': len(QUESTIONS),
            'msg': MSGS[score],
            'questions': questions,
        })

    return render(request, 'quiz.html')