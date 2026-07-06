



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VFS5YEA%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T100709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBggTUAgR5luD8b6hFrGo7sUFxsWZ42K00kDhjpeU1M6AiEAkcmIBWnEqdwWEQKra9%2BlKutmx1I2JPhyiUDZBDuNr4Eq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDF1hzqAHWvvXRfIsxyrcAz8XIjdpd0pDXulYiAW8%2FgZ3Q0gHgihqKFv2d3%2FRXqfiLiCGejV3vz7gugIb2Nfn9Si4%2F3pQZfEIoQCKEOH%2BJnCP3u2QQO4PybaO%2BH5O92S4MM1cr1hBZA7whlTBFnJ29XLWSUUQsfwYqoL2szut%2FABtko%2BqxIrRziK81U7J%2FpCTKGMlu5bTcYaqBkVsR0rmH8DM2yO%2F5t8rfMkfrNfMziYGUvtKNmJS5l%2FYmoKv%2FwcC5k8Tdo4%2B1zNlz6o%2FOx767Qn4pxts0UqgEhZ30eHC6krbZve1vEoUP%2Fdtad8grthr254GzPzI3qHr%2FuHpk77xFo87Pdx3hMpLsisGi%2BBRw%2B7HAaeuJdMPywMt33FTF5ElM9KSDdSfd9yF4E%2FwgRofdDS%2FrHWyPckXfngpbtp65lu4hDTK%2FphtaMgMYAitBpBLvveAXL76%2FQ%2Fap9V3gL5P6BcV65dN7SgUCa31MPCvc7kmrdxna3239%2BmbjkiqlbUr%2FbHZ3N%2FmEuFnZ01sjevLW1YolycM0g7A4bF3yqqh3bcMQIXQI%2BtpNFLnhrMXo7g96gDAfmQFLLGPmuirayUvjJOmqWy%2FI7yP8n3JY6qjEcLi179TrS0NgOyYsIUAITa7KNbDDqlbQtuBpskfMJ%2FLrdIGOqUBA95lklbyVtjSbejw%2FTeMIqWB67MPmRsZ3rFxzbjrtRNkSWBbChbE2b9CRr7a3v6Dsx04bZ%2BQK7TwAarkNtXsDQdGHP44tOmROYO3G9C%2FkASgiDqa9Oa2eLdIGqtEE951SBeQhuIZlbgk%2BJAYiSp4lldVR%2FGBDL1ydk5Z4oxOON9fsPaqs6o7NJVSW6tniui4c3tt8U7gocITFYFTvpC5BWEbsdq%2F&X-Amz-Signature=d4a47c89a424d02e14f5f03c85528de3dfe6cb939853eca09cd9a537b2cbdcca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VFS5YEA%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T100709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBggTUAgR5luD8b6hFrGo7sUFxsWZ42K00kDhjpeU1M6AiEAkcmIBWnEqdwWEQKra9%2BlKutmx1I2JPhyiUDZBDuNr4Eq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDF1hzqAHWvvXRfIsxyrcAz8XIjdpd0pDXulYiAW8%2FgZ3Q0gHgihqKFv2d3%2FRXqfiLiCGejV3vz7gugIb2Nfn9Si4%2F3pQZfEIoQCKEOH%2BJnCP3u2QQO4PybaO%2BH5O92S4MM1cr1hBZA7whlTBFnJ29XLWSUUQsfwYqoL2szut%2FABtko%2BqxIrRziK81U7J%2FpCTKGMlu5bTcYaqBkVsR0rmH8DM2yO%2F5t8rfMkfrNfMziYGUvtKNmJS5l%2FYmoKv%2FwcC5k8Tdo4%2B1zNlz6o%2FOx767Qn4pxts0UqgEhZ30eHC6krbZve1vEoUP%2Fdtad8grthr254GzPzI3qHr%2FuHpk77xFo87Pdx3hMpLsisGi%2BBRw%2B7HAaeuJdMPywMt33FTF5ElM9KSDdSfd9yF4E%2FwgRofdDS%2FrHWyPckXfngpbtp65lu4hDTK%2FphtaMgMYAitBpBLvveAXL76%2FQ%2Fap9V3gL5P6BcV65dN7SgUCa31MPCvc7kmrdxna3239%2BmbjkiqlbUr%2FbHZ3N%2FmEuFnZ01sjevLW1YolycM0g7A4bF3yqqh3bcMQIXQI%2BtpNFLnhrMXo7g96gDAfmQFLLGPmuirayUvjJOmqWy%2FI7yP8n3JY6qjEcLi179TrS0NgOyYsIUAITa7KNbDDqlbQtuBpskfMJ%2FLrdIGOqUBA95lklbyVtjSbejw%2FTeMIqWB67MPmRsZ3rFxzbjrtRNkSWBbChbE2b9CRr7a3v6Dsx04bZ%2BQK7TwAarkNtXsDQdGHP44tOmROYO3G9C%2FkASgiDqa9Oa2eLdIGqtEE951SBeQhuIZlbgk%2BJAYiSp4lldVR%2FGBDL1ydk5Z4oxOON9fsPaqs6o7NJVSW6tniui4c3tt8U7gocITFYFTvpC5BWEbsdq%2F&X-Amz-Signature=ca79a942b0e7899b37b098973118c09022cab0ae5f3c4652af0c058dc5e3e1b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







