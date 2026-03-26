class NobelParams:
    def __init__(
        self,
        offset=None,
        limit=None,
        sort=None,  # "asc" | "desc"
        nobelPrizeYear=None,
        yearTo=None,
        nobelPrizeCategory=None, # "che" | "eco" | "lit" | "pea" | "phy" | "med"
        format=None, # "json" | "csv"
        csvLang=None, # "es" | "en"
    ):
        self.offset = offset
        self.limit = limit
        self.sort = sort
        self.nobelPrizeYear = nobelPrizeYear
        self.yearTo = yearTo
        self.nobelPrizeCategory = nobelPrizeCategory
        self.format = format
        self.csvLang = csvLang

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}
    

class LaureateParams:
    def __init__(
            self,
            offset=None,
            limit=None,
            sort=None,  # "asc" | "desc"
            ID = None,
            name = None,
            gender = None, #"female" | "male" ", other"
            motivation = None,
            affiliation = None,
            residence = None,
            birthDate = None,
            birthDateTo = None, #if used previous is required
            deathDate = None,
            deathDateTo = None,#if used previous is required
            foundedDate = None,
            birthCity = None,
            birthCountry = None,
            birthContinent = None,
            deathCity = None,
            deathCountry = None,
            deathContinent = None,
            foundedCity = None,
            foundedCountry = None,
            foundedContinent = None, #"Africa" | "Asia" | "Europe" | "North America" | "Oceania" | "South America" | "Antartica"
            HeadquartersCity = None,
            nobelPrizeYear = None,
            yearTo = None,
            nobelPrizeCategory = None,
            format=None, # "json" | "csv"
            csvLang=None, # "es" | "en"
         ):
            self.offset = offset
            self.limit = limit
            self.sort = sort
            self.ID = ID
            self.name = name
            self.gender = gender
            self.motivation = motivation
            self.affiliation = affiliation
            self.residence = residence
            self.birthDate = birthDate
            self.birthDateTo = birthDateTo
            self.deathDate = deathDate
            self.deathDateTo = deathDateTo
            self.foundedDate = foundedDate
            self.birthCity = birthCity
            self.birthCountry = birthCountry
            self.birthContinent = birthContinent
            self.deathCity = deathCity
            self.deathCountry = deathCountry
            self.deathContinent = deathContinent
            self.foundedCity = foundedCity
            self.foundedCountry = foundedCountry
            self.foundedContinent = foundedContinent
            self.HeadquartersCity = HeadquartersCity
            self.nobelPrizeYear = nobelPrizeYear
            self.yearTo = yearTo
            self.nobelPrizeCategory = nobelPrizeCategory
            self.format = format
            self.csvLang = csvLang

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}