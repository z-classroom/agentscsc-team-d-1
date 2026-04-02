from __future__ import annotations
import os
from dataclasses import dataclass
from typing import Any, Dict, List

<<<<<<< HEAD
=======
from dotenv import load_dotenv
from openai import OpenAI


>>>>>>> db61cddc466cd0768128c8939d5b9488d5137b34
@dataclass
class LLMProvider:
    provider: str
    model: str

    @staticmethod
    def from_env_or_config(cfg: Dict[str, Any]) -> "LLMProvider":
<<<<<<< HEAD
        provider = os.getenv("LLM_PROVIDER") or cfg.get("llm_provider", "mock")
        model = os.getenv("LLM_MODEL") or cfg.get("llm_model", "mock-001")
=======
        # Load variables from the repo-root .env file, if present.
        # This makes both app.py and tests/stage2_test.py work automatically.
        load_dotenv()

        provider = os.getenv("LLM_PROVIDER") or cfg.get("llm_provider", "mock")
        model = os.getenv("LLM_MODEL") or cfg.get("llm_model", "gpt-4o-mini")
>>>>>>> db61cddc466cd0768128c8939d5b9488d5137b34
        return LLMProvider(provider=provider, model=model)

    def complete(
        self,
        system: str,
        messages: List[Dict[str, str]],
        user: str,
        refusal_prompt: str,
        mode: str = "normal",
    ) -> str:
<<<<<<< HEAD
        """
        Swap this with a real provider call.
        Keep the signature stable so students only change this file.
        """
        if self.provider == "mock":
            return self._mock_response(system, messages, user, refusal_prompt, mode)

        # Placeholder for real integrations:
        # - call your provider SDK
        # - pass system + messages + user
        # - return text
        raise NotImplementedError(
            "Non-mock provider not configured. Edit src/llm_provider.py to add your LLM call."
        )

    def _mock_response(
        self, system: str, messages: List[Dict[str, str]], user: str, refusal_prompt: str, mode: str
=======
        if self.provider == "mock":
            return self._mock_response(system, messages, user, refusal_prompt, mode)

        if self.provider == "openai":
            return self._openai_response(system, messages, user, refusal_prompt, mode)

        raise ValueError(f"Unsupported LLM provider: {self.provider}")

    def _openai_response(
        self,
        system: str,
        messages: List[Dict[str, str]],
        user: str,
        refusal_prompt: str,
        mode: str,
    ) -> str:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY is missing. Add it to your .env file at the repo root."
            )

        client = OpenAI(api_key=api_key)

        chat_messages: List[Dict[str, str]] = []
        chat_messages.append({"role": "system", "content": system})

        # Memory/history messages from your agent
        for msg in messages:
            chat_messages.append(msg)

        # For refusals, add an extra system instruction to shape the refusal tone
        if mode == "refusal":
            chat_messages.append({"role": "system", "content": refusal_prompt})

        # Current user turn
        chat_messages.append({"role": "user", "content": user})

        response = client.chat.completions.create(
            model=self.model,
            messages=chat_messages,
            temperature=0.3,
        )

        text = response.choices[0].message.content
        return text.strip() if text else ""

    def _mock_response(
        self,
        system: str,
        messages: List[Dict[str, str]],
        user: str,
        refusal_prompt: str,
        mode: str,
>>>>>>> db61cddc466cd0768128c8939d5b9488d5137b34
    ) -> str:
        if mode == "refusal":
            return (
                "I can’t help with that request.\n"
                "Reason: it appears to violate a course policy for safe/ethical behavior.\n"
                "Safe alternatives: I can explain the risks, provide defensive best practices, or help reframe the task."
            )

<<<<<<< HEAD
        # Simple “agent-like” behavior for offline testing
=======
>>>>>>> db61cddc466cd0768128c8939d5b9488d5137b34
        if "summarize" in user.lower():
            return "Summary (mock): I can summarize once you paste the text or describe the source."
        if "recommend" in user.lower():
            return "Recommendation (mock): Tell me your goal + constraints, and I’ll suggest options."
<<<<<<< HEAD
        return "Response (mock): I understand. Say 'summarize', 'recommend', or ask a specific question."
=======
        return "Response (mock): I understand. Say 'summarize', 'recommend', or ask a specific question."
>>>>>>> db61cddc466cd0768128c8939d5b9488d5137b34
