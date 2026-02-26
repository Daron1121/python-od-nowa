
#* 💣 Projekt: Mini API Service Simulator

# Zbuduj symulator backendowego serwisu, który:
# pobiera dane z „zewnętrznego API” (niestabilnego)
# ma retry
# ma rate limiter
# ma cache wyników
# ma autoryzację roli
# ma inicjalizację tylko raz
# Brzmi jak coś prawdziwego? Bo to jest realny backend pattern.

#* 🎯 Co masz zbudować

# 1️⃣ System użytkowników
# current_user_role = "user"
# Masz dekorator:
# @require_role("admin")
# def delete_user(user_id):
#     ...
# 2️⃣ Niestabilne API (losowo pada)
# def external_api_call(user_id):
#     # 50% szans na ValueError
# Ma być używane z:
# @retry(3)
# 3️⃣ Rate limiter
# Endpoint może być wywołany max 5 razy.
# @Limiter(5)
# 4️⃣ Cache wyników (once_per_args)
# Jeśli pytasz o tego samego usera drugi raz → nie pytasz API ponownie.
# @once_per_args
# def get_user_data(user_id):
#     ...
# 5️⃣ Inicjalizacja systemu tylko raz
# @once
# def initialize_database():
#     print("Connecting to DB..."
# 🧠 Finalny efekt
# Coś w stylu:
# initialize_database()
# print(get_user_data(1))
# print(get_user_data(1))  # z cache
# print(get_user_data(2))
# delete_user(1)  # tylko admin może

#* 🔥 Co ten projekt ćwiczy

# ✔ stacking dekoratorów
# ✔ kolejność wykonywania dekoratorów
# ✔ obsługa wyjątków
# ✔ stan w closure
# ✔ separację odpowiedzialności
# ✔ myślenie jak backend dev

#* 💣 Bonus (jeśli chcesz trudniej)

# Dodaj:
# logger dekorator, który loguje nazwę funkcji i czas wykonania
# retry tylko dla ValueError
# rate limiter resetujący się po czasie
# prostą klasę UserService zamiast luźnych funkcji