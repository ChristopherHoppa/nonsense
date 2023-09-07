import re

def find_state_timezone(address):
    # Dictionary of state acronyms and their respective time zones
    state_time_zones = {
        'AL': 'CST',
        'AK': 'AKST',
        'AZ': 'MST',
        'AR': 'CST',
        'CA': 'PST',
        'NY': 'EST',
        # Add more state acronyms and time zones as needed
    }

    # Regular expression pattern to match state acronyms (case insensitive)
    state_pattern = r'\b(' + '|'.join(state_time_zones.keys()) + r')\b'

    # Function to find and return the state acronym from an address
    def find_state_acronym(address):
        match = re.search(state_pattern, address, re.IGNORECASE)
        if match:
            return match.group().upper()
        else:
            return None

    state_acronym = find_state_acronym(address)
    if state_acronym:
        timezone = state_time_zones.get(state_acronym)
        if timezone:
            return timezone  # Return the time zone value from the dictionary
        else:
            return f"No time zone found for state acronym: {state_acronym}"
    else:
        return "No state acronym found in the address"

# Sample addresses
addresses = [
    "123 Main St, Springfield, IL 62701",
    "456 Oak Ave, Los Angeles, CA 90001",
    "789 Elm Rd, New York, NY 10001",
]

# Call the function for each address and print the result
for address in addresses:
    result = find_state_timezone(address)
    print(result)
