



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667R6MQ2X2%2F20260906%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260906T061135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQCMBpc6fe7uuICtiTw4oIZwfpWC3uXZSi1XeTdT7whIQgIhAMvnWJTC5LHebyYb0QJZ7NeuPyY9lZFCYn1litTFLXG8Kv8DCB4QABoMNjM3NDIzMTgzODA1IgytKdt3YqswYu4b2RIq3ANq93QVCxQFF9SgGBHWtY27kluXjd72N354FkJGsHqb0UnJ8W2mOi2aIM%2FlMSVs1d%2BdELy2ppzf4pDVt58CUG26ntP1CHl7gjD8rs7J%2BzP2nhjYM%2BWwn%2F%2FMW0%2BAaxIEYlboIXHf3B7Dve6xV8RYKxkZsxhyakJopewFZP72Q9kK5x4qpHU7SWXIRbQcRyF0A9scoQYgmmy9eoCySY1Rqht5%2FOiKKhnkKimPUWlMrsCmkNNpFdwFBK4mRpe5pojiHTncOhtFw3uLoyUTr6V6W4h%2FW8r%2B8Fc1v4TBCiGQWzDsxqvFA7nbRCBzZrJAy048P9enSiF7BoI39njt6Y9RjYCeNmLR3lmxXaJ5mcQmdWtG8WbFl98eFca9J%2BZ%2Fja0GB5byI4jhMbX%2BEsOV4t2YTLAt%2Bn%2BhqAhHb%2F67xTrGpuludlLPohHE2ipVyI9MRTcXxh6GgStQqmme84yBIGEZS90brOg8Cb%2FbbI2QDa2BIIyN1qb0Nw2x6L%2BdFCNIvr6opoJdnxet0562ZMsob%2B2f09v82OtgGCH3WN7TMJtfvGcBiywTaZ7bA3VJptL%2BfTtiLPLgwqiK%2FWf%2BDflwN4%2BydLNTFjGXRf58iPxk70gsaJVCa1d4tsyhFuDPyi2obTDL8PPUBjqkAU1SwOuwMVDwOYkyTP%2BZcG77quyemL2GK2mtyiw3tlHQEFaO7WZVx0HP2O0JvmP45zqi0qylYjST0a5gXd1Sagqu5fX37queXOMjya5Y7kUdkXnkBLGxfnmSSSYB3B%2BYQObw2zN1UoxlwpzRPCueKliAU1ehP5wUI24t4A58%2BxyT70p%2BVHaCdyuzRvPyLubEeSPqjipc8wguIbzla6WG%2Bqo%2BK6vu&X-Amz-Signature=25ab2400921f2695f4f4cb659b53abf56701c0c63fbfaec8ba6547c6e4a67e67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667R6MQ2X2%2F20260906%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260906T061135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQCMBpc6fe7uuICtiTw4oIZwfpWC3uXZSi1XeTdT7whIQgIhAMvnWJTC5LHebyYb0QJZ7NeuPyY9lZFCYn1litTFLXG8Kv8DCB4QABoMNjM3NDIzMTgzODA1IgytKdt3YqswYu4b2RIq3ANq93QVCxQFF9SgGBHWtY27kluXjd72N354FkJGsHqb0UnJ8W2mOi2aIM%2FlMSVs1d%2BdELy2ppzf4pDVt58CUG26ntP1CHl7gjD8rs7J%2BzP2nhjYM%2BWwn%2F%2FMW0%2BAaxIEYlboIXHf3B7Dve6xV8RYKxkZsxhyakJopewFZP72Q9kK5x4qpHU7SWXIRbQcRyF0A9scoQYgmmy9eoCySY1Rqht5%2FOiKKhnkKimPUWlMrsCmkNNpFdwFBK4mRpe5pojiHTncOhtFw3uLoyUTr6V6W4h%2FW8r%2B8Fc1v4TBCiGQWzDsxqvFA7nbRCBzZrJAy048P9enSiF7BoI39njt6Y9RjYCeNmLR3lmxXaJ5mcQmdWtG8WbFl98eFca9J%2BZ%2Fja0GB5byI4jhMbX%2BEsOV4t2YTLAt%2Bn%2BhqAhHb%2F67xTrGpuludlLPohHE2ipVyI9MRTcXxh6GgStQqmme84yBIGEZS90brOg8Cb%2FbbI2QDa2BIIyN1qb0Nw2x6L%2BdFCNIvr6opoJdnxet0562ZMsob%2B2f09v82OtgGCH3WN7TMJtfvGcBiywTaZ7bA3VJptL%2BfTtiLPLgwqiK%2FWf%2BDflwN4%2BydLNTFjGXRf58iPxk70gsaJVCa1d4tsyhFuDPyi2obTDL8PPUBjqkAU1SwOuwMVDwOYkyTP%2BZcG77quyemL2GK2mtyiw3tlHQEFaO7WZVx0HP2O0JvmP45zqi0qylYjST0a5gXd1Sagqu5fX37queXOMjya5Y7kUdkXnkBLGxfnmSSSYB3B%2BYQObw2zN1UoxlwpzRPCueKliAU1ehP5wUI24t4A58%2BxyT70p%2BVHaCdyuzRvPyLubEeSPqjipc8wguIbzla6WG%2Bqo%2BK6vu&X-Amz-Signature=e6438fd9d7cbc73e41a7d6bfdb27ec7a61b1400a19100db9778073edbff9b1c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Final Test







