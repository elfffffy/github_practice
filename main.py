from typing import Untion, Optional

def add(x: Untion[int, float], y: Untion[int, float]) -> Optional[Untion[int, float]]:
    try: 
        result = x + y
    except Exception as e:
            print(e)
            return None

    return result    

if __name__ == "--main__":
    print(add(1, 2))
    print(add(1, 2.5))
    print(add(1.5, 2))
    print(add(1.5, 2.5))