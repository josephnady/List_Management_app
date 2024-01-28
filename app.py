from utils import Utils as u
from View.main_gui import StartInterface as s



if __name__ == "__main__":
    cores = int(u.cpu_count())
    usedcores = cores/2
    print(f"cpu count are: {cores}\nused cores are: {usedcores}")
    u.flush_dns()
    s.run_start_gui()
    print(f"{' All processess completed ':*^40}")

