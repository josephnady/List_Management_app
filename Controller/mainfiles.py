from Model.Deactivator import Deactivate
from Model.Activator import Activate
from Controller.id_manip import Activation_id_manip
from Controller.id_manip import Dectivation_id_manip
from Controller.id_manip import Act_Deact_id_manip
from utils import Utils as u
from multiprocessing import Pool



def main_Deactivate():
    Deactive_list = Dectivation_id_manip()
    Deactivate(Deactive_list)


def main_Activate(c):
    cores = int(c)
    p = Pool(cores)
    
    ActivationIDs = Activation_id_manip()
    Active_Ids_count = len(ActivationIDs)
    bulk_Ids_count = 0
    while bulk_Ids_count <= Active_Ids_count:
        bulk_Ids = []
        # print("before for loop")
        for i, id in enumerate(ActivationIDs,1):
            print(f"{i} - {id}")
            bulk_Ids.append(id)
            if ((i % 5 == 0)|(ActivationIDs[-1]==id)):
                ask = input(f"\n{bulk_Ids_count} Ids have been opened, Do you Want to continue? (y/n) ").lower()
                if ask == 'y':
                    u.close_edge_browser()
                    break
                else:
                    ask2 = input(f"\nAre you Sure you want to Quit? (y/n) ").lower()
                    if ask2 != 'y':
                        return
                    return            
                
        # print("After for loop")
        p.map(Activate, bulk_Ids)
        bulk_Ids_count += i
        print(bulk_Ids_count)
        # print(f"Act IDs before assignement{len(ActivationIDs)}")
        ActivationIDs = [item for item in ActivationIDs if item not in bulk_Ids]
        # print(f"Act IDs After assignement{len(ActivationIDs)}")
        print(f"Next Ids to be activated {f'{ActivationIDs}':*>30}")


    p.close()
    p.join()

def main_Act_Deact(c):
    cores = int(c)
    p = Pool(cores)
    
    results = Act_Deact_id_manip()
    print(len(results))
    DeactIDs= results[0]
    ActIDs= results[1]
    IDs_to_be_actived = ActIDs
    # print(f"Main function -> Deactive IDs {len(DeactationIDs)}:\n{DeactationIDs}\
    #       \nMain Function -> Activate IDs:{len(ActivationIDs)}\n{ActivationIDs}\n")
    print(f"Main function -> Deactive IDs {len(DeactIDs)}:\n\
          \nMain Function -> Activate IDs:{len(ActIDs)}\n")
    bulk_Ids_count = 0
    endpoint = len(ActIDs)
    while bulk_Ids_count <= endpoint+1:
        bulk_Ids = []
        for i, id in enumerate(IDs_to_be_actived,1):
            bulk_Ids.append(id)
            if ((i % 10 == 0)|(ActIDs[-1]==id)):
                ask = input(f"\n{bulk_Ids_count} Ids have been opened, Do you Want to continue? (y/n) ").lower()
                if ask == 'y':
                    u.close_edge_browser()
                    break
                elif input(f"\nDo you want to go to Deactivation ? (y/n) ").lower() =='y':
                    u.close_edge_browser()
                    print(f"{' <><><><><><><><> ':*^60}")
                    print(f"{'  Activation has been finished  ':*^60}")
                    print(f"{' <><><><><><><><> '   :*^60}")
                    print("\n\n")
                    print(f"{'  Start Deactivation  ':*^60}")
                    Deactivate(DeactIDs)
                    return
                else:
                    u.close_edge_browser()
                    return
                                
        
        p.map(Activate, bulk_Ids)
        bulk_Ids_count += i
        IDs_to_be_actived = [item for item in IDs_to_be_actived if item not in bulk_Ids]
        print(f"Next Ids to be activated {f'{IDs_to_be_actived}':*>30}")

    # close_edge_browser()
    print(f"{' <><><><><><><><> ':*^60}")
    print(f"{'  Activation has been finished  ':*^60}")
    print(f"{' <><><><><><><><> ':*^60}")
    print("\n\n")
    print(f"{'  Start Deactivation  ':*^60}")
    Deactivate(DeactIDs)

    p.close()
    p.join()