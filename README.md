



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHJLEJ27%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T014209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQD18oxwFFvqDsHo4BH7e0laX5ho9osxvLg%2Bjm3Cvha3XwIhAILrXngwK2ERA7LJ1oQGMmDPP9NnVGSvbQKVDs8ApJHFKv8DCAoQABoMNjM3NDIzMTgzODA1Igz48RpBVfmAXwQ61W4q3AN6ijrc%2FNhaovbiQcGIGYJFoiPsGd5k20OTNu6C3%2BeL461V809L3YJAllHLkf6KE2EbCDQzS5s87peb08j%2B1X5V4RC2%2BUloMcG97tdXW65ZqqHSZNEgg%2BefX4zQh6c1I3JXNEyWANOyu1kGVPWxCZq7OdXZBsscG7MIamclx3D37HL78cm9i6sEe8l7CfFiNotAbTcgSRI7fYFWqWBivGLdlKpm%2BheFOP0ntfbr1Rt5xi1gaMES9H4jMtHusyCTwTLX08%2Fysk%2Bd9CHSF1qooL4lallBsRYAE9RF9T261U86r%2F2aEi9xk5jkXCTYMjUoqoiKVzfAl5WdbLQxLeEUGewcJ%2BecXkkKFC00iZoQwAfSl7ieZ2%2F4m%2BmE9YsSmrRlZAgNXoe7i3YoW6se4mjC5u9oDIy5kWqsB8aWm4sgA8087fK9QHc%2BIM5vyNerzWAUKWtNalD7%2BPtXJZp2p2X0TJJIsnFfgNEAQZu%2BdBW2qdbpJtjU7f1j%2BYpjPp%2FquV2l8Qov%2BfelnCxPf98llwvKbRz6o7YP3AXETtX%2BKKgesaS4jq42SsyUv%2FlE1cHXpQWd%2Bnxo9LaN5luwP9H3O5YMjvBaEvjDEvdiKNzoUE3w6I0qbwTwQe3sVbuNnugbZTCuqIrMBjqkATQwHGJh6j%2BtFl6eIRi74StEnWCgYQMpFd3dMZK2NbDROZZJWTooRjKnnEsD62FWiPjBCvPMiXFXVCKJUzd17JqLhhd5wVYwheo3g%2FBuNA7kQdueONlT6REYisjUhAdkhJfXE4AZTnZPJK2aVXB4ieQBZvQXdFnp8ZUPvHDrOQ%2F2lEIoKEhDnuT3Y2wKh2o4wrEpG0kqSX8V66tHZWWsVeyA32pW&X-Amz-Signature=032a867b5e57b782fc164c5d9ae5b8683a82fb8235bd9078d6724c73f437e6f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHJLEJ27%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T014210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQD18oxwFFvqDsHo4BH7e0laX5ho9osxvLg%2Bjm3Cvha3XwIhAILrXngwK2ERA7LJ1oQGMmDPP9NnVGSvbQKVDs8ApJHFKv8DCAoQABoMNjM3NDIzMTgzODA1Igz48RpBVfmAXwQ61W4q3AN6ijrc%2FNhaovbiQcGIGYJFoiPsGd5k20OTNu6C3%2BeL461V809L3YJAllHLkf6KE2EbCDQzS5s87peb08j%2B1X5V4RC2%2BUloMcG97tdXW65ZqqHSZNEgg%2BefX4zQh6c1I3JXNEyWANOyu1kGVPWxCZq7OdXZBsscG7MIamclx3D37HL78cm9i6sEe8l7CfFiNotAbTcgSRI7fYFWqWBivGLdlKpm%2BheFOP0ntfbr1Rt5xi1gaMES9H4jMtHusyCTwTLX08%2Fysk%2Bd9CHSF1qooL4lallBsRYAE9RF9T261U86r%2F2aEi9xk5jkXCTYMjUoqoiKVzfAl5WdbLQxLeEUGewcJ%2BecXkkKFC00iZoQwAfSl7ieZ2%2F4m%2BmE9YsSmrRlZAgNXoe7i3YoW6se4mjC5u9oDIy5kWqsB8aWm4sgA8087fK9QHc%2BIM5vyNerzWAUKWtNalD7%2BPtXJZp2p2X0TJJIsnFfgNEAQZu%2BdBW2qdbpJtjU7f1j%2BYpjPp%2FquV2l8Qov%2BfelnCxPf98llwvKbRz6o7YP3AXETtX%2BKKgesaS4jq42SsyUv%2FlE1cHXpQWd%2Bnxo9LaN5luwP9H3O5YMjvBaEvjDEvdiKNzoUE3w6I0qbwTwQe3sVbuNnugbZTCuqIrMBjqkATQwHGJh6j%2BtFl6eIRi74StEnWCgYQMpFd3dMZK2NbDROZZJWTooRjKnnEsD62FWiPjBCvPMiXFXVCKJUzd17JqLhhd5wVYwheo3g%2FBuNA7kQdueONlT6REYisjUhAdkhJfXE4AZTnZPJK2aVXB4ieQBZvQXdFnp8ZUPvHDrOQ%2F2lEIoKEhDnuT3Y2wKh2o4wrEpG0kqSX8V66tHZWWsVeyA32pW&X-Amz-Signature=91252a9bb84db5bb55ced2664f5839c472782bf10bd30f8a97c2bddd9aa0dca4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







