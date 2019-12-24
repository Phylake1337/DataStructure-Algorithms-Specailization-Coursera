# python3
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
Node = namedtuple("Node", ["threadN","nextFreeT"])


 
def leftChild(i):
    return 2 * i + 1
def rightChild(i):
    return 2 * i + 2

def SiftDown(i, n, threads):
    maxI = i

    l = leftChild(i)
    if l < n and threads[l].nextFreeT < threads[maxI].nextFreeT:
        maxI = l
        
    if (l < n and threads[l].nextFreeT == threads[maxI].nextFreeT 
                and threads[l].threadN < threads[maxI].threadN) :
        maxI = l
        
    r = rightChild(i)
    if r < n and threads[r].nextFreeT < threads[maxI].nextFreeT:
        maxI = r
    if (r < n and threads[r].nextFreeT == threads[maxI].nextFreeT 
                  and threads[r].threadN < threads[maxI].threadN) :
        maxI = r      
        
    if maxI != i:
        threads[maxI], threads[i] = threads[i], threads[maxI]
        SiftDown(maxI, n, threads)
    


def Assign_jobs(n_workers, jobs):
    #intializing the threads as a priority queue
    threads = []
    for i in range (n_workers):  
        threads.append(Node(i, 0))
    
    #process the jobs
    result = []
    while jobs:
        result.append(AssignedJob(threads[0].threadN, threads[0].nextFreeT))
        currJob = jobs.pop(0)
        threads[0] = Node(threads[0].threadN, threads[0].nextFreeT + currJob)
        SiftDown(0, n_workers, threads)
    return result
    


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = Assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
