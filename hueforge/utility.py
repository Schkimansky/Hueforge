
def percentage_to_factor(percentage: int | float) -> float:
    return (percentage + 100) / 100

def patch(channel: int | float) -> int:
    return max(0, min(255, int(channel)))

def patch_rgba(rgba):
    return tuple( patch(channel) for channel in rgba )  # noqa
