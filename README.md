



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636PIXGL5%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T082756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQD89J%2FASGOwZ7s0fpndwW0kaWEitbmMuZv1K6rS%2FlXGegIhAMaO6IWmv2wYVTuSDxbHMV5XT9cE8H0uAum4bPXPvrj0Kv8DCAkQABoMNjM3NDIzMTgzODA1IgyFGMmjVFiC9TZfQy8q3APCoR5vQdMm7DqPm3Ty%2BQeaJRU%2FzsdTdxUk2xCvfj8SNw82kk3XdXnP1xuIb6eTSFqv5blVJCE0zVYJ55pCfmK0Dwgw9dM4HchfwjINtlTzUJp5Ti2N1aabWv3Sk3BZ5XRwuXRTDGOStrqOwj9973lcC5%2FpjLj23J8dcjebtuCShSxhUMbwQWH9ixF%2BmOZW0Cwe2A7vKGBSZfktzG8BeNWbPSCPO9fOISrS9UpJyDLePsiXQGoH%2BZxdPjXBOSr4EFST1aeKWNneWvHMaOeeB173Rc5tpFQJbn1bb%2FbHGaN%2F6zHfsGvwDArZ1Scb7BEiU7yjk786hOSrqBmM2pBIkglfCPZyGdStNEtMBYSpsocoBb7smrU%2F3u%2B28VUKgBett%2BOJF2EYdo8iWBj3isCdLIKArk%2FNY4g%2BIB5kAc6UlFcmcdsH3TIIHLRQ8G0AdSVEQazrdfZeVE9YniFHkg3nQkssK6w7TGK27ORJfrs0epX%2FZeQugPB0YSSo9aq73BMgtcqu5uoMFdkZzqYY52XeUjvJC%2Bl%2FHV4BpVNIyGbScQYAVcoz%2FVGEhFw2Oxim36g09RpNQ%2FtUEYU%2B3CVI5ab6pOKfnld7kYOmQPRhEysvTkLByAxNPbF3NbkmT4U1azD%2Fu8bTBjqkATGhvalpRuFzAvDCBAabadhLLeHMlawUM%2BCZ3JApWIXrsLQNRjF3wEzx5Hz3SThORsgFrVMixw09drXKZTPdpv7rk7bJv%2F9OjRqs75%2BIxVQeaGfPTIfsWwtNEwUp%2BSyX38YG0jvX91KgCz6UBS73IEoRTgZnk0cnWUoD8q1W4pGUmKkqpvuzHvpneaH%2FTFx%2F5dkz0%2Bxc4%2BrNX93%2B47PLpFkrKePN&X-Amz-Signature=86665e8292f0c7511a2801e4cc1b870246dbdd283f85a319bab2ca5b375885b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636PIXGL5%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T082757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQD89J%2FASGOwZ7s0fpndwW0kaWEitbmMuZv1K6rS%2FlXGegIhAMaO6IWmv2wYVTuSDxbHMV5XT9cE8H0uAum4bPXPvrj0Kv8DCAkQABoMNjM3NDIzMTgzODA1IgyFGMmjVFiC9TZfQy8q3APCoR5vQdMm7DqPm3Ty%2BQeaJRU%2FzsdTdxUk2xCvfj8SNw82kk3XdXnP1xuIb6eTSFqv5blVJCE0zVYJ55pCfmK0Dwgw9dM4HchfwjINtlTzUJp5Ti2N1aabWv3Sk3BZ5XRwuXRTDGOStrqOwj9973lcC5%2FpjLj23J8dcjebtuCShSxhUMbwQWH9ixF%2BmOZW0Cwe2A7vKGBSZfktzG8BeNWbPSCPO9fOISrS9UpJyDLePsiXQGoH%2BZxdPjXBOSr4EFST1aeKWNneWvHMaOeeB173Rc5tpFQJbn1bb%2FbHGaN%2F6zHfsGvwDArZ1Scb7BEiU7yjk786hOSrqBmM2pBIkglfCPZyGdStNEtMBYSpsocoBb7smrU%2F3u%2B28VUKgBett%2BOJF2EYdo8iWBj3isCdLIKArk%2FNY4g%2BIB5kAc6UlFcmcdsH3TIIHLRQ8G0AdSVEQazrdfZeVE9YniFHkg3nQkssK6w7TGK27ORJfrs0epX%2FZeQugPB0YSSo9aq73BMgtcqu5uoMFdkZzqYY52XeUjvJC%2Bl%2FHV4BpVNIyGbScQYAVcoz%2FVGEhFw2Oxim36g09RpNQ%2FtUEYU%2B3CVI5ab6pOKfnld7kYOmQPRhEysvTkLByAxNPbF3NbkmT4U1azD%2Fu8bTBjqkATGhvalpRuFzAvDCBAabadhLLeHMlawUM%2BCZ3JApWIXrsLQNRjF3wEzx5Hz3SThORsgFrVMixw09drXKZTPdpv7rk7bJv%2F9OjRqs75%2BIxVQeaGfPTIfsWwtNEwUp%2BSyX38YG0jvX91KgCz6UBS73IEoRTgZnk0cnWUoD8q1W4pGUmKkqpvuzHvpneaH%2FTFx%2F5dkz0%2Bxc4%2BrNX93%2B47PLpFkrKePN&X-Amz-Signature=29839f739e3a1438b6b00f94dd100fe852990fde55ace6f5b9c10b2b9ac71c43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







