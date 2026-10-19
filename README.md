



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQIQ5BS2%2F20261019%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261019T121230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDPGx67a3YTh5p5yffr9SFu%2BDRLhDE35d4BqQyQgA7ezgIgOjwU6DkfXkibMY4wRehZAjZyNcQbBUcXXoxIy3RNvr4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDH%2FBfRpsY%2B3bLq2%2BzSrcA7r6XxxlBmkS0V17Xf1gy8QxqmAwo9SrajRpiSMv0VHEmIeofE93AZeig8JKKeelsuPgT4Q6o2uZWxOs4xBR5R1ZrZvUn2qnxR75Xe7RzLEs7F4zqY%2Fl%2BEst2Hbtl2XzhGuQq7Eb9GSc8ROEAkpANLON9mpk%2FQB%2Fhi9ZEkBDNRKLRnrCPMHfKQHZXlQyjHcNh1N516n%2FMmlKQvZJL80KsrtdVTpWQtwwyQVTrs%2BTwG0mohPO8M2ZSR66Qjq7C78EAn4RNl4zVWSohIkSuSk3%2Bbgq5D7TimINLwyuI6BDoP1ivCdFx4Pq6OQOjW8HMxU%2BicCMSQQm0clshrYmLhpPsxIg8b0%2FW68lAvHT9j0orIBKdNo9cmQKWoJ%2FSEKlfG2k%2B6LIbxkMUeO1tn%2BUtCWH2YjY6l4vpZKzlIyrM2UnS%2Bnt9MJR%2BKT%2F%2B0ZdE3yaSujtdicN8NaI6VoBWGbYVg3Eiz53bYu7QGPePcVys47hSt4If59zpfzU7jOPr3Eqv%2Ft12SIzfyy5HtJiopmA7RFIb8jg9Q6YNDFqhZgob5%2Fx65LuYVULwIxrc9JRvXofCBklG8LCO73cL4DmqcQH9nJNUjx19P%2BGbPzvIn1ikEd8NaWTkzzJksk%2F80QFbB6tMJrM19YGOqUBIcJyCKsyNRPF9DK%2FR43csqYuSjwqHdTssF9N4od7r5rduDXhtK1RAvRCgpoQcflEsP46TRdHS%2FQjMex5I%2FEe4qcPIR74ZSDk3vLR%2Bk09lHTvZCmbd3%2F0k%2BrCr8p%2Fm1AiP%2FXML0r9toPJl5Huy%2FU1woz6pC7ATpOrlid2nzqT4%2F9q7K%2B3aV3IicCPFoWLr3JC5B2lqt%2FYfwhY6jsv6K0aXPViSBMC&X-Amz-Signature=b088cc5be8a37f7a4c3e6295a0f1c8d37fcfa579ece64a5ad5fc593b7ef9efb2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQIQ5BS2%2F20261019%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261019T121230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDPGx67a3YTh5p5yffr9SFu%2BDRLhDE35d4BqQyQgA7ezgIgOjwU6DkfXkibMY4wRehZAjZyNcQbBUcXXoxIy3RNvr4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDH%2FBfRpsY%2B3bLq2%2BzSrcA7r6XxxlBmkS0V17Xf1gy8QxqmAwo9SrajRpiSMv0VHEmIeofE93AZeig8JKKeelsuPgT4Q6o2uZWxOs4xBR5R1ZrZvUn2qnxR75Xe7RzLEs7F4zqY%2Fl%2BEst2Hbtl2XzhGuQq7Eb9GSc8ROEAkpANLON9mpk%2FQB%2Fhi9ZEkBDNRKLRnrCPMHfKQHZXlQyjHcNh1N516n%2FMmlKQvZJL80KsrtdVTpWQtwwyQVTrs%2BTwG0mohPO8M2ZSR66Qjq7C78EAn4RNl4zVWSohIkSuSk3%2Bbgq5D7TimINLwyuI6BDoP1ivCdFx4Pq6OQOjW8HMxU%2BicCMSQQm0clshrYmLhpPsxIg8b0%2FW68lAvHT9j0orIBKdNo9cmQKWoJ%2FSEKlfG2k%2B6LIbxkMUeO1tn%2BUtCWH2YjY6l4vpZKzlIyrM2UnS%2Bnt9MJR%2BKT%2F%2B0ZdE3yaSujtdicN8NaI6VoBWGbYVg3Eiz53bYu7QGPePcVys47hSt4If59zpfzU7jOPr3Eqv%2Ft12SIzfyy5HtJiopmA7RFIb8jg9Q6YNDFqhZgob5%2Fx65LuYVULwIxrc9JRvXofCBklG8LCO73cL4DmqcQH9nJNUjx19P%2BGbPzvIn1ikEd8NaWTkzzJksk%2F80QFbB6tMJrM19YGOqUBIcJyCKsyNRPF9DK%2FR43csqYuSjwqHdTssF9N4od7r5rduDXhtK1RAvRCgpoQcflEsP46TRdHS%2FQjMex5I%2FEe4qcPIR74ZSDk3vLR%2Bk09lHTvZCmbd3%2F0k%2BrCr8p%2Fm1AiP%2FXML0r9toPJl5Huy%2FU1woz6pC7ATpOrlid2nzqT4%2F9q7K%2B3aV3IicCPFoWLr3JC5B2lqt%2FYfwhY6jsv6K0aXPViSBMC&X-Amz-Signature=aa9e910bb96550ab1a6f71a98b566f9d730b93f1cf9b73e4593382101bd65fb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







