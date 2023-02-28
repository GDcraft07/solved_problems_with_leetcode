class Solution:  # Не моё решение! Идея решения взята вот отсюда -> https://www.programmersought.com/article/61074299490/
    def reverseParentheses(self, s):
        new_word = ['']
        for i in s:
            if i == '(':
                new_word.append('')
            elif i == ')':
                add = new_word.pop()[::-1]
                new_word[-1] += add
            else:
                new_word[-1] += i

        return new_word

#  Несколько дней сяжу на LeetCode. Пока это самая интересная задача. Пытался решить сам... Не получилось(
