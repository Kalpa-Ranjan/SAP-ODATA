



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WHJVM35%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T092927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJIMEYCIQDvCxKfytY5P%2Fyu%2BT68PNZpKeS58vqYlEEd5iWj2h1jhgIhALegMaQdqPTxfybwYen1YglebCAKenq3kMBUE2mk4CwaKv8DCBoQABoMNjM3NDIzMTgzODA1IgySUFj%2B%2FmXgJ1Xbg1Aq3APDXOZcbDwFVbiudHIbrObbBGoqXJtMmIO3g63Q4LZV2sYeaw%2Bkz0VZJWBJINdpoh0AKPWXOTIdbj8COLXESHE1N3iStWB1N6HYwRCugQcU4nl7IXTDbNYCdIlwYLBVQsTkIyzczb%2B8Jap1HV%2BbxFa92ZDYd6l1xbi2Zq55CekjWGV3oWdOZP%2Fm8IGoJtFXp4zc%2FD9rpmI0LXllOE9kS4SKdCi%2FTDYfMbx8GeW4g946EPCPQD1SSY51r7FV0AvOx5kyY4t5pPr13nPun7oDbsrfTzA%2Brzx9TO%2FkjxyrYymraddEoQfiUmKSfJUYcEqEMwMuDM9v%2B4jTeev7uc%2B3BU2ts1ifVCU2B5xgK8AZCrkcr8UFi3t29ODMbWbGXYcsIkLemuUzEi0AvenxBSfwPO3DbxD5CHEy0GkzFsLk5SKrqf48OmShyqhra6kbuhoE2zHOxJ9XJM%2B1veCbni1KNcDprEIXvk%2Bjq%2ForMwwFihf7xt9AbyGn1jsUBx7tmTJjqBDtCRf68u2LaU6wFYZbJC1OM1wivDgKVfATNHkDMCvarxnceY6UG2iPg1H7kzDrhIuSkD3wNZecbexSjYtuEojLDA1bh%2FMxyBthkm9RFEAvnTmDwnPcUI9VdeH0vjCQnOnRBjqkAY9rue0o2vfz8tYNOqu4YDn5n4rm%2BtWZZ6iVFosgFUqAEBV4C0hkjAxn6dZd9G0OLZIURWCq3Wmd1yd%2FRsoq56hCFCUd3ss4M%2By9Og0sxJvjtKwhwqZAY5iaqCrBdLbow9PIfG4KK5qMSSqHl1isX6WqSurcRm%2FrMLeo8L4uyo3dFiuFMbQj%2BTFPJdYJou6LefOzjd6Iw8oOfUWxG9A7FWnyfoUP&X-Amz-Signature=371ed7dbb4912f17d0410ea522b4b41d89fce0e78bd728a3406676dc9343cc1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WHJVM35%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T092927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJIMEYCIQDvCxKfytY5P%2Fyu%2BT68PNZpKeS58vqYlEEd5iWj2h1jhgIhALegMaQdqPTxfybwYen1YglebCAKenq3kMBUE2mk4CwaKv8DCBoQABoMNjM3NDIzMTgzODA1IgySUFj%2B%2FmXgJ1Xbg1Aq3APDXOZcbDwFVbiudHIbrObbBGoqXJtMmIO3g63Q4LZV2sYeaw%2Bkz0VZJWBJINdpoh0AKPWXOTIdbj8COLXESHE1N3iStWB1N6HYwRCugQcU4nl7IXTDbNYCdIlwYLBVQsTkIyzczb%2B8Jap1HV%2BbxFa92ZDYd6l1xbi2Zq55CekjWGV3oWdOZP%2Fm8IGoJtFXp4zc%2FD9rpmI0LXllOE9kS4SKdCi%2FTDYfMbx8GeW4g946EPCPQD1SSY51r7FV0AvOx5kyY4t5pPr13nPun7oDbsrfTzA%2Brzx9TO%2FkjxyrYymraddEoQfiUmKSfJUYcEqEMwMuDM9v%2B4jTeev7uc%2B3BU2ts1ifVCU2B5xgK8AZCrkcr8UFi3t29ODMbWbGXYcsIkLemuUzEi0AvenxBSfwPO3DbxD5CHEy0GkzFsLk5SKrqf48OmShyqhra6kbuhoE2zHOxJ9XJM%2B1veCbni1KNcDprEIXvk%2Bjq%2ForMwwFihf7xt9AbyGn1jsUBx7tmTJjqBDtCRf68u2LaU6wFYZbJC1OM1wivDgKVfATNHkDMCvarxnceY6UG2iPg1H7kzDrhIuSkD3wNZecbexSjYtuEojLDA1bh%2FMxyBthkm9RFEAvnTmDwnPcUI9VdeH0vjCQnOnRBjqkAY9rue0o2vfz8tYNOqu4YDn5n4rm%2BtWZZ6iVFosgFUqAEBV4C0hkjAxn6dZd9G0OLZIURWCq3Wmd1yd%2FRsoq56hCFCUd3ss4M%2By9Og0sxJvjtKwhwqZAY5iaqCrBdLbow9PIfG4KK5qMSSqHl1isX6WqSurcRm%2FrMLeo8L4uyo3dFiuFMbQj%2BTFPJdYJou6LefOzjd6Iw8oOfUWxG9A7FWnyfoUP&X-Amz-Signature=3d390395a6b3b2333cbe8d81c06a96a592803020f182a3fc0471a4ae4715bf87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







