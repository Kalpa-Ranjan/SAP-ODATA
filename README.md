



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BNETM7U%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T131534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDaYA98Ux0l2HGjqoLOQeJfnmj649s%2FBof8TIFFCBT95gIhAO3vmibtVPGYhUwlQp%2B4FKmXfx%2FUh%2BZV42c5W2C%2FcmgfKv8DCHUQABoMNjM3NDIzMTgzODA1IgzJo7pmcqBkP%2BH6%2Fqcq3AMjlQu%2Fwi6f8qgxcIu0l2C4OqcPYdznh6IrrDuFyVBjR36eF64Cx7KJJN4AkUB8%2FM7dW79RP%2Bv05sYhTg90K0HwNHquFBpj8kCDmDCuduTAJswsnY2GbsxBjLb9sgfQxDdDBAYiURAyIlmm1aqhmqa0eRZ5niKSI8BI2vbnBfP6Zx5jtPuSDTQSCtPamSLvt5RLXmbJJp6gwBEuzYyCaRwJWhJzhxTnblMYdfLLRWj3GshvMiks29%2F3OZ5UogwvDpbvvWkR94tgGOlzuTL9M55d%2B45fCvNPbGqfvLWaLm%2FMzQdWVjxIx5uCicTOxlFDawMap%2FBzx7KUHOI0yGrPFcRxwNf5b%2Bask%2BXMi4PuTHXSMJB%2FAfL5KYyXXhjcXTK9tUtEKGmu%2BaZ8fyH5maHq8VGkCdRatcprnUFo%2BRInbYaKP68PRiYwX3IHCBQ9p8NyvjPTDyQfyiF9CVlEowAP7jYf8aeBlCBE9iHN%2BDfX5JG%2F3Ceb5zRUyuaHxUQuArEEXUJamnecBpvZaq%2B9ufnll1KZiyTUWwYuEtG0EpQc2KbbMBrf7kOFYL2bUczpIWr5WhgZ8SOZkq2lq6Zh1kQZKBkAd0c6jKncGukspOzoc9se5Lo64rFzfLn9US1Q9jCXufPOBjqkAaoHq14e4RsDJ9OYsHl%2BQUSqVYmITj7bmjkfRZJghyt6W36S2UxGJCM5saaXm%2F6K4WLbG54ytisv83mEJ%2FkLswgi9wuyCJDxA2yyO5Udsoz02%2BmmRsnq%2BuqiQQ2suM1AfiFkFwn46XmTcyDvGWFloF5Lxwt0IoUSZjjze1eOaHTRRmq4vX6EK0SleobjA0ypZyBdJtvaTuT1UXZGSeL3BUgalUEk&X-Amz-Signature=32e7b5fd036779591b4a23e3b14813c7fdc5ab11a23e4a61334d608b6e393273&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BNETM7U%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T131534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDaYA98Ux0l2HGjqoLOQeJfnmj649s%2FBof8TIFFCBT95gIhAO3vmibtVPGYhUwlQp%2B4FKmXfx%2FUh%2BZV42c5W2C%2FcmgfKv8DCHUQABoMNjM3NDIzMTgzODA1IgzJo7pmcqBkP%2BH6%2Fqcq3AMjlQu%2Fwi6f8qgxcIu0l2C4OqcPYdznh6IrrDuFyVBjR36eF64Cx7KJJN4AkUB8%2FM7dW79RP%2Bv05sYhTg90K0HwNHquFBpj8kCDmDCuduTAJswsnY2GbsxBjLb9sgfQxDdDBAYiURAyIlmm1aqhmqa0eRZ5niKSI8BI2vbnBfP6Zx5jtPuSDTQSCtPamSLvt5RLXmbJJp6gwBEuzYyCaRwJWhJzhxTnblMYdfLLRWj3GshvMiks29%2F3OZ5UogwvDpbvvWkR94tgGOlzuTL9M55d%2B45fCvNPbGqfvLWaLm%2FMzQdWVjxIx5uCicTOxlFDawMap%2FBzx7KUHOI0yGrPFcRxwNf5b%2Bask%2BXMi4PuTHXSMJB%2FAfL5KYyXXhjcXTK9tUtEKGmu%2BaZ8fyH5maHq8VGkCdRatcprnUFo%2BRInbYaKP68PRiYwX3IHCBQ9p8NyvjPTDyQfyiF9CVlEowAP7jYf8aeBlCBE9iHN%2BDfX5JG%2F3Ceb5zRUyuaHxUQuArEEXUJamnecBpvZaq%2B9ufnll1KZiyTUWwYuEtG0EpQc2KbbMBrf7kOFYL2bUczpIWr5WhgZ8SOZkq2lq6Zh1kQZKBkAd0c6jKncGukspOzoc9se5Lo64rFzfLn9US1Q9jCXufPOBjqkAaoHq14e4RsDJ9OYsHl%2BQUSqVYmITj7bmjkfRZJghyt6W36S2UxGJCM5saaXm%2F6K4WLbG54ytisv83mEJ%2FkLswgi9wuyCJDxA2yyO5Udsoz02%2BmmRsnq%2BuqiQQ2suM1AfiFkFwn46XmTcyDvGWFloF5Lxwt0IoUSZjjze1eOaHTRRmq4vX6EK0SleobjA0ypZyBdJtvaTuT1UXZGSeL3BUgalUEk&X-Amz-Signature=e42e61db53f4241cb4ffee1adcdf027fec09795c234f627a7d3adf09c63fb2ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







