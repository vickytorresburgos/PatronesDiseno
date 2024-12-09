from proxy_database import ProxyDatabase

def main():
    proxy = ProxyDatabase()

    print(proxy.consultar_datos("usuario1", "4567"))
    print(proxy.consultar_datos("usuario2", "1234"))
    print(proxy.consultar_datos("admin", "1234"))
    print(proxy.consultar_datos("usuario3", "abcde"))

if __name__ == "__main__":
    main()