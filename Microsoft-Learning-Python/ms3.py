print("Today's date?")
date = input()
print("Breakfast calories?")
breakfast = int(input())
print("Lunch calories?")
lunch = int(input())
print("Dinner calories?")
dinner = int(input())
sum = breakfast + lunch + dinner
print(f"Calories consumed on {date} {str(sum)}")
