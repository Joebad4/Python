questions = [ 
    { 
        "question": "What is the capital of France?", 
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": 3
        },
    
    { "question": "What is the capital of Germany?",
      "options": ["Berlin", "Lisbon", "Madrid", "Paris"], 
      "answer": 1
        },
    
    { "question": "What is the capital of Spain?",
      "options": ["Lisbon", "Madrid", "Rome", "Berlin"],
      "answer": 2
        },
    
    { "question": "What is the capital of Italy?", 
      "options": ["Rome", "Madrid", "Paris", "Berlin"], 
      "answer": 1 
        }, 
    
    { "question": "What is the capital of Portugal?",
      "options": ["Madrid", "Lisbon", "Paris", "Rome"], 
      "answer": 2
        } 
] 

def welcome_message():
    print("Welcome to the Geography Quiz!")
    
def display_questions():
    score = 0 
    for idx, question in enumerate(questions):
      print(f"\nQuestion {idx + 1}: {question['question']}")
    for i, option in enumerate(question["options"], start=1):
      print(f"{i}. {option}")
      
      user_answer = get_user_input(len(question["options"])) 
      
      if user_answer == question["answer"]:
            score += 1 
            print("Correct!") 
      else: print("Incorrect.")
      
    return score 

def get_user_input(num_options):
    while True:
      try:
          choice = int(input("Enter your answer (1-4): "))
          if 1 <= choice <= num_options:
              return choice 
          else: 
              print("Please enter a number within the range.")
      except ValueError:
              print("Invalid input. Please enter a number.")

def display_results(score, total_questions):
      print("\nQuiz Completed!")
      print(f"Your Score: {score} out of {total_questions}")
  
      if score == total_questions:
        print("Excellent! You got everything right!")
      elif score >= total_questions / 2:
        print("Good job! You passed the quiz.")
      else: print("Better luck next time!") 
    
def thank_you_message():
    print("Thank you for taking the quiz!")

def run_quiz():
    welcome_message()
    score = display_questions()
    display_results(score, len(questions)) 
    thank_you_message() 
    
run_quiz()