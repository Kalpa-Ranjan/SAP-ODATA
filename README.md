



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773GE7OU%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T182548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBQNPuFIOx882rg6clB4dJ4JjCJ%2BoTVm5YeVvF4f4kqlAiEAsVdctSqO5vwHJJCiRxFS7tjcjVEJrdHN8%2FvBZqT3o8cqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNck7xdKSm%2BjqBeOKCrcA7AGHNQWVD7FnffatKHMBg2yWWrJ59QKboiuasGO9ykblXqfsXhVjgGc5jzo%2Fkac2A0cxLfmG%2B8vKivFy2NN9ASibBBEYUejWABo8dii4iNFaav7FPhWFb55beaf6gBPixdg8UKD1rxeRRjMFqIoE8ogEFOTIKwzq46I8z2%2FuNG6lDAckXa5nfLfewysNd9Oji5gVH9bfg4S622GlKJFDXVG3U0iXuZ9jTFhYV3fGeg6AOzbcRVRQuoDa8ifs2%2FsOgVAf9RjM8vDUpy9DMcvP1IPiG38Nm837lgJGyTNFAdDvnqqU4G%2BKHbGfJ1jOkj%2FnQxcN3fVPzNidqgxlPEsO%2BWjLC3qbDUsiduk8T7%2BSmmTJFtD3xrCs%2FQW2vlOaxl%2Be6x5lJb7PWrEW%2Flax6yMYDZt9v6%2BRm1QpJetbYjxm2MtVbl12PS6kA6BqRA0R2AldFGFln2C9NI9SXLyHXTDrGE8mDc%2BIZIS2yBbHlMEbNQXvaNwYKYGLx%2FpBEiYQKnIWgoDedyxnUujYyK0%2BXEyZeKmLs%2FjqsZCPgD%2By0wyXFAnADijaG3wExDKe%2B5Yo7FF6GXBrtYd5TZUsZqcEuxuv9E%2BS8g3IonuzhMTjJ80uyDCJaVkeb1GonraxrorMNShucsGOqUBfqOoBqLmBwTqjA%2Bmbedm2Cd7BzfXicmcL2cUtLt0q1D%2FTFyAVtpHjdz1%2FTmQQNmu%2B%2B2UT92R2Lo9UNp0UIypBZe%2B1CGZXVQnSs24YjUTm7nV56vydaG3NrX0XLEH3UfPv4VZ5hf4Z9q1rhLAzIpxW1hBOrLYtUQx6m8Qm9OHEPUUbKM6tkP6Ca6cbuangDQPN3ijm6vQESVAfgig3zHY8Kbksrnu&X-Amz-Signature=cda9ce3067aa7c4d34d718fc50597ec8954e5cc7fad9eac49d15b6ba5b55f994&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466773GE7OU%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T182548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBQNPuFIOx882rg6clB4dJ4JjCJ%2BoTVm5YeVvF4f4kqlAiEAsVdctSqO5vwHJJCiRxFS7tjcjVEJrdHN8%2FvBZqT3o8cqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNck7xdKSm%2BjqBeOKCrcA7AGHNQWVD7FnffatKHMBg2yWWrJ59QKboiuasGO9ykblXqfsXhVjgGc5jzo%2Fkac2A0cxLfmG%2B8vKivFy2NN9ASibBBEYUejWABo8dii4iNFaav7FPhWFb55beaf6gBPixdg8UKD1rxeRRjMFqIoE8ogEFOTIKwzq46I8z2%2FuNG6lDAckXa5nfLfewysNd9Oji5gVH9bfg4S622GlKJFDXVG3U0iXuZ9jTFhYV3fGeg6AOzbcRVRQuoDa8ifs2%2FsOgVAf9RjM8vDUpy9DMcvP1IPiG38Nm837lgJGyTNFAdDvnqqU4G%2BKHbGfJ1jOkj%2FnQxcN3fVPzNidqgxlPEsO%2BWjLC3qbDUsiduk8T7%2BSmmTJFtD3xrCs%2FQW2vlOaxl%2Be6x5lJb7PWrEW%2Flax6yMYDZt9v6%2BRm1QpJetbYjxm2MtVbl12PS6kA6BqRA0R2AldFGFln2C9NI9SXLyHXTDrGE8mDc%2BIZIS2yBbHlMEbNQXvaNwYKYGLx%2FpBEiYQKnIWgoDedyxnUujYyK0%2BXEyZeKmLs%2FjqsZCPgD%2By0wyXFAnADijaG3wExDKe%2B5Yo7FF6GXBrtYd5TZUsZqcEuxuv9E%2BS8g3IonuzhMTjJ80uyDCJaVkeb1GonraxrorMNShucsGOqUBfqOoBqLmBwTqjA%2Bmbedm2Cd7BzfXicmcL2cUtLt0q1D%2FTFyAVtpHjdz1%2FTmQQNmu%2B%2B2UT92R2Lo9UNp0UIypBZe%2B1CGZXVQnSs24YjUTm7nV56vydaG3NrX0XLEH3UfPv4VZ5hf4Z9q1rhLAzIpxW1hBOrLYtUQx6m8Qm9OHEPUUbKM6tkP6Ca6cbuangDQPN3ijm6vQESVAfgig3zHY8Kbksrnu&X-Amz-Signature=4412df7872d1359ca6c49afb30bb74c10e559e7a95f9005086493c4129307b82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







