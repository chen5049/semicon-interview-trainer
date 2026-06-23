import pytest

from semicon_interview_trainer.quiz import (
    filter_questions,
    load_questions,
    select_questions,
)


def test_load_questions():
    questions = load_questions()
    assert len(questions) >= 23
    assert all(question.id for question in questions)


def test_filter_by_topic():
    questions = load_questions()
    result = filter_questions(questions, topic="diffusion")
    assert result
    assert all(question.topic == "diffusion" for question in result)


def test_filter_by_difficulty():
    questions = load_questions()
    result = filter_questions(questions, difficulty="beginner")
    assert result
    assert all(question.difficulty == "beginner" for question in result)


def test_filter_dry_etching_questions():
    questions = load_questions()
    result = filter_questions(questions, topic="dry-etching")

    assert len(result) == 15
    assert all(question.topic == "dry-etching" for question in result)


def test_dry_etching_difficulty_distribution():
    questions = load_questions()
    result = filter_questions(questions, topic="dry-etching")

    counts = {
        difficulty: sum(q.difficulty == difficulty for q in result)
        for difficulty in ("beginner", "intermediate", "advanced")
    }

    assert counts == {
        "beginner": 4,
        "intermediate": 7,
        "advanced": 4,
    }


def test_select_questions_is_repeatable():
    questions = load_questions()
    first = select_questions(questions, count=3, seed=42)
    second = select_questions(questions, count=3, seed=42)
    assert [q.id for q in first] == [q.id for q in second]


def test_select_questions_rejects_invalid_count():
    questions = load_questions()
    with pytest.raises(ValueError):
        select_questions(questions, count=0)
