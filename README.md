



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WN7LW7W%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T121114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAhlyXI2HL9vimPN%2FipB%2FN90Xcih8UbotiXE83FYcnZYAiAeUAF484MXq4Ani542rU0Qxs41x%2BboIX2Zekc%2Fv64hriqIBAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMN6n62u0M45zDLixDKtwDKCuARDHJ%2Ft9Vm8vE0dnTLyXxrzlOpHDvZjY67XC%2F4catOkxZA8tp0uv3YU5uxvcLMbXy%2FtFhoin0JSuPj%2FNt5tB2AFA0524tEyi%2FtU5lflWv3i8XnQYx4lR%2FqkoqW2kz6fwbfFqF3ApPaj0XKSWjT7%2BCHb9WGvflJEVBpmvo4NGrr7OwQ65Cf%2FVo2uMvT0gLzGXqstLttFtmubqhmMQwddZRnipXCJS7r0FbaLby6H6IWtL3CfTFmNhK4iq%2Fi%2FOLDDzZ4Yrl1pn%2FViJXs5mVWkAD%2BK7s9A29l6I0V0O1BZh65%2FF2eSnPceU%2FzzWw%2FAbTJgJXMLZldbtwzqZwB7Veciaev3gZrbSEg9bpm30bS1rF61Yc8CiRueYwBPqP8uUKGvEauRy88FsbxEKjB5rJ%2Blrwo26L8lqH2q%2B0F2pL6pyE2xyHycL1MsYsAW8CVa7aaW%2FglVdFyo5Jo3hOuJ2lLe8GQSnrDONqLD9qJfCxHWIMnVMdwZ1GoeeOqVw65zB09taMiSueP7UFO33%2BfNCpGZ0BP4PWUpgXLVrMDkGKIdlq4EvWi33L86Y0l7VKBN5VtG0IepDfTC5PjcnD2K1Hona4mWHyXLsKecLATslYe2LbFvEdTcK4lwI1yXswz8LI1QY6pgH9ZaFKJhYjdroN%2Fag4ZLRzULp076F700gJTOQj1622yxwLsOD29na6JA1rcKZ%2F6dX26tMPv36j7lzuo9Du%2FotQ6nyxnM2TK5RzCsY4%2BcLPmntG1jiQUKHnYytNEB8PdMRdJWm4eb5%2FqsDaQoU8vlmBE44WNaS0FVNUzhtiEmrgokZZdLC%2BunD9KQBZIzmw1NvvjYXU1BP%2B9Dydl0YKdy1yoedyjqwA&X-Amz-Signature=fe3e5093ec65900308b88a697ccc71a75eb431047bd293eaa9d33b3b466305d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WN7LW7W%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T121114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAhlyXI2HL9vimPN%2FipB%2FN90Xcih8UbotiXE83FYcnZYAiAeUAF484MXq4Ani542rU0Qxs41x%2BboIX2Zekc%2Fv64hriqIBAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMN6n62u0M45zDLixDKtwDKCuARDHJ%2Ft9Vm8vE0dnTLyXxrzlOpHDvZjY67XC%2F4catOkxZA8tp0uv3YU5uxvcLMbXy%2FtFhoin0JSuPj%2FNt5tB2AFA0524tEyi%2FtU5lflWv3i8XnQYx4lR%2FqkoqW2kz6fwbfFqF3ApPaj0XKSWjT7%2BCHb9WGvflJEVBpmvo4NGrr7OwQ65Cf%2FVo2uMvT0gLzGXqstLttFtmubqhmMQwddZRnipXCJS7r0FbaLby6H6IWtL3CfTFmNhK4iq%2Fi%2FOLDDzZ4Yrl1pn%2FViJXs5mVWkAD%2BK7s9A29l6I0V0O1BZh65%2FF2eSnPceU%2FzzWw%2FAbTJgJXMLZldbtwzqZwB7Veciaev3gZrbSEg9bpm30bS1rF61Yc8CiRueYwBPqP8uUKGvEauRy88FsbxEKjB5rJ%2Blrwo26L8lqH2q%2B0F2pL6pyE2xyHycL1MsYsAW8CVa7aaW%2FglVdFyo5Jo3hOuJ2lLe8GQSnrDONqLD9qJfCxHWIMnVMdwZ1GoeeOqVw65zB09taMiSueP7UFO33%2BfNCpGZ0BP4PWUpgXLVrMDkGKIdlq4EvWi33L86Y0l7VKBN5VtG0IepDfTC5PjcnD2K1Hona4mWHyXLsKecLATslYe2LbFvEdTcK4lwI1yXswz8LI1QY6pgH9ZaFKJhYjdroN%2Fag4ZLRzULp076F700gJTOQj1622yxwLsOD29na6JA1rcKZ%2F6dX26tMPv36j7lzuo9Du%2FotQ6nyxnM2TK5RzCsY4%2BcLPmntG1jiQUKHnYytNEB8PdMRdJWm4eb5%2FqsDaQoU8vlmBE44WNaS0FVNUzhtiEmrgokZZdLC%2BunD9KQBZIzmw1NvvjYXU1BP%2B9Dydl0YKdy1yoedyjqwA&X-Amz-Signature=a95731573ba1d312640507d0ea795f482d646d7f27e11f8df63be704b157ef1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







