# python3

MAX_PHONE_NUM = 10**7
RESPONSE_NOT_FOUND = "not found"


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == "add":
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print("\n".join(result))


def process_queries(queries):
    result = []
    contacts = [None] * MAX_PHONE_NUM

    for query in queries:
        number = query.number
        if query.type == "add":
            contacts[number] = query.name
        elif query.type == "del":
            if contacts[number]:
                contacts[number] = None
        elif query.type == "find":
            if contacts[query.number]:
                result.append(contacts[query.number])
            else:
                result.append(RESPONSE_NOT_FOUND)
        else:
            raise RuntimeError(f"Invalid query: {query.type}")

    return result


if __name__ == "__main__":
    write_responses(process_queries(read_queries()))
