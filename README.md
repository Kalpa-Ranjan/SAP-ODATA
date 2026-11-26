



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBAGNYLV%2F20261126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261126T180532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGj3CTgZFEbKTtJ2jCajAaCPgf4suUaGLwfDgUM%2FZm3oAiAyDZZ%2BOPR5c8ixAR6LVjpBuVamTdqyg%2FF8muPqhPr3ISqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVHybXt%2BiUs65qGmnKtwDa3TnWo0VMcVs9TCvYw%2B8BxnjLAS%2BtUHgS9QQ%2B0EepBUL9fIwPbae2cqO%2BCu06tsoUkpR9oo5uPSPd0qUP2t5uJTk6aeehsi%2FqlVQPwa%2BP1mPJ6dXiwnDdoSqkdKVdQyAz5DKEhY0zAG2rAp4dSiFTd5hGo%2Bmtx%2BNkL5dN6FLJFN4%2BKamUz8qonftB47W2GeaoAH3pXTvhTTfUYx%2B3AtrfkkMf%2Fti7Sbf2CaMDT%2BtHMLdL8iDfir%2Bd%2BRgdYVm1eeAKxBZ%2BoG2OFN8N7aZot2U5h3GVNwyOOFSThYNQk1fnCyRMuuJ9r2q16nGKg1iAIoT4oifmzPCrPxjBdS3mMG9CdaizEsgjQEtyGYR8tjBugB%2F2des9TJJ%2BHok24p8aXgWE7FNBSp5jPYlz6aJupcnwauW%2BeHeeaAaG57w8YvTQQ33VHrjskLitk%2B2PSuGtPv42vZG6YatBWwbcapgqa1%2FcKx9%2FMhl7q6dMNew8e9Ejdyy4IA2eP0opCPu%2F6lFEnEZpB77TcO9nU6Eoaq3umMP%2FvzCAMkNxM%2BYDBvKA58SDAFIKghz8iANHOFdL%2F2dsYOqDUyItM6zEALdXo%2FyiuwyHU1cLhbkLUyRQ1JNpPEUYwLxTNFS6WYcpPXL3Bcw9qyh2AY6pgG1Eu7NcSeylilhd%2BXc0HLCySwsvIROeTx%2FOZneukb9cbG0QyMgX6Q%2BEn6GCVIe77ykXkkxuWVVoWCVFG0BDI8i8cJpUgAhsrGPDl9vIchAUh4Lzu3cYjelrWHc%2BtaHboiXRMk%2BTIioEuyGtQcD830yqivE61nWHEi6TKrshrfCoUrzduoYRuELayV1dS1PCL975FOc3FdTvxH6WksrczYJCD44LIy8&X-Amz-Signature=dc15a4566bbcd676afd800d2dc8817426e690f7aa94417b334abf3a3bd825be7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBAGNYLV%2F20261126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261126T180532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGj3CTgZFEbKTtJ2jCajAaCPgf4suUaGLwfDgUM%2FZm3oAiAyDZZ%2BOPR5c8ixAR6LVjpBuVamTdqyg%2FF8muPqhPr3ISqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVHybXt%2BiUs65qGmnKtwDa3TnWo0VMcVs9TCvYw%2B8BxnjLAS%2BtUHgS9QQ%2B0EepBUL9fIwPbae2cqO%2BCu06tsoUkpR9oo5uPSPd0qUP2t5uJTk6aeehsi%2FqlVQPwa%2BP1mPJ6dXiwnDdoSqkdKVdQyAz5DKEhY0zAG2rAp4dSiFTd5hGo%2Bmtx%2BNkL5dN6FLJFN4%2BKamUz8qonftB47W2GeaoAH3pXTvhTTfUYx%2B3AtrfkkMf%2Fti7Sbf2CaMDT%2BtHMLdL8iDfir%2Bd%2BRgdYVm1eeAKxBZ%2BoG2OFN8N7aZot2U5h3GVNwyOOFSThYNQk1fnCyRMuuJ9r2q16nGKg1iAIoT4oifmzPCrPxjBdS3mMG9CdaizEsgjQEtyGYR8tjBugB%2F2des9TJJ%2BHok24p8aXgWE7FNBSp5jPYlz6aJupcnwauW%2BeHeeaAaG57w8YvTQQ33VHrjskLitk%2B2PSuGtPv42vZG6YatBWwbcapgqa1%2FcKx9%2FMhl7q6dMNew8e9Ejdyy4IA2eP0opCPu%2F6lFEnEZpB77TcO9nU6Eoaq3umMP%2FvzCAMkNxM%2BYDBvKA58SDAFIKghz8iANHOFdL%2F2dsYOqDUyItM6zEALdXo%2FyiuwyHU1cLhbkLUyRQ1JNpPEUYwLxTNFS6WYcpPXL3Bcw9qyh2AY6pgG1Eu7NcSeylilhd%2BXc0HLCySwsvIROeTx%2FOZneukb9cbG0QyMgX6Q%2BEn6GCVIe77ykXkkxuWVVoWCVFG0BDI8i8cJpUgAhsrGPDl9vIchAUh4Lzu3cYjelrWHc%2BtaHboiXRMk%2BTIioEuyGtQcD830yqivE61nWHEi6TKrshrfCoUrzduoYRuELayV1dS1PCL975FOc3FdTvxH6WksrczYJCD44LIy8&X-Amz-Signature=449e6c137792d067f4d7bd10820981050c6a69b5967e789ec67f232d7cbf33b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







