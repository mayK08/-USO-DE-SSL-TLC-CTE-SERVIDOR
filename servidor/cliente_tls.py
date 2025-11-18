import ssl
import socket

HOST = "127.0.0.1"
PORT = 5001

def imprimir_etapas_cliente():
    print("[Cliente] Conexión TCP establecida con el servidor.\n")
    print("[Cliente] === Etapas del Protocolo SSL/TLS ===")
    print("[Cliente] 1??  HANDSHAKE PROTOCOL")
    print("[Cliente]     - ClientHello / ServerHello")
    print("[Cliente]     - Certificados")
    print("[Cliente]     - Claves maestras compartidas\n")
    print("[Cliente] 2??  SESIÓN Y CONEXIÓN\n")
    print("[Cliente] 3??  CHANGE CIPHER SPEC\n")
    print("[Cliente] 4??  RECORD PROTOCOL\n")

def main():
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE  # Aceptar certificado autofirmado

    with socket.create_connection((HOST, PORT)) as sock:
        imprimir_etapas_cliente()

        with context.wrap_socket(sock, server_hostname="ServidorSSL") as ssock:
            print("[Cliente] Handshake completado exitosamente.")
            print("[Cliente] Protocolo:", ssock.version())
            print("[Cliente] Cifrado:", ssock.cipher()[0])
            print("[Cliente] ¿Cifrado activo?: True\n")

            mensaje = "Cliente: Hola servidor, confirmo cifrado y sesión TLS activa."
            ssock.sendall(mensaje.encode())
            print("[Cliente] Mensaje cifrado enviado al servidor.\n")

            data = ssock.recv(4096).decode()
            print("[Cliente] Respuesta descifrada del servidor:", data)

if __name__ == "__main__":
    main()
