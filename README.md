



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OIKWX4K%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T022118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID0fL%2Fvgorpqz4sbFLaobHneFsCbkeUm4M44AWrp%2B1RnAiEArmcwKCAw8yXfzTtn6njboeDt1KTSmZ2pIDJKiyHpBG4qiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPA8pyfii0%2F08C7UNircA39EM0jTJwVYNDzJOcpKwkRhjS3bWQE20nIcScrzlsab4yZ3jYQRggtw1W%2Fhn3MgsAnp931rYldvYNXWZPIw0dLM1QjhBPgZ3GVYK08FusePW%2FDKFPc00se8FdQGzl21ZzegTyeKpuzBYRg%2BT0TV7qOTQNKFhYNSDg4a%2Fr%2BUZJZIYheOQ24h2Ajen88zOpcS0vF4ALv%2FzG5lN%2BYgMnaXuQBa1Ok71OmhL2aLyAL3duiVEc%2FKHeEFTmZ5mUaSZEMg6w338kvQkci7oovfvorm0z%2B7%2BJbcjgZtAxQvY%2FuJbElW1LGsICVukVNbbsmHkH8gyeaBuyfZ4lOGQApFk4woumxObNP5MYFWHrJjXdPs%2Bt7hzVPDFo%2FD5x%2FWwFnmY3r4Wg23ag1pLgIX%2Ftk2Z%2BqpKG6f1Y9zhjWZuiVD576epGq7Y3btmtYjd4ypEtK7UskJvIUOQfYI%2BFmi%2FvBvf8D9Svb6wcICFD4QKMl75JrqzNO%2Bzz9nsrDO9J%2BN7HTEGUEM%2FlcXupFyscCYKcSTDh9cSrS9f1YXMGeUyd0MDM6g3BpQFIDh38YPsGP2xhoJ4Xvq6tWBBljgvcBPNXSpLlau9xMkuqc7MEe0Ke98dgxHGa%2F435MtvSbXnxJ%2BYEXKMJqLtdMGOqUBH7au7qgow5eDF9mqy862Kj%2Fy8GYEkyptP%2FRrVXngn4WD2N7l9C65MqTTqYYP3jSMehOXn%2BYil8It1W7TSTVTvXxgLYbNY6PH%2FF6XzfK3YgIUz1R%2BXhQ%2F38tbzNJyi7Jbc9h0TfANL0ilErbkHpNSzaIUXMmyQ0BrLPjaL4PbD944BOM5GXdaApidD%2Bczh%2FQeCdxlOac44JyJJ9f4LkSLA0%2F5so3q&X-Amz-Signature=228e89fe165499a1324a1749349dfdc4320a96673d13d6e4bfd7c96f3d0fd4d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OIKWX4K%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T022118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID0fL%2Fvgorpqz4sbFLaobHneFsCbkeUm4M44AWrp%2B1RnAiEArmcwKCAw8yXfzTtn6njboeDt1KTSmZ2pIDJKiyHpBG4qiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPA8pyfii0%2F08C7UNircA39EM0jTJwVYNDzJOcpKwkRhjS3bWQE20nIcScrzlsab4yZ3jYQRggtw1W%2Fhn3MgsAnp931rYldvYNXWZPIw0dLM1QjhBPgZ3GVYK08FusePW%2FDKFPc00se8FdQGzl21ZzegTyeKpuzBYRg%2BT0TV7qOTQNKFhYNSDg4a%2Fr%2BUZJZIYheOQ24h2Ajen88zOpcS0vF4ALv%2FzG5lN%2BYgMnaXuQBa1Ok71OmhL2aLyAL3duiVEc%2FKHeEFTmZ5mUaSZEMg6w338kvQkci7oovfvorm0z%2B7%2BJbcjgZtAxQvY%2FuJbElW1LGsICVukVNbbsmHkH8gyeaBuyfZ4lOGQApFk4woumxObNP5MYFWHrJjXdPs%2Bt7hzVPDFo%2FD5x%2FWwFnmY3r4Wg23ag1pLgIX%2Ftk2Z%2BqpKG6f1Y9zhjWZuiVD576epGq7Y3btmtYjd4ypEtK7UskJvIUOQfYI%2BFmi%2FvBvf8D9Svb6wcICFD4QKMl75JrqzNO%2Bzz9nsrDO9J%2BN7HTEGUEM%2FlcXupFyscCYKcSTDh9cSrS9f1YXMGeUyd0MDM6g3BpQFIDh38YPsGP2xhoJ4Xvq6tWBBljgvcBPNXSpLlau9xMkuqc7MEe0Ke98dgxHGa%2F435MtvSbXnxJ%2BYEXKMJqLtdMGOqUBH7au7qgow5eDF9mqy862Kj%2Fy8GYEkyptP%2FRrVXngn4WD2N7l9C65MqTTqYYP3jSMehOXn%2BYil8It1W7TSTVTvXxgLYbNY6PH%2FF6XzfK3YgIUz1R%2BXhQ%2F38tbzNJyi7Jbc9h0TfANL0ilErbkHpNSzaIUXMmyQ0BrLPjaL4PbD944BOM5GXdaApidD%2Bczh%2FQeCdxlOac44JyJJ9f4LkSLA0%2F5so3q&X-Amz-Signature=ce2a6978c82600c319d8a846c14d8501f96c0a3a50a0489fec76231f76548b5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







