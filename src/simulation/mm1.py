import simpy
import random

def mm1_simulation(arrival_rate: float, service_rate: float, n_customers: int, seed: int = 42):
    random.seed(seed)
    env = simpy.Environment()
    server = simpy.Resource(env, capacity=1)
    wait_times = []

    def customer(env, name, server, service_rate):
        arrival_time = env.now
        with server.request() as req:
            yield req
            wait = env.now - arrival_time
            wait_times.append(wait)
            service_time = random.expovariate(service_rate)
            yield env.timeout(service_time)

    def arrival_process(env, arrival_rate, server, service_rate, n_customers):
        for i in range(n_customers):
            inter_arrival = random.expovariate(arrival_rate)
            yield env.timeout(inter_arrival)
            env.process(customer(env, f"cust_{i}", server, service_rate))

    env.process(arrival_process(env, arrival_rate, server, service_rate, n_customers))
    env.run()
    return wait_times
