
rates = {
    "usd" : {
        "value" : 1,
        "symbol" : '$'
    },
    "inr" : {
        "value" : 65.44,
        "symbol" : '₹'
    },
    "cad" : {
        "value" : 1.25,
        "symbol" : '$'
    },
    "eur" : {
        "value" : 0.85,
        "symbol" : '€'
    },
    "gbp" : {
        "value" : 0.77,
        "symbol" : '£'
    },
    "yen" : {
        "value" : 112.63,
        "symbol" : '¥'
    },
    "aud" : {
        "value" : 1.29,
        "symbol" : '$'
    },
    "nzd" : {
        "value" : 1.41,
        "symbol" : '$'
    },
    "zar" : {
        "value" : 13.77,
        "symbol" : 'R'
    },
    "sek" : {
        "value" : 8.12,
        "symbol" : 'kr'
    }
}

#Logic
#print("200 INR to CAD = %.3f" % ((200 / rates["inr"]) * rates["cad"]))
#print("3 INR to USD = %.3f" % (3 / rates["inr"]))

userQuery = {
    'currencyValue' : '',
    'fromCurrency' : '',
    'toCurrency' : ''
}
result = ''
userInput = input("Enter the query : ").lower()
splittedInput = userInput.split(" ")

#Put the data into the dictionary
userQuery['currencyValue'] = float(splittedInput[0])
userQuery['fromCurrency'] = str(splittedInput[1])
userQuery['toCurrency'] = str(splittedInput[3])

#check if user have entered correct format
if(userQuery['fromCurrency'] in rates.keys() and userQuery['toCurrency'] in rates.keys()):
    if userQuery['toCurrency'] == 'usd':
        result = userQuery['currencyValue'] / rates[userQuery['fromCurrency']]['value']
    else:
        result = (userQuery['currencyValue'] / rates[userQuery['fromCurrency']]['value']) * rates[userQuery['toCurrency']]['value']

    print(rates[userQuery['toCurrency']]['symbol'] + "%.3f" % result)

else:
    print("Please enter the correct format, example: 400 USD to INR")