from datetime import datetime, timedelta
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
    while fees_paid < loan_term:
        fees_paid += 1
        interest = interest_rate * capital
        amortization = fee - interest
        capital = capital - amortization
        result_item = {
            'fee': round(fee,2),
            'interest': round(interest,2),
            'amortization': round(amortization,2),
            'capital': round(capital,2)
        }
        result.append(result_item)
    return result
        
def calculate_with_double_fee(data):
    dues = data.get('loan_term')
    days = get_days_paid(dues)
    print(days)

def get_days_paid(dues):
    days = []
    now = datetime.now()
    day = 28 if now.day > 28 else now.day
    month = now.month
    year = now.year
    for _ in range(1, dues):
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
        days.append(datetime(year, month, day))
    return days
        