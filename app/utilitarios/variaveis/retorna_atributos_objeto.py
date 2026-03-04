def imprimindo_dados_objeto(obj):
    try:
        for key,value in vars(obj).items():
            print(f"{key}: {value}")
    except:
        print("O objeto não possui atributos de instância (__dict__)")