



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXMFGHML%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T185106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHD3ZsICCFjPkQEOfYIUjoUswdKRXNeqbSAEdjZSiizyAiAQZSzTWaxHhd3D0I1tkKznfJzINYmMyrfhw5rqJJfhCyr%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIMfPPA%2FVDco6cbAXuyKtwDe4XFcHSdMpDfbmtZPkGMz3n%2FDo9%2BP5Tj1lVsM%2FQh58K8dkMI9vBvh%2Byc7pArTaORWZycPIdXElfHjfHzHA83zIJUs%2Bx4K4dxDce5pigGkrqUvM2yxei2pVIakyJuSsWgPAeU%2BhoFKBO3aO2n9KZFYRTAlrzrN2nxBKo8eRK%2Fr3GCf1f97AcnSNngoDi4YiscRV6YgZl05%2FbbNoqMYtpPnYPq14zZvKv%2B2Xpp5jof4%2BX2HC4W1rqhp3ACuqZ69TSNNdT4JkP9f5dTeOklvYE7N0Xyxm3mUV35VB0w9c1NNYaFi%2Bkh8R9nIdQrBaz4Wz0lQnRQQtZxp1%2Bxqppj3pnfnKbGrzsH%2BWS%2BOu9Jw4%2BHO4hWZ36VJGc3z0NBHt%2FntOfo4ZpE1dp5CZxeTHYx2XXMWY9im6fQaCaF1EbniqTxAk9chNjuvFNtRhcgmpMYEXWzgZfab93IFd%2BiZz8kvxCc4CAZlrvKqh21L0YTlFT0%2BSFALyOxWlmb9INnv8A%2FKNkE5LCdNCmoOQn1Zn1NuMJ0pg70%2Fy5Mn%2BvlDg6KBP%2FheWDCISr9m2nWnibdxhIvF7aL6Gq%2F5JpZTayTxHTwTpyv5kAjUCaeuynkfPw6l2E4kL9Ls5R5zc0NHdku1Ccwj9nSzAY6pgEFFfbTkAA959OG56Mw1dOL2NIYTAorr1fyJqS49CzzLxLNGBi8ntTQOikg7suOgGH0WsqBDpth1YSZh7%2BIeQr84Pnj0JEUkTeuuCY1oSqyfy9RQONieQa1LqAtVHpeYL4WMGfbkpz%2FHU909Qqxo6uH3R1nODsrfiaNCNK7UAj%2FMJPlCBGB6I3Mge7o29Ih2qnYdgCI4c7YbnCTn4kkk%2BVef6WMV8%2FS&X-Amz-Signature=3306053db7922e4a8b7e2843163b0bf34ce8ffe0de3d97f23199e462b6e5d84a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXMFGHML%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T185106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHD3ZsICCFjPkQEOfYIUjoUswdKRXNeqbSAEdjZSiizyAiAQZSzTWaxHhd3D0I1tkKznfJzINYmMyrfhw5rqJJfhCyr%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIMfPPA%2FVDco6cbAXuyKtwDe4XFcHSdMpDfbmtZPkGMz3n%2FDo9%2BP5Tj1lVsM%2FQh58K8dkMI9vBvh%2Byc7pArTaORWZycPIdXElfHjfHzHA83zIJUs%2Bx4K4dxDce5pigGkrqUvM2yxei2pVIakyJuSsWgPAeU%2BhoFKBO3aO2n9KZFYRTAlrzrN2nxBKo8eRK%2Fr3GCf1f97AcnSNngoDi4YiscRV6YgZl05%2FbbNoqMYtpPnYPq14zZvKv%2B2Xpp5jof4%2BX2HC4W1rqhp3ACuqZ69TSNNdT4JkP9f5dTeOklvYE7N0Xyxm3mUV35VB0w9c1NNYaFi%2Bkh8R9nIdQrBaz4Wz0lQnRQQtZxp1%2Bxqppj3pnfnKbGrzsH%2BWS%2BOu9Jw4%2BHO4hWZ36VJGc3z0NBHt%2FntOfo4ZpE1dp5CZxeTHYx2XXMWY9im6fQaCaF1EbniqTxAk9chNjuvFNtRhcgmpMYEXWzgZfab93IFd%2BiZz8kvxCc4CAZlrvKqh21L0YTlFT0%2BSFALyOxWlmb9INnv8A%2FKNkE5LCdNCmoOQn1Zn1NuMJ0pg70%2Fy5Mn%2BvlDg6KBP%2FheWDCISr9m2nWnibdxhIvF7aL6Gq%2F5JpZTayTxHTwTpyv5kAjUCaeuynkfPw6l2E4kL9Ls5R5zc0NHdku1Ccwj9nSzAY6pgEFFfbTkAA959OG56Mw1dOL2NIYTAorr1fyJqS49CzzLxLNGBi8ntTQOikg7suOgGH0WsqBDpth1YSZh7%2BIeQr84Pnj0JEUkTeuuCY1oSqyfy9RQONieQa1LqAtVHpeYL4WMGfbkpz%2FHU909Qqxo6uH3R1nODsrfiaNCNK7UAj%2FMJPlCBGB6I3Mge7o29Ih2qnYdgCI4c7YbnCTn4kkk%2BVef6WMV8%2FS&X-Amz-Signature=453def5efcb2f532b96b81a54a392262811374cee545ece5f2a2c17de5c11c75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







