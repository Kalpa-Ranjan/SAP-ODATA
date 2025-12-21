



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCQQM5UW%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T012132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIFmQRhT8dr5P14dGT9bUL4YYiXGOZU6%2BstHS8PAuL8YmAiBfy5to8RbT41J4Pl5sErr1E79LXM0zF9u0CpVsoE4bTCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIBv2ASy0XMosWFidKtwDjorThAAaB%2BpICLDAu1k6WdX%2BqZqXH2THzphgjWRgWbogxwbABWMnpt%2FpVGianYNF6YGPh6pejRDenkmDBeV6qw0HRizRh8pF0g%2B%2FDg4WCtYOySgXy0VM8FfkBJdGQAOBVVvmokDRIvTignQKTPaCrdBRDpfz1W7inhTOKt0PZBbEydSnjPF%2FqxabXjBrV2HtouYQXwS%2Bar7objzRKLF%2F4uq3QJ5n5aVcFUa%2Fm4lM0ORAwyAuwat0P7yX6qstCIO4gcgJgWDnm%2FbSZhx3rX7o7E8%2BB%2FGaoLOUgC2P8J2p4I2dnGR4eVeeQEC1dd%2B5bO0YkHw6rGSOaducm8Ur9sm%2FPp54PfYZp8mMZgsydXWKQKwFA0DTHkR%2BUvnGVDvx%2FnCHFnPwvPI%2FHC%2BNXGnXxA1Jzug3S8HdOkF%2F2d0wz54RBQwic%2BAx%2FHvwBx4wc8iIedW8QTX7jnAJwoX%2Fe5WJZHWavtpZeP5brMticTMKlEyp5WXlwODmLnDCafenc8kqiZD9K8MIj8mVRmZVAkfNecMhseEx8Oh2F5Qoq1SIXhwnNIeEutXtUIqcAOgcOZihF83zouMsTmHNEs0iwfGpZhf3Q11RPH5zWLJPma1DJ61SKipibXDvzp3W307eWJcwr%2FicygY6pgEUhK4Ry0gmcADuEpoUiDxVK6ZgFXU4s%2BQu8mHdldtdMaFE0fIqZRRftAzUeLlJFSircVNzEVmQYA%2FIQ%2FngQoRDGgDBI%2FUIdWF8xEOW7bnmfupdfKRYcEnE9Qv%2BqOPyFyiiL8FF9SDme9awEYS7x8sRpRc097OmOcdfz%2Fg%2B2gNnsFejFVsHxW5doL4II8%2BdES%2F4MKfg0LAEPoZg671ccaHvUyMEPvdc&X-Amz-Signature=fee71bd9f1a9b633ec19a61b7222420fe85c069195004c046dce42cec68e6822&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCQQM5UW%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T012132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIFmQRhT8dr5P14dGT9bUL4YYiXGOZU6%2BstHS8PAuL8YmAiBfy5to8RbT41J4Pl5sErr1E79LXM0zF9u0CpVsoE4bTCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIBv2ASy0XMosWFidKtwDjorThAAaB%2BpICLDAu1k6WdX%2BqZqXH2THzphgjWRgWbogxwbABWMnpt%2FpVGianYNF6YGPh6pejRDenkmDBeV6qw0HRizRh8pF0g%2B%2FDg4WCtYOySgXy0VM8FfkBJdGQAOBVVvmokDRIvTignQKTPaCrdBRDpfz1W7inhTOKt0PZBbEydSnjPF%2FqxabXjBrV2HtouYQXwS%2Bar7objzRKLF%2F4uq3QJ5n5aVcFUa%2Fm4lM0ORAwyAuwat0P7yX6qstCIO4gcgJgWDnm%2FbSZhx3rX7o7E8%2BB%2FGaoLOUgC2P8J2p4I2dnGR4eVeeQEC1dd%2B5bO0YkHw6rGSOaducm8Ur9sm%2FPp54PfYZp8mMZgsydXWKQKwFA0DTHkR%2BUvnGVDvx%2FnCHFnPwvPI%2FHC%2BNXGnXxA1Jzug3S8HdOkF%2F2d0wz54RBQwic%2BAx%2FHvwBx4wc8iIedW8QTX7jnAJwoX%2Fe5WJZHWavtpZeP5brMticTMKlEyp5WXlwODmLnDCafenc8kqiZD9K8MIj8mVRmZVAkfNecMhseEx8Oh2F5Qoq1SIXhwnNIeEutXtUIqcAOgcOZihF83zouMsTmHNEs0iwfGpZhf3Q11RPH5zWLJPma1DJ61SKipibXDvzp3W307eWJcwr%2FicygY6pgEUhK4Ry0gmcADuEpoUiDxVK6ZgFXU4s%2BQu8mHdldtdMaFE0fIqZRRftAzUeLlJFSircVNzEVmQYA%2FIQ%2FngQoRDGgDBI%2FUIdWF8xEOW7bnmfupdfKRYcEnE9Qv%2BqOPyFyiiL8FF9SDme9awEYS7x8sRpRc097OmOcdfz%2Fg%2B2gNnsFejFVsHxW5doL4II8%2BdES%2F4MKfg0LAEPoZg671ccaHvUyMEPvdc&X-Amz-Signature=2a08d8277f2648c99081b10c840ecd666f122e65ab33a3e2ee8276c380e7618f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







