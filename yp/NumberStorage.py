class NumberStorage:
    def __init__(self, numbers):
        self.buckets = [[] for _ in range(len(numbers))]
        
        for number in numbers:
            bucket = self.get_bucket(number)
            self.buckets[bucket].append(number)

    def get_bucket(self, x):
        return abs(x) % len(self.buckets)

    def has_number(self, x):
        bucket = self.get_bucket(x)
        return x in self.buckets[bucket]
