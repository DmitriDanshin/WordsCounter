
class Counter:
    def __init__(self, text, divider):
        self.text = text,
        self.divider = divider

    def count_words(self):
        text = self.text[0]

        for i in self.divider:
            self.text = text.replace(i, ' ')

        words = list(filter(None, text.split()))

        unique = {}
        for word in words:
            try:
                unique[word] += 1
            except KeyError:
                unique[word] = 1

        return unique
