



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVY6ICLG%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T122752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQC5TqBmty4asnhy2acohr7AaDtCc%2FSLcWMpmHFDOAX1YQIhAI%2FgVagVFkjvGG9HplDEbpdaY6h1rb7D%2BHHFqaSYyvUZKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPu59GqWB1B9KvrXEq3APv3iMJEeXj%2F0bcmz5buyQPOH23gQXdtifQK1IpRtTqbdf1DtG2%2BTX4FkjqfXKkbDWwRy3zvS2smRu3mL2hsdVQp31bCUnC%2BNzVd1%2BKkMpvT20%2BaV4BzBmaL4icU9blXwhu%2BeBZ4gmb4jTY0ZSexPfirUcC8rZqpspSbIR%2FwVV4Z2qQwqSff4z6%2BuosZhn6jDMLqD4pfvhfIQocE%2FuUBUN6TwCS7BUKzKXU3CYOpW11tqEBVO1vIVbWe2pSQm9ARKeA1%2FmBf9g4pPcNPt6h8492dllity6g6y1kBDzxrDyvUtnXWMDcXTak1k6qX2aZI9xoA0KTCGGdumSj0Nuz53EhbL9bvrpn%2BbCUqRwLGOLSGkFrz1miSchHCg2cHP6ZsTGjXOWmC72uh8tM6uJeO64Gk1HrANKyoSxqxH2CzZDkOzYDTfFjwguGvsyDqxhzxxTgkP9%2BDK6gPHolSBXHPhM0KbSLnNOmHq7iDUcVGNwcBREpV2%2FfHpQRJZhB7WO9GbryZWRcbyuIvZJBNI6y3NWAAfvy0UKGAuycDivHrs7XrD8AuspAT2AELnZx6nhV9u2jKAgumfndXXVInFmamq3xLS8kTnyrat%2BnTPae8DhyghgzAF11MRj1QWaLzzD4oLzIBjqkAVruAmGM2CD1ZxJQRfsoiD5GMm4fWONu9UElrJDxOB0Kos2YQhZmAIlgwlWc1EvDaOJ%2B%2FJR%2Bz7MMbYZT6w7M93ivO5RXGjELti6RWsJS4WYA9fXnm49LKDBOKSp8ARi0w64zDG%2F7gCn2Gs444geDyvYz%2BxJ1MFU6VC7F8iI91fxLXgdnrQ6Y4lNws%2FD6iJg4Do4nlkSrMGvqZ3ZdCgJ9jCjccyRQ&X-Amz-Signature=9428f38aef4e6ad0cde48b79c2c411c2ae55237687d30afa4a36e10d74ec99ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVY6ICLG%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T122752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQC5TqBmty4asnhy2acohr7AaDtCc%2FSLcWMpmHFDOAX1YQIhAI%2FgVagVFkjvGG9HplDEbpdaY6h1rb7D%2BHHFqaSYyvUZKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxPu59GqWB1B9KvrXEq3APv3iMJEeXj%2F0bcmz5buyQPOH23gQXdtifQK1IpRtTqbdf1DtG2%2BTX4FkjqfXKkbDWwRy3zvS2smRu3mL2hsdVQp31bCUnC%2BNzVd1%2BKkMpvT20%2BaV4BzBmaL4icU9blXwhu%2BeBZ4gmb4jTY0ZSexPfirUcC8rZqpspSbIR%2FwVV4Z2qQwqSff4z6%2BuosZhn6jDMLqD4pfvhfIQocE%2FuUBUN6TwCS7BUKzKXU3CYOpW11tqEBVO1vIVbWe2pSQm9ARKeA1%2FmBf9g4pPcNPt6h8492dllity6g6y1kBDzxrDyvUtnXWMDcXTak1k6qX2aZI9xoA0KTCGGdumSj0Nuz53EhbL9bvrpn%2BbCUqRwLGOLSGkFrz1miSchHCg2cHP6ZsTGjXOWmC72uh8tM6uJeO64Gk1HrANKyoSxqxH2CzZDkOzYDTfFjwguGvsyDqxhzxxTgkP9%2BDK6gPHolSBXHPhM0KbSLnNOmHq7iDUcVGNwcBREpV2%2FfHpQRJZhB7WO9GbryZWRcbyuIvZJBNI6y3NWAAfvy0UKGAuycDivHrs7XrD8AuspAT2AELnZx6nhV9u2jKAgumfndXXVInFmamq3xLS8kTnyrat%2BnTPae8DhyghgzAF11MRj1QWaLzzD4oLzIBjqkAVruAmGM2CD1ZxJQRfsoiD5GMm4fWONu9UElrJDxOB0Kos2YQhZmAIlgwlWc1EvDaOJ%2B%2FJR%2Bz7MMbYZT6w7M93ivO5RXGjELti6RWsJS4WYA9fXnm49LKDBOKSp8ARi0w64zDG%2F7gCn2Gs444geDyvYz%2BxJ1MFU6VC7F8iI91fxLXgdnrQ6Y4lNws%2FD6iJg4Do4nlkSrMGvqZ3ZdCgJ9jCjccyRQ&X-Amz-Signature=12493894ecd36c68eb2ce9f7c3c85adbf6ba2bbb5377d382c89a733e359ffb02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







