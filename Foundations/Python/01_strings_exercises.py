"""
Python Foundations - Exercise set 01: Strings & f-strings

How to use
----------
1. Replace each `raise NotImplementedError` with your own solution.
2. Run:  python 01_strings_exercises.py
3. Each exercise prints PASS / FAIL. Keep going until everything is green.

Rules: no looking things up for the "core" ones, and no peeking at the tests
to reverse-engineer the answer. Hints are at the bottom of each docstring.
"""


# --- Exercise 1: slicing ---------------------------------------------------
def last_n(s: str, n: int) -> str:
    """Return the last n characters of s. If n >= len(s), return s.
    last_n("python", 3) -> "hon"
    Hint: negative indices, but watch out for n == 0.
    """
    raise NotImplementedError


# --- Exercise 2: reverse + palindrome --------------------------------------
def is_palindrome(s: str) -> bool:
    """Case-insensitive, ignoring anything that isn't a letter or digit.
    is_palindrome("A man, a plan, a canal: Panama") -> True
    Hint: str.isalnum(), str.lower(), and the [::-1] slice.
    """
    raise NotImplementedError


# --- Exercise 3: split / join ----------------------------------------------
def title_words(sentence: str) -> str:
    """Capitalise the first letter of each word and collapse extra whitespace.
    title_words("  hello    big   world ") -> "Hello Big World"
    Hint: split() with no argument, then " ".join(...).
    """
    raise NotImplementedError


# --- Exercise 4: counting --------------------------------------------------
def count_vowels(s: str) -> int:
    """Count vowels (a, e, i, o, u), case-insensitive.
    count_vowels("Interview") -> 4
    """
    raise NotImplementedError


# --- Exercise 5: f-string formatting ---------------------------------------
def receipt_line(item: str, qty: int, price: float) -> str:
    """Format as: item left-aligned in 10 chars, qty zero-padded to 3 digits,
    and the total (qty * price) with a thousands separator and 2 decimals.
    receipt_line("Pen", 5, 1.5)     -> "Pen        |005|7.50"
    receipt_line("Laptop", 2, 999.99) -> "Laptop     |002|1,999.98"
    Hint: f"{item:<10}|{qty:03d}|{total:,.2f}"
    """
    raise NotImplementedError


# --- Exercise 6: building strings efficiently ------------------------------
def compress(s: str) -> str:
    """Run-length encode. Use a list + "".join, NOT repeated +=.
    compress("aaabccdddd") -> "a3b1c2d4"
    compress("") -> ""
    """
    raise NotImplementedError


# --- Exercise 7: interview classic -----------------------------------------
def is_anagram(a: str, b: str) -> bool:
    """True if a and b use exactly the same letters (case-insensitive,
    ignore spaces).
    is_anagram("Dormitory", "dirty room") -> True
    Hint: sorted(...) or collections.Counter.
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Tests - do not edit below this line
# ---------------------------------------------------------------------------
TESTS = [
    ("last_n", last_n, [
        (("python", 3), "hon"),
        (("python", 0), ""),
        (("hi", 10), "hi"),
        (("", 2), ""),
    ]),
    ("is_palindrome", is_palindrome, [
        (("A man, a plan, a canal: Panama",), True),
        (("hello",), False),
        (("",), True),
        (("No 'x' in Nixon",), True),
    ]),
    ("title_words", title_words, [
        (("  hello    big   world ",), "Hello Big World"),
        (("a",), "A"),
        (("",), ""),
    ]),
    ("count_vowels", count_vowels, [
        (("Interview",), 4),
        (("rhythm",), 0),
        (("AEIOU",), 5),
    ]),
    ("receipt_line", receipt_line, [
        (("Pen", 5, 1.5), "Pen        |005|7.50"),
        (("Laptop", 2, 999.99), "Laptop     |002|1,999.98"),
    ]),
    ("compress", compress, [
        (("aaabccdddd",), "a3b1c2d4"),
        (("",), ""),
        (("z",), "z1"),
    ]),
    ("is_anagram", is_anagram, [
        (("Dormitory", "dirty room"), True),
        (("abc", "abd"), False),
        (("", ""), True),
    ]),
]


def run_tests() -> None:
    passed_exercises = 0
    for name, fn, cases in TESTS:
        failures = []
        for args, expected in cases:
            try:
                got = fn(*args)
            except NotImplementedError:
                failures.append("not implemented yet")
                break
            except Exception as exc:  # noqa: BLE001
                failures.append(f"{args!r} raised {type(exc).__name__}: {exc}")
                continue
            if got != expected:
                failures.append(f"{args!r}: expected {expected!r}, got {got!r}")
        if failures:
            print(f"FAIL  {name}")
            for f in failures:
                print(f"        - {f}")
        else:
            print(f"PASS  {name}")
            passed_exercises += 1
    print(f"\n{passed_exercises}/{len(TESTS)} exercises passing")


if __name__ == "__main__":
    run_tests()
