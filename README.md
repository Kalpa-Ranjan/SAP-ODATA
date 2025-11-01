



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZMZMW42%2F20251101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251101T011456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQC7KthQRFzl7nuThWrU4rZzW2Yn4EMsnp8z3xWcthnSNgIgQwbYoH3LYrAhkDs53pyOPu%2BY69bMAk1j3rxjqlfsE7oq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDLD2rPw9aMf8SMoNSyrcA%2B%2BYPcVWwJ%2FGt9kgO6ZWMgH5MxkDu8w975OVqwIYtwhcfLU3V3zNr7fHYgwWTjEs0yKi8nxwLlCOUcSNBygb5Sso4M8tOYaQEZqh6aAhywWGCB3xPmE%2F2LShwH%2FtsJaUDe%2Fbdlys7NUyHQPCd5eDzbl6iBfdMYh72HApxhbnKP6b%2Fnd0N%2B8g8d%2Fx9y2G%2BRbPRbBrK6zRZQan%2F23lDK3HzFtE033EwOuL2sXyFinXblQwxseN1KOxxRs0dURABTN7tFFzkDwyho%2BjqZQNz0%2F2P2Lvaw4w8SQf6xrdYPMhHbN8RGTlKiDUhqANfgFlNy%2BiYDzaMESw5fRRusI%2F1I7dJUfjJUYNoYAoARyz1RLMKQEinC5yhfxZI71fQkN9u12VXi9xfjs3jeX2N7yRwoTqjeSrgFYLzeFUAwlXs6%2FC7OJC97f6cD%2Byf00usQl%2BlI%2Fjdu12wIGOJOClCj694YE%2B%2BNrdNm3i9JBweXzxjKS%2BzFw7ol47jc14zLouyK0TpWKtvOOrctcMiKF%2FcESMEC0QfuCUDe5R3umdg%2BKE17lR5w6w6y6u%2FLVi0C09gXpwSejamw0hB3yKfhIvkpVQOMYkLvk1JWcw%2BNehFj3wOiko615KinX7nKmqGB54B2kYMIv6lMgGOqUBI426L8t8mQ6YlODBsP0N5Vxn44GOCYKRup9xtjud%2FcndyESzppPs5eCcgCRGhyYmstw9cPo7zT1xgCf2ire2DSx2cRY0S6rFkVhg7X%2BuBDuIYM7Qw4%2BzE7yPUnIzCo9oHRQOvE835byq%2FScDiYREelcbpKKIAgGHfnajDlWo4x1mL4FObtSSlGux2pWpQqWVbSyFmQzysOVqq0tzIDXdYNSwrCbH&X-Amz-Signature=4d42f1dad6f6f909570d9a384461b7789573532798bdce12dbafb5152d3b6ffe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZMZMW42%2F20251101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251101T011456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQC7KthQRFzl7nuThWrU4rZzW2Yn4EMsnp8z3xWcthnSNgIgQwbYoH3LYrAhkDs53pyOPu%2BY69bMAk1j3rxjqlfsE7oq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDLD2rPw9aMf8SMoNSyrcA%2B%2BYPcVWwJ%2FGt9kgO6ZWMgH5MxkDu8w975OVqwIYtwhcfLU3V3zNr7fHYgwWTjEs0yKi8nxwLlCOUcSNBygb5Sso4M8tOYaQEZqh6aAhywWGCB3xPmE%2F2LShwH%2FtsJaUDe%2Fbdlys7NUyHQPCd5eDzbl6iBfdMYh72HApxhbnKP6b%2Fnd0N%2B8g8d%2Fx9y2G%2BRbPRbBrK6zRZQan%2F23lDK3HzFtE033EwOuL2sXyFinXblQwxseN1KOxxRs0dURABTN7tFFzkDwyho%2BjqZQNz0%2F2P2Lvaw4w8SQf6xrdYPMhHbN8RGTlKiDUhqANfgFlNy%2BiYDzaMESw5fRRusI%2F1I7dJUfjJUYNoYAoARyz1RLMKQEinC5yhfxZI71fQkN9u12VXi9xfjs3jeX2N7yRwoTqjeSrgFYLzeFUAwlXs6%2FC7OJC97f6cD%2Byf00usQl%2BlI%2Fjdu12wIGOJOClCj694YE%2B%2BNrdNm3i9JBweXzxjKS%2BzFw7ol47jc14zLouyK0TpWKtvOOrctcMiKF%2FcESMEC0QfuCUDe5R3umdg%2BKE17lR5w6w6y6u%2FLVi0C09gXpwSejamw0hB3yKfhIvkpVQOMYkLvk1JWcw%2BNehFj3wOiko615KinX7nKmqGB54B2kYMIv6lMgGOqUBI426L8t8mQ6YlODBsP0N5Vxn44GOCYKRup9xtjud%2FcndyESzppPs5eCcgCRGhyYmstw9cPo7zT1xgCf2ire2DSx2cRY0S6rFkVhg7X%2BuBDuIYM7Qw4%2BzE7yPUnIzCo9oHRQOvE835byq%2FScDiYREelcbpKKIAgGHfnajDlWo4x1mL4FObtSSlGux2pWpQqWVbSyFmQzysOVqq0tzIDXdYNSwrCbH&X-Amz-Signature=df8ac31ac2996f339ce77864d6a2fc3302bc86cb964d4b5b6ed743248a10855e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







