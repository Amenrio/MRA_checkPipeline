import MRA_library_variableNames_v01 as libVars

c = ["main", "skin", "geo"]
for x in c:
    if x not in libVars.pipeline_groups:
        print("{0} not found".format(x))
    else:
        print("{0} found".format(x))
