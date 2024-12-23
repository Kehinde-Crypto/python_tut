def what_year_is(value , values):
  years_passed = values// 365
  final_year = value + years_passed
  if years_passed > 0:
    print(f"{values} days after,{value} , is going to be the {final_year}")
  else:
    print(f"{values} days after Jan 1st, {final_year} , is going to be the {final_year}")
  print("Happy new year!")
  what_year_is(1950 , 204)
  what_year_is(2005 , 2024)
  