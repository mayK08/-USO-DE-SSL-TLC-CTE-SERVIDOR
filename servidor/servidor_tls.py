import ssl
import socket

HOST = "127.0.0.1"
PORT = 5001

def imprimir_etapas_servidor():
    print()
    print("[Servidor] === Etapas del Protocolo SSL/TLS ===")
    print("[Servidor] 1??  HANDSHAKE PROTOCOL ␦ intercambio de claves, certificados, algoritmos.")
    print("[Servidor]     - ClientHello / ServerHello")
    print("[Servidor]     - Intercambio de certificados digitales")
    print("[Servidor]     - Generación de claves maestras compartidas (session keys)\n")
    print("[Servidor] 2??  SESIÓN Y CONEXIÓN ␦ se establece la sesión segura TLS.")
    print("[Servidor]     - Se asocian claves temporales (ephemeral)")
    print("[Servidor]     - Se crea la conexión cifrada\n")
    print("[Servidor] 3??  CHANGE CIPHER SPEC ␦ indica que inicia el cifrado real.\n")
    print("[Servidor] 4??  RECORD PROTOCOL ␦ encapsula, cifra y transmite datos.\n")

def main():
    print("=== DEMOSTRACIÓN DEL PROTOCOLO SSL/TLS===\n")
    print("[Servidor] Escuchando en 127.0.0.1:5001 ...")

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind((HOST, PORT))
        sock.listen(5)

        conn, addr = sock.accept()
        print("[Servidor] Conexión TCP aceptada. Preparando SslStream...")

        with context.wrap_socket(conn, server_side=True) as ssock:
            imprimir_etapas_servidor()

            print("[Servidor] Handshake completado correctamente.")
            print("[Servidor] Protocolo:", ssock.version())
            cipher = ssock.cipher()
            print("[Servidor] Cifrado:", cipher[0])
            print("[Servidor] ¿Cifrado activo?: True\n")

            data = ssock.recv(4096).decode()
            print("[Servidor] Mensaje recibido (descifrado):", data)

            respuesta = "Servidor: handshake, sesión y cifrado TLS confirmados"
            ssock.sendall(respuesta.encode())
            print("[Servidor] Respuesta cifrada enviada al cliente.")

if __name__ == "__main__":
    main()
