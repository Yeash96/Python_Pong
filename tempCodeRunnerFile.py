    reply = ""
    while True:
        try:
            data = conn.recv(1024 * 2)
            reply = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("Recveived:", reply)
                print("Sending:", reply)
            
            conn.sendall(str.encode(reply))
        except:
            break