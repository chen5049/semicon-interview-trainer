from __future__ import annotations

import argparse
import sys

from .quiz import filter_questions, load_questions, select_questions


LANGUAGES = ("en", "zh-TW")
DIFFICULTIES = ("beginner", "intermediate", "advanced")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="semicon-trainer",
        description="Practice semiconductor process engineering interview questions.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    quiz_parser = subparsers.add_parser("quiz", help="Start an interactive quiz")
    quiz_parser.add_argument("--topic", help="Filter by topic")
    quiz_parser.add_argument(
        "--difficulty",
        choices=DIFFICULTIES,
        help="Filter by difficulty",
    )
    quiz_parser.add_argument(
        "--language",
        choices=LANGUAGES,
        default="en",
        help="Prompt and answer language",
    )
    quiz_parser.add_argument(
        "--count",
        type=int,
        default=5,
        help="Number of questions",
    )
    quiz_parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional random seed for repeatable quizzes",
    )

    subparsers.add_parser("topics", help="List available topics")
    return parser


def run_quiz(args: argparse.Namespace) -> int:
    questions = load_questions()
    filtered = filter_questions(
        questions,
        topic=args.topic,
        difficulty=args.difficulty,
    )

    if not filtered:
        print("No questions match the selected filters.", file=sys.stderr)
        return 2

    count = min(args.count, len(filtered))
    selected = select_questions(filtered, count=count, seed=args.seed)

    score = 0

    for index, question in enumerate(selected, start=1):
        print()
        print(f"[{index}/{len(selected)}] Topic: {question.topic}")
        print(f"Difficulty: {question.difficulty}")
        print()
        print(question.prompt(args.language))
        input("\nPress Enter to reveal the reference answer...")
        print()
        print(question.answer(args.language))
        rating = input(
            "\nDid your answer cover the key points? [y/n]: "
        ).strip().lower()
        if rating in {"y", "yes"}:
            score += 1

    print()
    print(f"Final score: {score}/{len(selected)}")
    return 0


def list_topics() -> int:
    questions = load_questions()
    topics = sorted({question.topic for question in questions})
    for topic in topics:
        print(topic)
    return 0


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "quiz":
        raise SystemExit(run_quiz(args))

    if args.command == "topics":
        raise SystemExit(list_topics())

    parser.error("Unknown command")


if __name__ == "__main__":
    main()
