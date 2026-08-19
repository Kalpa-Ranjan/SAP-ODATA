



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW2VTQNB%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T182536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBwD%2FImFt9p2CmUG1gTbETjsKCT1g3ebeYagD7VRjjTmAiEA%2FSvcVgL%2BJ041UplUxmP9aJGajNlhPYGMhQ27P6Mirfoq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDJ3fNRdzXswmtvPQ8CrcA72%2BO7iTFc5He0C%2F%2BLNqG2alJ7Z4%2BYHRxkzdSVf%2BvkG%2F6bmYizX8WlYWyyBlsOLu5%2Bd1s0OHcGPByN4zDwEEupJmLxymnIqJz1hxTCrbVgmpf9zRPXuYeGh6jobfGU7j5JoJXHa5sakj0iLTVSonzkH6IHPRAfmec3m1Mgeok0beY4qETCdP5s7RVrnkKQF5cY84vxZGpHUzhDzd0RR5NxBcJ3Reqx%2FTCwGfgz9B3aTb0wY4mtSzt%2Fz7JNQ%2FwzcksqP1eE8riKtu6gclNbpoVmhbKk6KvOICvef%2BQrLoRtWnMNpcIn5xE8zQgIiMyLmlSRePGaw4d8cRgHqdEAUvqeQahPldHskmqnd0aEhFIYR7eLU8tHdIkO0m7A3UPRroZVNHxrtxq2sr5F6kUBB2%2FFTCos49OcFgTJfMS3Pa8wh95RgTt2EVY9yE7zpaTNv9J1s9vt1TK3szQ2W5j4qZhmqDOwTRBm9hX7BHKbqMiDWlj9NkzMbIjB5bhs1ARL94wCwvAmCqTVlzFEH8Q6mhTEeKh%2FDp7fkYrZ4O6EbRE8R2izkf4aGIy5DReEUXNn27yY3rmB4KrZBMfiW085fCMwH1erP5Bc9bwj%2BBQEf1C6zrxMJ%2BtKuD5l2HfiCRMITTl9QGOqUBNPDMkSEWd6AEZxT%2Bgy51e1EiIgT32Vgp%2B%2FY5Jcd4%2F5jCEAbS9RKU5NYQwaB%2BuJ4O8gL7XOccG9c7GQHNZXoD%2BiicanKQu%2B6BCqbIFE7oQY2%2BxqekwIM22L2hVIyfxhaORLtjwm6C5JP73WK2UB0al8uMUy85MqYh258me16pRo0Pajg%2BTLgizpIsEWnrzhe0RaqFc8%2Ba26gchVUR6qKiVb7KUeXh&X-Amz-Signature=8f1cd621ac1bfec42127992b754f2ab26be7305771c7f477e3f5d1874fc951aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW2VTQNB%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T182537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBwD%2FImFt9p2CmUG1gTbETjsKCT1g3ebeYagD7VRjjTmAiEA%2FSvcVgL%2BJ041UplUxmP9aJGajNlhPYGMhQ27P6Mirfoq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDJ3fNRdzXswmtvPQ8CrcA72%2BO7iTFc5He0C%2F%2BLNqG2alJ7Z4%2BYHRxkzdSVf%2BvkG%2F6bmYizX8WlYWyyBlsOLu5%2Bd1s0OHcGPByN4zDwEEupJmLxymnIqJz1hxTCrbVgmpf9zRPXuYeGh6jobfGU7j5JoJXHa5sakj0iLTVSonzkH6IHPRAfmec3m1Mgeok0beY4qETCdP5s7RVrnkKQF5cY84vxZGpHUzhDzd0RR5NxBcJ3Reqx%2FTCwGfgz9B3aTb0wY4mtSzt%2Fz7JNQ%2FwzcksqP1eE8riKtu6gclNbpoVmhbKk6KvOICvef%2BQrLoRtWnMNpcIn5xE8zQgIiMyLmlSRePGaw4d8cRgHqdEAUvqeQahPldHskmqnd0aEhFIYR7eLU8tHdIkO0m7A3UPRroZVNHxrtxq2sr5F6kUBB2%2FFTCos49OcFgTJfMS3Pa8wh95RgTt2EVY9yE7zpaTNv9J1s9vt1TK3szQ2W5j4qZhmqDOwTRBm9hX7BHKbqMiDWlj9NkzMbIjB5bhs1ARL94wCwvAmCqTVlzFEH8Q6mhTEeKh%2FDp7fkYrZ4O6EbRE8R2izkf4aGIy5DReEUXNn27yY3rmB4KrZBMfiW085fCMwH1erP5Bc9bwj%2BBQEf1C6zrxMJ%2BtKuD5l2HfiCRMITTl9QGOqUBNPDMkSEWd6AEZxT%2Bgy51e1EiIgT32Vgp%2B%2FY5Jcd4%2F5jCEAbS9RKU5NYQwaB%2BuJ4O8gL7XOccG9c7GQHNZXoD%2BiicanKQu%2B6BCqbIFE7oQY2%2BxqekwIM22L2hVIyfxhaORLtjwm6C5JP73WK2UB0al8uMUy85MqYh258me16pRo0Pajg%2BTLgizpIsEWnrzhe0RaqFc8%2Ba26gchVUR6qKiVb7KUeXh&X-Amz-Signature=ebe39a310c49aedf30f084c5e73928eff785215cf7fd3d5d20174ab17f906f66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







