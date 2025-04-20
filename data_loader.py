import numpy as np

def load_data(file_path):
    with open(file_path, 'r') as file:
        # İlk satır depo ve müşteri sayısını alıyoruz
        first_line = file.readline().strip().split()
        num_depots = int(first_line[0])
        num_customers = int(first_line[1])
        
        # Depo kapasiteleri ve kurulum maliyetlerini alıyoruz
        depot_capacities = []
        setup_costs = []
        for _ in range(num_depots):
            line = file.readline().strip().split()
            depot_capacities.append(float(line[0]))
            setup_costs.append(float(line[1]))

        # Müşteri talepleri ve maliyetlerini alıyoruz
        customer_demands = []
        cost_matrix = []
        
        for _ in range(num_customers):
            # İlk başta müşteri talebini alıyoruz
            demand_line = file.readline().strip().split()
            demand = float(demand_line[0])
            customer_demands.append(demand)
            
            # Müşteri ile her depo arasındaki maliyetleri alıyoruz
            costs_line = file.readline().strip().split()
            costs = [float(cost) for cost in costs_line]
            cost_matrix.append(costs)
        
    return num_depots, num_customers, depot_capacities, setup_costs, customer_demands, cost_matrix
