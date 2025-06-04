"""Attributes (private):
__model
__battery_level (0 to 100)
Methods (public):
__init__(self, model)
charge(self, amount) — increases battery
use(self, amount) — decreases battery
get_battery_level(self)
get_phone_info(self)
Prevent direct access to __battery_level.
Cap battery between 0 and 100%.
Validate inputs to avoid overcharging or draining below 0%.
Add a method is_battery_low() that returns True if battery < 20%.
Add charging time simulation using time.sleep() (for realism)."""
class MobileBattery:
    def __init__(self):
        model=input("Enter the name of your phone: ")
        self.model=model
        self.__battery_lvl=80
        print(f"Model of the phone: {self.model}")
    
    def charge(self, charged_lvl):
        if charged_lvl > 0:
            self.__battery_lvl += charged_lvl
            if self.__battery_lvl > 100:  
                self.__battery_lvl = 100
            print(f"Charge = {self.__battery_lvl}%")
        else:
            print("Charged amount must be positive.")

    def battery_used(self,used_lvl):
        if used_lvl>0:
            self.__battery_lvl-=used_lvl
            print(f"Charge = {self.__battery_lvl}%")

        else:
            print("Used amount of battery must be positive.")
        
        if self.__battery_lvl<20:
            print("Battery Saver turned ON")
        else:
            return ""
        
def takeinput():
    c1=MobileBattery()
    increasecharge=int(input("Enter the charged charge: "))
    c1.charge(increasecharge)
    decreasechargee=int(input("Enter the used charge: "))
    c1.battery_used(decreasechargee)
     
takeinput()