import pyupbit

access = "your-access"
secret = "your-secret"
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))
print(upbit.get_balance("KRW"))
