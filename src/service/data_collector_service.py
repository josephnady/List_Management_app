import os
import pandas as pd
from pandas import DataFrame

from src.utils.logger import Logger


class DataCollectorService:
    # file management
    absolute_path = os.getcwd()
    relative_path = "IDs.xlsx"
    data_path = os.path.join(str(absolute_path), relative_path)

    # worksheets names
    deactivated_ids_worksheet_name = "Deactivator"
    activated_ids_worksheet_name = "Activator"
    act_deact_ids_worksheet_name = "Act_Deact"

    # logger for debugging
    log = Logger()

    def __init__(self, is_debug_enable: bool = False):
        self.is_debug_enable = is_debug_enable

    def deactivated_ids_collector(self):
        worksheet = self.__get_worksheet(self.deactivated_ids_worksheet_name)

        in_active_mr_values = worksheet["ENTER IDs HERE"].dropna().astype(int).values
        in_active_mr_list = in_active_mr_values.tolist()

        ids_to_be_inactived = []
        for id in in_active_mr_list:
            strid = str(id)
            ids_to_be_inactived.append(strid)

        prefinal_in_active_list = ids_to_be_inactived

        final_in_active_list = pd.Series(prefinal_in_active_list)
        # print(final_in_active_list)
        final_in_active_list_no_duplicate = final_in_active_list.drop_duplicates().tolist()
        # print("Final Active list with no duplicates :")
        # print(FinalInActiveListNoDuplicate)
        self.log.info(f"No of InActive IDs List  : {len(final_in_active_list_no_duplicate)}")

        return final_in_active_list_no_duplicate

    def activation_ids_collector(self):
        worksheet = self.__get_worksheet(self.activated_ids_worksheet_name)

        active_mr_values = worksheet["ENTER IDs HERE"].dropna().astype(int).values
        active_mr_list = active_mr_values.tolist()

        ids_to_be_actived = []
        for id in active_mr_list:
            strid = str(id)
            ids_to_be_actived.append(strid)

        prefinal_active_list = ids_to_be_actived
        final_active_list = pd.Series(prefinal_active_list)
        final_active_list_no_duplicate = final_active_list.drop_duplicates().tolist()

        return final_active_list_no_duplicate

    def act_deact_ids_collector(self):
        worksheet = self.__get_worksheet(self.act_deact_ids_worksheet_name)

        active_mr_values2 = worksheet.ActiveMRList.dropna().astype(int).values
        active_mr_list2 = active_mr_values2.tolist()

        inactive_mr_values2 = worksheet.InactiveMRList.dropna().astype(int).values
        inactive_mr_list2 = inactive_mr_values2.tolist()

        active_crm_values2 = worksheet.ActiveCrmList.dropna().astype(int).values
        active_crm_list2 = active_crm_values2.tolist()

        # Ids that exists in Active Med Rep List but not in his/her Active Crm List
        ids_to_be_activated2 = []
        for id in active_mr_list2:
            if id not in active_crm_list2:
                strid = str(id)
                ids_to_be_activated2.append(strid)

        # Ids that exists in Active Med Rep List but not in his/her Active Crm List
        self.log.info(f"IDs To Be Actived Count '{len(ids_to_be_activated2)}':")
        self.log.info(f"{ids_to_be_activated2}\n\n")

        # Add not found ids to active crm list
        # for id in IDsToBeActivated2:
        #    ActiveCrmList2.append(id)

        final_active_crm_list2 = active_crm_list2

        # append Active Crm List Ids that not found in Active MR list to the Inactive list
        # preparing for removing duplicates and create final Inactivation List
        for id in final_active_crm_list2:
            if id not in active_crm_list2:
                strid2 = str(id)
                inactive_mr_list2.append(strid2)

        final_inactive_list2 = pd.Series(inactive_mr_list2)
        # print(FinalInactiveList)
        final_inactive_list_no_duplicate2 = final_inactive_list2.drop_duplicates().tolist()
        self.log.info(f"Accounts to be Deactivated Count '{len(final_inactive_list_no_duplicate2)}':")
        self.log.info(f"{final_inactive_list_no_duplicate2}")
        results = [final_inactive_list_no_duplicate2, ids_to_be_activated2]
        return results

    def __get_worksheet(self, sheet_name) -> DataFrame:
        worksheet = pd.read_excel(self.data_path, sheet_name=sheet_name)
        return worksheet
