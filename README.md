



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TSCM4QJ%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T014022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA4f%2F%2BzrZ2QDQ0Ypu2IUnafNm7xKPBWsj28EgdRYdpnuAiEA7lFkoniJlVEJ65y66qzssedHC7U5s4N%2BRdIA4Il%2FetgqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIiukX72PKMvhp03kSrcAwI88S%2Bb4c5QgsZwDVT%2Fi%2FTWcKlt4bvwFSP5fd7zwyKyc0b%2FqxmKl6tUWs0PKHc1EZCj9hwQ4Y7hmu8wd16adT0F9W7%2FiUsNipnOiSsWystbd1d3bv7aww7OAYsZm4wYBb%2BKQGrjeF%2FjBLus4XP%2F%2BYV%2FCC%2FGX9Uc7ZpI69BpXWd%2FNkMw2xiVHU4bw87sphK8BY9LxZ0Dl%2FB%2BqNfpW%2BD0jdzu0zYMkas34FBvgwWcWq1F%2BgXwOOdjP8nPOBa1ZCG0qjz0zcciNeDV5GlWG6uMax%2FIeQmte9HDECccg7z7LD%2FDFw9GitvoCEBBSO3tfTorl6ZusTD5JJm%2FUGPVSin2bhZ9HhWwzKRAd6vLkffSnv2owOs4RZYkUa0nmH%2FznqAugvd4TjMSZ6DhgrmRnxgcaAzel7AVasRm9a1RNzyjQHuxXzTBgw1%2F9XU8Op%2BxdBx2SRbIOIU7hDR7DLIdZ63yHmZNQPkzj2HMgBkZnmrZdy2Ffe4XSc0wTq4eyMp28%2F14qawz%2FjzG%2FM8zEX%2Fg37OWx9GDRMS8VDHpkqTHp1ZOHV0c%2Fv%2BSpuB3xdpX%2BsPf72xa3WA%2FuxO40ZyIBEmcaUo4Do3DklJqZ0X0vf4tRqUhFwlMkimn%2BaPmZD3CibDzMMO%2F48wGOqUBCXE4ygXzJ856VE3PzUWgrYJApQDCK5Kfo46ELnGFbKYeAwGdLF72AVNYDtlznnH0eEcCt4TEVdfi1r75Dvhz%2FOoIYaCIQK8VBdZM%2B23IzQs%2F0Ma37XNAaQVENLkWe%2Bb5er8%2FNeZfzI9bU%2Fx8acpEm92IwjWMIk21hl2LD%2Blchr02Kxnxg1%2FZ8p9SE0RJuc75kaiGlcdsB61sxAUXOss5MLnYy1O8&X-Amz-Signature=79239b58b0a1ff75bd9da9c90127fe270eaf76b12c9a967e9dd94e22c145b5ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TSCM4QJ%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T014023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA4f%2F%2BzrZ2QDQ0Ypu2IUnafNm7xKPBWsj28EgdRYdpnuAiEA7lFkoniJlVEJ65y66qzssedHC7U5s4N%2BRdIA4Il%2FetgqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIiukX72PKMvhp03kSrcAwI88S%2Bb4c5QgsZwDVT%2Fi%2FTWcKlt4bvwFSP5fd7zwyKyc0b%2FqxmKl6tUWs0PKHc1EZCj9hwQ4Y7hmu8wd16adT0F9W7%2FiUsNipnOiSsWystbd1d3bv7aww7OAYsZm4wYBb%2BKQGrjeF%2FjBLus4XP%2F%2BYV%2FCC%2FGX9Uc7ZpI69BpXWd%2FNkMw2xiVHU4bw87sphK8BY9LxZ0Dl%2FB%2BqNfpW%2BD0jdzu0zYMkas34FBvgwWcWq1F%2BgXwOOdjP8nPOBa1ZCG0qjz0zcciNeDV5GlWG6uMax%2FIeQmte9HDECccg7z7LD%2FDFw9GitvoCEBBSO3tfTorl6ZusTD5JJm%2FUGPVSin2bhZ9HhWwzKRAd6vLkffSnv2owOs4RZYkUa0nmH%2FznqAugvd4TjMSZ6DhgrmRnxgcaAzel7AVasRm9a1RNzyjQHuxXzTBgw1%2F9XU8Op%2BxdBx2SRbIOIU7hDR7DLIdZ63yHmZNQPkzj2HMgBkZnmrZdy2Ffe4XSc0wTq4eyMp28%2F14qawz%2FjzG%2FM8zEX%2Fg37OWx9GDRMS8VDHpkqTHp1ZOHV0c%2Fv%2BSpuB3xdpX%2BsPf72xa3WA%2FuxO40ZyIBEmcaUo4Do3DklJqZ0X0vf4tRqUhFwlMkimn%2BaPmZD3CibDzMMO%2F48wGOqUBCXE4ygXzJ856VE3PzUWgrYJApQDCK5Kfo46ELnGFbKYeAwGdLF72AVNYDtlznnH0eEcCt4TEVdfi1r75Dvhz%2FOoIYaCIQK8VBdZM%2B23IzQs%2F0Ma37XNAaQVENLkWe%2Bb5er8%2FNeZfzI9bU%2Fx8acpEm92IwjWMIk21hl2LD%2Blchr02Kxnxg1%2FZ8p9SE0RJuc75kaiGlcdsB61sxAUXOss5MLnYy1O8&X-Amz-Signature=84152983d0830e026018a2f33406ce59b48f590422a4b45f515ce5a494d5af90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







