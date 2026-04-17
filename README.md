



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMQDO2PF%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T185327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIDlWwLlLTX0ZwKDr5AP6GImQEFbNPMqzlT5fG6vGQemyAiBjruuxSbY2bgb686o0r3yjQStNUr10%2F9qP0VXUk28TCiqIBAjc%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVozPWdn58svlsMpnKtwDYgI5xlkS9muZ3AMUrrJWeg7bZf2EVpXzYQVkQfW85FdUoTNmn%2FL2HPwuzNJPwzLCYPA58sgFRVZbxpd%2FQNWx2d7grRQE%2FnqxPVtN6Y7xNABy6lXGUjvPi6AXZrgdtTcm8ohv9zv%2Fc4oEXG0oLPv6c4o%2FJaTKgxDSANorTJLP702fT0UQFfnBLqCO1wf%2Fdas5yXBZI8hAbT9pGcGGzXlBF%2FsJkWKhQmK%2BpDGYmT1LEYw0%2BYBktBjdw15xbx7JGzYvPzRg%2B7xY5koh7Eh0aJpYo4BoRNOuK%2FuK8cs21Hd%2BDdYU6IIykxoVHMCFc8qjNYcscqGldE%2B%2FMbAtQ6H75EMVNOu17SiHZ8Fg8ervsEwIDb83JMIoH6JgqFlE71xUSLWp25XYKL44EaveLcUSdXm97TwGrMRLMJkZSKDuwtHW0%2Fr3mz8q%2BjMf8YMyYXYxhF4s1h99QIdK5rVBd53SrlGCs%2Fc0AXmfzkNGzc5%2FAa5tvrSlu2mLN%2B0pnDhrC8dNLzeVYVKDRLldlvSGrc2G%2BkTIuTrMsRk3xIDmNxCxElkdZTGucNOi7XkOSTCjqDVEHL8lYKgAoaYHxxJi6u0yrvEm1CJilnK246QI3usDGwuK%2FY64ATLml4XNFao90LAwsvmJzwY6pgFyk3zkh0UeFecpvETy9d9K7de1oC3%2BnbmavibKpZKVLsg6PcQC6cIV4%2B3qnkcSEN%2FvlGCbItWEuLVZxdQCQCz7XHayNzV2XhoqXmWFQ2bpRVnxgiMoZRGysQ%2Fn6g6rGG0hGmrcgK3qO6ypMKaBMbOWMGHuYasxrCyYXq3s7%2BnoqjnNLcduwrDw7CZbuGYN9fPJU0YhG2rYtrKmMhduh5bxJBFnVnPH&X-Amz-Signature=8132534a5665ac28910b6f10e4a80dd29ee196beafe7fc0a86308d79aae6930f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMQDO2PF%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T185327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIDlWwLlLTX0ZwKDr5AP6GImQEFbNPMqzlT5fG6vGQemyAiBjruuxSbY2bgb686o0r3yjQStNUr10%2F9qP0VXUk28TCiqIBAjc%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVozPWdn58svlsMpnKtwDYgI5xlkS9muZ3AMUrrJWeg7bZf2EVpXzYQVkQfW85FdUoTNmn%2FL2HPwuzNJPwzLCYPA58sgFRVZbxpd%2FQNWx2d7grRQE%2FnqxPVtN6Y7xNABy6lXGUjvPi6AXZrgdtTcm8ohv9zv%2Fc4oEXG0oLPv6c4o%2FJaTKgxDSANorTJLP702fT0UQFfnBLqCO1wf%2Fdas5yXBZI8hAbT9pGcGGzXlBF%2FsJkWKhQmK%2BpDGYmT1LEYw0%2BYBktBjdw15xbx7JGzYvPzRg%2B7xY5koh7Eh0aJpYo4BoRNOuK%2FuK8cs21Hd%2BDdYU6IIykxoVHMCFc8qjNYcscqGldE%2B%2FMbAtQ6H75EMVNOu17SiHZ8Fg8ervsEwIDb83JMIoH6JgqFlE71xUSLWp25XYKL44EaveLcUSdXm97TwGrMRLMJkZSKDuwtHW0%2Fr3mz8q%2BjMf8YMyYXYxhF4s1h99QIdK5rVBd53SrlGCs%2Fc0AXmfzkNGzc5%2FAa5tvrSlu2mLN%2B0pnDhrC8dNLzeVYVKDRLldlvSGrc2G%2BkTIuTrMsRk3xIDmNxCxElkdZTGucNOi7XkOSTCjqDVEHL8lYKgAoaYHxxJi6u0yrvEm1CJilnK246QI3usDGwuK%2FY64ATLml4XNFao90LAwsvmJzwY6pgFyk3zkh0UeFecpvETy9d9K7de1oC3%2BnbmavibKpZKVLsg6PcQC6cIV4%2B3qnkcSEN%2FvlGCbItWEuLVZxdQCQCz7XHayNzV2XhoqXmWFQ2bpRVnxgiMoZRGysQ%2Fn6g6rGG0hGmrcgK3qO6ypMKaBMbOWMGHuYasxrCyYXq3s7%2BnoqjnNLcduwrDw7CZbuGYN9fPJU0YhG2rYtrKmMhduh5bxJBFnVnPH&X-Amz-Signature=ecfd214c42aab0fd5dde3e4e9ba71aa41f21c1e7a9552bae6d9de19ee36c739e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







