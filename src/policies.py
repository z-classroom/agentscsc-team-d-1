from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, List
import re

@dataclass
class PolicyResult:
    action: str               # "ALLOW" or "REFUSE"
    matched_rules: List[str]
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {"action": self.action, "matched_rules": self.matched_rules, "notes": self.notes}

class PolicyEngine:
    def __init__(self, policy_yaml: Dict[str, Any]) -> None:
        self.rules = policy_yaml.get("rules", [])
        self.overrides = policy_yaml.get("response_overrides", {"blocked": "REFUSE", "safe": "ALLOW"})

    def evaluate(self, user_text: str) -> PolicyResult:
<<<<<<< HEAD
        matched = []
=======

        if not user_text.strip():
            return PolicyResult(
                action="REFUSE",
                matched_rules=["invalid_input"],
                notes="Blank input rejected.",
            )

        if len(user_text) > 2000:
            return PolicyResult(
                action="REFUSE",
                matched_rules=["input_too_long"],
                notes="Input exceeds maximum length.",
            )

        matched = []

>>>>>>> db61cddc466cd0768128c8939d5b9488d5137b34
        for r in self.rules:
            for pat in r.get("block_patterns", []):
                if re.search(pat, user_text, flags=re.IGNORECASE):
                    matched.append(r.get("id", "unknown"))
                    break

        if matched:
<<<<<<< HEAD
            return PolicyResult(action=self.overrides.get("blocked", "REFUSE"),
                                matched_rules=matched,
                                notes="Blocked by policy patterns.")
        return PolicyResult(action=self.overrides.get("safe", "ALLOW"),
                            matched_rules=[],
                            notes="No policy match.")
=======
            return PolicyResult(
                action=self.overrides.get("blocked", "REFUSE"),
                matched_rules=matched,
                notes="Blocked by policy patterns.",
            )

        return PolicyResult(
            action=self.overrides.get("safe", "ALLOW"),
            matched_rules=[],
            notes="No policy match.",
        )
>>>>>>> db61cddc466cd0768128c8939d5b9488d5137b34
