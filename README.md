



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMEPINVD%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T183921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLjVstK0LpoIygIq%2BvF9TDAjDY5LLI7vMdsGUjlOyxsAIgU%2FMRqpAqIO9UwNFOx%2BW2nmgd%2F7aByxlin6MyBcf4VrcqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLAzSshrOZlrlRRGoyrcA0q9QJY34HWLwTY9dCzoJRcKWU8Ky30E6a08DmQOtNCXu9r8LZRl8SU0URT1Fd7xn54n1Yvr5RbztDEAnvEEWMjYPqx8N%2FVezNjA6A66L2DsPYlzfmV5VC1nnsyDdNJeR5lJTnHJdiZ2FbjFC2haO9u2uX8nuf7o9UMncRS7ea0HKzs55nnLZ1OAjUgosInkUZHpbhi0IpDg9WR%2BbO1GnYU6ywZ4Y4%2BRo2VwOOltTlCQxL8l9DczC8QB8pG3hYR%2F42qGDr41C%2FV6Q6lT7Z9loawD0j33wFjbDV7ek0%2BhgtycbYKOUYJtlA6c4NGOykBcAzqkm2U75qcOi0eA0c%2BZUPIDcRxxz6gOx0C8l3fFRd9x6Xi2Tt7x2NKHNNGSVvIrjOHZiz8e%2B4GG529NS35RG8TOdmdPjgCzxCThE2lrewlzx3OnIk6GQWck4wH6t2%2Bvx%2F3xkWIR2Vpj50BrBp8bKh6cRrbnMHLhjIFzMHOJixOPEXTDOjuDWAQ7%2FfCsJ7n3t6o%2Bfsg%2FKm3zN%2Fuo7z42Bq2hcubHZXoOskv5vRuRk8lESJjOR9jnmMSEbe%2FZibZEyk%2BiCU2FB%2FPcdz8xjXI11ossjOEaRrDUyjO2V6Y9DIXBWlAWPAPFqVAzdBzMMNCel80GOqUBrF54942CFurB6mqEWCUan1OW4%2FqXp0eX6%2F2OmHwCI5xWSRxTqAc263z%2BabFmbV3l5QLhYTW06uqr7WAT5R3NzoTO%2Fm9ZqEQmuf3YPC%2Fpf6l8pLRaqMz83Pgt3ZnSuakzy7LkuVSqYDF4gq4IJMt%2F4ZXFwjjbodkUX4OspMG%2BmndW1HPqzm0q5hme%2B%2FitqQdofzR%2B200vfdXR%2FZSate469TojH4ia&X-Amz-Signature=dffe95bc9efca2a87248fcde3a2beb76b1182ae6124ea0c36ad86215dd4ca00d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMEPINVD%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T183921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLjVstK0LpoIygIq%2BvF9TDAjDY5LLI7vMdsGUjlOyxsAIgU%2FMRqpAqIO9UwNFOx%2BW2nmgd%2F7aByxlin6MyBcf4VrcqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLAzSshrOZlrlRRGoyrcA0q9QJY34HWLwTY9dCzoJRcKWU8Ky30E6a08DmQOtNCXu9r8LZRl8SU0URT1Fd7xn54n1Yvr5RbztDEAnvEEWMjYPqx8N%2FVezNjA6A66L2DsPYlzfmV5VC1nnsyDdNJeR5lJTnHJdiZ2FbjFC2haO9u2uX8nuf7o9UMncRS7ea0HKzs55nnLZ1OAjUgosInkUZHpbhi0IpDg9WR%2BbO1GnYU6ywZ4Y4%2BRo2VwOOltTlCQxL8l9DczC8QB8pG3hYR%2F42qGDr41C%2FV6Q6lT7Z9loawD0j33wFjbDV7ek0%2BhgtycbYKOUYJtlA6c4NGOykBcAzqkm2U75qcOi0eA0c%2BZUPIDcRxxz6gOx0C8l3fFRd9x6Xi2Tt7x2NKHNNGSVvIrjOHZiz8e%2B4GG529NS35RG8TOdmdPjgCzxCThE2lrewlzx3OnIk6GQWck4wH6t2%2Bvx%2F3xkWIR2Vpj50BrBp8bKh6cRrbnMHLhjIFzMHOJixOPEXTDOjuDWAQ7%2FfCsJ7n3t6o%2Bfsg%2FKm3zN%2Fuo7z42Bq2hcubHZXoOskv5vRuRk8lESJjOR9jnmMSEbe%2FZibZEyk%2BiCU2FB%2FPcdz8xjXI11ossjOEaRrDUyjO2V6Y9DIXBWlAWPAPFqVAzdBzMMNCel80GOqUBrF54942CFurB6mqEWCUan1OW4%2FqXp0eX6%2F2OmHwCI5xWSRxTqAc263z%2BabFmbV3l5QLhYTW06uqr7WAT5R3NzoTO%2Fm9ZqEQmuf3YPC%2Fpf6l8pLRaqMz83Pgt3ZnSuakzy7LkuVSqYDF4gq4IJMt%2F4ZXFwjjbodkUX4OspMG%2BmndW1HPqzm0q5hme%2B%2FitqQdofzR%2B200vfdXR%2FZSate469TojH4ia&X-Amz-Signature=cdb7441ed1552cabf3336fa6957a105033dabdb635ffd63d0b23f7f0d1903528&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







