



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRO6JXQK%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T131623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxUkLfc%2FDNLuET6igOVoADbRnU2icHdT2JJA4sVLvumAiBsJGdGU0vhnh7Rzl9F9%2BiiKHxCbCVEoDGkv1m6gm04rCr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIM9jAKm05L1wdoCuXfKtwDhfKM8SHhkkziOZMnb6GCqtNT0V%2Bav11PYC8CMCp%2FFb8F3ByaeR33bY1MDyZmwn0hkCU4h1AgrGMJuLw4o3XZ47Ko5jqQyznHFjzXGgVMmeEO020dtjCMSu8n9FTb1qBtckNsZcg1r2QtbFw%2Bfk6YceE6omg3NOIEHS%2BqXkAVCaH0T9laZNjM%2B1vu5KTRa2k%2Bem%2FVNflso%2BD2xjFw56J5%2FKG%2FbbaS4aWlA3FBLlL9sUkC2kV6ekphdDChaoxg03xhKbdJj23ML9p77wv44oPtw4JL7pfsoS2ihWHZp9l95H2yk0yG7OHzhKfBdcPDpEGYva8Lf4XvSQIiK5mk2SPDEX%2BI8VuBnNJ7dLyKJhuIbEJMBzl%2BU0gGXWcONADhN1RxrUqkd649OGNYIPOncyIab5nFC1hS2%2BrKUmc%2BCZQ2oQ1wtrYBaklqzuPmciLk%2FPTkgYWk05N%2B0p%2BGX%2ByMYzYhRugi1ryz4tzPmRO4U3xEi%2FHMnwco%2B7822wajse2yz7CjMzKX%2B%2F5XjyMSQ0S9eJVCq6IpuEAXnPLVZ6jvAhzFBqeUFd1o3vTN3BVmanxHBNhESHdNXz40trYmv7AMjYU%2BmzPfVAPlHC30pSLsDTcwoG6eAxYYv7R93L3Xinsw4ojo0gY6pgFtg2mIP0IPSHg%2FX%2F2K%2F9Gtvu7B3vFZub72yIvP%2FRj7W9hv57hC8397BHIZ9Ae5kZ%2B7PLG%2FSc%2FcAhsC%2F2jhLAY2sOELF6EQEz62jaB5ghuTaNUzmZhONlhIJdwLpsBBla9xEDK13njB%2BRKfkzWfTT3K8ZTj1K9qvWjuTFYm8QDtNtw90P4pFfoclAPNP6MPz2s8YrXyuEV%2FWCsc3E7qTYCw4w0iunqc&X-Amz-Signature=74f1204b7a4a92cba9df6114cbbcd0bd8c84e8498a130f6d3c2ad1caf7c266b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRO6JXQK%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T131624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxUkLfc%2FDNLuET6igOVoADbRnU2icHdT2JJA4sVLvumAiBsJGdGU0vhnh7Rzl9F9%2BiiKHxCbCVEoDGkv1m6gm04rCr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIM9jAKm05L1wdoCuXfKtwDhfKM8SHhkkziOZMnb6GCqtNT0V%2Bav11PYC8CMCp%2FFb8F3ByaeR33bY1MDyZmwn0hkCU4h1AgrGMJuLw4o3XZ47Ko5jqQyznHFjzXGgVMmeEO020dtjCMSu8n9FTb1qBtckNsZcg1r2QtbFw%2Bfk6YceE6omg3NOIEHS%2BqXkAVCaH0T9laZNjM%2B1vu5KTRa2k%2Bem%2FVNflso%2BD2xjFw56J5%2FKG%2FbbaS4aWlA3FBLlL9sUkC2kV6ekphdDChaoxg03xhKbdJj23ML9p77wv44oPtw4JL7pfsoS2ihWHZp9l95H2yk0yG7OHzhKfBdcPDpEGYva8Lf4XvSQIiK5mk2SPDEX%2BI8VuBnNJ7dLyKJhuIbEJMBzl%2BU0gGXWcONADhN1RxrUqkd649OGNYIPOncyIab5nFC1hS2%2BrKUmc%2BCZQ2oQ1wtrYBaklqzuPmciLk%2FPTkgYWk05N%2B0p%2BGX%2ByMYzYhRugi1ryz4tzPmRO4U3xEi%2FHMnwco%2B7822wajse2yz7CjMzKX%2B%2F5XjyMSQ0S9eJVCq6IpuEAXnPLVZ6jvAhzFBqeUFd1o3vTN3BVmanxHBNhESHdNXz40trYmv7AMjYU%2BmzPfVAPlHC30pSLsDTcwoG6eAxYYv7R93L3Xinsw4ojo0gY6pgFtg2mIP0IPSHg%2FX%2F2K%2F9Gtvu7B3vFZub72yIvP%2FRj7W9hv57hC8397BHIZ9Ae5kZ%2B7PLG%2FSc%2FcAhsC%2F2jhLAY2sOELF6EQEz62jaB5ghuTaNUzmZhONlhIJdwLpsBBla9xEDK13njB%2BRKfkzWfTT3K8ZTj1K9qvWjuTFYm8QDtNtw90P4pFfoclAPNP6MPz2s8YrXyuEV%2FWCsc3E7qTYCw4w0iunqc&X-Amz-Signature=ff90acc3bd41134048c06b769d1592352ad6a61e674bca309c953f40e86655ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







