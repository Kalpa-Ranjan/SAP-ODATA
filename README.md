



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5OAR2DN%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T072427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBZiVkrWYG4LNDFOVyPyWVxzuX1QDShNPICfQx6GJ5qSAiEAiXUNb1mGJHKh4uCVLZaU0dSzr5az22GcwxN6lmu44fAqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEbyA%2FCIZNGKHSiTZCrcAyX8wXmNrRasaBCZP3JNYHB6PHmc2fUQlavFW0A0zqu%2Fz3BkeyVI4PncnwShqc8fBkPLdFX99zHB6oxC9e%2Ffs8G2d0ohHJgUpHtTWeC%2F38F0ezc7fCubq2k4%2BGVdD0anwllg1KeGv%2B7GUzeG4Aob1TggE%2FO2EViGhB9IEB0Awco6FK8S1PfEFjwIeh2i%2BanZ1DG4GQ526DRVacmEjVqMietsQzq%2F%2BLBnamzRSVjjG5goxoF41bfSu8OeWfkwwfdVLD%2BBa%2FdQvPf%2FN1SZ76PtGtL%2BYzd0lfxE%2FcI8jIv0zuRTNTt3XQ6I0efwBMkd9bTspcgxQhoNR8E%2FgmOtkmB3mcrHj%2FLmIGpyf%2BAgcbTb5A0rkL7Xa6LOc3K%2BS%2BxNNduOMMUaHiBKV6f0iRUQ%2BsqWZGB22gwqrRBxOIgOj18nLlUByU6x5tLnQ1nNGJ5v409Qk9AGJ1V%2FfXfK9Go1lQi5dNwjyVO7WCjJUW%2BphFv0gLSQ2vi08%2FBcYduJ6Oi4f3FHQymvgCAfsiquG1dSZTyJkKHngL8luDvft%2BSCy%2BO5%2BAFy3hXEKglpmfkkbv0ZnpXj2CZCWP2riFhD2UhRNy%2BqSyTjq3Ye0IsF648ALgPfl9c0kWB0EdysoXMoXwMKML3l%2FM4GOqUBnQKksNxs0wQvCDvlWxUFkY5XwgZ1TriG79Kxo0tpN69EHLwbqotmqV1OeLIpxaVQRwitZPEGr%2BGS2sFLCxbLFRbRMfiCzr%2B4QNHjYmByVTG4UZg6rt5e0bOiSk9PK%2Br0j5QKoT3mTA4HNXmdEU9MLHBYSziFYyq9nPZ%2BmBZAj5OwstgoSQi2bWm0voIYvX1t7y8xQ3RCuStQh%2FRdI36moJYCbk57&X-Amz-Signature=7153e8d9be36430ee3439655e2b10424d87d7c936360cc94f3fce7e7cca263c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5OAR2DN%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T072429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBZiVkrWYG4LNDFOVyPyWVxzuX1QDShNPICfQx6GJ5qSAiEAiXUNb1mGJHKh4uCVLZaU0dSzr5az22GcwxN6lmu44fAqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEbyA%2FCIZNGKHSiTZCrcAyX8wXmNrRasaBCZP3JNYHB6PHmc2fUQlavFW0A0zqu%2Fz3BkeyVI4PncnwShqc8fBkPLdFX99zHB6oxC9e%2Ffs8G2d0ohHJgUpHtTWeC%2F38F0ezc7fCubq2k4%2BGVdD0anwllg1KeGv%2B7GUzeG4Aob1TggE%2FO2EViGhB9IEB0Awco6FK8S1PfEFjwIeh2i%2BanZ1DG4GQ526DRVacmEjVqMietsQzq%2F%2BLBnamzRSVjjG5goxoF41bfSu8OeWfkwwfdVLD%2BBa%2FdQvPf%2FN1SZ76PtGtL%2BYzd0lfxE%2FcI8jIv0zuRTNTt3XQ6I0efwBMkd9bTspcgxQhoNR8E%2FgmOtkmB3mcrHj%2FLmIGpyf%2BAgcbTb5A0rkL7Xa6LOc3K%2BS%2BxNNduOMMUaHiBKV6f0iRUQ%2BsqWZGB22gwqrRBxOIgOj18nLlUByU6x5tLnQ1nNGJ5v409Qk9AGJ1V%2FfXfK9Go1lQi5dNwjyVO7WCjJUW%2BphFv0gLSQ2vi08%2FBcYduJ6Oi4f3FHQymvgCAfsiquG1dSZTyJkKHngL8luDvft%2BSCy%2BO5%2BAFy3hXEKglpmfkkbv0ZnpXj2CZCWP2riFhD2UhRNy%2BqSyTjq3Ye0IsF648ALgPfl9c0kWB0EdysoXMoXwMKML3l%2FM4GOqUBnQKksNxs0wQvCDvlWxUFkY5XwgZ1TriG79Kxo0tpN69EHLwbqotmqV1OeLIpxaVQRwitZPEGr%2BGS2sFLCxbLFRbRMfiCzr%2B4QNHjYmByVTG4UZg6rt5e0bOiSk9PK%2Br0j5QKoT3mTA4HNXmdEU9MLHBYSziFYyq9nPZ%2BmBZAj5OwstgoSQi2bWm0voIYvX1t7y8xQ3RCuStQh%2FRdI36moJYCbk57&X-Amz-Signature=a885f755bb1f7897f7211d25191eced796bcae201b393d94c1fe9b29704d3d66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







