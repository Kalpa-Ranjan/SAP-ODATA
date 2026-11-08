



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677KWZXRB%2F20261108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261108T120604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQClYPP3MOuM%2BDBcf4snpCaPFUXk14Wk7%2Fm7xaO7PDYFQwIhAKaYit1ntneC73uGk2Ae9jEorxel9jy7m2WqjEmpmz0fKv8DCAsQABoMNjM3NDIzMTgzODA1IgzroK5FP296LUdIdZ8q3ANlXIbLw9n3yji2x2QUk5KJEBFSSCI8hnGGdSGYQY7w8BtrCYH0x6Agjxi4bqIsOlem4pesSve1RLCao9nS2utAxFUyifBT7fnyh7Do59yqWyBCH6JWEPwjv57Lf1QQlG1ZklmBbirKhIs90baQxmAf2MOlYwF51aP7yP6yKbpl6LR1Cs%2FckkiqGrvntdZKL6YCzYpq%2BOZD4GW8rsjWoIqBn6TSOSnBAox6IcTG8Ztnics6aRk%2BFRYXTMnWtXlYtk7Jq56K7nEw1tx7AJFs7pFc7uf71A4q6jH4dNZqqzVFINSVqvBGpJlpxWOlhGrfmAWPWfWmvuRNAu3yPHm3RywDYqXrGiyL8f3MyHShbJ%2B%2FmN6g%2BsOT2VorNLfMwWk3Oqs4Fb2EaW1IKcjHoPlcpL6NQKXRx9gKrZBGRQWD5v%2BOys%2FDqTe0Puu7gErwgMIRmBgYd4qkzJE5wxwx5HkAPneIFVaY9g%2FbF9wI%2Bl7hQemSrAZHW6bxICWG3Tx6D2f23xpk79ha9Ny7RNmVdhBG8D4YnI4h91kVz07DxFAkewQPQGGQjCQzVNx7hGlX2kxY7zh%2FX05n9977VJ7yBNAHgHPkbx1SbJ2W3cNRZG%2FtOqrkR8rDT%2B534FjE5VsJ0DCAocHXBjqkAcj6D6bz7vwc4HOsWQFEC9z01gqCjCMAKELVZytjxQShi4XaoHQb4e2ovkERoffUlRpR%2B%2FrHjYTI43LQSqsGZEv4EBzlspOlKiIxh67IQdKw%2FTdo1iWP%2B0e3pdZX5VTNIHCvihlHd49X2AnIPqSBLz%2B6TNqYaJpjhN%2BbfFz846ttVp4npHYEB9GY2e82GSG9vdgolG4CH4ynFKYBRzmXSKh23Wgr&X-Amz-Signature=b26a5e750f60dd061d1cde1142669641fa273ffe0042ff21d4f91f7f6118e941&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677KWZXRB%2F20261108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261108T120604Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQClYPP3MOuM%2BDBcf4snpCaPFUXk14Wk7%2Fm7xaO7PDYFQwIhAKaYit1ntneC73uGk2Ae9jEorxel9jy7m2WqjEmpmz0fKv8DCAsQABoMNjM3NDIzMTgzODA1IgzroK5FP296LUdIdZ8q3ANlXIbLw9n3yji2x2QUk5KJEBFSSCI8hnGGdSGYQY7w8BtrCYH0x6Agjxi4bqIsOlem4pesSve1RLCao9nS2utAxFUyifBT7fnyh7Do59yqWyBCH6JWEPwjv57Lf1QQlG1ZklmBbirKhIs90baQxmAf2MOlYwF51aP7yP6yKbpl6LR1Cs%2FckkiqGrvntdZKL6YCzYpq%2BOZD4GW8rsjWoIqBn6TSOSnBAox6IcTG8Ztnics6aRk%2BFRYXTMnWtXlYtk7Jq56K7nEw1tx7AJFs7pFc7uf71A4q6jH4dNZqqzVFINSVqvBGpJlpxWOlhGrfmAWPWfWmvuRNAu3yPHm3RywDYqXrGiyL8f3MyHShbJ%2B%2FmN6g%2BsOT2VorNLfMwWk3Oqs4Fb2EaW1IKcjHoPlcpL6NQKXRx9gKrZBGRQWD5v%2BOys%2FDqTe0Puu7gErwgMIRmBgYd4qkzJE5wxwx5HkAPneIFVaY9g%2FbF9wI%2Bl7hQemSrAZHW6bxICWG3Tx6D2f23xpk79ha9Ny7RNmVdhBG8D4YnI4h91kVz07DxFAkewQPQGGQjCQzVNx7hGlX2kxY7zh%2FX05n9977VJ7yBNAHgHPkbx1SbJ2W3cNRZG%2FtOqrkR8rDT%2B534FjE5VsJ0DCAocHXBjqkAcj6D6bz7vwc4HOsWQFEC9z01gqCjCMAKELVZytjxQShi4XaoHQb4e2ovkERoffUlRpR%2B%2FrHjYTI43LQSqsGZEv4EBzlspOlKiIxh67IQdKw%2FTdo1iWP%2B0e3pdZX5VTNIHCvihlHd49X2AnIPqSBLz%2B6TNqYaJpjhN%2BbfFz846ttVp4npHYEB9GY2e82GSG9vdgolG4CH4ynFKYBRzmXSKh23Wgr&X-Amz-Signature=e28c2de03ca20708335290cb134eecfe122f4551857eb9f75abdd317cc266d5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







