



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS6J3FVX%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T185618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCjvjumEEikBmKC42BhamuL0NCx1Gn5dK8mSutvVi7bAIhAJWLUk6zVoIyh3jwoUFYUHIi5YitRD8YYnXqlehS3h%2FaKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybIkUv2%2B2tiE3xA1Eq3AOpERKXCY9%2FdbZOq10jkKzhyEk3HuVmVjCqN6JwsGVQBVxleZUJn1ItOZH2NeISV6DlvGIF2dZK9zSW9RXGbOAziaL481t%2BK7jhOdger5trgwVQYiLk5V5Dc7hkp1%2FY9Bk7tB0%2FB91WL3jEil2QYvpjk26gRMl39eE4K14K2mXSsM0QRY1FXoVvUMKEW6PZtOvF0oIRmZZtMBcI5z%2BhHn8dlZtx6XCpmt46h73fIlzpJb14G%2Fc6pMU1D5maqaRsAmUyHiYcanfrQw6fLjDAdzYpJS1uLV6Ngg4nkefsQ6YEdXliKwrIAuFT7RDYms43KGHBFUdQUpLIPs5qrKKnKzexlXkl9ZiPp2uZNTnbFP4gq0EOQNS%2BN4rv8aO66w3lv8m2luWgjrMXdGB7KBJoqd%2BdYGhJyyNxq3nRI%2F5JnFFf59GQQp7AqJ%2FaVddG%2FP8shW5ZqCe9yZarifl6kiEnQzPhMU2gZYANR5MD3Kdkx1h1Mgkt2cCa4mne9C2tkHkgLU9N6wcHs1m5akK5Fk0e%2FsPYtag8a29aW3UNeUrN0vguE4ZJjqwxTgDtpThKguWB%2B6nkWnVJnBxTuX99FWI2T%2FLHHZcCsmGOlXMv%2Bn6gTivxk%2Fiq2VtQt3l3ZlwBMTCRqIvOBjqkAVeB6%2FPu5vNJL4xgrod17D3334gd6losSJ%2BkKAWaCmE4Gj17%2BceBp8FzjcMwwVLr9r2bs9gtdCN97Qgv2m0UxyUAjLJkOxoGiFWCaXmsWrcDIgjINQYjhB%2Bt0mE6qEtvKegx84RQv3qo13R9enQCyr7AaIzc545kVeX0lq2uB1tcGKO41SZO0yHCF9tYkRKaGrREm7ni11pBRNCfQL%2BOBXSCJZ05&X-Amz-Signature=028603067e2b74ab776d28ff0ce65d28ef5c1e6df2c0b245340fe823062e7865&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS6J3FVX%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T185618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCjvjumEEikBmKC42BhamuL0NCx1Gn5dK8mSutvVi7bAIhAJWLUk6zVoIyh3jwoUFYUHIi5YitRD8YYnXqlehS3h%2FaKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybIkUv2%2B2tiE3xA1Eq3AOpERKXCY9%2FdbZOq10jkKzhyEk3HuVmVjCqN6JwsGVQBVxleZUJn1ItOZH2NeISV6DlvGIF2dZK9zSW9RXGbOAziaL481t%2BK7jhOdger5trgwVQYiLk5V5Dc7hkp1%2FY9Bk7tB0%2FB91WL3jEil2QYvpjk26gRMl39eE4K14K2mXSsM0QRY1FXoVvUMKEW6PZtOvF0oIRmZZtMBcI5z%2BhHn8dlZtx6XCpmt46h73fIlzpJb14G%2Fc6pMU1D5maqaRsAmUyHiYcanfrQw6fLjDAdzYpJS1uLV6Ngg4nkefsQ6YEdXliKwrIAuFT7RDYms43KGHBFUdQUpLIPs5qrKKnKzexlXkl9ZiPp2uZNTnbFP4gq0EOQNS%2BN4rv8aO66w3lv8m2luWgjrMXdGB7KBJoqd%2BdYGhJyyNxq3nRI%2F5JnFFf59GQQp7AqJ%2FaVddG%2FP8shW5ZqCe9yZarifl6kiEnQzPhMU2gZYANR5MD3Kdkx1h1Mgkt2cCa4mne9C2tkHkgLU9N6wcHs1m5akK5Fk0e%2FsPYtag8a29aW3UNeUrN0vguE4ZJjqwxTgDtpThKguWB%2B6nkWnVJnBxTuX99FWI2T%2FLHHZcCsmGOlXMv%2Bn6gTivxk%2Fiq2VtQt3l3ZlwBMTCRqIvOBjqkAVeB6%2FPu5vNJL4xgrod17D3334gd6losSJ%2BkKAWaCmE4Gj17%2BceBp8FzjcMwwVLr9r2bs9gtdCN97Qgv2m0UxyUAjLJkOxoGiFWCaXmsWrcDIgjINQYjhB%2Bt0mE6qEtvKegx84RQv3qo13R9enQCyr7AaIzc545kVeX0lq2uB1tcGKO41SZO0yHCF9tYkRKaGrREm7ni11pBRNCfQL%2BOBXSCJZ05&X-Amz-Signature=306355d0b3132dcef9d5c6eae236731f95b1e9c2f3aa18ae3334ce43b301df23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







