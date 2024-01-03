import os
import pandas as pd

def Dectivation_id_manip():
    # # Add IDs in IDs.xlsx file:
    AbsolutePath = os.getcwd()
    relativepath = "IDs.xlsx"
    finalpath = os.path.join(str(AbsolutePath), relativepath)
    ID_file_path = finalpath
    ID_file = pd.read_excel(ID_file_path, sheet_name="Deactivator")
    # print(type(ID_file))
    # print(ID_file.dtypes)
    # print(ID_file)

    InActiveMRvalues = ID_file["ENTER IDs HERE"].dropna().astype(int).values
    InActiveMRList = InActiveMRvalues.tolist()
    # print(ActiveMRList)

    IDstobeInActived = []
    for id in InActiveMRList:
        strid = str(id)
        IDstobeInActived.append(strid)

    prefinalInActiveList = IDstobeInActived

    FinalInActiveList = pd.Series(prefinalInActiveList)
    # print(FinalInactiveList)
    FinalInActiveListNoDuplicate = FinalInActiveList.drop_duplicates().tolist()
    # print("Final Active list with no duplicates :")
    # print(FinalInActiveListNoDuplicate)
    print(f"No of InActive IDs List  : {len(FinalInActiveListNoDuplicate)}")

    return FinalInActiveListNoDuplicate


def Activation_id_manip():
    # # Add IDs in IDs.xlsx file:
    AbsolutePath = os.getcwd()
    relativepath = "IDs.xlsx"
    finalpath = os.path.join(str(AbsolutePath), relativepath)
    ID_file_path = finalpath
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
    # Add IDs in IDs.xlsx file:
    AbsolutePath = os.getcwd()
    # print(AbsolutePath)
    relativepath = "IDs.xlsx"
    finalpath = os.path.join(str(AbsolutePath), relativepath)
    ID_file_path = finalpath
    ID_file = pd.read_excel(ID_file_path, sheet_name="Act_Deact")
    # print(type(ID_file))
    # print(ID_file.dtypes)
    # print(ID_file)

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
    # Add not found ids to active crm list
    # for id in IDsToBeActivated2:
    #    ActiveCrmList2.append(id)

    finalActiveCRMList2 = ActiveCrmList2

    # append Active Crm List Ids that not found in Active MR list to the Inactive list
    # preparing for removing duplicates and create final Inactivation List
    for id in finalActiveCRMList2:
        if id not in ActiveMRList2:
            strid2 = str(id)
            InactiveMRList2.append(strid2)

    FinalInactiveList2 = pd.Series(InactiveMRList2)
    # print(FinalInactiveList)
    FinalInactiveListNoDuplicate2 = FinalInactiveList2.drop_duplicates().tolist()
    print(f"Accounts to be Deactived Count '{len(FinalInactiveListNoDuplicate2)}':")
    print(f"{FinalInactiveListNoDuplicate2}")
    results = [FinalInactiveListNoDuplicate2, IDsToBeActivated2]
    return results