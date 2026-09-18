



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6DZMRIJ%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T002031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCwHJDvZyjtd4aFgtJC8nc7N9Ma%2FO4bE2UBMRJHstk68AIgdTMTnmcrD6b%2BKvwM1IPXaMpM0TruEDIFBq9C5foFjnIq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDK%2FhooLVU7c%2BI6nfzCrcAzLUIeYa9q9JZ8v23ayEESQn69k4PBzzcBq7W8JRl%2BQKZOLOd4zhKYo3kn7NlO2zZUq4z2RgWL9wHIvwG%2FYkMKLwV%2BoRBj7dbHvCIqHKa%2F5wKTz8fxAf28lL1kst%2FBvxmMKPR7sOeHmWuyNWZkavRqIhqhbnyb5kont1ByjIsViimsGhInZ9KAUg2iSpzDm3FzOBmNA2oRfRzrSWLGgDlBpOqSPBMU5SIO6mDX0WBxEOqwWGVmj3kXjxAbF2v0MDBMekQpJb3u3uRDmq7TNxq8vLNeMLkrKZU5%2BHucoVYON8nldRlxYqy%2BHcIR2LqEZz%2BzqHaZeFn8ZCMyoOlaWT9FZWKJRedfd7rpuAIL50LCI%2BkC0u%2FK%2FOkeV8BlfkAg0irwd5sMufmih8uU0cTrGHkHe0pSj783OFY06XJeIiZ0O%2FSlk80gMFAvF4dqT9McyZiZeKhTuz1cPGgo9ROHWiZkBUD9tW6Thjnc%2Bg94%2BkY0U5gj00wVLxJAvg6Xqwc26jkIUScp5XN7tzrmxgcbhaH0W7wW7ikRdElZYMgbY2u3aUJ45mS6YcYWs%2BxhJrhIJ81VMP3N6Oe2pms5Cpt2SfaWbZAEKLEijTg70BesU94YzCjqyUjvpdcHvdCxwcMPbjsNUGOqUBavDW%2FTH%2FCdIZzWX6SrUNOU73x9EgIVc8pQCWCMoQ%2FNTlzbFMzxGE%2BhVs7e1jGFO3XKh1ivlj%2BWm2hCnrwW%2BLd%2FRm0yTOk%2FDXA%2F5bBfy7BN1K%2FPU2BgLSc5wL0Jc%2BHai5B7w8%2BRFxp8A73V9qJUFKY3ojpHME5nqaIqzRcqwBEz5WxjHlM2xDJNii3R8q3p%2FtPODPMnisoywdrRDpcaPXlz9LgbX%2B&X-Amz-Signature=6a36029e8b89e430fd6c81aaaf5bddd6fdcce0bd0c0200b817b9b653885ee107&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6DZMRIJ%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T002031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCwHJDvZyjtd4aFgtJC8nc7N9Ma%2FO4bE2UBMRJHstk68AIgdTMTnmcrD6b%2BKvwM1IPXaMpM0TruEDIFBq9C5foFjnIq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDK%2FhooLVU7c%2BI6nfzCrcAzLUIeYa9q9JZ8v23ayEESQn69k4PBzzcBq7W8JRl%2BQKZOLOd4zhKYo3kn7NlO2zZUq4z2RgWL9wHIvwG%2FYkMKLwV%2BoRBj7dbHvCIqHKa%2F5wKTz8fxAf28lL1kst%2FBvxmMKPR7sOeHmWuyNWZkavRqIhqhbnyb5kont1ByjIsViimsGhInZ9KAUg2iSpzDm3FzOBmNA2oRfRzrSWLGgDlBpOqSPBMU5SIO6mDX0WBxEOqwWGVmj3kXjxAbF2v0MDBMekQpJb3u3uRDmq7TNxq8vLNeMLkrKZU5%2BHucoVYON8nldRlxYqy%2BHcIR2LqEZz%2BzqHaZeFn8ZCMyoOlaWT9FZWKJRedfd7rpuAIL50LCI%2BkC0u%2FK%2FOkeV8BlfkAg0irwd5sMufmih8uU0cTrGHkHe0pSj783OFY06XJeIiZ0O%2FSlk80gMFAvF4dqT9McyZiZeKhTuz1cPGgo9ROHWiZkBUD9tW6Thjnc%2Bg94%2BkY0U5gj00wVLxJAvg6Xqwc26jkIUScp5XN7tzrmxgcbhaH0W7wW7ikRdElZYMgbY2u3aUJ45mS6YcYWs%2BxhJrhIJ81VMP3N6Oe2pms5Cpt2SfaWbZAEKLEijTg70BesU94YzCjqyUjvpdcHvdCxwcMPbjsNUGOqUBavDW%2FTH%2FCdIZzWX6SrUNOU73x9EgIVc8pQCWCMoQ%2FNTlzbFMzxGE%2BhVs7e1jGFO3XKh1ivlj%2BWm2hCnrwW%2BLd%2FRm0yTOk%2FDXA%2F5bBfy7BN1K%2FPU2BgLSc5wL0Jc%2BHai5B7w8%2BRFxp8A73V9qJUFKY3ojpHME5nqaIqzRcqwBEz5WxjHlM2xDJNii3R8q3p%2FtPODPMnisoywdrRDpcaPXlz9LgbX%2B&X-Amz-Signature=21fc6fc4e8161a7354157a3d87b2b046e987e1029fa4bec2a23d8e56f749526a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







