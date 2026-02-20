def is_positive(x):
     return x > 0
def is_even(x):
     return x % 2 == 0

def validator(rules):
    
    def rule_checker(number):
        for rule in rules:
            if rule(number):
                continue
            else:
                return False
        return True
    return rule_checker   

validate_number = validator([is_positive, is_even])

print(validate_number(4))   # True
print(validate_number(3))   # False