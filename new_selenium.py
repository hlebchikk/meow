from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from string import punctuation


class WorkParser:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.vacancy_cards = []
        self.middle_salary = 0

    def open_page(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 3)
        vacancy_container = self.driver.find_element(By.ID, "pjax-jobs-list")
        self.vacancy_cards = vacancy_container.find_elements(By.CLASS_NAME, "card")

    def remove_symbol(self, text):
        cyrillic_letters = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
        letters = cyrillic_letters + cyrillic_letters.upper()
        punct_to_remove = punctuation.replace("-", " ")
        symbols = ['\u202f', '\u2009', ' ']

        for s in symbols:
            text = text.replace(s, '')
        for l in text:
            if l in letters or l in punct_to_remove:
                text = text.replace(l, '')
        return text

    def calculate_average_salary(self):
        raw_salaries = []

        for card in self.vacancy_cards:
            strong_600 = card.find_elements(By.CLASS_NAME, "strong-600")
            for el in strong_600:
                if "грн" not in el.text:
                    continue
                raw_salaries.append(el.text)

        salaries = []

        for text in raw_salaries:
            text = text.strip()
            if not any(ch.isdigit() for ch in text):
                continue

            text = text.replace("–", "-")
            text = self.remove_symbol(text)
            digits_text = text.split("-")

            try:
                digits = list(map(int, digits_text))
            except ValueError as ex:
                print("Ошибка преобразования:", ex)
                continue

            if digits:
                if len(digits) > 1:
                    salary = sum(digits) / len(digits)
                else:
                    salary = digits[0]
                salaries.append(salary)

        print(salaries)

        if salaries:
            self.middle_salary = round(sum(salaries) / len(salaries))
        else:
            self.middle_salary = 0

    def run(self):
        self.open_page()
        self.calculate_average_salary()
        self.close()
        print(f"Средняя зарплата: {self.middle_salary}")

    def close(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    url = "https://www.work.ua/jobs-odesa-it"
    parser = WorkParser(url)
    parser.run()
