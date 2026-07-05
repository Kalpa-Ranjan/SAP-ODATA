



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PFE362L%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T084552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIC7eSLyD2wqHFjbFLrYkeY1OaqHTTJU1k%2BiQjMdg4Vu4AiB4YzEyFrSGd31N4ULDoa20zRfM4Fj6FECiQAiUo9FQiCr%2FAwg4EAAaDDYzNzQyMzE4MzgwNSIMEiH0WFL3VXbGp0NeKtwDPweFi32KOJifFGvKBLhkRoxtz%2BewksbT%2BNoduWUhqzfC4SR5yz3qYfYbXz%2BREPEj4ANSC%2BfpQNm2p7tDIH0PEarlcUS%2B9SYz0%2FfyEqKX0BJjPlW1L%2B%2B2jfS%2B%2BwqqtFnoc4ko0NojHdlOssAl6dMTLQFoOY1tAcS7GLQj%2FR3aupqH9oX6op8KwfGZ6QfsnmXpue4iTx0oiXcWOypwvnbsH6hrk42VXE6kVBTFKip0UXe0rwrnF0ueEvWWUpMt15tsxjwxfmTWZaYE1YA09ZiZ%2B3Ear4NanTZG6%2F4f69fP9mW1C5L6TC%2FOPc5H8H7ZNhJ3gN%2FPZkARIpmLrOX4Ox6wahHvrjA4Mj0wEiOLZ17PedogeJVKgMAsuKQZIG5wKN01CIjEBXv6yJc9xoso1dRKm7II0o%2B70LJ6d6boRshvoPL3KkHjgYQXedqYNSBWfFi8Y5hlNhInu4D8TjPi%2F30rO9onjnzFfm3W0AuRS%2Fn8RJBHuuutcl8kX%2Fd%2FJqrr9NSqTs%2FfpF8bjinXoEMrJfQatGO8N4Ahxpdj9IW6RQKulRyGXIoBItFEA2cVoK12Lp4BGqZTYNotyA36Hs7kwHpV7EkwLnS6iPTusjUlbcnX3uklioiu%2FgPHldWpIVYw5P%2Bn0gY6pgHlKyGvJevEzcPiA%2BGG36ylFi0cwe2moCYyspSK7mYXzoVhnKoVaFfv5SL%2F9U6UXfXEQnzEEbpl%2FheoP8kYw7ViBC%2BlflhURWwOVk7docXGy32A8OHM%2BVlpcf8AZtn13infkjimMD%2FACptuIXCXDPwBRdyj3WgX884VSO%2Bp1MrYM86DnU65zSk3gazxjgIqFr2JTZarL2hnVzKIygybfnblr%2FSa9c8B&X-Amz-Signature=1f9ba0065cd99eb8da6ca460078ac8fc6d074ba184aa35b92500507b16d29dee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PFE362L%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T084552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIC7eSLyD2wqHFjbFLrYkeY1OaqHTTJU1k%2BiQjMdg4Vu4AiB4YzEyFrSGd31N4ULDoa20zRfM4Fj6FECiQAiUo9FQiCr%2FAwg4EAAaDDYzNzQyMzE4MzgwNSIMEiH0WFL3VXbGp0NeKtwDPweFi32KOJifFGvKBLhkRoxtz%2BewksbT%2BNoduWUhqzfC4SR5yz3qYfYbXz%2BREPEj4ANSC%2BfpQNm2p7tDIH0PEarlcUS%2B9SYz0%2FfyEqKX0BJjPlW1L%2B%2B2jfS%2B%2BwqqtFnoc4ko0NojHdlOssAl6dMTLQFoOY1tAcS7GLQj%2FR3aupqH9oX6op8KwfGZ6QfsnmXpue4iTx0oiXcWOypwvnbsH6hrk42VXE6kVBTFKip0UXe0rwrnF0ueEvWWUpMt15tsxjwxfmTWZaYE1YA09ZiZ%2B3Ear4NanTZG6%2F4f69fP9mW1C5L6TC%2FOPc5H8H7ZNhJ3gN%2FPZkARIpmLrOX4Ox6wahHvrjA4Mj0wEiOLZ17PedogeJVKgMAsuKQZIG5wKN01CIjEBXv6yJc9xoso1dRKm7II0o%2B70LJ6d6boRshvoPL3KkHjgYQXedqYNSBWfFi8Y5hlNhInu4D8TjPi%2F30rO9onjnzFfm3W0AuRS%2Fn8RJBHuuutcl8kX%2Fd%2FJqrr9NSqTs%2FfpF8bjinXoEMrJfQatGO8N4Ahxpdj9IW6RQKulRyGXIoBItFEA2cVoK12Lp4BGqZTYNotyA36Hs7kwHpV7EkwLnS6iPTusjUlbcnX3uklioiu%2FgPHldWpIVYw5P%2Bn0gY6pgHlKyGvJevEzcPiA%2BGG36ylFi0cwe2moCYyspSK7mYXzoVhnKoVaFfv5SL%2F9U6UXfXEQnzEEbpl%2FheoP8kYw7ViBC%2BlflhURWwOVk7docXGy32A8OHM%2BVlpcf8AZtn13infkjimMD%2FACptuIXCXDPwBRdyj3WgX884VSO%2Bp1MrYM86DnU65zSk3gazxjgIqFr2JTZarL2hnVzKIygybfnblr%2FSa9c8B&X-Amz-Signature=7abe0594081159ad9378f23d90cd2b90614acc73a28d2d9d0032002f710888f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







