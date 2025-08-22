def convert_to_human_readable(value: float) -> str:
    thresholds = [
        (1_000_000_000, "B"),
        (1_000_000, "M"),
        (1_000, "K"),
    ]
    for threshold, label in thresholds:
        if value > threshold:
            return f"{value / threshold:.2f}{label}"

    return str(value)
