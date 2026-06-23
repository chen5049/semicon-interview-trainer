import pytest

from semicon_interview_trainer.quiz import (
    filter_questions,
    load_questions,
    select_questions,
)


def test_load_questions():
    questions = load_questions()
    assert len(questions) == 30
    assert all(question.id for question in questions)


def test_question_ids_are_unique():
    questions = load_questions()
    ids = [question.id for question in questions]
    assert len(ids) == len(set(ids))


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


def test_filter_ion_implantation_questions():
    questions = load_questions()
    result = filter_questions(questions, topic="ion-implantation")

    assert len(result) == 4
    assert all(question.topic == "ion-implantation" for question in result)


def test_diffusion_question_count():
    questions = load_questions()
    result = filter_questions(questions, topic="diffusion")

    assert len(result) == 5


def test_new_module_difficulty_distribution():
    questions = load_questions()
    new_ids = {
        "ion-implantation-001",
        "ion-implantation-002",
        "ion-implantation-003",
        "ion-implantation-004",
        "diffusion-003",
        "diffusion-004",
        "diffusion-005",
    }
    result = [q for q in questions if q.id in new_ids]

    counts = {
        difficulty: sum(q.difficulty == difficulty for q in result)
        for difficulty in ("beginner", "intermediate", "advanced")
    }

    assert counts == {
        "beginner": 2,
        "intermediate": 3,
        "advanced": 2,
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
