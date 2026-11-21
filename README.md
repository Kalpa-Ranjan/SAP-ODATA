



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJN7YBJK%2F20261121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261121T120628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIBu1aT00EwxlVwXldEBtbzBbqOLHP1RJgjN41gxf%2FNbEAiAZ1NKOXKRx0%2FwGY3ktntZHFF5p37iRbOjedPamOes22Sr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMYRMlgbHB1%2FZU3jhzKtwDOtuAr%2Ff39q2ygJXZfhk0N560k%2BEvdRPeoFT5cLrqBdTEkQiPINAXJShjPHsTMfpZ1gkxPrXb6lxknL7jMjtU4N7QFLB0r2zid%2FEHwHTwtkYzy%2B%2FkPyop8Ttc7ea2XVJ8ZsrFxeYH5NUryzrnLAxZ4cFtb2pKBNaxK64SfJ0xPuXyISZMIR5UnpERfvErbHCEGPx95QVkgajt7q3xp%2BVeRxg0%2BQzselz8N%2FBCiHrza7F%2BISnoOAHOB%2B8gd7xEK8Y%2B7Hy7T8H%2FflKuoKQGriNfsRO%2F152so6lCiHmxJ2y8VkNQKaI70w27aO0JGuofqvdfla3jZOFZ23CH0wZH9sjQeEtqhZOVPZ0YZM7cBUhru9KT%2BLb4PQ3WzvuCaq1eyTx3xVDyAHxMCh9Bl%2BejZQuWKTbKztlyUh6iykuZu95y7rxGX8C6b%2FrHazr5LOnemL3owtAGz3%2B3cu609vMAXcMm22FQ3s7xlML0dw4FejPwrJ58Ab1IMns6T9SrB7jWWq59upk%2BSRYX4zkSLtWy5TXcGCJNS2dcAtenRg%2FnFJe8zHVHgHx7zgfL2zV6w8%2Fj5nXvIRmZQoRGWL5YPeIY6OYIpTygnnF%2Bc8srcehym2G6kKuiQCG2F7IKWe9dRM4w9faF2AY6pgHRYV1r6pTys2N1iE%2FLJcTvjJ1m7ScV%2FXMVb%2BGCsL62V63o6TDYwSKK6BVaa1hDM7hoW7HKB2NjTfC9jsnwkSvHvJq2qvmYdZJe%2FxijQXmg6jwystNaJm7eI%2F5L2B%2FeMNlutLywWZR%2BjFr6Ny4mHaRmxNG1jCYODcs5nhBI2Kas2sCKlU7lzkbHVJuuxvRwNYuXdVBxFfy9L7evG5DwM0SPEZ1uXDQZ&X-Amz-Signature=64f1dce2ed6f97a4d0e6c81d25561c651461ce8008889b50740c6bfbfc686222&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJN7YBJK%2F20261121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261121T120628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIBu1aT00EwxlVwXldEBtbzBbqOLHP1RJgjN41gxf%2FNbEAiAZ1NKOXKRx0%2FwGY3ktntZHFF5p37iRbOjedPamOes22Sr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMYRMlgbHB1%2FZU3jhzKtwDOtuAr%2Ff39q2ygJXZfhk0N560k%2BEvdRPeoFT5cLrqBdTEkQiPINAXJShjPHsTMfpZ1gkxPrXb6lxknL7jMjtU4N7QFLB0r2zid%2FEHwHTwtkYzy%2B%2FkPyop8Ttc7ea2XVJ8ZsrFxeYH5NUryzrnLAxZ4cFtb2pKBNaxK64SfJ0xPuXyISZMIR5UnpERfvErbHCEGPx95QVkgajt7q3xp%2BVeRxg0%2BQzselz8N%2FBCiHrza7F%2BISnoOAHOB%2B8gd7xEK8Y%2B7Hy7T8H%2FflKuoKQGriNfsRO%2F152so6lCiHmxJ2y8VkNQKaI70w27aO0JGuofqvdfla3jZOFZ23CH0wZH9sjQeEtqhZOVPZ0YZM7cBUhru9KT%2BLb4PQ3WzvuCaq1eyTx3xVDyAHxMCh9Bl%2BejZQuWKTbKztlyUh6iykuZu95y7rxGX8C6b%2FrHazr5LOnemL3owtAGz3%2B3cu609vMAXcMm22FQ3s7xlML0dw4FejPwrJ58Ab1IMns6T9SrB7jWWq59upk%2BSRYX4zkSLtWy5TXcGCJNS2dcAtenRg%2FnFJe8zHVHgHx7zgfL2zV6w8%2Fj5nXvIRmZQoRGWL5YPeIY6OYIpTygnnF%2Bc8srcehym2G6kKuiQCG2F7IKWe9dRM4w9faF2AY6pgHRYV1r6pTys2N1iE%2FLJcTvjJ1m7ScV%2FXMVb%2BGCsL62V63o6TDYwSKK6BVaa1hDM7hoW7HKB2NjTfC9jsnwkSvHvJq2qvmYdZJe%2FxijQXmg6jwystNaJm7eI%2F5L2B%2FeMNlutLywWZR%2BjFr6Ny4mHaRmxNG1jCYODcs5nhBI2Kas2sCKlU7lzkbHVJuuxvRwNYuXdVBxFfy9L7evG5DwM0SPEZ1uXDQZ&X-Amz-Signature=049dd6f488a07bd62b4e30e3330b28a2486afe13468c42c8888cc3ccde29354a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







