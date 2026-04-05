


def fix_phone_num(phone_num_to_fix):
    if not phone_num_to_fix.isdigit():
        raise ValueError("Phone number must contain only digits")
    
    # Strip leading country code 1 if 11 digits
    if len(phone_num_to_fix) == 11 and phone_num_to_fix[0] == '1':
        phone_num_to_fix = phone_num_to_fix[1:]
    
    if len(phone_num_to_fix) != 10:
        raise ValueError("Phone number must be 10 digits")
    
    area_code = phone_num_to_fix[0:3]
    three_part = phone_num_to_fix[3:6]
    four_part = phone_num_to_fix[6:]
    
    return "(" + area_code + ") " + three_part + " " + four_part



