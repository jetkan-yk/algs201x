# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store strings in a dictionary with hash values as keys
        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # check if hash number exists in dictionary keys
            if query.ind in self.elems:
                for elem in reversed(self.elems[query.ind]):  # print in reverse
                    print(elem, end=" ")
                print("")
            else:  # print blank line
                print("")
        else:
            if query.type == 'find':
                hash_num = self._hash_func(query.s)
                # check if hash number exists in dictionary keys
                if hash_num in self.elems:
                    # check if string is in chain
                    if query.s in self.elems[hash_num]:
                        print("yes")
                    else:
                        print("no")
                else:  # print no
                    print("no")
            elif query.type == 'add':
                hash_num = self._hash_func(query.s)
                # check if hash number exists in dictionary keys
                if hash_num in self.elems:
                    # append to chain of hash number key if element does not exist
                    if query.s not in self.elems[hash_num]:
                        self.elems[hash_num].append(query.s)
                else:  # else, create new key and list as value
                    self.elems[hash_num] = [query.s]
            else:  # delete element
                hash_num = self._hash_func(query.s)
                if hash_num in self.elems:
                    for i in range(len(self.elems[hash_num])):
                        if self.elems[hash_num][i] == query.s:
                            self.elems[hash_num].pop(i)
                            break
                    # delete key if chain is empty
                    if len(self.elems[hash_num]) == 0:
                        del self.elems[hash_num]

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
