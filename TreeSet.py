import pandas as pd
import numpy as np

class Node:
    def __init__(self, dataframe, ID):
        ID = dataframe.loc[dataframe["ID"].item() == np.int64(ID)]["ID"]
        Name = dataframe.loc[dataframe["ID"].item() == np.int64(ID)]["Quest"]
        if self.ID == 304:
            Parent = [289, 298]
        else:
            Parent = [dataframe.loc[dataframe["ID"] == ID]["Dependancy"]]
    def __str__(self):
        return self.ID
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

class TreeSet:

    def __init__(self, dataframe):
        self.Tree = []
        for i,r in dataframe.iterrows():
            if r[4] == "Main":
                self.Tree.append(Node(dataframe, r[0]))
            else:
                pass

    def __str__(self):
        return self.Tree

    def findDependancies(self, QuestID, full=False): #returns in descending order
        #if QuestID == 23:
        if full:
            ans = []
            for i in self.Tree:
                if i.ID == QuestID:
                    ans.append(i.Parent)
            for j in ans:
                if j == 23: # First quest in the game
                    break
                else:
                    self.findDependancies(j, full=True)
            return ans
        else:
            for k in self.Tree:
                if k.ID == QuestID:
                    return k.Parent

df = pd.read_csv("witcher_school_of_python\Quest.csv")
T = TreeSet(df)
print(T)