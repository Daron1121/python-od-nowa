current_user_role = "admin"

def require_role(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if role == current_user_role:
                return func(*args, **kwargs)
            else:
                raise PermissionError("You dont have permission to do that!")
        return wrapper
    return decorator

@require_role("admin")
def delete_user():
    return 'User deleted!'

print(delete_user())
print(delete_user())