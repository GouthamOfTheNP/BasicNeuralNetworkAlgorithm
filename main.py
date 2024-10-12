import random
import math
from decimal import Decimal

total_neurons_first_layer = 16
total_neurons_second_layer = 16
total_results = 8
length_of_inputs = 100
total_inputs = 100
bias = Decimal(-10)
array_of_results = []
array_of_second_layer = []

for d in range(total_results):
    total_val_for_second = Decimal(0)
    array_of_first_layer = []
    for s in range(total_neurons_second_layer):
        total_val_for_neuron = Decimal(0)
        array_of_neurons = []
        for a in range(total_neurons_first_layer):
            array_of_calculated_sum = []
            for l in range(total_inputs):
                array_of_tensors = [Decimal(random.uniform(-20, 20)) for i in range(length_of_inputs)]
                weights = [Decimal(random.uniform(-5, 5)) for j in range(length_of_inputs)]
                total_val_for_input = Decimal(0)
                for k in range(length_of_inputs):
                    total_val_for_input += array_of_tensors[k] * weights[k]
                total_val_for_input += bias
                total_val_for_input = max(Decimal(-10), min(Decimal(10), total_val_for_input))
                total_val_for_input = Decimal(1 / (1 + math.exp(-float(total_val_for_input))))
                array_of_calculated_sum.append(total_val_for_input)
            array_of_neurons.append(sum(array_of_calculated_sum))
        
        weights_second = [Decimal(random.uniform(-5, 5)) for j in range(total_neurons_first_layer)]
        for k in range(total_neurons_first_layer):
            total_val_for_neuron += array_of_neurons[k] * weights_second[k]
        total_val_for_neuron += bias
        total_val_for_neuron = max(Decimal(-10), min(Decimal(10), total_val_for_neuron))
        total_val_for_neuron = Decimal(1 / (1 + math.exp(-float(total_val_for_neuron))))
        array_of_first_layer.append(total_val_for_neuron)
    
    array_of_second_layer.append(sum(array_of_first_layer))
    
    weights_results = [Decimal(random.uniform(-5, 5)) for j in range(total_neurons_first_layer)]
    for k in range(total_neurons_first_layer):
        total_val_for_second += array_of_first_layer[k] * weights_results[k]
    total_val_for_second += bias
    total_val_for_second = max(Decimal(-10), min(Decimal(10), total_val_for_second))
    total_val_for_second = Decimal(1 / (1 + math.exp(-float(total_val_for_second))))
    array_of_results.append(total_val_for_second)

print(array_of_results)
