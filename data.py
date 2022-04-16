import os
from form import Form

class DataFiles:
    def __init__(self) -> None:
        self.budget = "budget.csv"
        self.budgetRaw = "budget_raw.csv"
        self.comsumption = "comsumption.csv"
        self.consumptionRaw = "consumption_raw.csv"
        self.financialGrowth = "financial_growth.csv"
        self.firstIndustryAddition = "first_industry_addition.csv"
        self.gdp = "gdp.csv"
        self.gdpAll = "gdp_all.csv"
        self.gdpAverage = "gdp_average.csv"
        self.population = "population.csv"
        self.populationDensity = "population_density.csv"
        self.populationDensityRaw = "population_density_raw.csv"
        self.secondIndustryAddition = "second_industry_addition.csv"
        self.secondIndustryAdditionRaw = "second_industry_addition_raw.csv"
        self.technicist = "technicist.csv"
        self.thirdIndustryAddition = "third_industry_addition.csv"
        self.thirdIndustryAdditionRaw = "third_industry_addition_raw.csv"
    def Attrs(self )->dict:
        return self.__dict__

# store all datas
class Datas:
    def __init__(self,dataPath="") -> None:
        print("> check data fold")
        if dataPath=="":
            self.dataPath="data/"
        else:
            self.dataPath=dataPath

        if not os.path.exists(self.dataPath):
            print("%s is not exists"%self.dataPath)
            return
        print("ok.")

        self.forms={}
        for attr,path in DataFiles().Attrs().items():
            self.forms[attr]=Form(os.path.join(self.dataPath,path))

        print("> check data file")
        if not self.Check():
            print("datas meet lost.")
            return
        else:
            print("ok.")

        print(">start to load datas...")
        self.LoadDatas()
        print("ok.\n")
    
    def __getitem__(self,attr="")->Form:
        if attr=="":
            return None
        
        if attr not in self.forms.keys():
            return None

        try:
            return self.forms[attr]
        except:
            return None

    # load data from files
    def LoadDatas(self):
        for _,form in self.forms.items():
            form.LoadCSV()

    def Check(self)-> bool:
        flag = True
        for _,form in self.forms.items():
            if not form.Check():
                flag=False
        return flag

