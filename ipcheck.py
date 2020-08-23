from __future__ import print_function

if __name__ == '__main__':
    
    import sys
    import socket

    base_ip = "192.168.0."
    port = 80

    if len(sys.argv) > 2:
        setbip = False
        setport = False
        for arg in sys.argv:
            if setbip:
                base_ip = arg
                setbip = False
            elif setport:
                port = arg
                setport = False
            else:
                if arg == '-bip':
                    setbip = True
                elif arg == '-port':
                    setport = True
            


    opts = {
        "show_details": '--details' in sys.argv or '-d' in sys.argv
    }

    if base_ip[-1] != '.':
        base_ip += '.'
        
    timeout = 0.01

    sockets = []
    sockets.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    sockets[-1].settimeout(timeout)

    base_string = "\n{}:{} valid!\n" if opts["show_details"] else "{}:{} valid!"

    if opts["show_details"]:
        status_list = {}

    for i in xrange(256):

        actual_ip = base_ip+str(i)
        status = sockets[-1].connect_ex((actual_ip, port))

        if status == 0:
            print(base_string.format(actual_ip, port))
            sockets[-1].shutdown(socket.SHUT_RDWR)
        
        sockets[-1].close()
        sockets.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        sockets[-1].settimeout(timeout)

        if opts["show_details"]:
    
            sstatus = str(status)

            if status != 0:
                print(i, end=' ')

            if(not sstatus in status_list):
                status_list[sstatus] = []
            
            status_list[sstatus].append( '{}:{}'.format(actual_ip, port) )

    if opts["show_details"]:
        print()
        print(status_list)