import pandas as pd

def loadQuests(dir):
    try:
        return pd.read_csv(dir)
    except:
        print("An error occured when loading" + dir + "\n")
        return -1

def getQuests(data, main_quest=True, territory="All", includeDLC=True, level=0, minlevel=-1, maxlevel=-1):
    if minlevel == -1:
        minim = level - 1
    else:
        minim = minlevel
    if maxlevel == -1:
        maxim = level + 1
    else:
        maxim = maxlevel
    i = minim
    while i <= maxim:
        if i > minim:
            ans = pd.concat([ans, data[data["Level"] == i]])
        else:
            ans = data[data["Level"] == i]
        i += 1
    if main_quest == False:
        ans = ans[ans["Type"] != "Main"]
    if includeDLC == False:
        ans = ans[ans["DLC"] == "Base Game"]
    if territory != "All":
        ans = ans[ans["Territory"] == territory]
    return ans

def getMissable(data, main_quest=True, territory="All"):
    ans = data[data["Missable"] == "Y"]
    if main_quest == False:
        ans = ans[ans["Type"] != "Main"]
    if territory != "All":
        ans = ans[ans["Territory"] == territory]
    return ans

def getNotes(data, main_quest=True, territory="All", includeDLC=True):
    ans = data.loc[data["Notes"].notnull()]
    if main_quest == False:
        ans = ans[ans["Type"] != "Main"]
    if includeDLC == False:
        ans = ans[ans["DLC"] == "Base Game"]
    if territory != "All":
        ans = ans[ans["Territory"] == territory]
    return ans

#print(getQuests(territory="White Orchard", maxlevel=100))
#df = loadQuests("source\Quest.csv")
#print(getQuests(df, main_quest=False, territory="All", includeDLC=True, level=10))
#print(getMissable(df))
#getNotes(df).to_csv("out.csv", index=False)