



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KXQT3GH%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T071220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIHcrTOre2RNfqRuDlFNrARiH%2Bwnoywite3zscseBeeczAiEAgx6AZG0zwiK9Wq%2BzNGZWVx9zA0r8bPGxnROUu9C4eaUq%2FwMIABAAGgw2Mzc0MjMxODM4MDUiDAKINvvWp5wyPgV1dCrcAyfAz9phYH1MeGCqkTMnPxaXTocOUXzBrisZNRPXt6mG%2Fu266FH0pAa8oFasgvwF4m%2FHlcAKG6NFOYg0IUd5etaqsksbbIUR62u%2FPzqpQ77LE%2Bt5pIKgWSouc5vJwJaWmvllzv3BI6XURIzs8fid4yNUFVEvcJVf71sK7ttMsi6Ec%2FKeP%2B8iyMXsCfvpwnnrEd%2FvwldCML%2FZ84yz9YlzdIiKY%2Bt7zHsfHHSoqaC5d1lumGphkGBcwn5FgaLH3U%2FF6qPGc32plmzRKwQjH%2FcEA0VK1D3szSCOw4l0N4lZXK269gR5rdZj34pxa6iS%2FhPX9T6c25unf%2BwoYoSzNXfamWRoSwkH%2BqsTHmw2BNondDT3%2BHCPYRo70a6Aff%2B9iEDovql7asuHjqfGi9bCSWKnG6NKBWPAFOCnJ7SRdvM178u7KcDjK4qg8aQdzK1iAM6eh6VPyk6QpRtJB%2BaVqs3WJibabXnoBRIoWSGI7njibGHFyYZeZj%2FHycBl3UCsO37NBIMuB%2FB5BwgrHpMNl9bYIgtFHzewTocem4RHUId7r43J%2Bk1UkXasdAW2Zwl3iett23GsBHY%2FMTm7b6BDxldUDWT7E2JyVDx2WFIcuk%2FGCoF%2F2T5rNbSxim%2FEqlLeMN%2Frkc8GOqUB0dvE%2FFcwZMT4k%2F852WIwz0smakalX7vyS3KacOAcaOv9%2FX5AVkqvD7OVLOeWzXIUigXrw4b%2B0Fbkd1qkwDgrWIvfU9Q57O8ENM1g4NCayYB7CbNc52ZkXZZfSx68fzmhkBC8MvfFo7wwxC%2FMfZgrnJp5U%2FS54x3NhJJgEPyO3%2FPSsz9PaCPrtnxNX1sBqPL7gIUtvhQ%2BXETiE6XQ4pQn1xWEYvdH&X-Amz-Signature=216bd3ee2b3b0307b766029e77aaebc0e6acb2f6fc2c4bf39ffb0e95bc240415&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KXQT3GH%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T071220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIHcrTOre2RNfqRuDlFNrARiH%2Bwnoywite3zscseBeeczAiEAgx6AZG0zwiK9Wq%2BzNGZWVx9zA0r8bPGxnROUu9C4eaUq%2FwMIABAAGgw2Mzc0MjMxODM4MDUiDAKINvvWp5wyPgV1dCrcAyfAz9phYH1MeGCqkTMnPxaXTocOUXzBrisZNRPXt6mG%2Fu266FH0pAa8oFasgvwF4m%2FHlcAKG6NFOYg0IUd5etaqsksbbIUR62u%2FPzqpQ77LE%2Bt5pIKgWSouc5vJwJaWmvllzv3BI6XURIzs8fid4yNUFVEvcJVf71sK7ttMsi6Ec%2FKeP%2B8iyMXsCfvpwnnrEd%2FvwldCML%2FZ84yz9YlzdIiKY%2Bt7zHsfHHSoqaC5d1lumGphkGBcwn5FgaLH3U%2FF6qPGc32plmzRKwQjH%2FcEA0VK1D3szSCOw4l0N4lZXK269gR5rdZj34pxa6iS%2FhPX9T6c25unf%2BwoYoSzNXfamWRoSwkH%2BqsTHmw2BNondDT3%2BHCPYRo70a6Aff%2B9iEDovql7asuHjqfGi9bCSWKnG6NKBWPAFOCnJ7SRdvM178u7KcDjK4qg8aQdzK1iAM6eh6VPyk6QpRtJB%2BaVqs3WJibabXnoBRIoWSGI7njibGHFyYZeZj%2FHycBl3UCsO37NBIMuB%2FB5BwgrHpMNl9bYIgtFHzewTocem4RHUId7r43J%2Bk1UkXasdAW2Zwl3iett23GsBHY%2FMTm7b6BDxldUDWT7E2JyVDx2WFIcuk%2FGCoF%2F2T5rNbSxim%2FEqlLeMN%2Frkc8GOqUB0dvE%2FFcwZMT4k%2F852WIwz0smakalX7vyS3KacOAcaOv9%2FX5AVkqvD7OVLOeWzXIUigXrw4b%2B0Fbkd1qkwDgrWIvfU9Q57O8ENM1g4NCayYB7CbNc52ZkXZZfSx68fzmhkBC8MvfFo7wwxC%2FMfZgrnJp5U%2FS54x3NhJJgEPyO3%2FPSsz9PaCPrtnxNX1sBqPL7gIUtvhQ%2BXETiE6XQ4pQn1xWEYvdH&X-Amz-Signature=7b7b5e1580d3dee4c82ceec3348cc66cdb3cf22f103fa6d35f6bbb0e9208e1c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







