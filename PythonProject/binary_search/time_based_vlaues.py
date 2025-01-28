class TimeMap:
    def __init__(self):
        self.keyStore = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore: # if the key is not in the dictionary
            self.keyStore[key] = [] # create a new key
        self.keyStore[key].append([value, timestamp]) # append the value and timestamp to the key


    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, []) # get the values of the key
        l, r = 0, len(values) - 1
        while l <= r: # perform binary search so that we can get a value which is less than or equal to the timestamp
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res