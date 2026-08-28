



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667P3FAMON%2F20260828%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260828T083839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmiJo55j0PSpA3uaKXMkqNp0kWWJYcuI8vPzrwKzg0rAIgWlQ7iuPEDO3PYXceCvtBsI1DMONdrpVybTkVJjAdM80q%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDEP4ZgKt7vJRfW2SzCrcA%2FhCngcZyIJq3b6mx9%2BFewkta%2Ftd4YWCojeAnRi6sVaeCHrLFobILcsFvLu1YzboqwdYqut0IiqOBGJ9Wsx1070sCVNSKOeE%2FvGurgA9HUolzUH1Kca4NokQmm7h20NOPVs%2BWAT4mfDF203rZkrvg7uZtDzKTeCsRZOmyrlKpGY9%2BcPIL5EVWokqx1K9VTIw6ES2ZR0FjTcAyl4Lwox27PIqKnU1%2F5eQCnSO5miq2EDRzI%2FP79EU1PEzlCTUpEIn1Z%2FpRg%2FS4opecetUVOQxR7LbWSoxmaUFA7Zi9g2T5LPBDdXRWRQO5FF%2FN7rWl2m4jYSqWMIWPUpyc%2FwiGVLViMBgDUHJ4RUZ5sSKWyXubaWFPwE6RqcDaa3YYDxkIyckW%2FBBFAMz6jgU7hlzFztCaJffDDggYTx71naWRGsgzYIehsQO0wAw3uBuwVp%2FFEm3ZEJWLC0qyuT5Wz%2FZ00U7gdxNok4E4QAgeeOksxVosJURyuFHRLYZVgVc7NpOkj%2FeGXv5QJo2W%2B7dOArRYXoI6KUd99Qn%2F3enmokpCh%2BwRz9OPw9a5WSqvHUjaOUDMqAB7UlKkkpyPeY60%2FqNdAwZSdchWNbDjDgWaekkHrtH52FxojynTrYvu%2FEUiM2OMJfvxNQGOqUBTuQCnHaYckXIAJG778ZCFfFtYX9ieR4%2BlEPiauCDZsu48m6X2jm1VCL3hkKqS6BbP2j1mVWauqoCJV749Y5WtdYCwrmZ%2FuroFbIAyKOJ6ebHHRskPmzAS%2BcvBwgdcJKUKu7RaAve0P%2FfX2BzaSpfP6MVYYAYUtLhR8tRdVx0pi2Kv0S6ymYtsOGlFpmN6NsumC2XZ18RAtdJUxrvfDxLntoMZtzF&X-Amz-Signature=a4e35d5db7c88512f380739f7841c9cd842c3b6865ae9f6a1c1456fbb53868d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667P3FAMON%2F20260828%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260828T083839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmiJo55j0PSpA3uaKXMkqNp0kWWJYcuI8vPzrwKzg0rAIgWlQ7iuPEDO3PYXceCvtBsI1DMONdrpVybTkVJjAdM80q%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDEP4ZgKt7vJRfW2SzCrcA%2FhCngcZyIJq3b6mx9%2BFewkta%2Ftd4YWCojeAnRi6sVaeCHrLFobILcsFvLu1YzboqwdYqut0IiqOBGJ9Wsx1070sCVNSKOeE%2FvGurgA9HUolzUH1Kca4NokQmm7h20NOPVs%2BWAT4mfDF203rZkrvg7uZtDzKTeCsRZOmyrlKpGY9%2BcPIL5EVWokqx1K9VTIw6ES2ZR0FjTcAyl4Lwox27PIqKnU1%2F5eQCnSO5miq2EDRzI%2FP79EU1PEzlCTUpEIn1Z%2FpRg%2FS4opecetUVOQxR7LbWSoxmaUFA7Zi9g2T5LPBDdXRWRQO5FF%2FN7rWl2m4jYSqWMIWPUpyc%2FwiGVLViMBgDUHJ4RUZ5sSKWyXubaWFPwE6RqcDaa3YYDxkIyckW%2FBBFAMz6jgU7hlzFztCaJffDDggYTx71naWRGsgzYIehsQO0wAw3uBuwVp%2FFEm3ZEJWLC0qyuT5Wz%2FZ00U7gdxNok4E4QAgeeOksxVosJURyuFHRLYZVgVc7NpOkj%2FeGXv5QJo2W%2B7dOArRYXoI6KUd99Qn%2F3enmokpCh%2BwRz9OPw9a5WSqvHUjaOUDMqAB7UlKkkpyPeY60%2FqNdAwZSdchWNbDjDgWaekkHrtH52FxojynTrYvu%2FEUiM2OMJfvxNQGOqUBTuQCnHaYckXIAJG778ZCFfFtYX9ieR4%2BlEPiauCDZsu48m6X2jm1VCL3hkKqS6BbP2j1mVWauqoCJV749Y5WtdYCwrmZ%2FuroFbIAyKOJ6ebHHRskPmzAS%2BcvBwgdcJKUKu7RaAve0P%2FfX2BzaSpfP6MVYYAYUtLhR8tRdVx0pi2Kv0S6ymYtsOGlFpmN6NsumC2XZ18RAtdJUxrvfDxLntoMZtzF&X-Amz-Signature=2e535cc7c2a547ac797f341ca69ab0af1a4b6f952adaa3e0031e15f20a4e0b13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







