



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV6YO3MU%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T083028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHvynG%2BgUPB038AkyN4YRBiO%2BmVTAxqjZ2M7dPUowijeAiEA70nf8XRZ6HQN0m4CRR41r%2BS5JAbPVYwtKtAT2mXzknUq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDORlvD6nNkNSljgHZyrcAxzar%2FOORff88MyMvv5IJWbV66txIcvzNrd4w%2By4KR5TBRZVHzD6XTcHTmJagz5MtibFbVewinCNiMQ6%2Bi%2BzL2KzbO9Zqk9D5ImeJhFLnkZN7%2FL0K0d59ozbbs2ZW47wrTrp%2F0QhKJtou56qE5DECTT9a14xy6vdtkD5oM%2B2YGYPnLqIbRrlpV9B8Zob07QpyZnRDT7%2BArTPQD3VUlRPWgnOAG6NdG0gHJa9DxEJX234bhXRxoZIuS0SMtK%2FznUD6dze0gLuprijz%2B%2FU7wokiZq%2FqbHsk%2FTX0%2F4fSUdASmoYoKDE1Wil56X4MniuD63vcN5yEHNPqNTphJRp1gHmemBp%2BgAmLdL8tRqU7BA61J23zWWTaxfUPu6PXzIkukFogd99FrxSNJD3xSUIG2wg3vdZ8tRxXJ8APcC9UJibOcggBZTCmhmvBnN31fm2gGZb41Gjab5XwAI8Zimir0VU%2FD4b9SoFBhxgCELwklSGXm4Fqc7LSC8FOkJiHE%2Bdbm%2BFKfAIuIx%2Fnini6mBSdeNBxxNjcK4raBjImZQ7ZI96tLeLMWmQW9XskR5QqhH%2BUoQ2shm1RFMkepV5n5LmfYLbqYB7%2Ff8GR4BqpnfD6ISwTrQOrHlSd%2Fk%2BEkCvqkwRMN3lptMGOqUBiUqR0s4LJ8%2BlZYKkieQKhUNrDSfq%2FgpNwMRmyH4tsoxoHDVoDU2pkeTv04zuIHBOU5oIsSzVfBKDYqYpMVWsEFuOyZ9D44nrkzxQKTLiwtDGbhz0qqXSBiGG8ZgsUaM2N0IpNvdgY01WXN%2FxxyAwySCrN9HRztJ%2BARZu19lTmJeVQROGGNJrDAOhUygSlhISG7U%2BHP5lH%2Fkc4a4bsPUfe6K94iMj&X-Amz-Signature=1585c9a555da1156276f3c31750cb8ac0f03f92e4326ebc50b0e73c4d4454780&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV6YO3MU%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T083028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHvynG%2BgUPB038AkyN4YRBiO%2BmVTAxqjZ2M7dPUowijeAiEA70nf8XRZ6HQN0m4CRR41r%2BS5JAbPVYwtKtAT2mXzknUq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDORlvD6nNkNSljgHZyrcAxzar%2FOORff88MyMvv5IJWbV66txIcvzNrd4w%2By4KR5TBRZVHzD6XTcHTmJagz5MtibFbVewinCNiMQ6%2Bi%2BzL2KzbO9Zqk9D5ImeJhFLnkZN7%2FL0K0d59ozbbs2ZW47wrTrp%2F0QhKJtou56qE5DECTT9a14xy6vdtkD5oM%2B2YGYPnLqIbRrlpV9B8Zob07QpyZnRDT7%2BArTPQD3VUlRPWgnOAG6NdG0gHJa9DxEJX234bhXRxoZIuS0SMtK%2FznUD6dze0gLuprijz%2B%2FU7wokiZq%2FqbHsk%2FTX0%2F4fSUdASmoYoKDE1Wil56X4MniuD63vcN5yEHNPqNTphJRp1gHmemBp%2BgAmLdL8tRqU7BA61J23zWWTaxfUPu6PXzIkukFogd99FrxSNJD3xSUIG2wg3vdZ8tRxXJ8APcC9UJibOcggBZTCmhmvBnN31fm2gGZb41Gjab5XwAI8Zimir0VU%2FD4b9SoFBhxgCELwklSGXm4Fqc7LSC8FOkJiHE%2Bdbm%2BFKfAIuIx%2Fnini6mBSdeNBxxNjcK4raBjImZQ7ZI96tLeLMWmQW9XskR5QqhH%2BUoQ2shm1RFMkepV5n5LmfYLbqYB7%2Ff8GR4BqpnfD6ISwTrQOrHlSd%2Fk%2BEkCvqkwRMN3lptMGOqUBiUqR0s4LJ8%2BlZYKkieQKhUNrDSfq%2FgpNwMRmyH4tsoxoHDVoDU2pkeTv04zuIHBOU5oIsSzVfBKDYqYpMVWsEFuOyZ9D44nrkzxQKTLiwtDGbhz0qqXSBiGG8ZgsUaM2N0IpNvdgY01WXN%2FxxyAwySCrN9HRztJ%2BARZu19lTmJeVQROGGNJrDAOhUygSlhISG7U%2BHP5lH%2Fkc4a4bsPUfe6K94iMj&X-Amz-Signature=67182f4495ab1c3ac066381be6385d64cedb547411787f5b8a608181c0d8dbee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







