import cProfile
import pstats
import time
from functions_to_profile import load_files, read_database, get_id, get_user_data, generate_words


TASK_FUNCTIONS_ORDER = ['load_files', 'read_database', 'get_id', 'get_user_data', 'generate_words']

profiler = cProfile.Profile()
profiler.enable()
time_start = time.time()
load_files()
read_database()
get_id()
get_user_data()
generate_words()
time_end = time.time()
profiler.disable()

stats = pstats.Stats(profiler).get_stats_profile()
total_time = time_end - time_start
for func in TASK_FUNCTIONS_ORDER:
    time = round(stats.func_profiles[func].cumtime, 4)
    percent = round(stats.func_profiles[func].cumtime/total_time*100)
    print(f"{time}: {percent}%")