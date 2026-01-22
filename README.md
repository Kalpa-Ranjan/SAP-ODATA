



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJIN7IVB%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T062750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCICo5PmUDUZB7OCTvhHQGC9G00eyUV97Yh6CJcbncAYHsAiEA7P%2By7EoijdKYmoCFwOsVflF58arJh%2FcERKggid3BNhQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIzLFccnodxrPk%2FIWyrcA%2FkA0m6HG1gJBOemDjXWMBlnEZJjTmtxnzyLUC0e86ljFpczmrahrTlDRNRhIWPFABcph8NgE%2Fg0GgK1WVbSCVOABggoyWPNnXBR15ikln87Qe9ajuC7rincwbpR%2F%2BweUtoIqezT%2Fo6LYkKtW5IqqexxclxrAKPiLOeZbUUbuKkUv3jRYDiFIbO1XzVzC0Qzaty6G0qtu6psS7o00T0QoFI3KYHTw%2F8vS90RQ58OO8MtZp0Vghg0BHperBrb8IbTp1Hg9t%2FCQIdSJ%2FJO8A8t7iIEMaw77hmMAJQQDd8T4Mgky6fe4B8jNat6b5BMcaCaWC1Nxx%2FoHcRb03qwuDaZ9Vm5%2FktNpIAusy0o6W1fpbIOCRVfdwwU17GcKRZZGRd1dD%2FCmZ%2BHxGt3AYpbUPTQc2%2F0I8i9xd5SAGKAxM9vSPXshSbdczvM7h6VWPjB8mu%2FrPwPHxt7i1bRVQXZmbbai0qx%2FXS3JmfWhbV%2Fn2wIik2A3gvP87vookrmCcEi%2FQN6LvdDLpZnC6Q7sxp0O174LQ8P6eprd7x0A95ym66ncYiiDH04jLXydtaGca9LKTsbRpC1gvIZqgcwn2pQkWyoBzWUEdoPHE4KSs2Rdcbhepv9Ls0rKH9oDx5u8%2BBzMLn2xssGOqUBTC9excTcNj24PZmfoFQVGZ010ka3dTFMfBUXzZ1LHKPcIqIypPV92fK%2Fjov3%2FrBajmga6rsrgrg4dODijyh%2B6%2BM%2FYxw%2F5WN58twyaGiaylebK9aVixXMSPVvrDuSgSmZJGTXrEz8IEOpptN13BmfL81daX%2F6lw9WVfr2sZ5jn%2BJfyO937nbLaELTCYQYTixKKe%2Fa0Mnoh8jV8zqKc%2BI1jsMiPX0d&X-Amz-Signature=c25832b4f0b4edd304c331b42811731850894ec7480afd3675a09e42b39bd914&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJIN7IVB%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T062750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCICo5PmUDUZB7OCTvhHQGC9G00eyUV97Yh6CJcbncAYHsAiEA7P%2By7EoijdKYmoCFwOsVflF58arJh%2FcERKggid3BNhQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIzLFccnodxrPk%2FIWyrcA%2FkA0m6HG1gJBOemDjXWMBlnEZJjTmtxnzyLUC0e86ljFpczmrahrTlDRNRhIWPFABcph8NgE%2Fg0GgK1WVbSCVOABggoyWPNnXBR15ikln87Qe9ajuC7rincwbpR%2F%2BweUtoIqezT%2Fo6LYkKtW5IqqexxclxrAKPiLOeZbUUbuKkUv3jRYDiFIbO1XzVzC0Qzaty6G0qtu6psS7o00T0QoFI3KYHTw%2F8vS90RQ58OO8MtZp0Vghg0BHperBrb8IbTp1Hg9t%2FCQIdSJ%2FJO8A8t7iIEMaw77hmMAJQQDd8T4Mgky6fe4B8jNat6b5BMcaCaWC1Nxx%2FoHcRb03qwuDaZ9Vm5%2FktNpIAusy0o6W1fpbIOCRVfdwwU17GcKRZZGRd1dD%2FCmZ%2BHxGt3AYpbUPTQc2%2F0I8i9xd5SAGKAxM9vSPXshSbdczvM7h6VWPjB8mu%2FrPwPHxt7i1bRVQXZmbbai0qx%2FXS3JmfWhbV%2Fn2wIik2A3gvP87vookrmCcEi%2FQN6LvdDLpZnC6Q7sxp0O174LQ8P6eprd7x0A95ym66ncYiiDH04jLXydtaGca9LKTsbRpC1gvIZqgcwn2pQkWyoBzWUEdoPHE4KSs2Rdcbhepv9Ls0rKH9oDx5u8%2BBzMLn2xssGOqUBTC9excTcNj24PZmfoFQVGZ010ka3dTFMfBUXzZ1LHKPcIqIypPV92fK%2Fjov3%2FrBajmga6rsrgrg4dODijyh%2B6%2BM%2FYxw%2F5WN58twyaGiaylebK9aVixXMSPVvrDuSgSmZJGTXrEz8IEOpptN13BmfL81daX%2F6lw9WVfr2sZ5jn%2BJfyO937nbLaELTCYQYTixKKe%2Fa0Mnoh8jV8zqKc%2BI1jsMiPX0d&X-Amz-Signature=e476291ef65fac8f44873e14477904db59e9950d38b492a9ffccbcc9d562a0f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







