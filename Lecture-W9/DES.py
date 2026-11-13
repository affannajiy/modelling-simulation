import random
import heapq

random.seed(1)

# Parameters
arrival_rate = 1.0   # lambda (events per time unit)
service_rate = 1.25  # mu (services per time unit)
num_served_target = 1000

# Event types
ARRIVAL = "arrival"
DEPARTURE = "departure"

# State
clock = 0.0
server_busy = False
queue = []
served = 0
total_wait = 0.0
area_server_busy = 0.0   # for utilization
last_event_time = 0.0

# Event list as (time, counter, type, data)
event_list = []
counter = 0

def schedule(time, etype, data=None):
    global counter
    heapq.heappush(event_list, (time, counter, etype, data))
    counter += 1

# Schedule first arrival
schedule(random.expovariate(arrival_rate), ARRIVAL)

while served < num_served_target:
    time, _, etype, data = heapq.heappop(event_list)
    # update time-averaged server busy area
    area_server_busy += (time - last_event_time) * (1.0 if server_busy else 0.0)
    last_event_time = time
    clock = time

    if etype == ARRIVAL:
        # schedule next arrival
        schedule(clock + random.expovariate(arrival_rate), ARRIVAL)
        if not server_busy:
            # start service immediately
            server_busy = True
            service_time = random.expovariate(service_rate)
            schedule(clock + service_time, DEPARTURE, {"arrival_time": clock})
        else:
            # join queue (store arrival time for waiting calc)
            queue.append(clock)

    elif etype == DEPARTURE:
        served += 1
        arrival_time = data["arrival_time"]
        wait = (clock - arrival_time) - (0.0)  # waiting time in queue (service included later)
        # If the arrival started service immediately, wait = 0; else arrival_time is when they entered queue
        # For queued customers, we compute their waiting when they start service below.
        # Serve next customer if any
        if queue:
            next_arrival_time = queue.pop(0)
            # waiting time in queue for that customer = current time - their arrival to queue
            w = clock - next_arrival_time
            total_wait += w
            service_time = random.expovariate(service_rate)
            schedule(clock + service_time, DEPARTURE, {"arrival_time": next_arrival_time})
        else:
            server_busy = False

# Final stats
sim_time = clock
avg_wait = total_wait / served
utilization = area_server_busy / sim_time

print(f"Served: {served}")
print(f"Sim time: {sim_time:.4f}")
print(f"Average waiting time in queue: {avg_wait:.4f}")
print(f"Server utilization: {utilization:.4f}")
