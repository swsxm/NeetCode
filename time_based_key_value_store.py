class TimeMap:

    def __init__(self):
        self.key_value_store = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_value_store:
            self.key_value_store[key] = []
        self.key_value_store[key].append([timestamp, value])
        print(self.key_value_store)
 

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.key_value_store.get(key, [])) - 1
        res = ""
        while l <= r:
            mid = (l+r) // 2
            val = self.key_value_store[key][mid]
            if val[0] <= timestamp:
                l = mid + 1
                res = val[1]
            else:
                r = mid - 1
        return res 

timeMap = TimeMap()
timeMap.set("alice", "happy", 1)  # store the key "alice" and value "happy" along with timestamp = 1.
print(timeMap.get("alice", 1))            # return "happy"
print(timeMap.get("alice", 2))           # return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
timeMap.set("alice", "sad", 3)    # store the key "alice" and value "sad" along with timestamp = 3.
print(timeMap.get("alice", 3))           # return "sad"
