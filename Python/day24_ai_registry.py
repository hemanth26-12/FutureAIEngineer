class SecurityOfficier:
    def __init__(self,name,id,location):
        self.name = name
        print(f'Officier Name: {self.name}')
        self.id = id
        print(f'Officier ID: {self.id}')
        self.location = location
        print(f'Location :{location}')

s = SecurityOfficier("Hemanth",101,"Main Gate\n")
s = SecurityOfficier("Rahul",102,"Back Gate\n")
s = SecurityOfficier("Ramesh",103,"Main Gate\n")


