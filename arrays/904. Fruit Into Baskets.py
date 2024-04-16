class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, max_fruits = 0, -1
        fruit_counter = Counter()

        for i in range(len(fruits)):
            fruit_counter[fruits[i]] += 1
            while left <= i and len(fruit_counter) > 2:
                fruit_counter[fruits[left]] -= 1
                if fruit_counter[fruits[left]] == 0:
                    del fruit_counter[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, i - left + 1)

        return max_fruits
