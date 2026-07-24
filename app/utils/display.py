from models.feedback import Feedback


def display_feedback(feedback: Feedback):
    print("\n" + "=" * 60)
    print("              INTERVIEW FEEDBACK")
    print("=" * 60)

    print(f"\n⭐ Score: {feedback.score}/10")

    print("\n✅ Strengths")
    for s in feedback.strengths:
        print(f"  • {s}")

    print("\n❌ Weaknesses")
    for w in feedback.weaknesses:
        print(f"  • {w}")

    print("\n📚 Missing Concepts")
    for m in feedback.missing_concepts:
        print(f"  • {m}")

    print("\n💡 Ideal Answer")
    print(feedback.ideal_answer)

    print("\n🚀 Improvement Suggestions")
    for s in feedback.improvement_suggestions:
        print(f"  • {s}")

    print("\n" + "=" * 60)