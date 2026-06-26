



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTSC5EOY%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T085523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6o%2F7c94pWh0hQIGEJS3wf4alpl2QwsQHZ3et9n%2Fa6zAIgW4AqEEgXBZqSSMZ9OvVRU09J0%2F%2BxIAOG6dJGLad8jlEq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDOWTC8JJvgHPMFZviCrcAwNZcsGQGMgk0h47XjGUcCEQuclRKg%2F8qiHXYwGQ436LttGvv19iXYmMEnGVX%2BFQEKiMbmcKM%2FLHCh1GxELa16MVWRt94yvWlyy6MnGekXTqttVMfxYzwHOrhf8NeEidDzi7QiEUkE67vAs8faSwvZfqo%2Famv5H2TgCT2jidY1P8fpT6zEaVNv5bA41dF9L2uzjf9eTytZe2kRP8bROyPPDP3u2S9BjyTOw7Lww2d7CurU4MY20WHM8sU85PY3GVv%2FWSP3dE4pKGk50zAT76OvqOU8At685kd%2B%2FBmk0nk4zUf2MzcMRKcE1FfE4N7q32tHyAlhVsCNqrmdxyEGUA7X4%2B1U2mhlRuFZtU4CwUdtSLhnAorjSTnYswfMeGHoVgI7GBujJ8BCaDerJgYNbcK3khQSpujuCs9y7Nqy0jzo4ISoiHLuawCX2%2FSQPZLRw41nbuQR5DNHUCAm6UPIP7wkflmT3jFDkvghjdsmcYi%2BiwSaG98EQNh9oIjUKBlqEy3fokRmepA2Ww34%2BuoaFPUqW0yvI6M7qQRh1cWJ%2BCPh5hQBFxe%2ByFfM%2B645nUx%2BC9lUZj1YP98JsuXEVnx49l8fQFabFty1xaz9m%2BJc9WNh1kWfZ3ZeTE4dhWNF3bMNf1%2BNEGOqUBQonxoVerqRQC0Oi7fhO3UZdtc8aXVJggBosySlxcCOIoWYSk8PkPPftmDFKn6YIpu5YDrQey3oFW8sbqK97dhU%2BGR8xry7nsN9ZD8oEvBb2LtvdUrt0OfsB3rl830gfPGeoaZF2HcMIUIYhWxLHxjSxoiHpsLQidJibLZ7RXmSbJy%2BCJfXsCQFzJN1PY6I9cv382PYnlSoieJHpNh34S%2FqWjFIke&X-Amz-Signature=a658a9ae2a9c3d4eb0988f7012a9434c9cd4080df844d048b10949376c61ed9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTSC5EOY%2F20260626%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260626T085523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6o%2F7c94pWh0hQIGEJS3wf4alpl2QwsQHZ3et9n%2Fa6zAIgW4AqEEgXBZqSSMZ9OvVRU09J0%2F%2BxIAOG6dJGLad8jlEq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDOWTC8JJvgHPMFZviCrcAwNZcsGQGMgk0h47XjGUcCEQuclRKg%2F8qiHXYwGQ436LttGvv19iXYmMEnGVX%2BFQEKiMbmcKM%2FLHCh1GxELa16MVWRt94yvWlyy6MnGekXTqttVMfxYzwHOrhf8NeEidDzi7QiEUkE67vAs8faSwvZfqo%2Famv5H2TgCT2jidY1P8fpT6zEaVNv5bA41dF9L2uzjf9eTytZe2kRP8bROyPPDP3u2S9BjyTOw7Lww2d7CurU4MY20WHM8sU85PY3GVv%2FWSP3dE4pKGk50zAT76OvqOU8At685kd%2B%2FBmk0nk4zUf2MzcMRKcE1FfE4N7q32tHyAlhVsCNqrmdxyEGUA7X4%2B1U2mhlRuFZtU4CwUdtSLhnAorjSTnYswfMeGHoVgI7GBujJ8BCaDerJgYNbcK3khQSpujuCs9y7Nqy0jzo4ISoiHLuawCX2%2FSQPZLRw41nbuQR5DNHUCAm6UPIP7wkflmT3jFDkvghjdsmcYi%2BiwSaG98EQNh9oIjUKBlqEy3fokRmepA2Ww34%2BuoaFPUqW0yvI6M7qQRh1cWJ%2BCPh5hQBFxe%2ByFfM%2B645nUx%2BC9lUZj1YP98JsuXEVnx49l8fQFabFty1xaz9m%2BJc9WNh1kWfZ3ZeTE4dhWNF3bMNf1%2BNEGOqUBQonxoVerqRQC0Oi7fhO3UZdtc8aXVJggBosySlxcCOIoWYSk8PkPPftmDFKn6YIpu5YDrQey3oFW8sbqK97dhU%2BGR8xry7nsN9ZD8oEvBb2LtvdUrt0OfsB3rl830gfPGeoaZF2HcMIUIYhWxLHxjSxoiHpsLQidJibLZ7RXmSbJy%2BCJfXsCQFzJN1PY6I9cv382PYnlSoieJHpNh34S%2FqWjFIke&X-Amz-Signature=af2d2fd31074f2e1d3b05c5a77ecd6fefe3ec240a2bcf6af6f6ec22ef4b2f806&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







