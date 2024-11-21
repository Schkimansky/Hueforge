
def rangify(component: int) -> int: return max(0, min(255, component))

def percentage_to_factor(percentage: int | float) -> float:
    factor = (percentage + 100) / 100

    # if percentage < 0:
    #     factor = -factor

    return factor

def unfloatify(component: float) -> int: return int(component)
