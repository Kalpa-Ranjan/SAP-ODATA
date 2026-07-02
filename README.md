



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G7XHMAE%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T024609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIQDMrNEo5n63DXZ20RKSQIHLakwSrZ5odyJmj9vgv1W3mgIgY4%2FjXU6u8K9cwgpq0mOpiVsz1xQEq8lT1gSbCbsuQtkqiAQI5v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAV61FA94t2glgWkEircAwpKEkcLzxHJspG1YjXgkq4nFNh%2Fp5FEjtTQ8k1VOolpw2euGtLRDBJR0Jh7rLcZ2I09J61blPMYE%2F9IKsidiElK7s2DxOjIN7qJJ6p8yTnLB08etGBB9WU2Dx56w3OpwCwbjpxkNIV0FRb3czv7eu8tLIoapxI8qiiO70tMsyofOOeszLMahuyWyQTudjFQBFPHIuKBCIZXs18ixXpICh5ZUTRmh2SehvwiQHivaSvtJ8rDVqiqxKl7lfhd9MjPsgo3NrVpJPOqNaljyRzp6uB2pdy2PWQr1pRF6B49LubP%2B9rQbxdOR3i7SHaEFkBeJG%2F4c2iOeISavN0UdIGReBDFP8e7o8%2BmHbASBSyVOibHY%2BW9c7NrhiF3Y4HjWWza%2BpA9%2BxowJkLGkL30i2ye1TY2i1Ju3OWBvm7gBgPt0koiCdxkJyQAzV1swihxT%2BM%2FoxBZ4sgBDu3xC6rVXLBw2eyrKNps%2BoTPPwOC0v7h9G2lT%2F9oH8yrtbb%2FfQHASFWQwkzmAMYdFkpvcdx2WykXNTuwT9%2BnGJicvai7BGrCpY9YTyPTaLcwJM6IuzwMxHE6X4JXM4iOkmJbpnjrez1Uos2PiblOkTcSzxQak108egNXkHKkFa2BjgjA339iMKKCltIGOqUB4Vvn7jf7mW%2BuBGUd1Ma%2F8yhFdWpUKrY9J2CH8cDxpERdqx3BbXy%2BtaAfcxAvHGBoMYPdw%2FoxjMNyeiKLo1ssEBMbaHYxpdN2T6H3tnlMLXCCDUfM4ED5%2BA%2Bbs8bZjYb6TcM3yaH5HiGa6M%2FU1HiiAPtMP9EhAMkUGSz44zSwWYsScEc59cWXQQrWcfZ47AO3FIniJPSgTQ39ntSmeV1K3gCwPP0C&X-Amz-Signature=26d5451fdd9f51bc686717c321be7d0dae76a63ba14ca829a1947ac1936ac67e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G7XHMAE%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T024609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIQDMrNEo5n63DXZ20RKSQIHLakwSrZ5odyJmj9vgv1W3mgIgY4%2FjXU6u8K9cwgpq0mOpiVsz1xQEq8lT1gSbCbsuQtkqiAQI5v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAV61FA94t2glgWkEircAwpKEkcLzxHJspG1YjXgkq4nFNh%2Fp5FEjtTQ8k1VOolpw2euGtLRDBJR0Jh7rLcZ2I09J61blPMYE%2F9IKsidiElK7s2DxOjIN7qJJ6p8yTnLB08etGBB9WU2Dx56w3OpwCwbjpxkNIV0FRb3czv7eu8tLIoapxI8qiiO70tMsyofOOeszLMahuyWyQTudjFQBFPHIuKBCIZXs18ixXpICh5ZUTRmh2SehvwiQHivaSvtJ8rDVqiqxKl7lfhd9MjPsgo3NrVpJPOqNaljyRzp6uB2pdy2PWQr1pRF6B49LubP%2B9rQbxdOR3i7SHaEFkBeJG%2F4c2iOeISavN0UdIGReBDFP8e7o8%2BmHbASBSyVOibHY%2BW9c7NrhiF3Y4HjWWza%2BpA9%2BxowJkLGkL30i2ye1TY2i1Ju3OWBvm7gBgPt0koiCdxkJyQAzV1swihxT%2BM%2FoxBZ4sgBDu3xC6rVXLBw2eyrKNps%2BoTPPwOC0v7h9G2lT%2F9oH8yrtbb%2FfQHASFWQwkzmAMYdFkpvcdx2WykXNTuwT9%2BnGJicvai7BGrCpY9YTyPTaLcwJM6IuzwMxHE6X4JXM4iOkmJbpnjrez1Uos2PiblOkTcSzxQak108egNXkHKkFa2BjgjA339iMKKCltIGOqUB4Vvn7jf7mW%2BuBGUd1Ma%2F8yhFdWpUKrY9J2CH8cDxpERdqx3BbXy%2BtaAfcxAvHGBoMYPdw%2FoxjMNyeiKLo1ssEBMbaHYxpdN2T6H3tnlMLXCCDUfM4ED5%2BA%2Bbs8bZjYb6TcM3yaH5HiGa6M%2FU1HiiAPtMP9EhAMkUGSz44zSwWYsScEc59cWXQQrWcfZ47AO3FIniJPSgTQ39ntSmeV1K3gCwPP0C&X-Amz-Signature=9a611f0e08a544804a7226f386721c1bda0a80de42edfafbb17420ed3a2c80fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







