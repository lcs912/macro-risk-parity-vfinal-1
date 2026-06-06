from app.data import get_data
from app.quadrant import quadrant
from app.allocator import allocate
from app.rebalance import rebalance
from app.email_notify import send_email

def run():

    df = get_data()

    returns = df.pct_change().dropna()

    growth = returns["SPY"].mean()
    inflation = -returns["TLT"].mean()

    q = quadrant(growth, inflation)

    target = allocate(q)

    current = {k:0.25 for k in target}

    actions = rebalance(current, target)

    msg = f"""
Macro Risk Parity System

Regime: {q}

Growth: {growth:.4f}
Inflation: {inflation:.4f}

Target Allocation:
{target}

Rebalance:
{actions}
"""

    send_email(msg)

if __name__ == "__main__":
    run()
