



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK4Q35KG%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T012246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQIjfO6gN3%2BB1hE3Iq8lxo8%2BgEFhLFgLkwrgON5QbJ2QIhAJ97GvvcAlvzWYqUiMN%2BRU5Lxol5RFh3M3TlRd4MQEruKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2Fn9xo20xvmWqKc7Yq3AM6KcJ7Zfqi5p5jxNGoaY%2FGjzYlyuWHFnlSMl4%2BAB9JNdPL%2BNrI2H95orYot7aq3zAIiAw8hVgi%2BBmkCkYfID77b4zoTblHDsUnYJgQowW1c33Un4brmTfMbSWO6fztbNfHUNVgr%2B05uVLqtmvHJmLQcOVVgnM0LAo5JKlijuAdlr3jmgXbx8V9%2Bt0wjQttABKHwztDY3whC%2FoIZQ60MANoaDWP6aDiz71DyH1OFASLGCqdgTc6BZlelqPXNisdjj%2BrD5R0h%2BmP4G%2Bh76tBHTfND49Lq3FGd0eFRiFVSEi1GMcFIqHAZPIjrHCc%2F92jmhzLfivwxSplXgGtYtnzVa4ITR0NiMfbg5wD8N%2FIotFVGu2h%2B6uyllKGNaOJV2p0BaNREAXl4PVj6AbuZHTcboeumxakmKjonRepWq2Ks83IMRnYu5LSVSwvHy1h9rmbleXYgdaw1NfKm9DLnsIJhfSZE5zD3%2BeJc40NuyKcubwFavkehod28ZmAtUEli94Gh5szFhtgHBfNXIRhT4T4WIk3Oid9sUTXF6e%2Fmlf5HyPsSDPxeuweEsfWCxb9p0ILfdt%2BVOSfzDeLD%2BPtiRO07zQxlb%2BX7X1QQaXY%2FMJKVY9l3SWH4hGki%2Befxss0VTDGocfKBjqkAagJYcl2v1qOeBT5rOPWPKo20fQJ5JcdDK7bRED0fbpXmgAEzJQo2Ihl8xLeGCrVFJ7ej78QBNLCFaz%2B4EvjvSF50XJisaPMPgQGeMsg%2FlAa9nHE05PXpuwdMKHAgH17CLZp8P7smCiqf1CbX00kh2tRmT%2FR6BL5PupPmCNS06uitQ2Zkp5HpVA0fXIuJnd%2BzWJm2XuIrHwu1eCNWARSmbHu6CFm&X-Amz-Signature=0082e6d498c4c1e1b5e6161b0933a1782fb8417e66ba33c121dc58a57a5ac849&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK4Q35KG%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T012247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQIjfO6gN3%2BB1hE3Iq8lxo8%2BgEFhLFgLkwrgON5QbJ2QIhAJ97GvvcAlvzWYqUiMN%2BRU5Lxol5RFh3M3TlRd4MQEruKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2Fn9xo20xvmWqKc7Yq3AM6KcJ7Zfqi5p5jxNGoaY%2FGjzYlyuWHFnlSMl4%2BAB9JNdPL%2BNrI2H95orYot7aq3zAIiAw8hVgi%2BBmkCkYfID77b4zoTblHDsUnYJgQowW1c33Un4brmTfMbSWO6fztbNfHUNVgr%2B05uVLqtmvHJmLQcOVVgnM0LAo5JKlijuAdlr3jmgXbx8V9%2Bt0wjQttABKHwztDY3whC%2FoIZQ60MANoaDWP6aDiz71DyH1OFASLGCqdgTc6BZlelqPXNisdjj%2BrD5R0h%2BmP4G%2Bh76tBHTfND49Lq3FGd0eFRiFVSEi1GMcFIqHAZPIjrHCc%2F92jmhzLfivwxSplXgGtYtnzVa4ITR0NiMfbg5wD8N%2FIotFVGu2h%2B6uyllKGNaOJV2p0BaNREAXl4PVj6AbuZHTcboeumxakmKjonRepWq2Ks83IMRnYu5LSVSwvHy1h9rmbleXYgdaw1NfKm9DLnsIJhfSZE5zD3%2BeJc40NuyKcubwFavkehod28ZmAtUEli94Gh5szFhtgHBfNXIRhT4T4WIk3Oid9sUTXF6e%2Fmlf5HyPsSDPxeuweEsfWCxb9p0ILfdt%2BVOSfzDeLD%2BPtiRO07zQxlb%2BX7X1QQaXY%2FMJKVY9l3SWH4hGki%2Befxss0VTDGocfKBjqkAagJYcl2v1qOeBT5rOPWPKo20fQJ5JcdDK7bRED0fbpXmgAEzJQo2Ihl8xLeGCrVFJ7ej78QBNLCFaz%2B4EvjvSF50XJisaPMPgQGeMsg%2FlAa9nHE05PXpuwdMKHAgH17CLZp8P7smCiqf1CbX00kh2tRmT%2FR6BL5PupPmCNS06uitQ2Zkp5HpVA0fXIuJnd%2BzWJm2XuIrHwu1eCNWARSmbHu6CFm&X-Amz-Signature=71ddacd3891af3a967fc035d899d502e2fff68b4ca8ea280e9b883d49463389f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







