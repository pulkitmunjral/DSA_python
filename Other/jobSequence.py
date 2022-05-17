"""Given a set of N jobs where each jobi has a deadline and profit associated with it.

Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with job if and only if the job is completed by its deadline.

Find the number of jobs done and the maximum profit.

Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job

Input:
N = 4
Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output:
2 60
Explanation:
Job1 and Job3 can be done with
maximum profit of 60 (20+40).
Input:
N = 5
Jobs = {(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)}
Output:
2 127
Explanation:
2 jobs can be done with
maximum profit of 127 (100+27).
"""
def JobScheduling(Jobs, n):
    Jobs = sorted(Jobs, key=lambda x: x[2], reverse=True)

    count = 0
    money = 0
    time = [-1 for _ in range(101)]
    for job in Jobs:
        temp = job[1]
        while temp:
            if time[temp] == -1:
                money += job[2]
                count += 1
                time[temp] = 1
                break
            temp -= 1
    print(count, money)


JobScheduling([(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)],5)