



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675RQNLZD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T132632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB0JP7SNf8Kw6yryRyeLJ6FRaeCshgiwAN7LFy5wW0TRAiEA2FBuNtLq2nme5%2BbrkVmPtqopD4JMb%2FGJYFrkvzBTsRcqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISOXUGzYY57zAb7ySrcAzen20v7CIl0crmayDqnNEaIu2apIhGTnjVRIDcqpeCRK%2BuPlmZFY5ZSjZ2qR9Ox0U2j0qvLVRKJn8GSeJrlb5uIVuhOsHiMm5lb36X6Az2ZlullOovxjmA%2F1oCXdiKbbbxlUWspiLTF9CuYttjGCHe1ja1fdAIgAnKQGCbSs78LBhuinXJ1zQRdR78%2F%2FRzxVpFCuckLvOHRtwm0BOk22pwvNmvNU%2FvLqmyR6xzRinhxTkj19qblkClxmjgiQYc%2BTvoMA8mBc115Of8pbpOaEVBAGBf2nMCqNAbsqpx1GanSm1Jg0VEnd1umNna36qdrYY9lUfl8pwyJNcFA1SjVACrHyk10bjk6RhqHMLpIRB1DggjatwJ0alf5fpRBkqfFI7K0fRKuULSV7cGEcZn8FN7E6DOcpKRDSR%2BaspN1PWLwD3uMODxq5zK1H8ybrBgoguUCzqRhXunmsqKVInFK3hbE6nlV1bwwXaFHpT8IdXXP%2FeDGN3s0i4hMtdqkZGfZMgfFcpM%2BNarTMWEWqZT3yCukLxpI0l7FZfmmWleyyMabA%2FH9GKSNuOphA9kricvrNA8jUEVmzMNaHyrJlBS2t3WAe27yyhA3DmbjTEcRdvm8quIOoKME0uB4knEdMKzE%2FdIGOqUBhCM%2B%2BU2bmKGnpO090N9DxAijcLOTsuuYzt8YPKVB9nugC2ul6gZP3BhGm0UaLBi%2FAVprFm1hiQWepSQtDsIzZ%2Fp%2BR0uWEj60dK4QyWpezQTahSSIwHyZsAt846tYGc319mknYkJnl4uHdSAqDbV1WaPcF7eNX0wuyy1VCnFUbCbjMBZxocfkEUJIUZHata3SDjdLJjDTD14EkR4UMFZNuIS5MUcE&X-Amz-Signature=8c4a2349fadaf7a4f3c650460354db5c19592fa79934a21af65c1dbe729960ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675RQNLZD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T132632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB0JP7SNf8Kw6yryRyeLJ6FRaeCshgiwAN7LFy5wW0TRAiEA2FBuNtLq2nme5%2BbrkVmPtqopD4JMb%2FGJYFrkvzBTsRcqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISOXUGzYY57zAb7ySrcAzen20v7CIl0crmayDqnNEaIu2apIhGTnjVRIDcqpeCRK%2BuPlmZFY5ZSjZ2qR9Ox0U2j0qvLVRKJn8GSeJrlb5uIVuhOsHiMm5lb36X6Az2ZlullOovxjmA%2F1oCXdiKbbbxlUWspiLTF9CuYttjGCHe1ja1fdAIgAnKQGCbSs78LBhuinXJ1zQRdR78%2F%2FRzxVpFCuckLvOHRtwm0BOk22pwvNmvNU%2FvLqmyR6xzRinhxTkj19qblkClxmjgiQYc%2BTvoMA8mBc115Of8pbpOaEVBAGBf2nMCqNAbsqpx1GanSm1Jg0VEnd1umNna36qdrYY9lUfl8pwyJNcFA1SjVACrHyk10bjk6RhqHMLpIRB1DggjatwJ0alf5fpRBkqfFI7K0fRKuULSV7cGEcZn8FN7E6DOcpKRDSR%2BaspN1PWLwD3uMODxq5zK1H8ybrBgoguUCzqRhXunmsqKVInFK3hbE6nlV1bwwXaFHpT8IdXXP%2FeDGN3s0i4hMtdqkZGfZMgfFcpM%2BNarTMWEWqZT3yCukLxpI0l7FZfmmWleyyMabA%2FH9GKSNuOphA9kricvrNA8jUEVmzMNaHyrJlBS2t3WAe27yyhA3DmbjTEcRdvm8quIOoKME0uB4knEdMKzE%2FdIGOqUBhCM%2B%2BU2bmKGnpO090N9DxAijcLOTsuuYzt8YPKVB9nugC2ul6gZP3BhGm0UaLBi%2FAVprFm1hiQWepSQtDsIzZ%2Fp%2BR0uWEj60dK4QyWpezQTahSSIwHyZsAt846tYGc319mknYkJnl4uHdSAqDbV1WaPcF7eNX0wuyy1VCnFUbCbjMBZxocfkEUJIUZHata3SDjdLJjDTD14EkR4UMFZNuIS5MUcE&X-Amz-Signature=047e84a5c497ec78d97c86c17df68f1cd597574b1c81291015b8d600c18f231d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







