# BasicProxy

### Running the proxy server
pythons proxy.py \<port\> 

### Stop the server
Ctrl + C

### Making a request using telnet absolute URLexample
telnet localhost \<port\> 

Trying 127.0.0.1...

Connected to localhost.localdomain (127.0.0.1).

Escape character is ’^]’.

GET http://www.cs.utah.edu/~kobus/simple.html HTTP/1.0 //->[Enter URL and press enter]

//->[In order to let the server know you're done entering input press enter again]

### Making a request using telnet relative URL example
telnet localhost <port>

Trying 127.0.0.1...

Connected to localhost.localdomain (127.0.0.1).

Escape character is ’^]’.

GET /~kobus/simple.html HTTP/1.0 //-> [Press Enter]

Host: www.cs.utah.edu //-> [Press Enter]
[Press Enter once more to let the server know you are finished]


## Notes:
* The server will print out some stuff to the console letting the user know what's happening with the current process.

