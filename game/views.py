from django.shortcuts import render
from django.http import JsonResponse

def game(request):
    return render(request, 'game/game.html')

def get_dialogue(request, dialogue_id):
    dialogues = {
        1: {
            "message": "Hey my idiot! 🌟 Ready for a special birthday surprise?",
            "choices": [
                {"text": "Yes, I'm excited! 😊", "next": 2},
                {"text": "What's this about? 🤔", "next": 3}
            ]
        },
        2: {
            "message": "I love how enthusiastic you are! Just like one of the many things I adore about you! ❤️",
            "choices": [{"text": "Continue 💕", "next": 4}]
        },
        3: {
            "message": "Well, I wanted to make your birthday extra special with a little surprise! 🎁",
            "choices": [{"text": "That's so sweet! 🥰", "next": 4}]
        },
        4: {
            "message": "You know what I wish for on your birthday? That your smile stays as bright as it is now! 🌟",
            "choices": [{"text": "Make a wish! 🎂", "next": 5}]
        },
        5: {
            "message": "HAPPY BIRTHDAY! 🎉🎂✨\nYou make my world better just by being in it!\nI love you! ❤️",
            "choices": []
        }
    }
    return JsonResponse(dialogues.get(dialogue_id, {}))