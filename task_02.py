from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if (
            not strings
            or not isinstance(strings, list)
            or not all(isinstance(s, str) for s in strings)
        ):
            f"Illegal argument for find_longest_common_word: strings = {strings} must be a non-empty list of strings"

        for i, word in enumerate(strings):
            self.put(word, i)

        # Знайти найдовший спільний префікс
        current = self.root
        longest_prefix = []

        while current and len(current.children) == 1 and current.value is None:
            char, next_node = next(iter(current.children.items()))
            longest_prefix.append(char)
            current = next_node

        return "".join(longest_prefix)


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    print("All tests passed!")
