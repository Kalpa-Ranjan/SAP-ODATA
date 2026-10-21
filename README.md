



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSNWEK7V%2F20261021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261021T061253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKzitefeZa3NSM0SiI1XnkYDHH3R63u%2BeWPgRqapM4UgIgDhXahEm6UWv5KKWnLFxgR6FnLpSkSPBkrtKybydAW2Mq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDHk44jGj1j283cnM3CrcA9o625oLcQFNygtQZfJx1XljEsvX2aVpB%2FtDLr1g6Zz6pbhl%2BR%2FMbmrWZr%2Ffy0x4UtiPR6qNIJZWtTRyxNIWFKZV1gTIP9IfSmmCd5bYtORGv4N%2BwaoqhIRF3i7ff8WFwnoO20GbOX%2FnNCBzIclydQ7fqWKDFazr81nb8%2FW7z3dQnEfRGWxYPFUhrLBMd68fTK8G6RSqeQAkpZsOxyIp6zUNfQ3CmvuGxZ6cW10YXgnywzxqV9msgKrFB89py6ugqhGxXPI7zKsptsjTSFzhT%2FQ4qw0aR0Ya2UfgcIkJsdZm1GB1Y4gORu0IJOHBgVQxhWulSB%2BizhlD18q3PyPcMlwiGI6H4okAIPVG5ZIoxOOEJ%2BsPA6xmBZ%2Fj%2FYQ2DC3Yyqqg9X6Ixzq7qMxIW%2FQ7OUf2xZ%2FUeuguWVka0q9qJgVs3%2FMeoPKEUMJB1J6M5cWcD9uyqrkB57VHtfe%2F4ZaBEMFVNeZmagBKFPs1phc0NrCgG%2FHFPi%2FG7a32%2FNdZ4Qz0TNrqumGU0vUIWAqLrIl9Sk3uvlk2eELE6i6rXAmQR1jZ0LZ73yavHFIUUPKpyjJZbAeQGBFWx%2B2SRTNiuGWRAZS%2FDyA6vT%2BmNU20B7xkhj3tvD00lhIGSqZWNherMICd4dYGOqUBWKjEahnUpPE9Eg8hwJ9aVbgzDpvb1R7Zcy2bgUsySX%2B9tHWBH0abTKJMfhkpdkCq5YNZb030vx4MIG2pIyvUyTxQcP8AZ6dm0wVODqW%2FLAndFKaTu3AkhsB03rWtrKeY3mQK%2B%2B4hhLhl7XcoJ5%2Fgm%2FfD3i1ROrBV1bVXcGItUzVESsJiTiqrwFszUqH%2Bt%2Fz5Tc4cM0TN%2B22LrqNMKhm%2BH4WfPJY3&X-Amz-Signature=548ed99f996a136f83b28126de679da26980d9c0aa9047a6e8fa8f12d9b05b14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSNWEK7V%2F20261021%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261021T061253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKzitefeZa3NSM0SiI1XnkYDHH3R63u%2BeWPgRqapM4UgIgDhXahEm6UWv5KKWnLFxgR6FnLpSkSPBkrtKybydAW2Mq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDHk44jGj1j283cnM3CrcA9o625oLcQFNygtQZfJx1XljEsvX2aVpB%2FtDLr1g6Zz6pbhl%2BR%2FMbmrWZr%2Ffy0x4UtiPR6qNIJZWtTRyxNIWFKZV1gTIP9IfSmmCd5bYtORGv4N%2BwaoqhIRF3i7ff8WFwnoO20GbOX%2FnNCBzIclydQ7fqWKDFazr81nb8%2FW7z3dQnEfRGWxYPFUhrLBMd68fTK8G6RSqeQAkpZsOxyIp6zUNfQ3CmvuGxZ6cW10YXgnywzxqV9msgKrFB89py6ugqhGxXPI7zKsptsjTSFzhT%2FQ4qw0aR0Ya2UfgcIkJsdZm1GB1Y4gORu0IJOHBgVQxhWulSB%2BizhlD18q3PyPcMlwiGI6H4okAIPVG5ZIoxOOEJ%2BsPA6xmBZ%2Fj%2FYQ2DC3Yyqqg9X6Ixzq7qMxIW%2FQ7OUf2xZ%2FUeuguWVka0q9qJgVs3%2FMeoPKEUMJB1J6M5cWcD9uyqrkB57VHtfe%2F4ZaBEMFVNeZmagBKFPs1phc0NrCgG%2FHFPi%2FG7a32%2FNdZ4Qz0TNrqumGU0vUIWAqLrIl9Sk3uvlk2eELE6i6rXAmQR1jZ0LZ73yavHFIUUPKpyjJZbAeQGBFWx%2B2SRTNiuGWRAZS%2FDyA6vT%2BmNU20B7xkhj3tvD00lhIGSqZWNherMICd4dYGOqUBWKjEahnUpPE9Eg8hwJ9aVbgzDpvb1R7Zcy2bgUsySX%2B9tHWBH0abTKJMfhkpdkCq5YNZb030vx4MIG2pIyvUyTxQcP8AZ6dm0wVODqW%2FLAndFKaTu3AkhsB03rWtrKeY3mQK%2B%2B4hhLhl7XcoJ5%2Fgm%2FfD3i1ROrBV1bVXcGItUzVESsJiTiqrwFszUqH%2Bt%2Fz5Tc4cM0TN%2B22LrqNMKhm%2BH4WfPJY3&X-Amz-Signature=395bf05c3e77d39df1ac84f37b1cff30ece9f4c03742dc0dbc8756b2404ba818&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







