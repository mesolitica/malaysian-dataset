## Overview
This dataset contains over 1,000 questions and answers focused on Malay language grammar (tatabahasa), tailored for primary school students aged 7 to 12. The dataset is designed to aid in educational research, language learning applications, and to benchmark the performance of Large Language Models (LLMs) on Malay language understanding and processing.

## Dataset Description
The dataset is organized in JSON Lines (JSONL) format, where each line is a JSON object representing a single question. Each JSON object contains the following fields:

- instruction: Instructions for the question.
- question: The question.
- choices: A dictionary of answer choices, where each key is an option identifier (e.g., "A", "B") and the value is a dictionary containing:
  - text: The text of the answer choice.
  - answer: A boolean indicating whether the choice is the correct answer.