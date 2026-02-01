



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPWXE3IZ%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T182759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQC3frBowwe%2BfaSFXNnqAEoWxcDQjL4CoH0ZGF%2BVSi2%2FNAIhAN2jj0p9ma%2FKL4nrGjMSTneYzC64da8%2FQgj5b%2BcqWl7pKogECNL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxiJ5ZKUEmjjvoqj8Eq3AMy38yIBBLQ%2BPnvEkNPluGREdYBozr3Fqr3I6%2BxIoDNIn9uq5DDioBYqM4N2C4mOWuiEGzPClDntE7glHuu5ZaW4xS%2F20jawf6wVheZPpVjm5WjmmTi%2B4faKvjFksUNwJhMK5%2FJcO7eoGY%2FfFvhGQEtOsD2FUBtxCt2rlv8jdeKgeIT7HJRUl5rZBotCsxKd5145uuAF8H10awCC4Bjdg%2BnZ%2BcNbHbHuDLPgbq5uXBFbpRLY%2B16JIZGJySaoa3fONFaypQ8owwveAGP%2FSCUFre7LKCt3o1kVJ5XJTT3TSuRiRDcK7vfvMetO%2BEgsW7c2xB2ykRY8TtclejbOXmDrCrkrzUGdKu6linprjhclGRxVKMtjVOzt%2FB1KYvXN2VJ9pNYR9rLlW39tTq6zt9%2BNU0tpF3YhZf9PTbU83guwRP9POGLDF%2Fw1CGIyERor1GdbpgBTu3IeEsyOj3PRBka0k7w8IDHekETRKVwNvQcrSYHm73Am0kmWSktSy8n9XSQI0L29ZpSgSvaI4iFSO5ZnqJwVQhC%2BVUBsD7LUiIvEvAUTQn6j7OiFtgZzCyJ5CPZoDrtizYoYTxjXjbz%2BT1lfSrRb6azElYO0h6b8pdr6D8TxAXV7%2BL1oawWoV8gmjDyhv7LBjqkAR%2Bi07XOyIlRiGivxUa0a7nWv1HmdPIP8pjkgX0%2B%2Fh6boAEwdF11FeqFncpmJLTCWjfnG%2F0o3Afr1rgunySRjqvXtvgfbm6Ltt%2BHgnOAiJI6pY2Il%2BeO8s6nVMIFzpDdttZ9Roa2mWHBT%2BZ0JSYGOqWndVy6vu%2FcMn1dnQA90Pim69IY1d7F8NuSw%2BQoV%2FMVsaM%2FnpV9AS2pKqIl8xtVP0DS8cw1&X-Amz-Signature=be9ae8adc16757b0d13f28138edcc5a39b4305b3e9a864c8fd4050cb98247678&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPWXE3IZ%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T182759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQC3frBowwe%2BfaSFXNnqAEoWxcDQjL4CoH0ZGF%2BVSi2%2FNAIhAN2jj0p9ma%2FKL4nrGjMSTneYzC64da8%2FQgj5b%2BcqWl7pKogECNL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxiJ5ZKUEmjjvoqj8Eq3AMy38yIBBLQ%2BPnvEkNPluGREdYBozr3Fqr3I6%2BxIoDNIn9uq5DDioBYqM4N2C4mOWuiEGzPClDntE7glHuu5ZaW4xS%2F20jawf6wVheZPpVjm5WjmmTi%2B4faKvjFksUNwJhMK5%2FJcO7eoGY%2FfFvhGQEtOsD2FUBtxCt2rlv8jdeKgeIT7HJRUl5rZBotCsxKd5145uuAF8H10awCC4Bjdg%2BnZ%2BcNbHbHuDLPgbq5uXBFbpRLY%2B16JIZGJySaoa3fONFaypQ8owwveAGP%2FSCUFre7LKCt3o1kVJ5XJTT3TSuRiRDcK7vfvMetO%2BEgsW7c2xB2ykRY8TtclejbOXmDrCrkrzUGdKu6linprjhclGRxVKMtjVOzt%2FB1KYvXN2VJ9pNYR9rLlW39tTq6zt9%2BNU0tpF3YhZf9PTbU83guwRP9POGLDF%2Fw1CGIyERor1GdbpgBTu3IeEsyOj3PRBka0k7w8IDHekETRKVwNvQcrSYHm73Am0kmWSktSy8n9XSQI0L29ZpSgSvaI4iFSO5ZnqJwVQhC%2BVUBsD7LUiIvEvAUTQn6j7OiFtgZzCyJ5CPZoDrtizYoYTxjXjbz%2BT1lfSrRb6azElYO0h6b8pdr6D8TxAXV7%2BL1oawWoV8gmjDyhv7LBjqkAR%2Bi07XOyIlRiGivxUa0a7nWv1HmdPIP8pjkgX0%2B%2Fh6boAEwdF11FeqFncpmJLTCWjfnG%2F0o3Afr1rgunySRjqvXtvgfbm6Ltt%2BHgnOAiJI6pY2Il%2BeO8s6nVMIFzpDdttZ9Roa2mWHBT%2BZ0JSYGOqWndVy6vu%2FcMn1dnQA90Pim69IY1d7F8NuSw%2BQoV%2FMVsaM%2FnpV9AS2pKqIl8xtVP0DS8cw1&X-Amz-Signature=c8360d78517e03176292090062cc4c9b3c68c86a94590ad6979c7de471a1d445&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







