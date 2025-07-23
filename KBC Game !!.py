KBC Game !!
import time
import random

def welcome():
    print("\n" + "="*50)
    print("\t🌟 WELCOME TO KAUN BANEGA CROREPATI 🌟")
    print("="*50)
    name = input("\nPlease enter your name: ")
    print(f"\nHello {name}, get ready to play KBC!\n")
    time.sleep(1)
    print("You'll be asked 10 multiple-choice questions.")
    print("Each correct answer gives you ₹10,000.\n")
    input("Press Enter to start the game...")
    return name

def lifeline_5050(options, correct):
    wrong_indices = [i for i in range(4) if i != correct]
    removed = random.sample(wrong_indices, 2)
    filtered = [opt if i not in removed else "" for i, opt in enumerate(options)]
    return filtered

def ask_question(q_num, question, options, correct, lifelines):
    print("\n" + "-"*50)
    print(f"\nQuestion {q_num}: {question}\n")
    for i, opt in enumerate(options):
        print(f"  {chr(65+i)}. {opt}")

    if lifelines['5050']:
        use_lifeline = input("\nDo you want to use 50-50 lifeline? (yes/no): ").strip().lower()
        if use_lifeline == 'yes':
            lifelines['5050'] = False
            filtered = lifeline_5050(options, correct)
            print("\n50-50 Lifeline Applied! Choose from:")
            for i, opt in enumerate(filtered):
                if opt:
                    print(f"  {chr(65+i)}. {opt}")

    answer = input("\nYour answer (A/B/C/D): ").strip().upper()
    if answer == chr(65 + correct):
        print("\n✅ Correct Answer!")
        return True
    else:
        print(f"\n❌ Wrong Answer! The correct answer was {chr(65+correct)}. {options[correct]}")
        return False

def play_kbc():
    name = welcome()
    score = 0
    lifelines = {'5050': True}

    questions = [
        ("What is the capital of India?", ["Mumbai", "New Delhi", "Chennai", "Kolkata"], 1),
        ("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], 2),
        ("Who wrote the Mahabharata?", ["Tulsidas", "Valmiki", "Ved Vyasa", "Kalidasa"], 2),
        ("Which gas do plants absorb from the atmosphere?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], 2),
        ("Who was the first President of India?", ["Dr. Rajendra Prasad", "Jawaharlal Nehru", "Lal Bahadur Shastri", "Dr. S. Radhakrishnan"], 0),
        ("Which is the longest river in the world?", ["Amazon", "Yangtze", "Nile", "Ganga"], 2),
        ("What is the national animal of India?", ["Lion", "Elephant", "Tiger", "Leopard"], 2),
        ("What is H2O commonly known as?", ["Salt", "Water", "Oxygen", "Hydrogen"], 1),
        ("Which Indian city is known as the Silicon Valley of India?", ["Mumbai", "Chennai", "Hyderabad", "Bangalore"], 3),
        ("In which year did India become independent?", ["1945", "1947", "1950", "1942"], 1),
    ]

    for i, (q, opts, ans) in enumerate(questions, 1):
        correct = ask_question(i, q, opts, ans, lifelines)
        if correct:
            score += 10000
        time.sleep(1)

    print("\n" + "="*50)
    print(f"\n🎉 Thank you for playing, {name}!")
    print(f"💰 Your total winnings: ₹{score}")
    print("\n" + "="*50)

if __name__ == '__main__':
    play_kbc()

