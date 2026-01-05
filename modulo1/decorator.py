def decorLog(func):
    def wrapper(*args, **kwargs):
        print(f"Chama  funcao: {func.__name__} com os argumentos: {args} e {kwargs}")
        result = func(*args, **kwargs)
        print("Operacao Concluida")
        return result
    return wrapper

@decorLog
def soma(a, b):
    return a + b

@decorLog
def saudacao(nome, saudacao="Ola"):
    print(f"{saudacao}, {nome}")

print(soma(1,7))
saudacao("AAAAA", saudacao="Bom dia")