def quadrant(growth, inflation):

    if growth > 0 and inflation < 0:
        return "GOLDILOCKS"

    if growth > 0 and inflation > 0:
        return "INFLATION"

    if growth < 0 and inflation < 0:
        return "DEFLATION"

    return "STAGFLATION"
