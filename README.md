



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HRFJAZ7%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T182455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICEctktpszPfzVDMwy5YYSojwE8VZW%2FB55oQpWHJN%2FMaAiAj3yUTvqo%2F5UMD3HgM%2FbAysUubt2iQo740up56n3ZD2Cr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIM%2FA54MZEdJ8E%2BS7ZuKtwD2ARgrtTtxKHl%2B%2Fzce%2B%2BQtxzFxj2lfCx7layBGHxK369ZLGicwdA%2FVqXZk5Lw39c26S1d47r0i%2BEo4MNxVs639IanM8eyl6Fnlq%2Fqv1EqjzmQduxSaQyvHI6xU65nI0v2HKEhyA00oXNmkdHA3GDgOi%2FxmaROdoRbPpgHNWISHYKI%2FCSPwYw%2FPCE%2BGOmwsBy3ObW%2BazxsyNfLxnNkkglBAeb7nVT40pDXXqUQg22YVZ10ClfrO78eGvZicr%2BezJtWfFOwtjR8Za5cSI5X5%2FLFPIrAuwAnPyoCTV6geeRHom7f%2FCvZ87d9ASv%2BwPHTHJhv%2FivL6hQryLs%2FGlrmSI0h3XmpMRl93qY4TUx19kUhogvQqzEDCKWhouCjKKv%2FZcjuWBicM5%2FrWzNEoTSUdbIXHu5gaFFcFE5OEPIKjJwOyxHebYTwvNiwOoANnYvpRlBGVp4igPCT%2FrFWxNbPK5MklNt%2BAzNokmtv808RyekegykF3ZfCPSx7UnlhZJU%2BHs3JgMlVUd0XbLBHzJ8tpEQcAL6E%2FYwmsxEsxolV9%2BnVhPJ1jzbor3h9iOJmRRa1OLp6IKqXRTsbWZmU%2BIAJUUjTSKIGBt7czhqLR1k3wP2IJroMIfgMv7NsZLBZ9ZkwnaP1ygY6pgHi12haLg04BN0TdD6f3uLpKSGBHWvQHbB9%2BtdJ%2FnTXVWxwC2OKXsg7%2Bxb3KZ24rlf7pdDK0DA4rAC0mfoVJGbFtjguFuLakbTbSUur8UgBx6TrWo8KNqs1eGosfYfoUlX8ys%2BxKUr7KrqvcQjh3OOfcfV61sbRjY64m3L0HPx5H2WSwLZ7vqSu%2Fzyj5%2BMPX1A5pSsCkMEAl8SHTvm3mKpvPg%2BFAscF&X-Amz-Signature=b76c99a37ce2eee95695aff0607f60a4371820c86e8aa020ad4293ceb9a841fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HRFJAZ7%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T182455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICEctktpszPfzVDMwy5YYSojwE8VZW%2FB55oQpWHJN%2FMaAiAj3yUTvqo%2F5UMD3HgM%2FbAysUubt2iQo740up56n3ZD2Cr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIM%2FA54MZEdJ8E%2BS7ZuKtwD2ARgrtTtxKHl%2B%2Fzce%2B%2BQtxzFxj2lfCx7layBGHxK369ZLGicwdA%2FVqXZk5Lw39c26S1d47r0i%2BEo4MNxVs639IanM8eyl6Fnlq%2Fqv1EqjzmQduxSaQyvHI6xU65nI0v2HKEhyA00oXNmkdHA3GDgOi%2FxmaROdoRbPpgHNWISHYKI%2FCSPwYw%2FPCE%2BGOmwsBy3ObW%2BazxsyNfLxnNkkglBAeb7nVT40pDXXqUQg22YVZ10ClfrO78eGvZicr%2BezJtWfFOwtjR8Za5cSI5X5%2FLFPIrAuwAnPyoCTV6geeRHom7f%2FCvZ87d9ASv%2BwPHTHJhv%2FivL6hQryLs%2FGlrmSI0h3XmpMRl93qY4TUx19kUhogvQqzEDCKWhouCjKKv%2FZcjuWBicM5%2FrWzNEoTSUdbIXHu5gaFFcFE5OEPIKjJwOyxHebYTwvNiwOoANnYvpRlBGVp4igPCT%2FrFWxNbPK5MklNt%2BAzNokmtv808RyekegykF3ZfCPSx7UnlhZJU%2BHs3JgMlVUd0XbLBHzJ8tpEQcAL6E%2FYwmsxEsxolV9%2BnVhPJ1jzbor3h9iOJmRRa1OLp6IKqXRTsbWZmU%2BIAJUUjTSKIGBt7czhqLR1k3wP2IJroMIfgMv7NsZLBZ9ZkwnaP1ygY6pgHi12haLg04BN0TdD6f3uLpKSGBHWvQHbB9%2BtdJ%2FnTXVWxwC2OKXsg7%2Bxb3KZ24rlf7pdDK0DA4rAC0mfoVJGbFtjguFuLakbTbSUur8UgBx6TrWo8KNqs1eGosfYfoUlX8ys%2BxKUr7KrqvcQjh3OOfcfV61sbRjY64m3L0HPx5H2WSwLZ7vqSu%2Fzyj5%2BMPX1A5pSsCkMEAl8SHTvm3mKpvPg%2BFAscF&X-Amz-Signature=4f84b4b5976c58d4e75cd214a99c8d1409ddc87309996731b09b81e0b8c994f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







