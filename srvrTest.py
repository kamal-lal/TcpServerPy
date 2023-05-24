import socket
from datetime import datetime

host = input('Enter interface IP: ')
# host = '192.168.70.100'
port = int(input('Local TCP Port to open: '))
# port = 3701

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print(f'[INFO] Server "{host}" listening on port "{port}"...')
    conn, addr = s.accept()

    try:
        with conn:
            print(f'\n[INFO] Connected to "{addr[0]}" on port "{addr[1]}"!\n')
            while True:
                data = conn.recv(1024)
                now_str = str(datetime.now().time())
                first_int = (data[0] << 8) | data[1]
                last_int = (data[-2] << 8) | data[-1]
                print(f'Source [{addr[0]}:{addr[1]}]. Timestamp [{now_str[:-4]}]')
                print(f'Bytes Received: {len(data)},  FirstElement: {first_int:02d},  LastElement: {last_int:02d}')
                print()
    except KeyboardInterrupt:
        print('[INFO] Closing connection. Exiting application.')
    except Exception as e:
        print(f'[ERROR] Error occured! Exiting application.\nErr: {e}, Type: {type(e)}.')

