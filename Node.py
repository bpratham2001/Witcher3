#import pandas as pd
class Node:
    def __init__(self, dataframe, ID):
        ID = dataframe.loc[dataframe["ID"] == ID]["ID"]
        Name = dataframe.loc[dataframe["ID"] == ID]["Quest"]
        if self.ID == 304:
            Parent = [289, 298]
        else:
            Parent = [dataframe.loc[dataframe["ID"] == ID]["Dependancy"]]
    def __str__(self):
        return self.Name
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.ID == other.ID
        else:
            return False
    def __ne__(self, other):
        if self.__eq__(other):
            return False
        else:
            return True
    def addParent(self, newParent):
        self.Parent.append(newParent)