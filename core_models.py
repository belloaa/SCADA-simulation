# core_models.py

from abc import ABC, abstractmethod 
from typing import List, Optional

# foundation for all elements - name and abstract update_state
class PowerElement(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def update_state(self):
        pass 

# simulates power generation 
class PowerSource(PowerElement):
    def __init__(self, name: str, type: str, capacity: float):
        super().__init__(name)
        self.type = type
        self.capacity = capacity
        self.current_output = 0.0

    def generate_power(self) -> float:
        self.current_output = min(self.capacity, self.capacity * 0.8) # assume 80% efficiency
        return self.current_output
    
    def update_state(self):
        self.generate_power()


# simulates power consumption, represents entities that consume power
class PowerConsumer(PowerElement):
    def __init__(self, name: str, peak_demand: float):
        super().__init__(name)
        self.peak_demand = peak_demand
        self.current_demand = 0.0

    # power consumption logic
    def consume_power(self) -> float:
        self.current_demand = self.peak_demand * 0.7
        return self.current_demand
    
    def update_state(self):
        self.consume_power()


# represents transmission lines/ other netowork components
class NetworkElement(PowerElement):
    def __init__(self, name: str, capacity: float):
        super().__init__(name)
        self.capacity = capacity
        self.current_load = 0.0
        self.connected_elements: List[PowerElement] = []

    def connect_element(self, element: PowerElement):
        self.connected_elements.append(element)

    def transfer_power(self) -> float:
        total_load = sum(elem.current_demand if isinstance(elem, PowerConsumer) else -elem.current_output
                         for elem in self.connected_elements)
        self.current_load = abs(total_load)
        return self.current_load

    def check_overload(self) -> bool:
        return self.current_load > self.capacity
    
    def update_state(self):
        self.transfer_power()
        if self.check_overload():
            print(f"warning: Overload in {self.name}")
        


