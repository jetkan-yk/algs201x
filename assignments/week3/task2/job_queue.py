# python3


from heapq import heapify, heappop, heappush


class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)

        scheduler = [(0, i) for i in range(self.num_workers)]
        heapify(scheduler)
        for i, duration in enumerate(self.jobs):
            start_time, assigned_worker = heappop(scheduler)
            self.start_times[i], self.assigned_workers[i] = start_time, assigned_worker
            new_schedule = (start_time + duration, assigned_worker)
            heappush(scheduler, new_schedule)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == "__main__":
    job_queue = JobQueue()
    job_queue.solve()
