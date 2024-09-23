class Counter:
    def __init__(self):
        self._count = 0
        self._open = False

    def __enter__(self):
        self._open = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._open = False

    def add(self):
        if not self._open:
            raise Exception("Counter not used in a resource context")
        self._count += 1

    def get_count(self):
        return self._count

# Использование
try:
    with Counter() as counter:
        counter.add()
except Exception as e:
    print(e)
