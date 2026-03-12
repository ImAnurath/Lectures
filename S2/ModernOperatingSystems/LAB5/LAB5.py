import numpy as np

class BankersAlgorithm:
    def __init__(self, allocation, max_demand, available):
        self.allocation = np.array(allocation)
        self.max_demand = np.array(max_demand)
        self.available = np.array(available)
        self.num_processes = self.allocation.shape[0]
        self.num_resources = self.allocation.shape[1]
        self.need = self.max_demand - self.allocation

    def is_safe(self):
        work = self.available.copy()
        finish = [False] * self.num_processes
        safe_sequence = []

        while len(safe_sequence) < self.num_processes:
            progress_made = False
            for i in range(self.num_processes):
                if not finish[i] and all(self.need[i] <= work):
                    work += self.allocation[i]
                    finish[i] = True
                    safe_sequence.append(i)
                    progress_made = True
                    break
            if not progress_made:
                return False, []
        return True, safe_sequence

    def request_resources(self, process_id, request):
        request = np.array(request)
        if any(request > self.need[process_id]):
            raise ValueError("Error: Process has exceeded its maximum claim.")

        if all(request <= self.available):
            # Try allocating temporarily
            self.available -= request
            self.allocation[process_id] += request
            self.need[process_id] -= request

            safe, _ = self.is_safe()
            if safe:
                return True
            else:
                # Roll back
                self.available += request
                self.allocation[process_id] -= request
                self.need[process_id] += request
                return False
        else:
            return False

# Example data from your PDF

allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2],
]

max_demand = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3],
]

available = [3, 3, 2]

banker = BankersAlgorithm(allocation, max_demand, available)

# Check system safety
safe, sequence = banker.is_safe()
print("System is in a safe state:", safe)
if safe:
    print("Safe sequence:", sequence)

# Example resource request by T1: [1, 0, 2]
can_grant = banker.request_resources(1, [1, 0, 2])
print("Request granted:", can_grant)
