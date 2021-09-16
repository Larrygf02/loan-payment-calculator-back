from datetime import datetime
import math

def run(data):
    is_double_fee = data.get('is_double_fee')
    if not is_double_fee:
        result = calculate_with_simple_fee(data)
    else:
        result = calculate_with_double_fee(data)
    return result

def calculate_with_simple_fee(data):
    result = []
    amount = data.get('amount')
    loan_term = data.get('loan_term')
    interest_rate = data.get('interest_rate')
    interest_rate = (interest_rate / 12) / 100
    fee = ((((1 + interest_rate)**loan_term) * interest_rate) / (((1 + interest_rate)**loan_term) -1)) * amount
    fees_paid = 0
    capital = amount
    dates = get_dates_paid(loan_term)
    dates = dates[1:]
    while fees_paid < loan_term:
        payday = dates[fees_paid]
        interest = interest_rate * capital
        amortization = fee - interest
        capital = capital - amortization
        result_item = {
            'fee': round(fee,2),
            'interest': round(interest,2),
            'amortization': round(amortization,2),
            'capital': round(capital,2),
            'payday': formate_date(payday)
        }
        result.append(result_item)
        fees_paid += 1
    return result
        
def calculate_with_double_fee(data):
    result = []
    amount = data.get('amount')
    dues = data.get('loan_term')
    interest_rate = data.get('interest_rate')
    interest_rate = interest_rate / 100
    interest_per_day = (math.pow((1+interest_rate), (1/360)) - 1)
    dates = get_dates_paid(dues)
    fsas , difference_days = get_fsa(dates, dues, interest_per_day)
    dates = dates[1:]
    fee = amount / sum(fsas)
    fee = round(fee, 2)
    balance = amount
    for i in range(dues):
        interest = balance * (math.pow((1+interest_per_day), difference_days[i]) - 1)
        payday = dates[i]
        if payday.month == 6 or payday.month == 12:
            fee_month = fee * 2
        else:
            fee_month = fee
        amortization = fee_month - interest
        balance -= amortization
        result_item = {
            'fee': fee_month,
            'interest': round(interest,2),
            'amortization': round(amortization,2),
            'capital': round(balance,2),
            'payday': formate_date(payday)
        }
        result.append(result_item)
    return result

def get_dates_paid(dues):
    days = []
    now = datetime.now()
    day = 28 if now.day > 28 else now.day
    month = now.month
    year = now.year
    days.append(datetime(year, month, day))
    for _ in range(1, dues+1):
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
        days.append(datetime(year, month, day))
    return days

def get_fsa(dates, dues, interest_per_day):
    i = 0
    acummulate_days = 0
    fsas = []
    difference_days = []
    while i <= (dues-1):
        payday = dates[i+1]
        days = (dates[i+1] - dates[i]).days
        acummulate_days += days
        if payday.month == 6 or payday.month == 12:
            fsa = math.pow((1+interest_per_day), -acummulate_days) * 2
        else:
            fsa = math.pow((1+interest_per_day), -acummulate_days)
        fsas.append(fsa)
        difference_days.append(days)
        i+= 1
    return (fsas, difference_days)

def formate_date(date):
    return date.strftime("%Y-%m-%d")