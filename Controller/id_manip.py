import os
import pandas as pd

def Dectivation_id_manip():
    # # Add IDs in IDs.xlsx file:
    AbsolutePath = os.getcwd()
    relativepath = "IDs.xlsx"
    finalpath = os.path.join(str(AbsolutePath), relativepath)
    ID_file_path = finalpath
    ID_file = pd.read_excel(ID_file_path, sheet_name="Deactivator")

    InActiveMRvalues = ID_file["ENTER IDs HERE"].dropna().astype(int).values
    InActiveMRList = InActiveMRvalues.tolist()

    IDstobeInActived = []
    for id in InActiveMRList:
        strid = str(id)
        IDstobeInActived.append(strid)

    prefinalInActiveList = IDstobeInActived

    FinalInActiveList = pd.Series(prefinalInActiveList)
    FinalInActiveListNoDuplicate = FinalInActiveList.drop_duplicates().tolist()
    print(f"No of InActive IDs List  : {len(FinalInActiveListNoDuplicate)}")

    return FinalInActiveListNoDuplicate


def Activation_id_manip():
    # Add IDs in IDs.xlsx file:
    AbsolutePath = os.getcwd()
    relativepath = "IDs.xlsx"
    finalpath = os.path.join(str(AbsolutePath), relativepath)
    ID_file_path = finalpath
    print(ID_file_path)
    ID_file = pd.read_excel(ID_file_path, sheet_name="Activator")

    ActiveMRvalues = ID_file["ENTER IDs HERE"].dropna().astype(int).values
    ActiveMRList = ActiveMRvalues.tolist()

    IDstobeActived = []
    for id in ActiveMRList:
        strid = str(id)
        IDstobeActived.append(strid)

    prefinalActiveList = IDstobeActived
    FinalActiveList = pd.Series(prefinalActiveList)
    FinalActiveListNoDuplicate = FinalActiveList.drop_duplicates().tolist()

    return FinalActiveListNoDuplicate

def Act_Deact_id_manip():
    # ID MANIPULATION:
    # ________________________________________________________________________________
    AbsolutePath = os.getcwd()
    relativepath = "IDs.xlsx"
    finalpath = os.path.join(str(AbsolutePath), relativepath)
    ID_file_path = finalpath
    ID_file = pd.read_excel(ID_file_path, sheet_name="Act_Deact")

    ActiveMRvalues2 = ID_file.ActiveMRList.dropna().astype(int).values
    ActiveMRList2 = ActiveMRvalues2.tolist()

    InactiveMRvalues2 = ID_file.InactiveMRList.dropna().astype(int).values
    InactiveMRList2 = InactiveMRvalues2.tolist()

    ActiveCrmvalues2 = ID_file.ActiveCrmList.dropna().astype(int).values
    ActiveCrmList2 = ActiveCrmvalues2.tolist()

    # Ids that excists in Active Med Rep List but not in his/her Active Crm List
    IDsToBeActivated2 = []
    for id in ActiveMRList2:
        if id not in ActiveCrmList2:
            strid = str(id)
            IDsToBeActivated2.append(strid)

    # Ids that excists in Active Med Rep List but not in his/her Active Crm List
    print(f"IDs To Be Actived Count '{len(IDsToBeActivated2)}':")
    print(f"{IDsToBeActivated2}\n\n")

    finalActiveCRMList2 = ActiveCrmList2

    # append Active Crm List Ids that not found in Active MR list to the Inactive list
    # preparing for removing duplicates and create final Inactivation List
    for id in finalActiveCRMList2:
        if id not in ActiveMRList2:
            strid2 = str(id)
            InactiveMRList2.append(strid2)

    FinalInactiveList2 = pd.Series(InactiveMRList2)
    FinalInactiveListNoDuplicate2 = FinalInactiveList2.drop_duplicates().tolist()
    print(f"Accounts to be Deactived Count '{len(FinalInactiveListNoDuplicate2)}':")
    print(f"{FinalInactiveListNoDuplicate2}")
    results = [FinalInactiveListNoDuplicate2, IDsToBeActivated2]
    return results

def am_data_importer():
    # Add IDs in IDs.xlsx file:
    AbsolutePath = os.getcwd()
    relativepath = "IDs.xlsx"
    finalpath = os.path.join(str(AbsolutePath), relativepath)
    ID_file_path = finalpath
    # print(ID_file_path)
    ID_file = pd.read_excel(ID_file_path, sheet_name="Am")

    AccountIdslist = list(map(lambda y: str(y) , [x for x in ID_file["ID Am account"].dropna().astype(int).values]))
    NamesList = list(map(lambda y: str(y) , [x for x in ID_file["Territory Name"].dropna().values]))
    BrickList = list(map(lambda y: str(y) , [x for x in ID_file["Brick"].dropna().values]))
    Recordslist = list(zip(AccountIdslist,NamesList,BrickList))
    results = pd.Series(Recordslist)
    results_unique = results.drop_duplicates().tolist()

    return Recordslist