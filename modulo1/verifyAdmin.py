# decorador verifica argumento 1 da func
# se arg1 for admin, corre
# caso contario, impede execucao e "Acesso Negado!"

def verifyAdmin(func):
    def wrapper(*args, **kwargs):
        if args and args[0] == "admin":
            return func(*args, **kwargs)
        else:
            print("Acesso Negado!")
    return wrapper

@verifyAdmin
def acessSys(user):
    print(f"Bem-vindo(a), {user}! Acedendo aos dados...")

print("Admin: ")
acessSys("admin")
print("=========================================")
print("Not Admin: ")
acessSys("not admin")