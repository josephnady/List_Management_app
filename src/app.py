from src.utils.utils import Utils as u
from view.main_gui import StartMyApp as s

if __name__ == "__main__":
    cores = int(u.cpu_count())
    usedcores = cores / 2
    print(f"cpu count are: {cores}\nused cores are: {usedcores}")
    u.flush_dns()

    s.run_start_gui()
    # Multiprocess Version
    # m.run_gui(usedcores)
    # Sync Version
    # ms.run_gui()
    print(f"{' All processess completed ':*^40}")
