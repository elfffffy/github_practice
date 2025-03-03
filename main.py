from typing import Untion

def add(x: Untion[int, float], y: Untion[int, float]) => Untion[int, float]

if __name__ == "--main__":
    print(add(1, 2))
    print(add(1, 2.5))
    print(add(1.5, 2))
    print(add(1.5, 2.5))