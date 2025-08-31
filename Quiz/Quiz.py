import datetime
import time


class Question:
    def __init__(self, question, choices, answer):
        if not isinstance(question, str) or not question.strip():
            raise ValueError("Soru metni boş olamaz.")
        if not isinstance(choices, list) or len(choices) < 2:
            raise ValueError("En az 2 seçenek olmalıdır.")
        if answer not in choices:
            raise ValueError("Doğru cevap seçenekler arasında olmalıdır.")

        self.question = question.strip()
        self.choices = [choice.strip() for choice in choices]
        self.answer = answer.strip()

    def check_answer(self, answer):
        return self.answer.lower() == answer.strip().lower()


class Quiz:
    def __init__(self, questions):
        if not questions:
            raise ValueError("En az bir soru gereklidir.")
        self.questions = questions
        self.score = 0
        self.question_index = 0
        self.start_time = None
        self.end_time = None

    def start_quiz(self):
        self.start_time = datetime.datetime.now()
        self.display_question()

    def get_question(self):
        if self.question_index >= len(self.questions):
            return None
        return self.questions[self.question_index]

    def display_question(self):
        selected_question = self.get_question()
        if not selected_question:
            self.show_score()
            return

        self.display_progress()
        print(f"\n{selected_question.question}")

        for i, choice in enumerate(selected_question.choices, 1):
            print(f"{i}. {choice}")

        self.get_user_answer()

    def get_user_answer(self):
        selected_question = self.get_question()
        while True:
            try:
                answer = input("\nCevabınız (1-4 veya metin): ").strip()
                if answer.isdigit():
                    choice_index = int(answer) - 1
                    if 0 <= choice_index < len(selected_question.choices):
                        answer = selected_question.choices[choice_index]
                        break
                    else:
                        print("Geçersiz seçenek numarası!")
                elif answer:
                    break
                else:
                    print("Lütfen bir cevap girin!")
            except ValueError:
                print("Geçersiz giriş!")

        self.guess(answer)

    def guess(self, answer):
        selected_question = self.get_question()
        if selected_question.check_answer(answer):
            self.score += 1
            print("✅ Doğru!")
        else:
            print(f"❌ Yanlış! Doğru cevap: {selected_question.answer}")

        self.question_index += 1
        time.sleep(1)
        self.display_question()

    def show_score(self):
        self.end_time = datetime.datetime.now()
        duration = (self.end_time - self.start_time).total_seconds()

        print(f"\n{'=' * 50}")
        print(f"QUİZ BİTTİ!")
        print(f"{'=' * 50}")
        print(f"Toplam Soru: {len(self.questions)}")
        print(f"Doğru Cevaplar: {self.score}")
        print(f"Yanlış Cevaplar: {len(self.questions) - self.score}")
        print(f"Başarı Oranı: {(self.score / len(self.questions)) * 100:.1f}%")
        print(f"Süre: {duration:.1f} saniye")
        print(f"{'=' * 50}")

    def display_progress(self):
        total = len(self.questions)
        current = self.question_index + 1
        progress = (current / total) * 100

        print(f"\n[{current}/{total}] - %{progress:.0f} tamamlandı")


q1 = Question("En iyi programlama dili hangisidir?", ["C++", "Java", "Python", "Javascript"], "C++")
q2 = Question("Python hangi programlama paradigmasını destekler?",
              ["Nesne yönelimli", "Fonksiyonel", "Prosedürel", "Hepsi"], "Hepsi")
q3 = Question("HTML bir programlama dili midir?", ["Evet", "Hayır", "Kısmen", "Sadece backend'de"], "Hayır")
q4 = Question("Hangi veri yapısı LIFO (Last-In-First-Out) prensibiyle çalışır?",
              ["Queue", "Stack", "Linked List", "Tree"], "Stack")
q5 = Question("SQL ne için kullanılır?",
              ["Veritabanı işlemleri", "Web tasarım", "Mobil uygulama geliştirme", "Oyun programlama"],
              "Veritabanı işlemleri")

questions = [q1, q2, q3, q4, q5]

quiz = Quiz(questions)
quiz.start_quiz()
