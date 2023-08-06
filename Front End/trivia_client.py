import requests

def fetch_trivia_questions():
    url = "http://localhost:3000/api/trivia_questions"
    response = requests.get(url)
    if response.status_code == 200:
        trivia_questions = response.json()
        for question in trivia_questions:
            print("Question:", question["question"])
            print("Options:")
            options = ["option1", "option2", "option3"]
            for i, option in enumerate(options, 1):
                print(f"{i}. {question[option]}")
            
            user_answer = input("Enter the number of your choice (1, 2, or 3), or type 'stop' to exit: ")
            if user_answer.lower() == 'stop':
                print("Exiting the trivia game.")
                break

            try:
                user_choice = int(user_answer)
                if 1 <= user_choice <= 3:
                    selected_option = options[user_choice - 1]
                    if question[selected_option] == question["correct_answer"]:
                        print("Correct!\n")
                    else:
                        print("Incorrect. The correct answer is:", question["correct_answer"], "\n")
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.\n")
            except ValueError:
                print("Invalid input. Please enter a number or 'stop'.\n")
    else:
        print("Failed to fetch trivia questions. Status code:", response.status_code)

if __name__ == "__main__":
    fetch_trivia_questions()
