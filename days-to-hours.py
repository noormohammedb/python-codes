user_input = input("Enter No.of Days: ")
# print(type(int(user_input)))
user_input_number = float(user_input)
calculation_units = 24
name_of_unit = "Hours"

def day_to_hours(days):
   if days > 0:
      return f"{days} days are {float(days) * calculation_units} {name_of_unit}"
   else:
      return "error"

print(day_to_hours(user_input_number))

# print(final_calculation)