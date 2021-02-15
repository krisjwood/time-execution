# Function that allows for the coder to insert a start and end point for the progreamme to track the time it took to execute

# Instructions:

# Put at start point:
   # start = xstart()

# Put at end point:
   # xend(start) 

# Start
def xstart():
    import time
    start = time.time()
    return start

# End
def xend(start):
    import time
    end = time.time()

    # Summary
    execution = end - start
    rounded = round(execution, 4)
    print("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(f"S: {time.ctime(start)}    E: {time.ctime(end)}   ({rounded} seconds)")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


# Operation
start = xstart()
range_num = 10000
[print(i) for i in range(range_num)]
xend(start)
