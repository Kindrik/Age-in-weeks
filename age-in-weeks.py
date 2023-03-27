age = input('What is your current age?'\n)

age_as_a_number = int(age)

years_remaining = 90 - age_as_a_number
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

message = f"you have {days_remaining} days, {months_remaining} months, and {days_remaining} days left."

print("message")


