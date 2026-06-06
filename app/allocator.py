def allocate(q):

    base = {
        "SPY": 0.25,
        "QQQ": 0.15,
        "TLT": 0.35,
        "GLD": 0.25
    }

    if q == "INFLATION":
        base["GLD"] += 0.1

    return base
