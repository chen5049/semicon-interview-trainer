from pathlib import Path

import pytest

from semicon_interview_trainer.quiz import (
    filter_questions,
    load_questions,
    select_questions,
)


def test_load_questions():
    questions = load_questions()
    assert len(questions) >= 5
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


def test_select_questions_is_repeatable():
    questions = load_questions()
    first = select_questions(questions, count=3, seed=42)
    second = select_questions(questions, count=3, seed=42)
    assert [q.id for q in first] == [q.id for q in second]


def test_select_questions_rejects_invalid_count():
    questions = load_questions()
    with pytest.raises(ValueError):
        select_questions(questions, count=0)
