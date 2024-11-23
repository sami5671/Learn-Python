import json

class QuizManager:
    def __init__(self, questions_file):
        self.questions = self.load_questions(questions_file)
        self.current_question_index = 0
        self.score = 0

    def load_questions(self, file_path):
        """Load questions from a JSON file."""
        with open(file_path, 'r') as file:
            questions = json.load(file)
        return questions

    def get_next_question(self):
        """Return the next question and its options, or None if quiz is over."""
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question_data
        return None

    def check_answer(self, selected_option):
        """Check if the selected answer is correct."""
        correct_option = self.questions[self.current_question_index - 1]["answer"]
        if selected_option == correct_option:
            self.score += 1
            return True
        return False
