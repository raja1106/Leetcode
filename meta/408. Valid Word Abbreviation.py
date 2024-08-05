class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Initialize pointers for word and abbreviation
        word_index = 0
        abbr_index = 0

        # Get lengths of word and abbreviation
        word_length = len(word)
        abbr_length = len(abbr)

        # Loop through the characters in the word
        while word_index < word_length:
            # Check if abbreviation index has become out of bound
            if abbr_index >= abbr_length:
                return False

            # If current characters match, move to the next ones
            if word[word_index] == abbr[abbr_index]:
                word_index += 1
                abbr_index += 1
                continue

            # Check if abbreviation character is not a digit
            if not abbr[abbr_index].isdigit():
                return False

            # Calculate the number representing the skipped characters
            num_start_index = abbr_index
            while abbr_index < abbr_length and abbr[abbr_index].isdigit():
                abbr_index += 1
            num_str = abbr[num_start_index:abbr_index]

            # Leading zero or invalid number check
            if num_str[0] == '0':
                return False

            # Move the word index forward by the number of skipped characters
            word_index += int(num_str)

        # If we've reached the end of both the word and the abbreviation, the abbreviation is valid
        return word_index == word_length and abbr_index == abbr_length
class Solution1:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Initialize pointers for word and abbreviation
        word_index = 0
        abbr_index = 0

        # Get lengths of word and abbreviation
        word_length = len(word)
        abbr_length = len(abbr)

        # Loop through the characters in the word
        while word_index < word_length and abbr_index < abbr_length:
            # If current characters match, move to the next ones
            if word[word_index] == abbr[abbr_index]:
                word_index += 1
                abbr_index += 1
                continue
            elif not abbr[abbr_index].isdigit():
                return False

            # Calculate the number representing the skipped characters
            num_start_index = abbr_index
            while abbr_index < abbr_length and abbr[abbr_index].isdigit():
                abbr_index += 1
            num_str = abbr[num_start_index:abbr_index]

            # Leading zero or invalid number check
            if num_str[0] == '0':
                return False

            # Move the word index forward by the number of skipped characters
            word_index += int(num_str)

        # If we've reached the end of both the word and the abbreviation, the abbreviation is valid
        return word_index == word_length and abbr_index == abbr_length
