



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSF5ORNW%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T064119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQDlJ7%2BPn0zLuKeI09fRRFvoJqLK4C2qWpcR8zNjdIZjVAIhANvfMKiaNGYmdErw3JIITbrK8Ycpexft6Fb3GaR3WE9WKv8DCD8QABoMNjM3NDIzMTgzODA1Igw7fF8jTvDGBv6hLxAq3AMPiuKWk98rtcpLRH8RzbtenxOtchzFCBZM7AzcCVoO7gHL1D7UKAhZgsM6%2FdmcP0QffFDQaUYaydHbizupBWIoWcufzW6D74aKLnuzRClGzwl5Do4SGvYtagtLIrOY9PY8QR%2FMxEh0Qi4MdKa8yxrj4aedVkhwb5lGbY%2B8imsH0BK1cK29KBAxjUIyzN0b%2BGuPvmPrpCSW%2BbDDE9ECPfdQoGr8Ew3VbYZm09brJGbwaTucMed57Fw3bWgTHNtz%2Bz7lJhUCHal9aKndCCkJmfU0soYqdA%2BxAgSGbah8eTHAA5Um%2FihXBqqBh0Hw5VOqWsiqyXlM0R9v96yQicD4Wj1w6CO7inPVbVzbCazSc%2BWuM4s9A7nhB2KWS0cMitRTgFZ7OHkAkchAZBxS8smY%2FOBzyKjF6%2Ff%2F0%2FngIakj2Go8ro85zHLyAD6mE%2B2TGSyRu%2B59wCTciDoWQ%2Bvuaeoq01px05Tg%2B8gqThm7%2F%2FUK9%2Fa6U%2Fi296Oc%2F2sDfmspC%2FHH2fKcgh088hjJjlP3kFymJiUR0qQLk5PJHNxoQ2er42cvP%2F32sWiNWqcf3X3IWVaxp1OjfpecX0wxWIy2pHVS4eha6lq4IYrwAIbhjOJpdna4jWpbRwLkGvV2oOLbNDDY477NBjqkAdIxVy8JYIVuKfFCaB7pGsjE8vAJvw3GLsZFsjoHi8ke9KHyTe%2FTbQt09yhhV5Cznvo66sXsqqq0SOzLAqUG0yiV8y9extuw2yJJgbvE4F4o%2BZN24X%2BPF1h118v9APhmkrPJPyMHtkJf%2BcJEun4rEIKqsxDNW1due0xVRZPeTITLbbijoagscKlsLPb9K4fSr1C4DPThls88IZSZxmckxsSh3XKx&X-Amz-Signature=f2f85b763baa3096edbfd128fdeb627c5c2aebed9622e40ac20be98ea9469c49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSF5ORNW%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T064119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQDlJ7%2BPn0zLuKeI09fRRFvoJqLK4C2qWpcR8zNjdIZjVAIhANvfMKiaNGYmdErw3JIITbrK8Ycpexft6Fb3GaR3WE9WKv8DCD8QABoMNjM3NDIzMTgzODA1Igw7fF8jTvDGBv6hLxAq3AMPiuKWk98rtcpLRH8RzbtenxOtchzFCBZM7AzcCVoO7gHL1D7UKAhZgsM6%2FdmcP0QffFDQaUYaydHbizupBWIoWcufzW6D74aKLnuzRClGzwl5Do4SGvYtagtLIrOY9PY8QR%2FMxEh0Qi4MdKa8yxrj4aedVkhwb5lGbY%2B8imsH0BK1cK29KBAxjUIyzN0b%2BGuPvmPrpCSW%2BbDDE9ECPfdQoGr8Ew3VbYZm09brJGbwaTucMed57Fw3bWgTHNtz%2Bz7lJhUCHal9aKndCCkJmfU0soYqdA%2BxAgSGbah8eTHAA5Um%2FihXBqqBh0Hw5VOqWsiqyXlM0R9v96yQicD4Wj1w6CO7inPVbVzbCazSc%2BWuM4s9A7nhB2KWS0cMitRTgFZ7OHkAkchAZBxS8smY%2FOBzyKjF6%2Ff%2F0%2FngIakj2Go8ro85zHLyAD6mE%2B2TGSyRu%2B59wCTciDoWQ%2Bvuaeoq01px05Tg%2B8gqThm7%2F%2FUK9%2Fa6U%2Fi296Oc%2F2sDfmspC%2FHH2fKcgh088hjJjlP3kFymJiUR0qQLk5PJHNxoQ2er42cvP%2F32sWiNWqcf3X3IWVaxp1OjfpecX0wxWIy2pHVS4eha6lq4IYrwAIbhjOJpdna4jWpbRwLkGvV2oOLbNDDY477NBjqkAdIxVy8JYIVuKfFCaB7pGsjE8vAJvw3GLsZFsjoHi8ke9KHyTe%2FTbQt09yhhV5Cznvo66sXsqqq0SOzLAqUG0yiV8y9extuw2yJJgbvE4F4o%2BZN24X%2BPF1h118v9APhmkrPJPyMHtkJf%2BcJEun4rEIKqsxDNW1due0xVRZPeTITLbbijoagscKlsLPb9K4fSr1C4DPThls88IZSZxmckxsSh3XKx&X-Amz-Signature=1955ad1e6b7fd662e9ca0fcf59b1b7941c8ec87b01dc38a75e00da8830522fcf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







