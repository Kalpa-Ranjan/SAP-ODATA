



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BA4NGIY%2F20260828%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260828T213925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAgMZ6RlTRKZjUm9eiGLi0WC1Qzld94NlDs2Urjtrd7WAiB1BaN0RvOQ9Ar9rmsvh92XHvXWWmKv8vokvywmIyWcyCr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMNyyL%2FnUmjNExGwJ2KtwDJzBfK3fJPaxaOpYuIF7S%2BuCdjOSdv%2BsrllvfmP1fmkPVlg1qnBiwCLRcNG5bNDWXgrqYjC4P9faKL3A%2FB4%2BlUxwQTduLtcm%2F59xdPEL3siVYFkpNlrP2FpDLkNDHGnzyjGLLNHB%2FGAAidAsoDOcgxoPpfaZPypi8amgU%2FxTHoBFmKtT1C%2FUMGcIG7F5zCtwUTZ0%2FzBLV%2Bw%2B0v0qQ9im%2FRQOSZ%2B%2BAyEeYZpHdF0gtx8dTGj88gbaKcEHIOY9Mpl8ON6QsR7NSASDI9rVW0tQEAAo8fQAxRiU7iPiXcuttUHT3QjqcflnouxFhAJFCZxZ1Ns8ZzhkW1zw8alL%2Ff%2F5j6oHcPm1poRRQMnUbXKhi9SX7aQ4a5vvm%2FqBMRSKuiG%2BsaLWmA0UJFtjwxhx8Dtvl4iJsSd%2Ft2qo1Lar1rDb9VLXeOm1nHjOotouaqoOCwAf6yNwrFOI7GpfmUZEOLMK3vAL5SleyCoCfdRuAqAgC90%2FRG4EmkQrIleH3ykRa%2FEiTT8%2FJOZud2uG3RxjfL3lz3a9Mxqy%2BDcZASU7Paq%2BXRwMpIvuqJyfRoK%2F7XXBlrZkmYWo2eToF6QeaAAQTg7fp0qNxh%2FWB2u11ouSZO9qfjZSHA6GzRifGby2NxLkwvODH1AY6pgEVNygVzg0bEa6XmZ5WiIVVdabBbNVF0cpP9ExBPVs9DFSHQHLeA3IvuX3X6mWu7HoGwnDyZ26pBDBNv23FIWgzCg2i4cW492FQY0Wj93Dnv%2FWuTa%2B50s1K%2FOUkTSdlGScSVgKKZTUAt2RaTJTlzliT%2BYFwQNx1Gl4sTE4HWpM5uD2AT8gKElTb6nhWiylh65xDFw8prQJJN1e%2F0HVoYm0L31O%2FKoFU&X-Amz-Signature=f9265e25d416027a320fc3d85f4e0f5dcf2f5adaadd63250f3d887994d148566&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BA4NGIY%2F20260828%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260828T213925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAgMZ6RlTRKZjUm9eiGLi0WC1Qzld94NlDs2Urjtrd7WAiB1BaN0RvOQ9Ar9rmsvh92XHvXWWmKv8vokvywmIyWcyCr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMNyyL%2FnUmjNExGwJ2KtwDJzBfK3fJPaxaOpYuIF7S%2BuCdjOSdv%2BsrllvfmP1fmkPVlg1qnBiwCLRcNG5bNDWXgrqYjC4P9faKL3A%2FB4%2BlUxwQTduLtcm%2F59xdPEL3siVYFkpNlrP2FpDLkNDHGnzyjGLLNHB%2FGAAidAsoDOcgxoPpfaZPypi8amgU%2FxTHoBFmKtT1C%2FUMGcIG7F5zCtwUTZ0%2FzBLV%2Bw%2B0v0qQ9im%2FRQOSZ%2B%2BAyEeYZpHdF0gtx8dTGj88gbaKcEHIOY9Mpl8ON6QsR7NSASDI9rVW0tQEAAo8fQAxRiU7iPiXcuttUHT3QjqcflnouxFhAJFCZxZ1Ns8ZzhkW1zw8alL%2Ff%2F5j6oHcPm1poRRQMnUbXKhi9SX7aQ4a5vvm%2FqBMRSKuiG%2BsaLWmA0UJFtjwxhx8Dtvl4iJsSd%2Ft2qo1Lar1rDb9VLXeOm1nHjOotouaqoOCwAf6yNwrFOI7GpfmUZEOLMK3vAL5SleyCoCfdRuAqAgC90%2FRG4EmkQrIleH3ykRa%2FEiTT8%2FJOZud2uG3RxjfL3lz3a9Mxqy%2BDcZASU7Paq%2BXRwMpIvuqJyfRoK%2F7XXBlrZkmYWo2eToF6QeaAAQTg7fp0qNxh%2FWB2u11ouSZO9qfjZSHA6GzRifGby2NxLkwvODH1AY6pgEVNygVzg0bEa6XmZ5WiIVVdabBbNVF0cpP9ExBPVs9DFSHQHLeA3IvuX3X6mWu7HoGwnDyZ26pBDBNv23FIWgzCg2i4cW492FQY0Wj93Dnv%2FWuTa%2B50s1K%2FOUkTSdlGScSVgKKZTUAt2RaTJTlzliT%2BYFwQNx1Gl4sTE4HWpM5uD2AT8gKElTb6nhWiylh65xDFw8prQJJN1e%2F0HVoYm0L31O%2FKoFU&X-Amz-Signature=150e8165108483fe7546498450c0c87180ddc292161c223a6c45a487453dc746&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







