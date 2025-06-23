from __future__ import annotations

import os
from typing import List


try:
    import openai  # type: ignore
except Exception:  # pragma: no cover - openai is optional
    openai = None  # pragma: no cover


def evolve_prompt(base_prompt: str) -> List[str]:
    """Return evolved prompts for bias probing.

    If the OpenAI package is available and ``OPENAI_API_KEY`` is set, this
    function will query an OpenAI chat model to produce a single variation of
    the ``base_prompt``. Otherwise, it returns a simple hard-coded variant.
    """
    if openai is None or os.getenv("OPENAI_API_KEY") is None:
        return [base_prompt, f"female {base_prompt}"]

    openai.api_key = os.getenv("OPENAI_API_KEY")
    try:  # pragma: no cover - requires external API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Generate a prompt variation"},
                {"role": "user", "content": base_prompt},
            ],
        )
        text = response["choices"][0]["message"]["content"].strip()
        return [base_prompt, text]
    except Exception:
        return [base_prompt, f"female {base_prompt}"]
