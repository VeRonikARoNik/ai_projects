# AI Translators Suite

**AI Translators Suite** is a repository that contains two machine translation projects built with the Hugging Face Transformers library.

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

1. **Polish-to-English Translator**
   - **File:** `pl_to_en.py`
   - **Description:** Translates text from Polish to English using the `Helsinki-NLP/opus-mt-pl-en` model.
   - **Features:** Interactive command-line interface (CLI) with options for configuring decoding parameters (e.g., `max_length`, `num_beams`).

2. **English-to-Chinese and English-to-Russian Translator**
   - **File:** `en_to_zh_ru.py`
   - **Description:** Translates English text into Chinese and Russian using the T5-based model `utrobinmv/t5_translate_en_ru_zh_small_1024`.
   - **Features:** Simultaneously provides translations into two target languages through an interactive CLI.

## Requirements

- Python 3.7 or later
- Libraries: `transformers`, `torch`
- (Optional) GPU with CUDA support if you wish to leverage GPU acceleration.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/ai-translators-suite.git
   cd ai-translators-suite
