



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYBDXVPI%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T125522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKOBMRf7WXKuwOnO4A0R9Y3TQnyh6KB%2BiQLOgxaWRkkwIgOaatJRi%2Fmi4g4YhYDkGDBNzX2N9Df1xgR5ztETulgusqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFdJXMF%2F9lPESh8b7SrcA21ekgNFUsQank2a%2F6rfKe%2FSckU2pnGOjycprGFEzTO8RgnSwHAbMOmY83JdcRiUgJW247tSrVDtKiRNTy46vmRCinIQD1%2BrthkE6w3DlezbX9b26w1DxMecMNL1Sbpe1uvGV1Kf5qCEcDU2j4zJXuWy%2FqI60uparPSBeugdFYkQ4Dgl5cIfru1ySlIlbrRF19BAUxwRg0VC1s435xh5rSF3P4lK4jGs6cQQhddBOKbJP%2FpQt0ldelt4GoLeQxZH2MHr2Z%2FsEM1XVcycfMgwzh45mkg4KYqe5bAJJf%2BQeeuygQaqgtOv3VfYPEZBSck7Vy6N1tIeH915OFX214VoIYsIyEw%2BtGfKpbWO3JlnpXMLdI%2FZjQvh0K3%2BG0RWT986lAqHKUHwDtQGo9KCperkZYhWvhEyn81peG5YaH6tszzt6GTDfNAt04xJwDTXg3Ucf4MHIPfXNFcpn7pIED1nRqy0mA7G6xypFOjdzGgDhI7NuqTQkY3qOcfZse4biM6fWsIl3TFhOsde4Ak12qlRAcuUSjVyeaXqn%2Fcx%2BU6Ijiq83I3bURybPiLQpAt4PNN23GN7C0fPHDj4Cl1BUaPGpHur61SOR28HnoK%2FfYkLjl8jfPmB4H4zCrNZx2ttMPjs5tMGOqUBSBRgsv2J37nqwc585kZolay2C8VePrRnNJgw1P7Erv2V9qjKRD6d6UFXClUMpglgZxlYQR%2BdWJPQ9iquvi%2Bt61yV7Kx9uvojQy9MVDLYzXnBqradPCfWnRdDTbypvYxxv%2FITGtbk16s1cvS007jGDnxUknoISuVq7wXjr7YMDpmew7ERBGwrIFS2GXdmnfyL%2FTb3k6AjISH35PH9%2BVZ5yBf4NLBs&X-Amz-Signature=fe394780626805a7bb7c925e672b34b2703508dc88be4ca3bb8751c63f5a06dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYBDXVPI%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T125522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKOBMRf7WXKuwOnO4A0R9Y3TQnyh6KB%2BiQLOgxaWRkkwIgOaatJRi%2Fmi4g4YhYDkGDBNzX2N9Df1xgR5ztETulgusqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFdJXMF%2F9lPESh8b7SrcA21ekgNFUsQank2a%2F6rfKe%2FSckU2pnGOjycprGFEzTO8RgnSwHAbMOmY83JdcRiUgJW247tSrVDtKiRNTy46vmRCinIQD1%2BrthkE6w3DlezbX9b26w1DxMecMNL1Sbpe1uvGV1Kf5qCEcDU2j4zJXuWy%2FqI60uparPSBeugdFYkQ4Dgl5cIfru1ySlIlbrRF19BAUxwRg0VC1s435xh5rSF3P4lK4jGs6cQQhddBOKbJP%2FpQt0ldelt4GoLeQxZH2MHr2Z%2FsEM1XVcycfMgwzh45mkg4KYqe5bAJJf%2BQeeuygQaqgtOv3VfYPEZBSck7Vy6N1tIeH915OFX214VoIYsIyEw%2BtGfKpbWO3JlnpXMLdI%2FZjQvh0K3%2BG0RWT986lAqHKUHwDtQGo9KCperkZYhWvhEyn81peG5YaH6tszzt6GTDfNAt04xJwDTXg3Ucf4MHIPfXNFcpn7pIED1nRqy0mA7G6xypFOjdzGgDhI7NuqTQkY3qOcfZse4biM6fWsIl3TFhOsde4Ak12qlRAcuUSjVyeaXqn%2Fcx%2BU6Ijiq83I3bURybPiLQpAt4PNN23GN7C0fPHDj4Cl1BUaPGpHur61SOR28HnoK%2FfYkLjl8jfPmB4H4zCrNZx2ttMPjs5tMGOqUBSBRgsv2J37nqwc585kZolay2C8VePrRnNJgw1P7Erv2V9qjKRD6d6UFXClUMpglgZxlYQR%2BdWJPQ9iquvi%2Bt61yV7Kx9uvojQy9MVDLYzXnBqradPCfWnRdDTbypvYxxv%2FITGtbk16s1cvS007jGDnxUknoISuVq7wXjr7YMDpmew7ERBGwrIFS2GXdmnfyL%2FTb3k6AjISH35PH9%2BVZ5yBf4NLBs&X-Amz-Signature=64d91d6ac294ab73dae3774b6cb6d9aadd75afe3514c7af460ede9738ab3ff51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







