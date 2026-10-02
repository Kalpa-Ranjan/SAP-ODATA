



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642V765X4%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T121304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn%2BKMQrvk%2FXA0OWP2vDD3o%2FFoJ3lp1f3C7jHKLi7MpdwIgOLI8zUevy6tDiM24OnS%2FQjp56%2FaRFAQnX0IDManQDRwqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKhQNKD8ndgfc7W7ySrcA3lsFOUzf5QpnKe9Eyk%2FaWjjFtr5erqhnLV3LQ5EZCcsP185NJf5lBbLGhQOUxR%2BGpdwK7NRdlRHFJTXwWVGEOGdRf83mohAoYBDbcrpGuTxFbhG7EmqefyZFhnJf1eVcLdTULhCcZe0RYpe3kT0qXQVB0Fu3TCQlsnxk06NIq4%2BQxrxbsiedmBTU33eb6eQdZLPaa7ZFd7OSRCzlv9Rp7WsHKT9iidzt9rKLwwfIQX%2F24GWope3Y2JgUbz%2FYJGK2rXB8mHmT50WLf0dCO%2BgPWH%2FFYsw1BRs4bz70HykUnuGWAG9RKtUvJyEmUFHr5C4ehXzBl6QEbT7QJZu58B5D9VlMZ8SwP8ox3stOacgfVLi9Z52NV9Pg%2FVo1zhl3jcpABO%2BtchKlwEG6pVzN%2FxjstjBXFzKkFHUi4xyMjndR%2BaTtS8S3Bc0XRUHuS0MA4KKG%2Bl0UJKxSarMTGeK8Qph%2FUVKDc6trh1rUy89XVRK1g635ycKlVV2RMZv2xScVqFo1ICo8tvZERNI4ioy52aEW%2FCYeGcmqZSovlPvz%2F0kY4WLZqsektmJ1VhcYX58H7cCBFvOSdxs5aJZfDrcLuzna5szhKbgHjTkx93DCy4kzT83COcZiq0y06ZGkxUHMNO5%2FtUGOqUBKBG%2BK3mV7%2FfjjLpxT9cH4FadK0YqoNJR%2FmsC02KvT83Jkui5PbSAHY4o%2Ba1FLflKz4eOvSOTjgEwq9S6DexQFKc6RyzJR9QGBySJxlkAl9hnbExCr9KPMxeQThp6a7roNGesONliqcDmxVs6gDdLWih2od0PGhE0IWS%2BPHb3gbiAJIeRnmWR0IMhBcn2OHrT47fqg%2Bi8kkcERbFjLvBju9PUvCRc&X-Amz-Signature=775d5f9b9b4a6a8aa01a7c2800f7b3c5bba9394b4dac7b4905e5bb923e0068d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642V765X4%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T121304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn%2BKMQrvk%2FXA0OWP2vDD3o%2FFoJ3lp1f3C7jHKLi7MpdwIgOLI8zUevy6tDiM24OnS%2FQjp56%2FaRFAQnX0IDManQDRwqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKhQNKD8ndgfc7W7ySrcA3lsFOUzf5QpnKe9Eyk%2FaWjjFtr5erqhnLV3LQ5EZCcsP185NJf5lBbLGhQOUxR%2BGpdwK7NRdlRHFJTXwWVGEOGdRf83mohAoYBDbcrpGuTxFbhG7EmqefyZFhnJf1eVcLdTULhCcZe0RYpe3kT0qXQVB0Fu3TCQlsnxk06NIq4%2BQxrxbsiedmBTU33eb6eQdZLPaa7ZFd7OSRCzlv9Rp7WsHKT9iidzt9rKLwwfIQX%2F24GWope3Y2JgUbz%2FYJGK2rXB8mHmT50WLf0dCO%2BgPWH%2FFYsw1BRs4bz70HykUnuGWAG9RKtUvJyEmUFHr5C4ehXzBl6QEbT7QJZu58B5D9VlMZ8SwP8ox3stOacgfVLi9Z52NV9Pg%2FVo1zhl3jcpABO%2BtchKlwEG6pVzN%2FxjstjBXFzKkFHUi4xyMjndR%2BaTtS8S3Bc0XRUHuS0MA4KKG%2Bl0UJKxSarMTGeK8Qph%2FUVKDc6trh1rUy89XVRK1g635ycKlVV2RMZv2xScVqFo1ICo8tvZERNI4ioy52aEW%2FCYeGcmqZSovlPvz%2F0kY4WLZqsektmJ1VhcYX58H7cCBFvOSdxs5aJZfDrcLuzna5szhKbgHjTkx93DCy4kzT83COcZiq0y06ZGkxUHMNO5%2FtUGOqUBKBG%2BK3mV7%2FfjjLpxT9cH4FadK0YqoNJR%2FmsC02KvT83Jkui5PbSAHY4o%2Ba1FLflKz4eOvSOTjgEwq9S6DexQFKc6RyzJR9QGBySJxlkAl9hnbExCr9KPMxeQThp6a7roNGesONliqcDmxVs6gDdLWih2od0PGhE0IWS%2BPHb3gbiAJIeRnmWR0IMhBcn2OHrT47fqg%2Bi8kkcERbFjLvBju9PUvCRc&X-Amz-Signature=0a3f1219f983f208465f81106ff345c52c7080cd74f753ea265ff43e38cdf46c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







