from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from string import punctuation


class WorkParser:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        #self.vacancy_cards = []
        self.raw_salaries = []
        self.middle_salary = 0

    def scroll_through_pages(self):
        while True:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "pjax-jobs-list")))

            vacancy_container = self.driver.find_element(By.ID, "pjax-jobs-list")
            cards = vacancy_container.find_elements(By.CLASS_NAME, "wordwrap")

            for i in cards:
                try:
                    box_salaries = i.find_elements(By.CLASS_NAME, "strong-600")
                    for j in box_salaries:
                        if "грн" not in j.text:
                            continue
                        self.raw_salaries.append(j.text)
                except Exception as ex:
                    print("Ошибка доступа к элементу:", ex)

            try:
                next_page = self.driver.find_element(By.LINK_TEXT, "Наступна")
                if "disabled" in next_page.get_attribute("class"):
                    break
                next_page.click()

                WebDriverWait(self.driver, 10).until(EC.staleness_of(cards[0]))
            except:
                break

    def collect_vacancy_cards(self):
        self.driver.get(self.url)
        self.scroll_through_pages()

    def remove_symbol(self, text):
        cyrillic_letters = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
        letters = cyrillic_letters + cyrillic_letters.upper()
        punct_to_remove = punctuation.replace("-", " ")
        symbols = ['\u202f', '\u2009', ' ']

        for i in symbols:
            text = text.replace(i, '')
        for l in text:
            if l in letters or l in punct_to_remove:
                text = text.replace(l, '')
        return text

    def calculate_average_salary(self):
        salaries = []

        for i in self.raw_salaries:
            text = i.strip()
            # if not any(c.isdigit() for c in text):
            #     continue

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
        print(len(salaries))

        if salaries:
            self.middle_salary = round(sum(salaries) / len(salaries))
        else:
            self.middle_salary = 0

    def run(self):
        self.collect_vacancy_cards()
        self.calculate_average_salary()
        self.scroll_through_pages()
        self.close()
        print(f"Средняя зарплата: {self.middle_salary}")

    def close(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    url = "https://www.work.ua/jobs-odesa-it"
    parser = WorkParser(url)
    parser.run()
