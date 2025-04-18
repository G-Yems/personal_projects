import pandas as pd  # type: ignore
from typing import List  # Import pour la liste typée

class Recipe:
    def __init__(self, type: str, link: str, desc: str):
        self.type = type
        self.link = link
        self.desc = desc

    @staticmethod
    def toxlsx(recipeList: List['Recipe'], outxlx: str):
        '''
        Convert a list of recipe object into a xlx file
        Input : List of recipe object, output file name
        Output : The xlsx file 
        '''
        # Convert the 'recipe' object into a dictionnary 
        data = [
            {"Type": recipe.type, "Link": recipe.link, "Description": recipe.desc}
            for recipe in recipeList
        ]
        df = pd.DataFrame(data)
        df.to_excel(outxlx, index=False)

    @staticmethod
    def xlsxToRecipeList(recipexlx: str):
        """
        Read the xlsx and return a dataframe
        Input : The xlsx path
        Output : the pandas dataframe of the xlx 
        """

        df = pd.read_excel(recipexlx)
        recipe_list = [Recipe(type=row["Type"], link=row["Link"], desc=row["Description"]) for _, row in df.iterrows()]
        return recipe_list
    
    @staticmethod
    def isInRecipeList(recipe:'Recipe',recipelist:List):
        ## TODO: add the fun
        pass