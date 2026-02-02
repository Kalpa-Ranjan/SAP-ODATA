



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TS4OBEVM%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T014825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIFN7Yh1Yr7AYvCeYv3sN6VTDxasPd4w4bad40BVPIirwAiEAoR9c%2FyblxIW1zOyWJj4H5HfYRvn%2FIKuG%2FF9isUAhgr8qiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIC7kwuA3P%2FObpx%2FayrcA8aHpScnDySdv6WfquWjlpUTNKf%2F%2FdPh2W2CdMXm4tTjh%2FNz3tJTaAGIbLx0TOvPebx5%2FwlM81Uut%2B0vUdGfxTafg7LlPd7RI4%2FyQxe2SbBt8RMcjdDriN2jkNnf1SszYVrvfjAIG%2FKIJpQSnVVcDFE3a%2BkvxlvfO197D0uu8RWCv7KumLvy5h7qzrxqm7xghZBT6fYKYYUD%2FROL0%2B6issqF3SkbxrFESNjsfD6elbjRgEB3bQRoiwPBXEkzAS9iVk5iNiMR4ug%2Fm790Orcicof5hetm1I6WThbUS%2FtnoVbMF3tld8LoItSaJsN%2F2y9TBFsuzF7tPzh4KjZnWAEnAuDWkLgh1HDKyoREI%2BlfuBqiT8oOp9jsfVlfZ3bEdeTJHPdyOhgcuxHPzairnGSD2Yt34mqI9ScyKHZRk8W3iRoCfbiqov8QoM8fM0uppTgXF9ksNILAX6KlGu5ydoCtvUBmJaK%2FWsGLVEHq6tYZf36w6FlzFuW1NcTfp3P2XB9wWxVJcPTgrNcGslmUIK1tybgrPvY%2BS8EZkCP4dscfZHi1%2FFTj7Q7bZFaURKN5I2k8XH4bvWinW3yOd5v7guxOJhxdoZUYs1iGJnECR22SeDzCMJ7YgcI2F%2F6iAzWmMMPr%2F8sGOqUBog2RtNkwrTirTP%2BHXDLRqL8m9B7vwHYYYlZGSyyN59xQtg2sPO0HtR2iJ0%2BLm%2F6yKDe1t0r82SCoasSjxvdJ1GgYOTUUnnrycdlVTPKhnxpXWpFu79xV2VTrlxNSzecM6alXZpTvKJRf9M7ujvr70TwVh5azP1NtjU6ewgLRtzvKCxh4mFXWt8bl59G%2FzlqlbjEQ6fkLgvWYLl81SI1epOXAvJiv&X-Amz-Signature=3470766fd6015b845619afc8812eccd20ec81301ceb2b13a7e4713738de73405&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TS4OBEVM%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T014826Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIFN7Yh1Yr7AYvCeYv3sN6VTDxasPd4w4bad40BVPIirwAiEAoR9c%2FyblxIW1zOyWJj4H5HfYRvn%2FIKuG%2FF9isUAhgr8qiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIC7kwuA3P%2FObpx%2FayrcA8aHpScnDySdv6WfquWjlpUTNKf%2F%2FdPh2W2CdMXm4tTjh%2FNz3tJTaAGIbLx0TOvPebx5%2FwlM81Uut%2B0vUdGfxTafg7LlPd7RI4%2FyQxe2SbBt8RMcjdDriN2jkNnf1SszYVrvfjAIG%2FKIJpQSnVVcDFE3a%2BkvxlvfO197D0uu8RWCv7KumLvy5h7qzrxqm7xghZBT6fYKYYUD%2FROL0%2B6issqF3SkbxrFESNjsfD6elbjRgEB3bQRoiwPBXEkzAS9iVk5iNiMR4ug%2Fm790Orcicof5hetm1I6WThbUS%2FtnoVbMF3tld8LoItSaJsN%2F2y9TBFsuzF7tPzh4KjZnWAEnAuDWkLgh1HDKyoREI%2BlfuBqiT8oOp9jsfVlfZ3bEdeTJHPdyOhgcuxHPzairnGSD2Yt34mqI9ScyKHZRk8W3iRoCfbiqov8QoM8fM0uppTgXF9ksNILAX6KlGu5ydoCtvUBmJaK%2FWsGLVEHq6tYZf36w6FlzFuW1NcTfp3P2XB9wWxVJcPTgrNcGslmUIK1tybgrPvY%2BS8EZkCP4dscfZHi1%2FFTj7Q7bZFaURKN5I2k8XH4bvWinW3yOd5v7guxOJhxdoZUYs1iGJnECR22SeDzCMJ7YgcI2F%2F6iAzWmMMPr%2F8sGOqUBog2RtNkwrTirTP%2BHXDLRqL8m9B7vwHYYYlZGSyyN59xQtg2sPO0HtR2iJ0%2BLm%2F6yKDe1t0r82SCoasSjxvdJ1GgYOTUUnnrycdlVTPKhnxpXWpFu79xV2VTrlxNSzecM6alXZpTvKJRf9M7ujvr70TwVh5azP1NtjU6ewgLRtzvKCxh4mFXWt8bl59G%2FzlqlbjEQ6fkLgvWYLl81SI1epOXAvJiv&X-Amz-Signature=f89415b4cf879ae6346fb4ebbe25bc8ad5ef8c06b7851f9d7c0f240d27abad89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







