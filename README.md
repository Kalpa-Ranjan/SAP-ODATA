



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XOH6Z7C%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T062334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8hTU0CxOArSnZXLqRShe6mlAO7BVLJNQX9AC%2F1vbtDwIgFlCxdD37fuB9iQGZM0a%2F5dKhqIZSvBIBYSlWLFOHehoqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF70koFrCvM%2FDrhzDCrcA3fTh2pilZpJzha4w4z3eQbnjkUZUpqMFHBJdRbIkj96VzQrY4nK3HzonCDIReWMFCy4AFjgAAKBPK3WkqJI0V0XNREwLDN15unkB8auOFkt5xcVdS7qjehTy1zMoJ014ki8AgfdJps48F9n5iJ1JPJ%2F%2BB0Gu6JZkRqBU8ztul7TY40erDOudRsFFhA0w78JiG0qlIFlm2okGojSSEKCWh8YJ1w0v15FkJfD7bWNLDBD7WgW3fvU%2FRpMFnzze3WT9w0hZlEOMic%2BTK1vRtoTLW5oyePCL1D8RH2ZAR4Fi14sbkQ7pgD2VGjxHMuBZGWt%2BMbfNXYyOOPFixW5Mu8IE%2BAGsJ4%2BloGk5uz6BB56IQFiGoJ4lr%2BZdu%2F0ND8sYJA7rt48tdl%2B7DLRmj3YCTae6PKWiU%2BqjZQLRHxCowOF8p%2B2XYjw5BxqHskbhvgZ4YrBSUurxKZMqpHyV%2B9mSzVqrOKjrw2MpeXhOtq731HWAWuWz52%2BZgRPxOmbQ1NzZ6r0StSIMHJBHJqBxk%2F%2FFomAcd8njOLIFoG2wgiVr9DbfETq%2BZNMHo8BNBcknIfWD5F0z7Vp%2F5Qh8K%2BHypAMX9UPSw2PGHkfqFy14wpMaIwV4c53SDo9%2BEsuEp%2FOqEw%2BMKaa8MgGOqUBmgOdn0oEe9KlP8jWA9vJz%2BWLgG%2B8o3kmQd5k2q1qIrbTeoHG09b2CzJHxbbus17bUYkDG%2FU0ov%2FW3C6meq0y1eWKtdA3BqPosl%2Bj1O6hQg9yL2yeVBB25RWqc2hMaGZXXKvi9RgXe1OKLin9%2Bkg1%2BxmL1Q2V1%2BUWUbSKXt%2FGErc7PzbejMAcn7oSzINN3vHVWXbbYZoaNuzeHou5jOBkXFx8Ili%2F&X-Amz-Signature=fd7e7c8aaa6b9f67b894ce01521522b90e76035957354fff13b8a6a38ac2ac87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XOH6Z7C%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T062334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8hTU0CxOArSnZXLqRShe6mlAO7BVLJNQX9AC%2F1vbtDwIgFlCxdD37fuB9iQGZM0a%2F5dKhqIZSvBIBYSlWLFOHehoqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF70koFrCvM%2FDrhzDCrcA3fTh2pilZpJzha4w4z3eQbnjkUZUpqMFHBJdRbIkj96VzQrY4nK3HzonCDIReWMFCy4AFjgAAKBPK3WkqJI0V0XNREwLDN15unkB8auOFkt5xcVdS7qjehTy1zMoJ014ki8AgfdJps48F9n5iJ1JPJ%2F%2BB0Gu6JZkRqBU8ztul7TY40erDOudRsFFhA0w78JiG0qlIFlm2okGojSSEKCWh8YJ1w0v15FkJfD7bWNLDBD7WgW3fvU%2FRpMFnzze3WT9w0hZlEOMic%2BTK1vRtoTLW5oyePCL1D8RH2ZAR4Fi14sbkQ7pgD2VGjxHMuBZGWt%2BMbfNXYyOOPFixW5Mu8IE%2BAGsJ4%2BloGk5uz6BB56IQFiGoJ4lr%2BZdu%2F0ND8sYJA7rt48tdl%2B7DLRmj3YCTae6PKWiU%2BqjZQLRHxCowOF8p%2B2XYjw5BxqHskbhvgZ4YrBSUurxKZMqpHyV%2B9mSzVqrOKjrw2MpeXhOtq731HWAWuWz52%2BZgRPxOmbQ1NzZ6r0StSIMHJBHJqBxk%2F%2FFomAcd8njOLIFoG2wgiVr9DbfETq%2BZNMHo8BNBcknIfWD5F0z7Vp%2F5Qh8K%2BHypAMX9UPSw2PGHkfqFy14wpMaIwV4c53SDo9%2BEsuEp%2FOqEw%2BMKaa8MgGOqUBmgOdn0oEe9KlP8jWA9vJz%2BWLgG%2B8o3kmQd5k2q1qIrbTeoHG09b2CzJHxbbus17bUYkDG%2FU0ov%2FW3C6meq0y1eWKtdA3BqPosl%2Bj1O6hQg9yL2yeVBB25RWqc2hMaGZXXKvi9RgXe1OKLin9%2Bkg1%2BxmL1Q2V1%2BUWUbSKXt%2FGErc7PzbejMAcn7oSzINN3vHVWXbbYZoaNuzeHou5jOBkXFx8Ili%2F&X-Amz-Signature=9b4bca1ea0f148de0cec23b66ccc6b32803a8b3ee9c831aa7c245766f5b589a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







