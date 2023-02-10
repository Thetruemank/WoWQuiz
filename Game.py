"""
    Author: Joseph Gabert
    Date: 02/10/2023
"""
import time
import pyttsx3
questions_and_answers = [
    {
        "question": "What is the name of the first expansion for World of Warcraft?",
        "options": [
            "Wrath of the Lich King",
            "The Burning Crusade",
            "Cataclysm",
            "Mists of Pandaria"
        ],
        "answer": 1
    },
    {
        "question": "What is the name of the main protagonist of the original World of Warcraft storyline?",
        "options": [
            "Arthas Menethil",
            "Medivh",
            "Thrall",
            "Anduin Wrynn"
        ],
        "answer": 0
    },
    {
        "question": "What is the name of the goblin capital city in World of Warcraft?",
        "options": [
            "Orgrimmar",
            "Undercity",
            "Thunder Bluff",
            "Gadgetzan"
        ],
        "answer": 3
    },
    {
        "question": "What is the name of the legendary sword wielded by Arthas Menethil in World of Warcraft?",
        "options": [
            "Frostmourne",
            "Shadowmourne",
            "Thunderfury",
            "Ashbringer"
        ],
        "answer": 0
    },
    {
        "question": "What is the name of the primary currency in World of Warcraft?",
        "options": [
            "Gold",
            "Silver",
            "Copper",
            "Platinum"
        ],
        "answer": 0
    },
    {
        "question": "What is the name of the main antagonist in the Burning Crusade expansion?",
        "options": [
            "Illidan Stormrage",
            "Sargeras",
            "Archimonde",
            "Kil'jaeden"
        ],
        "answer": 0
    },
    {
        "question": "What is the name of the faction that controls the undead race in World of Warcraft?",
        "options": [
            "The Horde",
            "The Alliance",
            "The Scourge",
            "The Burning Legion"
        ],
        "answer": 2
    },
    {
        "question": "What is the name of the capital city of the night elves in World of Warcraft?",
        "options": [
            "Darnassus",
            "Stormwind",
            "Ironforge",
            "Exodar"
        ],
        "answer": 0
    },
    {
        "question": "What is the name of the primary profession in World of Warcraft that involves gathering and processing materials?",
        "options": [
            "Herbalism",
            "Mining",
            "Skinning",
            "Fishing"
        ],
        "answer": 1
    },
    {
        "question": "What is the name of the race that controls the city of Orgrimmar in World of Warcraft?",
        "options": [
            "Orcs",
            "Trolls",
            "Tauren",
            "Goblins"
        ],
        "answer": 0
    },
    {
        "question": "What is the name of the continent that was introduced in the Cataclysm expansion?",
        "options": [
            "Pandaria",
            "Northrend",
            "Kalimdor",
            "Azeroth"
        ],
        "answer": 3
    },
    {
        "question": "What is the name of the powerful dragon aspect in World of Warcraft?",
        "options": [
            "Nozdormu",
            "Ysera",
            "Malygos",
            "Alexstrasza"
        ],
        "answer": 0
    },
    {
        "question": "What is the name of the race that controls the city of Undercity in World of Warcraft?",
        "options": [
            "Orcs",
            "Undead",
            "Trolls",
            "Goblins"
        ],
        "answer": 1
    },
    {
        "question": "What is the name of the race that controls the city of Thunder Bluff in World of Warcraft?",
        "options": [
            "Orcs",
            "Undead",
            "Tauren",
            "Goblins"
        ],
        "answer": 2
    },
    {
        "question": "What is the name of the primary profession in World of Warcraft that involves creating items using materials gathered by other professions?",
        "options": [
            "Enchanting",
            "Blacksmithing",
            "Tailoring",
            "Alchemy"
        ],
        "answer": 1
    },
    {
        "question": "What is the name of the race that controls the city of Silvermoon in World of Warcraft?",
        "options": [
            "Blood Elves",
            "Gnomes",
            "Dwarves",
            "Night Elves"
        ],
        "answer": 0
    },
    {
        "question": "What is the name of the race that controls the city of Ironforge in World of Warcraft?",
        "options": [
            "Gnomes",
            "Dwarves",
            "Night Elves",
            "Humans"
        ],
        "answer": 1
    },
    {
        "question": "What is the name of the legendary cloak in World of Warcraft that is said to grant its wearer immense power?",
        "options": [
            "Nerubian Shroud",
            "Shadowmantle",
            "Cloak of the Unseen Path",
            "Netherwind Cloak"
        ],
        "answer": 2
    },
    {
        "question": "What is the name of the primary profession in World of Warcraft that involves using magic to create items and cast spells?",
        "options": [
            "Enchanting",
            "Blacksmithing",
            "Tailoring",
            "Alchemy"
        ],
        "answer": 3
    },
    {
        "question": "What is the name of the race that controls the city of Exodar in World of Warcraft?",
        "options": [
            "Draenei",
            "Gnomes",
            "Dwarves",
            "Night Elves"
        ],
        "answer": 0
    }
]

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

start_time = time.time()
score = 0
for i, question_and_answer in enumerate(questions_and_answers):
    question = question_and_answer["question"]
    options = question_and_answer["options"]
    answer = question_and_answer["answer"]

    print("Question", i + 1, ":")
    speak_text(question)
    for j, option in enumerate(options):
        print("\t", j + 1, ")", option)
        speak_text(str(j + 1) + ") " + option)

    user_answer = int(input("Enter your answer: ")) - 1
    if user_answer == answer:
        print("Correct!")
        speak_text("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is", options[answer])
        speak_text("Incorrect.")
    print()

end_time = time.time()
elapsed_time = end_time - start_time

print("You got", score, "out of", len(questions_and_answers), "questions correct.")
print("Your percentage correct is", 100 * score / len(questions_and_answers), "%.")
print("The average time it took you to answer each question is", elapsed_time / len(questions_and_answers), "seconds.")

