# Program to represent data required for
# "Job Sequencing with Deadlines" using dataclass
from dataclasses import dataclass

@dataclass
class Job:
    job_id : str
    deadline : int
    profit : int

def jobSequencing(jobs):
# Sort jobs by profit in descending order
    jobs.sort(key = lambda x: x.profit, reverse = True)

    # Printing total jobs after sorting
    # in decreasing order of profit
    jobs_sorted = []
    print("Sorted job list: ")
    for item in jobs:
        jobs_sorted.append((item.job_id, item.deadline, item.profit))
    print(jobs_sorted,"\nThe scheduled jobs:")
        
    # Initialize result array with None
    # for schedules where jobs can not be
    # performed it will return 'None' at that place
    result = ['None'] * len(jobs)

    # Traverse jobs in sorted order
    for job in jobs:
        # Find the first empty slot from the deadline
        for i in range(min(job.deadline, len(jobs)) - 1, -1, -1):
            # If slot is empty, add job to result
            if result[i] == 'None':
                result[i] = job.job_id 
                break
  
    return result


# Driver code
jobs = [Job('J1', 3, 100), Job('J2', 2, 50), Job('J3', 1, 25),
        Job('J4', 2, 35), Job('J5', 3, 20)]

print(jobSequencing(jobs))