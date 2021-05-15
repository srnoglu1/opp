class Pet:
    all_breed = ["cat","dog","bird"]

    def __init__(self,name,genus):
        if genus not in Pet.all_breed:
            raise ValueError(f"{genus} is not a domestic animal.")
        self.name = name
        self.genus = genus

    def set_genus(self,genus):
        if genus not in Pet.all_breed:
            raise ValueError (f"{genus} is not a domestic animal.")
        self.genus = genus

boncuk = Pet("boncuk","cat")
pasa = Pet("boncuk","dog")
tekir = Pet("boncuk","bird")

# tekir.set_genus("lion")

boncuk.all_breed.append("fish")
pasa.all_breed.append("fish")

print(Pet.all_breed)
print(boncuk.all_breed)
print(pasa.all_breed)
