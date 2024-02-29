import random

questions = [
    {"question": "What is the state animal of Nagaland?", "options": ["A. Mithun", "B. Snow Leopard", "C. Red Panda", "D. Bengal Tiger"], "answer": "A"},
    {"question": "Which is famous festival of Nagaland?", "options": ["A. Peacock", "B. Hornbill", "C. Sparrow", "D. Eagle"], "answer": "B"},
    {"question": "Which flower is known as the state flower of Nagaland?", "options": ["A. Rose", "B. Sunflower", "C. Rhododendron", "D. Lotus"], "answer": "C"},
    {"question": "The Dzükou Valley, located in Nagaland, is known for its stunning landscape and rich biodiversity. What type of ecosystem is Dzükou Valley famous for?", "options": ["A. Desert", "B. Alpine", "C. Rainforest", "D. Mangrove"], "answer": "B"},
    {"question": "Which river in Nagaland is known for its clear waters and diverse aquatic life?", "options": ["A. Ganges", "B. Brahmaputra", "C. Doyang", "D. Yamuna"], "answer": "C"},
    {"question": "What is the state tree of Nagaland?", "options": ["A. Oak", "B. Pine", "C. Alder", "D. bamboo"], "answer": "B"},
    {"question": "Nagaland is home to the Hoolock Gibbon, which is a species of which animal?", "options": ["A. lion", "B. Elephant", "C. Deer", "D. Gibbon"], "answer": "D"},
    {"question": "Which bamboo species is commonly found in Nagaland and plays a significant role in the state's culture and economy?", "options": ["A. Golden Bamboo", "B. Black Bamboo", "C. Dwarf Bamboo", "D. Thorny Bamboo"], "answer": "B"},
    {"question": "The Amur Falcon, a migratory bird, visits Nagaland during its journey. What is its primary food source?", "options": ["A. Seeds", "B. Fish", "C. Insects", "D. Small mammals"], "answer": "C"},
    {"question": "Which national park in Nagaland is known for its conservation efforts and houses the Blyth's Tragopan, a rare pheasant species?", "options": ["A. Ntangki National Park", "B. Intanki Wildlife Sanctuary", "C. Rangapahar Wildlife Sanctuary", "D. Puliebadze Wildlife Sanctuary"], "answer": "A"}
]

def randon_question():
    return random.choice(questions)

def display_options(options):
    for option in options:
        print(option)

def kbc_game():
    print("Welcome to Kaun Banega Crorepati!")
    score = 0

    for i in range(1,11):
        print(f"\nQuestion{i}:")
        current_question = randon_question()
        print(current_question["question"])
        options = display_options(current_question["options"])

        response = input('Please tell which Option to Lock: A, B, C, D\n')

        if response == current_question["answer"]:
            score=score+1
            print('Correct Answer')
        else:
            print(f"Sorry, the correct answer was {current_question['answer']}.")
            break
    print("\nGame Over!")
    print(f"You've won {score * 10000} rupees!")

if __name__ == "__main__":
    kbc_game()