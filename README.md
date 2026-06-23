# Semicon Interview Trainer

A lightweight, open-source interview practice tool for semiconductor process engineering roles.

It includes bilingual English / Traditional Chinese questions covering:

- Photolithography / 微影
- Diffusion and ion implantation / 擴散與離子佈植
- Etching / 蝕刻
- Dry Etching / 乾式蝕刻
- Thin films / 薄膜
- Defect analysis and root-cause investigation / 缺陷分析與根因調查

## Why this project exists

Semiconductor interviews often require candidates to explain process concepts clearly in both technical English and Mandarin. This project provides a structured question bank, a command-line quiz, and a simple scoring system for repeated practice.

## Features

- Randomised interview questions
- English and Traditional Chinese prompts
- Topic filtering
- Difficulty filtering
- Immediate reference answers
- Score tracking
- 23 bilingual interview questions, including a 15-question Dry Etching module
- JSON-based question bank that is easy to expand
- Automated tests and GitHub Actions CI

## Installation

```bash
git clone https://github.com/chen5049/semicon-interview-trainer.git
cd semicon-interview-trainer
python -m pip install -e .
```

## Usage

Start a five-question mixed quiz:

```bash
semicon-trainer quiz
```

Choose a topic:

```bash
semicon-trainer quiz --topic lithography
```

Practise the Dry Etching module:

```bash
semicon-trainer quiz --topic dry-etching --language zh-TW --count 5
```

Choose language and difficulty:

```bash
semicon-trainer quiz --language zh-TW --difficulty intermediate
```

List available topics:

```bash
semicon-trainer topics
```

## Example

```text
Topic: diffusion
Difficulty: intermediate

問題：
什麼是 slip line？它通常在什麼情況下形成？

Press Enter to reveal the reference answer...
```

## Project structure

```text
semicon-interview-trainer/
├─ src/semicon_interview_trainer/
├─ data/questions.json
├─ tests/
├─ .github/workflows/ci.yml
├─ CONTRIBUTING.md
├─ SECURITY.md
└─ LICENSE
```

## Contributing

Contributions are welcome. Good first contributions include:

- Adding verified interview questions
- Improving Traditional Chinese semiconductor terminology
- Adding references
- Adding new process modules
- Improving scoring and study modes

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

## Roadmap

- Web interface
- Spaced-repetition mode
- User progress storage
- Additional modules for CMP, metrology, yield and equipment engineering
- Exportable mock interview reports

## Licence

MIT
