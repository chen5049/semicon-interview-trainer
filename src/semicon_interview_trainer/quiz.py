from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
import json
import random


@dataclass(frozen=True)
class Question:
    id: str
    topic: str
    difficulty: str
    prompt_en: str
    prompt_zh_tw: str
    answer_en: str
    answer_zh_tw: str

    def prompt(self, language: str) -> str:
        return self.prompt_zh_tw if language == "zh-TW" else self.prompt_en

    def answer(self, language: str) -> str:
        return self.answer_zh_tw if language == "zh-TW" else self.answer_en


def default_question_path() -> Path:
    return Path(__file__).resolve().parents[2] / "data" / "questions.json"


def load_questions(path: Path | None = None) -> list[Question]:
    source = path or default_question_path()
    with source.open("r", encoding="utf-8") as f:
        raw = json.load(f)

    required = {
        "id",
        "topic",
        "difficulty",
        "prompt_en",
        "prompt_zh_tw",
        "answer_en",
        "answer_zh_tw",
    }

    questions: list[Question] = []
    for item in raw:
        missing = required - item.keys()
        if missing:
            raise ValueError(
                f"Question {item.get('id', '<unknown>')} is missing fields: "
                f"{', '.join(sorted(missing))}"
            )
        questions.append(Question(**{key: item[key] for key in required}))

    return questions


def filter_questions(
    questions: Iterable[Question],
    topic: str | None = None,
    difficulty: str | None = None,
) -> list[Question]:
    result = list(questions)

    if topic:
        result = [q for q in result if q.topic == topic]

    if difficulty:
        result = [q for q in result if q.difficulty == difficulty]

    return result


def select_questions(
    questions: Iterable[Question],
    count: int,
    seed: int | None = None,
) -> list[Question]:
    pool = list(questions)
    if count <= 0:
        raise ValueError("count must be greater than zero")
    if count > len(pool):
        raise ValueError(
            f"Requested {count} questions, but only {len(pool)} are available"
        )

    rng = random.Random(seed)
    return rng.sample(pool, count)
