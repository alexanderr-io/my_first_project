import re


# ── 1. Basic string reversal ──────────────────────────────────────────────────
def is_palindrome_basic(text: str) -> bool:
    """Check using simple string reversal."""
    cleaned = re.sub(r'[^a-z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]


# ── 2. Two-pointer approach ───────────────────────────────────────────────────
def is_palindrome_two_pointer(text: str) -> bool:
    """Check using two pointers (no extra string created)."""
    cleaned = re.sub(r'[^a-z0-9]', '', text.lower())
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


# ── 3. Recursive approach ─────────────────────────────────────────────────────
def is_palindrome_recursive(text: str) -> bool:
    """Check using recursion."""
    cleaned = re.sub(r'[^a-z0-9]', '', text.lower())

    def _check(s: str) -> bool:
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return _check(s[1:-1])

    return _check(cleaned)


# ── 4. Check if a number is a palindrome ─────────────────────────────────────
def is_palindrome_number(n: int) -> bool:
    """Check if an integer is a palindrome (no string conversion)."""
    if n < 0 or (n % 10 == 0 and n != 0):
        return False
    reversed_half = 0
    while n > reversed_half:
        reversed_half = reversed_half * 10 + n % 10
        n //= 10
    return n == reversed_half or n == reversed_half // 10


# ── 5. Find all palindromic substrings ───────────────────────────────────────
def find_palindromic_substrings(text: str) -> list[str]:
    """Return all unique palindromic substrings of length >= 2."""
    results = set()
    n = len(text)
    for i in range(n):
        for j in range(i + 2, n + 1):
            sub = text[i:j]
            cleaned = re.sub(r'[^a-z0-9]', '', sub.lower())
            if len(cleaned) >= 2 and cleaned == cleaned[::-1]:
                results.add(sub)
    return sorted(results, key=len, reverse=True)


# ── 6. Longest palindromic substring (expand-around-center) ──────────────────
def longest_palindrome(text: str) -> str:
    """Find the longest palindromic substring using expand-around-center."""
    if not text:
        return ""

    start, end = 0, 0

    def expand(l: int, r: int) -> tuple[int, int]:
        while l >= 0 and r < len(text) and text[l] == text[r]:
            l -= 1
            r += 1
        return l + 1, r - 1

    for i in range(len(text)):
        l1, r1 = expand(i, i)       # odd length
        l2, r2 = expand(i, i + 1)   # even length
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2

    return text[start:end + 1]


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    test_cases = [
        "racecar",
        "A man a plan a canal Panama",
        "hello",
        "Was it a car or a cat I saw",
        "Never odd or even",
        "Python",
    ]

    print("=" * 55)
    print(f"{'Input':<35} {'Result'}")
    print("=" * 55)
    for t in test_cases:
        result = "✓ Palindrome" if is_palindrome_basic(
            t) else "✗ Not a palindrome"
        print(f"{t:<35} {result}")

    print("\n── Number palindrome check ──────────────────────────")
    for n in [121, 1221, -121, 10, 0]:
        print(
            f"  {n:<10} → {'✓ Palindrome' if is_palindrome_number(n) else '✗ Not a palindrome'}")

    print("\n── Longest palindrome in 'babad' ────────────────────")
    print(f"  → '{longest_palindrome('babad')}'")

    print("\n── Palindromic substrings in 'raceacar' ─────────────")
    for s in find_palindromic_substrings("raceacar"):
        print(f"  → '{s}'")
