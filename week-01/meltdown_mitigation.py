def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced."""
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone."""
    generated_power = voltage * current
    percentage_value = (generated_power/theoretical_max_power)*100
    
    if percentage_value >= 80:
        return "green"
    elif 80 > percentage_value >= 60:
        return "orange"
    elif 60 > percentage_value >= 30:
        return "red"
    else:
        return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor."""
    criticality = temperature * neutrons_produced_per_second
    if criticality < (threshold * 90)/100:
        return "LOW"
    elif (threshold * 90)/100 <= criticality <= (threshold * 110)/100:
        return "NORMAL"
    else:
        return "DANGER"