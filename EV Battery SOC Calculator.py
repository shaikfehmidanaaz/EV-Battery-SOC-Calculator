# EV Battery SOC Calculator
# EEE Mini Project - Python

class EVBatterySOC:

    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def calculate_soc(self, initial_soc, energy_used):
        # Energy available at the beginning
        initial_energy = self.battery_capacity * (initial_soc / 100)

        # Remaining energy
        remaining_energy = initial_energy - energy_used

        if remaining_energy < 0:
            remaining_energy = 0

        # Calculate SOC
        soc = (remaining_energy / self.battery_capacity) * 100

        return remaining_energy, soc

    def display(self, remaining_energy, soc):
        print("\n================================")
        print("     EV BATTERY SOC CALCULATOR")
        print("================================")

        print(f"Battery Capacity : {self.battery_capacity:.2f} kWh")
        print(f"Remaining Energy : {remaining_energy:.2f} kWh")
        print(f"Battery SOC      : {soc:.2f}%")

        print("--------------------------------")

        if soc >= 80:
            print("Battery Status   : HIGH")
        elif soc >= 50:
            print("Battery Status   : GOOD")
        elif soc >= 20:
            print("Battery Status   : LOW")
        else:
            print("Battery Status   : CRITICAL")
            print("Warning: Please charge the battery!")

        print("================================")


# Main Program
print("EV BATTERY SOC CALCULATOR")

battery_capacity = float(
    input("Enter battery capacity (kWh): ")
)

initial_soc = float(
    input("Enter initial SOC (%): ")
)

energy_used = float(
    input("Enter energy consumed (kWh): ")
)

# Input validation
if battery_capacity <= 0:
    print("Invalid battery capacity.")

elif initial_soc < 0 or initial_soc > 100:
    print("SOC must be between 0 and 100%.")

elif energy_used < 0:
    print("Energy consumed cannot be negative.")

else:
    ev = EVBatterySOC(battery_capacity)

    remaining_energy, soc = ev.calculate_soc(
        initial_soc,
        energy_used
    )

    ev.display(
        remaining_energy,
        soc
    )
