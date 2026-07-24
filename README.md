



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OTQOZJL%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T081606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBYUHOWn3%2Bo7Mkq9OTjamB%2Fr21MzzQRMEzMXDQc9Ej6aAiEA1EIfWEI9X%2BLoY5S6a3%2FRxZinzOi7Ln6BW%2Bfng%2F0x0V4q%2FwMIARAAGgw2Mzc0MjMxODM4MDUiDMOC%2FfgRLtID9s5aJCrcA5rqsKPyWuJ41sdNn178dySTtcxWEjCtvq%2FRTZZkrVpH9BwI7tBaC%2BpNsrE%2FIp71xGzZiyu%2Fwz4%2FupkDYegaUPQ9%2FcveejhX4ysnxJAOK7IQDMgR%2FkHnfO9VmELWT3kyipRqly1Ce1UAAnpLHC5hn7TF6IWhnU4dJ2iABC1RidgMUM7ik9Onv%2Btrf7dvOYLw97Zm8V8fO%2FC%2Fcy4FYzAZGtr5ashayv5Ek8MNmvsqNKRFQmDtdePy7hxVAiZyf5raW4ZD0%2BDwu7eRGYr70txvjtzrQWDao0NHfaoBbBENGvDi5QPfGRlfxlxqtd4M1CLB2LTp99%2BKba0FxBGGSKzm89Uy3G3A%2FKUkYZToHoy%2BqP%2BlUevpMi2jyxywqp0cOo8EE2Od5%2BEjCK1DBtawc5Fx2%2BNISn2%2FQAkDIHNkDVjojIlmX4wn527KyJTFTFNmuxHj78IzXVSpNJPf75CAjj7ynwz%2F%2BmJXEUP%2BZn%2BsBfDSdOxzw9TBD4v1Qkc%2B32nTFGyjrwyH%2FRFvOnV1g4SgNyiqatRawUqtkNWJzqRJ4tqiKRaeXTGkWftxtbs1xdHHOhYkde7FJ5i%2F08KGnvBZaddlOP%2F5kFMKhtARfgbXOireqRfK8Q9gQyj5zXy%2BetVjMJOtjNMGOqUBANsSlwzH%2BcWHrxRNOhw9CfBSp8F4XN0BM89i%2FKOXQpmwx4JOeifkzwS7U3%2FX%2B9Ev5woo8k9yeizgIZU1sFRSjqXUk2o176PTMatcNbexgzNkxUDJ7MCKHZW4FkmJDsIMIIMFx7NumxuqlB1sEniP94kumTy9cmL%2F1wR04OzrTBYGl9A0GwVmQTJOCxOtej3H4FUCQInFxZnXOW4wx95P2Wjon3oI&X-Amz-Signature=6c3c8a394b65cbb0db54e5b2095c2656ca74e0b3b605d094d6364f3dfd603a99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OTQOZJL%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T081606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBYUHOWn3%2Bo7Mkq9OTjamB%2Fr21MzzQRMEzMXDQc9Ej6aAiEA1EIfWEI9X%2BLoY5S6a3%2FRxZinzOi7Ln6BW%2Bfng%2F0x0V4q%2FwMIARAAGgw2Mzc0MjMxODM4MDUiDMOC%2FfgRLtID9s5aJCrcA5rqsKPyWuJ41sdNn178dySTtcxWEjCtvq%2FRTZZkrVpH9BwI7tBaC%2BpNsrE%2FIp71xGzZiyu%2Fwz4%2FupkDYegaUPQ9%2FcveejhX4ysnxJAOK7IQDMgR%2FkHnfO9VmELWT3kyipRqly1Ce1UAAnpLHC5hn7TF6IWhnU4dJ2iABC1RidgMUM7ik9Onv%2Btrf7dvOYLw97Zm8V8fO%2FC%2Fcy4FYzAZGtr5ashayv5Ek8MNmvsqNKRFQmDtdePy7hxVAiZyf5raW4ZD0%2BDwu7eRGYr70txvjtzrQWDao0NHfaoBbBENGvDi5QPfGRlfxlxqtd4M1CLB2LTp99%2BKba0FxBGGSKzm89Uy3G3A%2FKUkYZToHoy%2BqP%2BlUevpMi2jyxywqp0cOo8EE2Od5%2BEjCK1DBtawc5Fx2%2BNISn2%2FQAkDIHNkDVjojIlmX4wn527KyJTFTFNmuxHj78IzXVSpNJPf75CAjj7ynwz%2F%2BmJXEUP%2BZn%2BsBfDSdOxzw9TBD4v1Qkc%2B32nTFGyjrwyH%2FRFvOnV1g4SgNyiqatRawUqtkNWJzqRJ4tqiKRaeXTGkWftxtbs1xdHHOhYkde7FJ5i%2F08KGnvBZaddlOP%2F5kFMKhtARfgbXOireqRfK8Q9gQyj5zXy%2BetVjMJOtjNMGOqUBANsSlwzH%2BcWHrxRNOhw9CfBSp8F4XN0BM89i%2FKOXQpmwx4JOeifkzwS7U3%2FX%2B9Ev5woo8k9yeizgIZU1sFRSjqXUk2o176PTMatcNbexgzNkxUDJ7MCKHZW4FkmJDsIMIIMFx7NumxuqlB1sEniP94kumTy9cmL%2F1wR04OzrTBYGl9A0GwVmQTJOCxOtej3H4FUCQInFxZnXOW4wx95P2Wjon3oI&X-Amz-Signature=fe0438eddb13e630f5bbaa442e302e43ea861625f38fbd6d94ca1f4d0d210f3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







