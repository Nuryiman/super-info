deposit = int(input("ВВедите сумму:"))


for item in range(1, 366):
    percent = deposit / 100
    deposit += percent
print(deposit)
