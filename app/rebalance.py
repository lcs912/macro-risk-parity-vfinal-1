def rebalance(current, target):

    actions = {}

    for k in target:
        actions[k] = round(
            target[k] - current.get(k, 0),
            3
        )

    return actions
