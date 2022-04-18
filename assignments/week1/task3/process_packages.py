# python3


from collections import deque


class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time


class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_times = deque()

    def process(self, request):
        while self.finish_times and self.finish_times[0] <= request.arrival_time:
            self.finish_times.popleft()

        if len(self.finish_times) == self.size:
            return Response(True, -1)
        else:
            start_time = (
                self.finish_times[-1] if self.finish_times else request.arrival_time
            )
            self.finish_times.append(start_time + request.process_time)
            return Response(False, start_time)


def read_requests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def print_responses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)


if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = read_requests(count)

    buffer = Buffer(size)
    responses = process_requests(requests, buffer)

    print_responses(responses)
