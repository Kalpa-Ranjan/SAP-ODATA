



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CBJK7DH%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T072006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCKJjt6%2BbmzR8ZC35g3LgP8P3YLMSf3Uaxh03EojUDWWQIhAKmuwDwf4njXp7u4kxc7MQTsmlj4aMBnOf1Rp0C6vjj%2FKv8DCCgQABoMNjM3NDIzMTgzODA1IgwDDRGDwdIFcib1bFwq3AO7fCBOv5%2BoAXkgRsa7fzBx8jwR4Z9r5w3MWmpO7SADwvfNHIXXkjyxva9Lgc3fOC5N7HAGFeaB4aUiqoatTiQrJP%2Fy7CXfq2vTcam8kZkqtkn3bTuvWS9PqYMmM8B9oG6chJkxscbTtAl8OL%2FKl2uh%2B0t93VQalMiWiVrpNCqRBqJUQAg9Rjy78DR11adA048TM2qo5QnVGkwKK2cEJXceuSSfxSDJsBjo1VwD%2B7yOdYEPAjidgki1vywWNip2vOsHyt%2FCCvnRA%2B2JSBl8ccKfrtrXK8Vr0zvISO2GAHgUzCw612Oo%2BlYqI2Swylrvu1lyArpShpYkMskB9xjezFQEH0WgAKWSGodlRnuV%2FXStl1T1xCjZVwOwCUefnRIYRvJ0D9ydUWElEW%2FyGOMumHJWCwYrTgCwlpZIMdwuorAg3khzpkhxBijRBqvaiZX17yEEAEnn8E2QP6ijAAyy5BfeMYCH9V7KhAKhxrUHVB3iC91YgS7tC8siwSDcRyPPEk8qddftDXhXoU1CU3ighsagi9Y7pkAnp3JwhoWVfuWHe0Jd3TenPy%2Boxc%2BLTj2vN2B%2FOhfSNen%2BuPix3poaaK5%2B8jRZ2KuZ8qQK7ojGeZvniDZDXjqL83fY0i%2FGpzCLteLOBjqkAVpR8pbPw4pLZKVl3yo%2BMX6X0yqCfjbQKUBdcPaPjjBg%2FjOQ0UOJlIbAQ28X%2FzTyeaUxDrLf5IdXAHwKVR9tpYqvT1JDUkqMDfJO0E2CYNje%2B6AEWlMqzAZXk7a%2B1LWLQ1S10HKpSbORj%2FfUEg0KAarucTq0pNRxPocXXM5KxdoFhRKN8pK%2F9SYQ50KL67jEZvyJfVUAct6gYo94k0xFGYzxfbMD&X-Amz-Signature=02fc144d8bd09e25729a692d40e82d81215b369adc585b1d7248a48222085cff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CBJK7DH%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T072007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQCKJjt6%2BbmzR8ZC35g3LgP8P3YLMSf3Uaxh03EojUDWWQIhAKmuwDwf4njXp7u4kxc7MQTsmlj4aMBnOf1Rp0C6vjj%2FKv8DCCgQABoMNjM3NDIzMTgzODA1IgwDDRGDwdIFcib1bFwq3AO7fCBOv5%2BoAXkgRsa7fzBx8jwR4Z9r5w3MWmpO7SADwvfNHIXXkjyxva9Lgc3fOC5N7HAGFeaB4aUiqoatTiQrJP%2Fy7CXfq2vTcam8kZkqtkn3bTuvWS9PqYMmM8B9oG6chJkxscbTtAl8OL%2FKl2uh%2B0t93VQalMiWiVrpNCqRBqJUQAg9Rjy78DR11adA048TM2qo5QnVGkwKK2cEJXceuSSfxSDJsBjo1VwD%2B7yOdYEPAjidgki1vywWNip2vOsHyt%2FCCvnRA%2B2JSBl8ccKfrtrXK8Vr0zvISO2GAHgUzCw612Oo%2BlYqI2Swylrvu1lyArpShpYkMskB9xjezFQEH0WgAKWSGodlRnuV%2FXStl1T1xCjZVwOwCUefnRIYRvJ0D9ydUWElEW%2FyGOMumHJWCwYrTgCwlpZIMdwuorAg3khzpkhxBijRBqvaiZX17yEEAEnn8E2QP6ijAAyy5BfeMYCH9V7KhAKhxrUHVB3iC91YgS7tC8siwSDcRyPPEk8qddftDXhXoU1CU3ighsagi9Y7pkAnp3JwhoWVfuWHe0Jd3TenPy%2Boxc%2BLTj2vN2B%2FOhfSNen%2BuPix3poaaK5%2B8jRZ2KuZ8qQK7ojGeZvniDZDXjqL83fY0i%2FGpzCLteLOBjqkAVpR8pbPw4pLZKVl3yo%2BMX6X0yqCfjbQKUBdcPaPjjBg%2FjOQ0UOJlIbAQ28X%2FzTyeaUxDrLf5IdXAHwKVR9tpYqvT1JDUkqMDfJO0E2CYNje%2B6AEWlMqzAZXk7a%2B1LWLQ1S10HKpSbORj%2FfUEg0KAarucTq0pNRxPocXXM5KxdoFhRKN8pK%2F9SYQ50KL67jEZvyJfVUAct6gYo94k0xFGYzxfbMD&X-Amz-Signature=9ed5360b7e1adaa27e49bbda0f9f7330e4b775a1a239f12fb7d0b8070e5b1c9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







