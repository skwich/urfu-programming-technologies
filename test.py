# import cProfile
# import pstats

# def test():
#     for i in range(10_000_000):
#         i += i
#     return 100
# def test2():
#     for i in range(10_000_005):
#         i += i
#     return 100

# TASK_FUNCTIONS_ORDER = ['test', 'test2']

# profiler = cProfile.Profile()

# profiler.enable()
# test()
# test2()
# profiler.disable()

# stats = pstats.Stats(profiler).get_stats_profile()
# total_time = sum([stats.func_profiles[func].cumtime for func in TASK_FUNCTIONS_ORDER])
# for func in TASK_FUNCTIONS_ORDER:
#     percent = 100 - round(stats.func_profiles[func].cumtime/total_time*100)
#     time = round(stats.func_profiles[func].cumtime, 4)
#     print(f"{time:.4f}: {percent}%")

a = {'0.1000': '2.081165452653486', '0.1220': '2.539021852237253', '1.3460': '28.012486992715925', '0.6830': '14.214360041623312', '2.5540': '53.152965660770036'}
for (key,value) in a.items():
    print(f"{key}: {value}%\t->\t{round(float(value))}%")