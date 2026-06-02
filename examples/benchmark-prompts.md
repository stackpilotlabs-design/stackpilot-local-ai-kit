# Benchmark Prompts

Versioned prompts used for qualitative benchmark testing across all models in this repository.

**How to use:**
1. Set LM Studio to the settings in [`docs/00-methodology.md`](../docs/00-methodology.md) (no system prompt, temperature 0.7, context 4096)
2. Paste the prompt below exactly as written into a **new chat session**
3. Record the result in `docs/10-benchmarks.md` using the format: Pass / Partial / Fail with a short observation note
4. When citing which prompt you used, refer to the section name and version (e.g. "Coding Benchmark v1")

---

## Coding Benchmark v1

```
Write a Python function called `flatten_dict` that takes a nested dictionary and returns a flat dictionary with dot-separated keys.

Example:
Input:  {"a": {"b": {"c": 1}, "d": 2}, "e": 3}
Output: {"a.b.c": 1, "a.d": 2, "e": 3}

Requirements:
- Handle arbitrarily deep nesting
- Handle empty dicts
- Include a docstring
- Include at least two test cases using assert statements at the bottom of the file
```

**What to look for:**
- Does it produce syntactically correct Python?
- Does the function handle the nested case correctly?
- Does it handle the edge case (empty dict)?
- Are the assert statements correct and do they pass?

---

## Refactoring Benchmark v1

```
Refactor the following Python code. Improve readability, remove duplication, and add type hints. Do not change the function's external behaviour.

    def process(data):
        result = []
        for i in range(len(data)):
            if data[i] > 0:
                result.append(data[i] * 2)
            elif data[i] < 0:
                result.append(data[i] * -1)
            else:
                result.append(0)
        return result
```

**What to look for:**
- Does it add correct type hints?
- Does it reduce the loop to a more Pythonic style (e.g. list comprehension or `abs`)?
- Does the refactored code produce identical output to the original?
- Does it preserve or improve readability?

---

## Reasoning Benchmark v1

```
A farmer has 17 sheep. All but 9 die. How many sheep does the farmer have left?

Show your reasoning step by step before giving the final answer.
```

**What to look for:**
- Does it get the correct answer (9)?
- Does it reason through the ambiguity of "all but 9" correctly, or does it calculate 17 - 9 = 8?
- Is the reasoning shown, or does it jump straight to an answer?

> This is a classic misdirection problem. Correct answer: 9 (because "all but 9 die" means 9 survive). A confident wrong answer of 8 is a meaningful failure signal.

---

## Prompt Changelog

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-05-31 | Initial prompts defined for coding, refactoring, and reasoning |
