import pyupbit

access = "TIomsZW1fMWmx7NMy0CoAqr30DD2gEaLE6eRhaiS"
secret = "9atdEcuwxWIt7AXyOGJ88LeEEe9bItGFG7gFNOPa"
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))
print(upbit.get_balance("KRW"))