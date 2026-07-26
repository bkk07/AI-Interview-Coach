from chains.question_chain import question_chain
from chains.feedback_chain import feedback_chain
from utils.display import display_feedback
from models.feedback import Feedback
from models.session import InterviewRound
from chains.report_chain import report_chain

from models.session import InterviewSession


class InterviewManager:

    def __init__(self):
        self.question_chain = question_chain
        self.feedback_chain = feedback_chain
        self.session = None
        self.report_chain = report_chain

    def start_session(self):

        print("===== AI Interview Coach =====")

        # Difficulty
        print("\nChoose Difficulty")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        difficulties = {
            "1": "Easy",
            "2": "Medium",
            "3": "Hard",
        }

        choice = input("Enter choice: ")
        difficulty = difficulties.get(choice)

        if difficulty is None:
            print("Invalid choice")
            return

        # Company
        company = input("\nEnter Company: ")

        # Create Interview Session
        self.session = InterviewSession(
            difficulty=difficulty,
            company=company,
        )

        # Start Interview
        for round_number in range(1, 6):
            print(f"\n========== Round {round_number} ==========")
            self.run_round()

        self.generate_final_report()

    def run_round(self):

        domain = self.choose_domain()

        question = self.generate_question(domain)

        print("\nQuestion:")
        print(question.question_text)

        answer = self.get_answer()

        feedback = self.evaluate_answer(question, answer)

        self.display_feedback(feedback)

        self.store_round(question, answer, feedback)

    def generate_question(self, domain):

        question = self.question_chain.invoke(
            {
                "domain": domain,
                "difficulty": self.session.difficulty,
                "round": self.session.company,
            }
        )

        return question

    def get_answer(self):

        print("\nEnter your answer (type END on a new line when finished):")

        lines = []

        while True:
            line = input()

            if line.strip().upper() == "END":
                break

            lines.append(line)

        return "\n".join(lines)

    def evaluate_answer(self, question, answer):
        print("==============DEBUG=============")
        print(f"Question: {question.question_text}")
        print(f"Answer: {answer}")

        if not answer.strip():
            return Feedback(
                score=0,
                strengths=["No answer was submitted."],
                weaknesses=["The response is empty, so no solution approach, code, complexity analysis, or edge cases can be evaluated."],
                missing_concepts=["A correct algorithm for the problem.", "Time and space complexity analysis.", "Edge case handling."],
                ideal_answer="Use Kadane's algorithm: scan the array once, keep the best subarray sum ending at the current index, and update the global maximum. This runs in O(n) time and O(1) space.",
                improvement_suggestions=["Submit at least a brief approach before typing END.", "Include the algorithm, complexity, and important edge cases."],
            )

        feedback = self.feedback_chain.invoke({
            "question": question.question_text,
            "answer": answer,
            }
        )
        return feedback

    def display_feedback(self, feedback):
        display_feedback(feedback);

    def store_round(self, question, answer, feedback):
        interview_round = InterviewRound(
                question=question,
                answer=answer,
                feedback=feedback,
            )
        self.session.rounds.append(interview_round)

    def generate_final_report(self):

        report = self.report_chain.invoke(
            {
                "session": self.session.model_dump_json(indent=4)
            }
        )

        print("\n")
        print("=" * 60)
        print("FINAL INTERVIEW REPORT")
        print("=" * 60)

        print(f"\nOverall Score: {report.overall_score}/100")

        print("\nSummary")
        print(report.summary)

        print("\nStrengths")
        for item in report.strengths:
            print(f"✔ {item}")

        print("\nWeaknesses")
        for item in report.weaknesses:
            print(f"✘ {item}")

        print("\nRecommendations")
        for item in report.recommendations:
            print(f"• {item}")


    def choose_domain(self):
        
        print("\nChoose Domain")
        print("1. Arrays")
        print("2. Strings")
        print("3. Graphs")
        print("4. Trees")
        print("5. Dynamic Programming")

        domains = {
            "1": "Arrays",
            "2": "Strings",
            "3": "Graphs",
            "4": "Trees",
            "5": "Dynamic Programming",
        }

        while True:
            choice = input("Enter choice: ")

            if choice in domains:
                return domains[choice]
            
            print("Invalid choice. Please try again.")
