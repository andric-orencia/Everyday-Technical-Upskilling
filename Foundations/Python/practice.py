"""Learn-as-you-go practice file. Write your code below, then run:

    python Foundations\\Python\\practice.py
"""


def has_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


def first_repeat(s):
    """Return the first character that appears a second time, else None."""
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return None


if __name__ == "__main__":
    print(has_duplicate([1, 2, 3, 1]))   # expect True
    print(has_duplicate([1, 2, 3]))      # expect False
    print(first_repeat("abcab"))         # expect a
    print(first_repeat("abcd"))          # expect None
    print(first_repeat(""))              # expect None
    print(first_repeat("aabb"))          # expect a
