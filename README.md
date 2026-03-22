



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QYI2N2X%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T015054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC67UxJEpC2sStiV313xzKsqDo%2Fc2tLIw1E%2BlrrgCmyDAIgdxuJT4IMENw7XDMggER3u%2BnW6aYeyXg74qOjsA%2By7s0q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDKUJCLTDAsKWHmxldCrcA6iD6SyieF7CnIcMj8meMUHQaoCIe4xsS%2FsDouCjmv1fpZPAa0MBDYtBCKszj%2BXVMDktpiET87DlzzvGvt%2BrY7zTABZrPmyYiC5hmRFJ7a4pslHukkYMAzHaHzB6dznDHRkyvkQjVJN1tijWDnZDBuHftiAqzg6tBY5PnQbXP0RjZiPSKgew21j%2FO0RreJDj3iAvaXROnpdjKnQiti55TES92JbB2YicGHv3PddQqxVNMxTBky9endrOx2bBlJuik6D4UFifdd4umtV37T%2FUcnSH7hQ7aHyT3GvM7QupZs4Lht5PBPjYpZyR5L%2FP7RDVkzgBEVvwgaiPSrsOx6MJoFCB1eOA2UY2S9q0BmN4TwmwrIA66lM9j3rSM7K%2FbbTSVfhh65BaC%2FZeNrAfMazZutJz0LlGlYquUYme3wecCJ53ix9%2Bo4j4oh75XcuLMs5vb4BsTPzNSVH8uo5NLlymh3rNz2%2Bj9dGlWEeWKp%2FfSTc7L1WCMPAN3CLr%2FoG14a8GJHerONlVV3Xq01F%2BQ28g6pcoDmNIRLa2WfMVKG9Yo1kC%2BpxzbUPX4vZVawrq%2BAGlocaky23TY%2BJezlniEk6KuE%2FbCONzbygX4n0hyd%2B5oLzCNIZa%2B02hn80P5TD1MOKI%2Fc0GOqUBYv7WeqJ0WlYfOpjchPlPZS5vaeAuiuo%2FwDij25E3f%2BZM%2B%2FS73m%2F5nUpLVvhwo2RC%2FrqGFRZaLD1TduzKKIEsON%2BSMTo%2FaC6ix3PvMVULGxq09Ma%2FQVup4bXQ2eGfmDBIIglKHw1Qh80NtwndhJWuHxQWUOnoFCYbX%2BU26kNlra2%2BgXms2oD76fFShUkKXbrThvIxAuL%2F10H7GkXA1ehlSlQ9Mquq&X-Amz-Signature=9d5b6691a344a4a3f638376e16adda6f00467d4f15e8a29aefa37bd837bd645b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QYI2N2X%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T015054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC67UxJEpC2sStiV313xzKsqDo%2Fc2tLIw1E%2BlrrgCmyDAIgdxuJT4IMENw7XDMggER3u%2BnW6aYeyXg74qOjsA%2By7s0q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDKUJCLTDAsKWHmxldCrcA6iD6SyieF7CnIcMj8meMUHQaoCIe4xsS%2FsDouCjmv1fpZPAa0MBDYtBCKszj%2BXVMDktpiET87DlzzvGvt%2BrY7zTABZrPmyYiC5hmRFJ7a4pslHukkYMAzHaHzB6dznDHRkyvkQjVJN1tijWDnZDBuHftiAqzg6tBY5PnQbXP0RjZiPSKgew21j%2FO0RreJDj3iAvaXROnpdjKnQiti55TES92JbB2YicGHv3PddQqxVNMxTBky9endrOx2bBlJuik6D4UFifdd4umtV37T%2FUcnSH7hQ7aHyT3GvM7QupZs4Lht5PBPjYpZyR5L%2FP7RDVkzgBEVvwgaiPSrsOx6MJoFCB1eOA2UY2S9q0BmN4TwmwrIA66lM9j3rSM7K%2FbbTSVfhh65BaC%2FZeNrAfMazZutJz0LlGlYquUYme3wecCJ53ix9%2Bo4j4oh75XcuLMs5vb4BsTPzNSVH8uo5NLlymh3rNz2%2Bj9dGlWEeWKp%2FfSTc7L1WCMPAN3CLr%2FoG14a8GJHerONlVV3Xq01F%2BQ28g6pcoDmNIRLa2WfMVKG9Yo1kC%2BpxzbUPX4vZVawrq%2BAGlocaky23TY%2BJezlniEk6KuE%2FbCONzbygX4n0hyd%2B5oLzCNIZa%2B02hn80P5TD1MOKI%2Fc0GOqUBYv7WeqJ0WlYfOpjchPlPZS5vaeAuiuo%2FwDij25E3f%2BZM%2B%2FS73m%2F5nUpLVvhwo2RC%2FrqGFRZaLD1TduzKKIEsON%2BSMTo%2FaC6ix3PvMVULGxq09Ma%2FQVup4bXQ2eGfmDBIIglKHw1Qh80NtwndhJWuHxQWUOnoFCYbX%2BU26kNlra2%2BgXms2oD76fFShUkKXbrThvIxAuL%2F10H7GkXA1ehlSlQ9Mquq&X-Amz-Signature=4d5b1fa9fe15963e65811b81de311455623b634be47bc7978709bba818a3e18f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







