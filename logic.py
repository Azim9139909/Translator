# Задание №3
from translate import Translator
from collections import defaultdict

# Задание №5
questions = {
    "как тебя зовут": "Я супер-крутой-бот и моё предназначение помогать тебе!",
    "сколько тебе лет": "Это слишком философский вопрос",
}


class TextAnalysis:

    # Задание №1
    memory = defaultdict(list)

    def __init__(self, text, owner):
        # Задание №2
        TextAnalysis.memory[owner].append(self)
        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")

        # Задание №6
        key = self.text.lower().strip(" ?!.")
        if key in questions:
            self.response = questions[key]
        else:
            self.response = self.get_answer()

    def get_answer(self):
        return f"Перевод: {self.translation}"

    def __translate(self, text, from_lang, to_lang):
        try:
            # Задание №4
            t = Translator(from_lang=from_lang, to_lang=to_lang)
            return t.translate(text)
        except Exception:
            return "Перевод не удался"
