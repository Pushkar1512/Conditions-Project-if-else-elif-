#Coditions: if, elif and else

battery_voltage = 10.5

if battery_voltage>12.5:
    print("Battery is fully charged")
elif 11<= battery_voltage <= 12.5:
    print("Battery is moderately charged")
elif 9 <= battery_voltage <=11:
    print("Battery is low. Consider recharging")

else:
    print("Battery is critically low! Recharge immediately")
    
