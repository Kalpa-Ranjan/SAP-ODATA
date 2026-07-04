



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKIEKZY7%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T190221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIHUA5ZozFWJgVmm7AWJH%2F9gjY3fnhxUlodHPocp3PdhPAiEAq%2FooUdg8EANN%2Bkkoz9N%2Bu0%2BYZu3mjgLkwLTjgFD6lJoq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDLsxSrYNLxy1cPtyhSrcA3hB8L4Y0HwNazXm6NZZ7b7xdzI196%2FxhvJ9tYLz2PHK2SMCL0GZOoC1SL%2BpZGxDyFDf7NxPriOWDOYx5fidA2m9QNuqWDJ8X%2FmCaTVblfbju0yXgZDsbTueSebJtYIPGtmt35CcayE7%2FjGet3veuolQIRIEidQIzoVZZ%2FrMOggafwaDCLA60COhkK8AAic1Po8oMRYOw9ijBfRUGCpRgokbtnBsuhk4J9exzLKuj3uM80hWNumw4NVR5V0MNuB5Nz6YFqrZkxAdO7U7Ajn8LCVzRSrcDVbMv6h%2BmOs5LvRFvsRQvpYgTGnY9LAu8T6a7PTVHbAx3W2HhMEkPAub1Dnf%2FDBy52VKtJQXUWq219jA%2B2zNS7JrSrMlNlM8UpUbQOGlxxqMpRO2SNnrtX%2F0Jv83y6k5op6RCJbQhRnu%2B8xs77aFwAWC3P6ZrX1rCDnE7orjgk1jsbKHp76PhDeWelGSSNGC64aOILllAIZn%2F9iiNHUYDh9Xd3pvWFR3xYbcZqm%2BnYFs55wLQZjk6BJTRYaNPdACKbkXFZxmGKb8Tjh6ooadc1ShIB5m0oX6uMFMKlBOqvuRBnYzwhoq0HixJ3ag6gMR%2FvW0aB2KP9qpk%2FYzjetnGKTEmKo9Jr28MKj9pNIGOqUB9L%2FiSDWqTBchqr9IRAeT5DHGr0RN6IJCh%2F8I5%2FNLLNw5IB3PxBSyLJdexw3I6zW2Ne0M8dRL2eO1KXIaSMkFr5yBETB66vI3lhWYAhTw2glbraY2NsB17NLMHFfL1wWKGJWRKY%2BShCROCdqlSd0KxjCLRTIQubu3cTLP0LgghdEhRalVX4I9LxUf9NN0dePjACFungrEF%2FVxEw%2BKyhZDB6haAtBS&X-Amz-Signature=565b0f1a464938454a9967efdb23d188dfd1ef14f3a5082231bce8c00a8dcb35&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKIEKZY7%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T190221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIHUA5ZozFWJgVmm7AWJH%2F9gjY3fnhxUlodHPocp3PdhPAiEAq%2FooUdg8EANN%2Bkkoz9N%2Bu0%2BYZu3mjgLkwLTjgFD6lJoq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDLsxSrYNLxy1cPtyhSrcA3hB8L4Y0HwNazXm6NZZ7b7xdzI196%2FxhvJ9tYLz2PHK2SMCL0GZOoC1SL%2BpZGxDyFDf7NxPriOWDOYx5fidA2m9QNuqWDJ8X%2FmCaTVblfbju0yXgZDsbTueSebJtYIPGtmt35CcayE7%2FjGet3veuolQIRIEidQIzoVZZ%2FrMOggafwaDCLA60COhkK8AAic1Po8oMRYOw9ijBfRUGCpRgokbtnBsuhk4J9exzLKuj3uM80hWNumw4NVR5V0MNuB5Nz6YFqrZkxAdO7U7Ajn8LCVzRSrcDVbMv6h%2BmOs5LvRFvsRQvpYgTGnY9LAu8T6a7PTVHbAx3W2HhMEkPAub1Dnf%2FDBy52VKtJQXUWq219jA%2B2zNS7JrSrMlNlM8UpUbQOGlxxqMpRO2SNnrtX%2F0Jv83y6k5op6RCJbQhRnu%2B8xs77aFwAWC3P6ZrX1rCDnE7orjgk1jsbKHp76PhDeWelGSSNGC64aOILllAIZn%2F9iiNHUYDh9Xd3pvWFR3xYbcZqm%2BnYFs55wLQZjk6BJTRYaNPdACKbkXFZxmGKb8Tjh6ooadc1ShIB5m0oX6uMFMKlBOqvuRBnYzwhoq0HixJ3ag6gMR%2FvW0aB2KP9qpk%2FYzjetnGKTEmKo9Jr28MKj9pNIGOqUB9L%2FiSDWqTBchqr9IRAeT5DHGr0RN6IJCh%2F8I5%2FNLLNw5IB3PxBSyLJdexw3I6zW2Ne0M8dRL2eO1KXIaSMkFr5yBETB66vI3lhWYAhTw2glbraY2NsB17NLMHFfL1wWKGJWRKY%2BShCROCdqlSd0KxjCLRTIQubu3cTLP0LgghdEhRalVX4I9LxUf9NN0dePjACFungrEF%2FVxEw%2BKyhZDB6haAtBS&X-Amz-Signature=d02f5f941ed4806e9a84e69be178ed3d28406bb37309500c221ca44f4be21b96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







