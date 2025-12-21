



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUEH36Q6%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T182151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCbAUztgChfSQ0Qg%2F2zff8V3%2FyL33YV4fikyP%2BKcbPkWAIgYwWvERSofM2Vq9EVBowi%2Bc3KBd1xc3gpwenyv5Wq6B0qiAQI4P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFYUyP9BtHJA8t1FoSrcA4acHvIOSHJ0bcmi3O0ckd6uJ7%2BiKmjRgWo5XXp1a5pSaicdFVbh8yrzgRsF3XV%2BojHu24a%2BQ7ze6SZ1ULYbV8Vz8ePYmmWY2W5QFVE%2FEVKzCR6IB02GCtZZvA6QbAGK4lSaQHYETJVRZqna0%2BCQZ86NB1d4AX28wdepw3DopkeCIfliwmMs3XTt4tLsOqzb9L0CMvubByFfTojWqvQ1MMgk7nGKGICjiqUOI95iHJ4XXpS5Jbr1XQGQauLcYXqxwkqgsPCPHzCPWBBkzNfOVwNY4e9D0hwnTe6NSV2CsR2UtQ%2FdwZNMOix27lN6MLL10HU13CQDz5F%2BT%2FHNb4O4L4BuVrs01Zp%2B82LEPnpa88%2FpJR4X9IGIAKVWV8V9%2BirtxDgj%2BS4bJ%2BOOXbPWBThcRyy%2FxfHtvGin50B2beio1OEM3BRS0AeBz1D5TY6eTGrL8X%2BMeMJgxVq%2Fqi9%2FVGsr%2BftNyXceV7JjailD3z%2F6zHrfV3CfDgFPp%2BwIZVsIKEpVt2LawbD7LsY1v2F0DVmeY5qVKxGI3tnksRcGEkb0ftxIR9bB2qDVtKZoPwvxoZo6jweRLj%2BF5dIEdwck4LBe70Is5LVhcYDwajVeEEsSuYODF5EGdmSI5RMsQNZdMLSeoMoGOqUBpdLMAKeQOePwhRaDZKni4wDdaYc%2F%2BZ%2BVzU16NCglm6VGJzVnHZ0lM1qvnD2ozhDC4zU5P7lxz8lj7dGUmrCySj8Fpy0IckJsvI8DNu4lQw3dcmrSmdKd9j9Uv8Tp9tfiu2nFO8FDpISrF3JzKW1UQjnenfZwcW6QH9jnhvFdbJjqDkbyUvVHN%2B8j4LXQLkB173LTMHmkK3Yn8%2Fhlxbf%2FKVFD9NKo&X-Amz-Signature=da1a4217be48899a83d8ce9e54db70065770c314a808230637a7cdae5b311a19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUEH36Q6%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T182151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCbAUztgChfSQ0Qg%2F2zff8V3%2FyL33YV4fikyP%2BKcbPkWAIgYwWvERSofM2Vq9EVBowi%2Bc3KBd1xc3gpwenyv5Wq6B0qiAQI4P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFYUyP9BtHJA8t1FoSrcA4acHvIOSHJ0bcmi3O0ckd6uJ7%2BiKmjRgWo5XXp1a5pSaicdFVbh8yrzgRsF3XV%2BojHu24a%2BQ7ze6SZ1ULYbV8Vz8ePYmmWY2W5QFVE%2FEVKzCR6IB02GCtZZvA6QbAGK4lSaQHYETJVRZqna0%2BCQZ86NB1d4AX28wdepw3DopkeCIfliwmMs3XTt4tLsOqzb9L0CMvubByFfTojWqvQ1MMgk7nGKGICjiqUOI95iHJ4XXpS5Jbr1XQGQauLcYXqxwkqgsPCPHzCPWBBkzNfOVwNY4e9D0hwnTe6NSV2CsR2UtQ%2FdwZNMOix27lN6MLL10HU13CQDz5F%2BT%2FHNb4O4L4BuVrs01Zp%2B82LEPnpa88%2FpJR4X9IGIAKVWV8V9%2BirtxDgj%2BS4bJ%2BOOXbPWBThcRyy%2FxfHtvGin50B2beio1OEM3BRS0AeBz1D5TY6eTGrL8X%2BMeMJgxVq%2Fqi9%2FVGsr%2BftNyXceV7JjailD3z%2F6zHrfV3CfDgFPp%2BwIZVsIKEpVt2LawbD7LsY1v2F0DVmeY5qVKxGI3tnksRcGEkb0ftxIR9bB2qDVtKZoPwvxoZo6jweRLj%2BF5dIEdwck4LBe70Is5LVhcYDwajVeEEsSuYODF5EGdmSI5RMsQNZdMLSeoMoGOqUBpdLMAKeQOePwhRaDZKni4wDdaYc%2F%2BZ%2BVzU16NCglm6VGJzVnHZ0lM1qvnD2ozhDC4zU5P7lxz8lj7dGUmrCySj8Fpy0IckJsvI8DNu4lQw3dcmrSmdKd9j9Uv8Tp9tfiu2nFO8FDpISrF3JzKW1UQjnenfZwcW6QH9jnhvFdbJjqDkbyUvVHN%2B8j4LXQLkB173LTMHmkK3Yn8%2Fhlxbf%2FKVFD9NKo&X-Amz-Signature=104a0dd8aab3c9620784f06c5afb4580f69dd767f13111d8d0cc974c30a01ef9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







