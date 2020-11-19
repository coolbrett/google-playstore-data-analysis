import pandas as pd

store_df = pd.read_csv("googleplaystore.csv", dtype={"Rating": float})
store_df = store_df.dropna()


def fix_size():
    """All apps are listed in Megabytes, so we are dropping the M off of all the Size columsn"""
    for index, row in store_df.iterrows():
        temp = row["Size"]
        temp = temp[:-1]
        row["Size"] = temp
        print("poop")


def fix_installs(dataframe):
    for index, row in dataframe.iterrows():
        temp = row["Installs"]
        temp = temp.strip("+")
        temp = temp.replace(',', "")
        name = row["App"]
        dataframe.loc[[name], ["Installs"]] = temp
    return dataframe


if __name__ == '__main__':
    store_df = fix_installs(store_df)
    print()
