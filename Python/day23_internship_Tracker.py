class Internship:
    def set_details(self, company, stipend):
        self.company = company
        self.stipend = stipend

    def show_details(self):
        print(f'Company={self.company}')
        print(f'Stipend={self.stipend}')


a1 = Internship()
a1.set_details("OpenAI", 10000)
a1.show_details()