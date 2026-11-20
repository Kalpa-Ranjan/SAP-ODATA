



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGE6XNIF%2F20261120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261120T180530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIH97L41I5j6i%2BpBTeIIWigpwqJwhVZD79foVg9wZuz%2BqAiEA6lpGZhMjAd7m3CMjlUbCcCmmb08PTfqzk3DlvvhXvCgq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDCbPtQZh0W4YqvLDNircA%2B0WczJk6IWlGbQ1LQKZMsYTXG9K41IatBxRL2EPG2dKufl3hZ4V1VrZwkl0e%2F5Xwip73IWEkmJesuU2JZ9V5LOO6IhZbVWEKPptZ2qHx73iw1EM0C2kwEouiOG1KEXjc%2F2Cc6y1RsbFeXlhc6c3beKoa%2FEvUX3JX8TdiEVogVmJ93fy2Ici0djhJqPznOf8RUQwA9Rl7Tw2JmmmkGjmvOi0IlZ51IqV3drS5IImmPzQvxg0uzWUMtuoteitmTZzOIlN75nsSznYtFqCqF%2Frov2XMaRM2445H0J%2BQ7eEJEY%2BtRaNg53HsHKT5nrgkBRROUgFnlg8rBzQhCtEKTT7e1Kn3EHQOcJdYFwUTkx9DAOLypMEQfYS9e8azUbEV7OYLhUQZBpfw7977I%2BSWt5QimpC6U31NsfT%2BLAsafqneqnN35Z%2Fq7Gdqzbsvkb%2BNS2jYygVdGwwvv3bSpR9XNUvHhyHHsplhgQFEh%2BfjgWRrGEPHrFzKP6DbGwZxSme70p1PQKJh%2BZZ2BHWo3MgAOveRR3%2B0j%2Bi3yVrJxXetg2bnJIo%2B4PJbKXJRxYqG85%2FQbLsfc%2BHOT1WWyZq7RKLo9JDNxdzWepPl1wPgqGYUtaw%2Bn2zd7aNS5eVhc54TMtMMJ3fgdgGOqUBMnE%2F6WgE%2FQgxD5mlkD8jbFgx757Nwj2jfloy6n5jU9SDLnRp9Ugetm3BnpyrHqxsyhfdKnla%2F%2FST3n4h8LJdPV1I0Rl5gWjJ6QNrNpyoGQT3dBlYhT3aIHA3xYKVks0IJMtlnJ4J%2BsJUD%2BK%2B5eJwdYbI2CpdeeINID385%2F3Gz%2BEv0Iz7hKwCg88f%2BF18seSGjcyCTIzRhGJR1738%2FoTJ1SLTfNUm&X-Amz-Signature=91cb60326f74156f05c38187dd12146d7deface0e19e1c29a18fff2b6a55d88d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGE6XNIF%2F20261120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261120T180530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIH97L41I5j6i%2BpBTeIIWigpwqJwhVZD79foVg9wZuz%2BqAiEA6lpGZhMjAd7m3CMjlUbCcCmmb08PTfqzk3DlvvhXvCgq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDCbPtQZh0W4YqvLDNircA%2B0WczJk6IWlGbQ1LQKZMsYTXG9K41IatBxRL2EPG2dKufl3hZ4V1VrZwkl0e%2F5Xwip73IWEkmJesuU2JZ9V5LOO6IhZbVWEKPptZ2qHx73iw1EM0C2kwEouiOG1KEXjc%2F2Cc6y1RsbFeXlhc6c3beKoa%2FEvUX3JX8TdiEVogVmJ93fy2Ici0djhJqPznOf8RUQwA9Rl7Tw2JmmmkGjmvOi0IlZ51IqV3drS5IImmPzQvxg0uzWUMtuoteitmTZzOIlN75nsSznYtFqCqF%2Frov2XMaRM2445H0J%2BQ7eEJEY%2BtRaNg53HsHKT5nrgkBRROUgFnlg8rBzQhCtEKTT7e1Kn3EHQOcJdYFwUTkx9DAOLypMEQfYS9e8azUbEV7OYLhUQZBpfw7977I%2BSWt5QimpC6U31NsfT%2BLAsafqneqnN35Z%2Fq7Gdqzbsvkb%2BNS2jYygVdGwwvv3bSpR9XNUvHhyHHsplhgQFEh%2BfjgWRrGEPHrFzKP6DbGwZxSme70p1PQKJh%2BZZ2BHWo3MgAOveRR3%2B0j%2Bi3yVrJxXetg2bnJIo%2B4PJbKXJRxYqG85%2FQbLsfc%2BHOT1WWyZq7RKLo9JDNxdzWepPl1wPgqGYUtaw%2Bn2zd7aNS5eVhc54TMtMMJ3fgdgGOqUBMnE%2F6WgE%2FQgxD5mlkD8jbFgx757Nwj2jfloy6n5jU9SDLnRp9Ugetm3BnpyrHqxsyhfdKnla%2F%2FST3n4h8LJdPV1I0Rl5gWjJ6QNrNpyoGQT3dBlYhT3aIHA3xYKVks0IJMtlnJ4J%2BsJUD%2BK%2B5eJwdYbI2CpdeeINID385%2F3Gz%2BEv0Iz7hKwCg88f%2BF18seSGjcyCTIzRhGJR1738%2FoTJ1SLTfNUm&X-Amz-Signature=86c0ccebb0c1ff220e9576ac1c1597afbbfe929bca75a3f0f949ec69800a5b34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







