'''
    sorted é uma função built-in que recebe como parâmentros:
        1. o iterável
        2. regra da ordenação - opcional, padrão: do menor ao maior
'''

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
