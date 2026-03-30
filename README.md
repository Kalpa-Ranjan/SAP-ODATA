



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2YQMISZ%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T072042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCICUhnGpkO%2BnnvSSaFUdALY3o0%2FGUhzWmyHgYo8EvK86NAiA4aEo6clAeqp%2Byl%2FQ5say6h5fLGlglBWJe1fWAWFYA2Cr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMC6%2F%2F8pUUqlibKRcSKtwD%2B78MkgiNhwYzE6TxdA5Nr9RGkyvdp4RQab8Ej2i4ia6AJRydtlNTNlcMfvt%2FWsapNy76I7djO132dMNCHkUScBqieiawndk9LaeoWwNZ%2BXVK%2Fb%2Fxg3P4A5TdMTsEhw9lIZtf3LLVrWf%2FTdd3IyJyjzDznSdUZCH8AnGkf6a1lODOHvFgdubUs6yP2NsmrSbidCqaFQL5hlanhCS39TJJk6X2%2FvjKS1gMgFPLM%2F84q2PM9MZpxofMfxcyaFORcq7OrmsXzxakLtZfRDqHnfhE0AZTPjRPX2unkxGA6p7YXMMIg4VBTr5BIyqQdJcUu920lN0t3Mt1AAcKItK%2BFyVRJ0yuxRuSSeDGY7P9lmtqBI4jYenYQReEVH%2BQeZGE5fyJBUh2arSIgiAuceEQSsLbkSV%2FWd9KmAHe6rc6x8OdP6btC0GR5%2BbPdAtybMZYra5StkQ4jM%2BWrin%2BCJO11aqOQW9GbkmFGPGmEu%2BzuMB9wpz0TFkApv%2Blk9Hwnx%2BDENk6BIF7PdQNbgBGKOP2KuA3ZUfktAEWRccRu2a%2BXo15xwZfpcnmLTm0mU5tyqcwF9o7ncFYLfGz6eeIak0P%2BXkhJxUPhQcHSKno784O1WQx%2BnLY403ecde6NIW7%2FiIwrbGozgY6pgHo9iyO17x3MqqmNOPZsPnuXdCDY9kG6HKWlCPao27AYsXM%2B14bdyHQd1Uu2biFPe17XicyIGRWkA9DNweNLnzzH77kA7IfKxW1a76n2KDn89ouoyQkfRCm7Y4FgQXGBdL90rDoylaLr5jzfQz4wNhXDBy9zym4PpANsKtCN%2FUaFgeChmWYSLQyNgsYOWaFQmIP3wc7bKXiaPH9XY0IvyL65pbJLhve&X-Amz-Signature=bebc7136991d452d5569580128c53327ae469d18d87fa007bd1be94570e9a902&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2YQMISZ%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T072042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCICUhnGpkO%2BnnvSSaFUdALY3o0%2FGUhzWmyHgYo8EvK86NAiA4aEo6clAeqp%2Byl%2FQ5say6h5fLGlglBWJe1fWAWFYA2Cr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMC6%2F%2F8pUUqlibKRcSKtwD%2B78MkgiNhwYzE6TxdA5Nr9RGkyvdp4RQab8Ej2i4ia6AJRydtlNTNlcMfvt%2FWsapNy76I7djO132dMNCHkUScBqieiawndk9LaeoWwNZ%2BXVK%2Fb%2Fxg3P4A5TdMTsEhw9lIZtf3LLVrWf%2FTdd3IyJyjzDznSdUZCH8AnGkf6a1lODOHvFgdubUs6yP2NsmrSbidCqaFQL5hlanhCS39TJJk6X2%2FvjKS1gMgFPLM%2F84q2PM9MZpxofMfxcyaFORcq7OrmsXzxakLtZfRDqHnfhE0AZTPjRPX2unkxGA6p7YXMMIg4VBTr5BIyqQdJcUu920lN0t3Mt1AAcKItK%2BFyVRJ0yuxRuSSeDGY7P9lmtqBI4jYenYQReEVH%2BQeZGE5fyJBUh2arSIgiAuceEQSsLbkSV%2FWd9KmAHe6rc6x8OdP6btC0GR5%2BbPdAtybMZYra5StkQ4jM%2BWrin%2BCJO11aqOQW9GbkmFGPGmEu%2BzuMB9wpz0TFkApv%2Blk9Hwnx%2BDENk6BIF7PdQNbgBGKOP2KuA3ZUfktAEWRccRu2a%2BXo15xwZfpcnmLTm0mU5tyqcwF9o7ncFYLfGz6eeIak0P%2BXkhJxUPhQcHSKno784O1WQx%2BnLY403ecde6NIW7%2FiIwrbGozgY6pgHo9iyO17x3MqqmNOPZsPnuXdCDY9kG6HKWlCPao27AYsXM%2B14bdyHQd1Uu2biFPe17XicyIGRWkA9DNweNLnzzH77kA7IfKxW1a76n2KDn89ouoyQkfRCm7Y4FgQXGBdL90rDoylaLr5jzfQz4wNhXDBy9zym4PpANsKtCN%2FUaFgeChmWYSLQyNgsYOWaFQmIP3wc7bKXiaPH9XY0IvyL65pbJLhve&X-Amz-Signature=f3629447b23feead35788c2ed8c19125a631ea9ae8b91afd4f57d253ad4ef76e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







