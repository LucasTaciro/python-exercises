EXPECTED_BAKE_TIME = 40
def bake_time_remaining(elapsed_bake_time):
    """Calculate the time period left for the cake to be ready"""
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
def preparation_time_in_minutes(number_of_layers):
    """Calculate the time to add tha lasagna layers"""
    return number_of_layers * 2
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time ):
    """Calculate the time that it spends on the kitchen"""
    return (number_of_layers * 2) + elapsed_bake_time 
