



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V7IOK2X%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T082123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIASpiHq3ECMs7QxQATdt1mCbq8LuduH9xRmFSCOHkAoHAiEA8wKGKeyBYaXt6BaRvV91qazevgTibD9lNJWlWL2aZrEqiAQI6f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6jn8fwXsv4bOULPyrcA8nwURWkr%2FbzUT1yPaHIkBunsg%2Bl%2Fb2oQAfKX1WZB4LuXA0fSkc%2BPDENhDrEvak1cI4TEqcydZxasmnAGzeFPUOvx6f74UgC2TZEkrm%2BDzxTp4SMtTLmLUpEtKd%2FUgxF1aX3eooyuTqPBUJwVmhvqST63a6beZATgOnh3zqqLjU8OUJosOenVRsH4LvMwWEe49BrBa1qGgL7GSNx5DJm3hjggI%2B%2F0lslTLQc%2FvjDBTqBA47WvOKJ8gpmQHRsswDzbI%2FK2Flkxk1TU3hbOPcOD5mmevu1VSHr37DWXCRE0Q2aFyxnmH%2BV13o4hk3GBizw3g7%2FmGYiTgRda%2F32f1EB9J597FcxfqLAx%2BtJOTIud6pwDyP0De4DFhXbqYFEUQCVZM2Yym22a7opTmqlqACTrgEIC316mjwpY9G8%2FbmYAykCB3bLoiJUqpBOyHXaIwWCbSHfWsumZgdbGfe7OYmMV0nlwAIFeNTtTl9xQ3A2LZFr0QfcXnpRanputCsEYznWmKyu%2Bspu0JzJkJTJtoYeOAEgdGApBlfRju%2FERAPiF8JmTZqMFqyTcQMT9tHI2qlpvFCoBiDhIITHyZDBD3zZCnDIdeBSRX1sKkH7hhE1E5s%2F3YI%2FMCMsdpwow9xbMM6Xh9MGOqUBtCtMZgHjAJpkycdHx327YMuqxK9ic4G52mSjbJsFwnJSJm%2F8N2muDMEFnlmohiekSazJ7XCP9%2B087y4I3UIFmy%2FcooLt5GDQaY7SOzaad07hUPk57rVS8ZIxXo4Is8mZePQBm2xa3sCxVYFVTSg0mIM8tU9hu7U6BnNlY84nm3v9LlCNnu4sQHnRPZJuu9F%2FdJtsMGzNUPmu8X9vzx9yDoHuXTa%2F&X-Amz-Signature=edb67d80c57df97e3cab56638b2a768d084de075eda4bade8e7b555d181905c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V7IOK2X%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T082124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIASpiHq3ECMs7QxQATdt1mCbq8LuduH9xRmFSCOHkAoHAiEA8wKGKeyBYaXt6BaRvV91qazevgTibD9lNJWlWL2aZrEqiAQI6f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6jn8fwXsv4bOULPyrcA8nwURWkr%2FbzUT1yPaHIkBunsg%2Bl%2Fb2oQAfKX1WZB4LuXA0fSkc%2BPDENhDrEvak1cI4TEqcydZxasmnAGzeFPUOvx6f74UgC2TZEkrm%2BDzxTp4SMtTLmLUpEtKd%2FUgxF1aX3eooyuTqPBUJwVmhvqST63a6beZATgOnh3zqqLjU8OUJosOenVRsH4LvMwWEe49BrBa1qGgL7GSNx5DJm3hjggI%2B%2F0lslTLQc%2FvjDBTqBA47WvOKJ8gpmQHRsswDzbI%2FK2Flkxk1TU3hbOPcOD5mmevu1VSHr37DWXCRE0Q2aFyxnmH%2BV13o4hk3GBizw3g7%2FmGYiTgRda%2F32f1EB9J597FcxfqLAx%2BtJOTIud6pwDyP0De4DFhXbqYFEUQCVZM2Yym22a7opTmqlqACTrgEIC316mjwpY9G8%2FbmYAykCB3bLoiJUqpBOyHXaIwWCbSHfWsumZgdbGfe7OYmMV0nlwAIFeNTtTl9xQ3A2LZFr0QfcXnpRanputCsEYznWmKyu%2Bspu0JzJkJTJtoYeOAEgdGApBlfRju%2FERAPiF8JmTZqMFqyTcQMT9tHI2qlpvFCoBiDhIITHyZDBD3zZCnDIdeBSRX1sKkH7hhE1E5s%2F3YI%2FMCMsdpwow9xbMM6Xh9MGOqUBtCtMZgHjAJpkycdHx327YMuqxK9ic4G52mSjbJsFwnJSJm%2F8N2muDMEFnlmohiekSazJ7XCP9%2B087y4I3UIFmy%2FcooLt5GDQaY7SOzaad07hUPk57rVS8ZIxXo4Is8mZePQBm2xa3sCxVYFVTSg0mIM8tU9hu7U6BnNlY84nm3v9LlCNnu4sQHnRPZJuu9F%2FdJtsMGzNUPmu8X9vzx9yDoHuXTa%2F&X-Amz-Signature=ebf8b4708b765027b093cafae37a9467691e006febbab9b7b5bd5481ee3703c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







