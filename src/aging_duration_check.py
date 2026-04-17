from temperature_limits import AGING_DURATION_HOURS
# aging is dependent on recipe. In this model, version 06.2025 recipe is activated.
def check_aging_duration(actual_hours):
    if actual_hours >= AGING_DURATION_HOURS:
        return "Aging duration OK"
    return "Aging duration NOT sufficient"
