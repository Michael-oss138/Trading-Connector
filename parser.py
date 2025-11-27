import re


def parsesignal(message: str):
    pattern = r"(BUY|SELL)\s+([A-Z]{2,10})\s+([\d.]+)\s*@\s*([\d.]+)"
    match = re.search(pattern, message.upper())

    if match:
        action = match.group(1)
        coin = match.group(2)
        amount = float(match(3))
        price = flot(match(4))

        return{
            "action": action,
            "coin": coin,
            "amount": amount,
            "price": price
        }
    return None