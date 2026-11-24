



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675CDB4PI%2F20261124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261124T001234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4%2Bzq6Lk%2FnlF0OUPqncLenM8jWMf%2FPhv1meBI3sCPhNgIhAMmRvj45%2FfCld%2BBEHXnXxznxn3Mj7H%2B7vHwnIckgXP9oKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzdexCkpQPQPSDverAq3AMiYp3mNKJqIIr%2BlXu3RzW6TpRgVDSmF9IF1LZTBF6jH0tGWyCr8S5CUBJzAynZ6Bx3B9fmFdwGbj0jOAn%2FyV9yupHT6eh%2FT%2FRQSVXZSNRQ%2FEvqcGCIrD7hNAPUJy7viOITwRbYCN4P1r4WsbJ8En%2BhK0Fk8pFqNp3Sq%2Fzg1WQSuuQMflb0kd9CmZP92THVbJ1gV%2BapnnPlM3trkPqV1nEBDgifGK0uROjuhZ43U2IF5BmlzolrvFGz7qf1crKLJFlfdY84Gjp6Pz8IwIjUoRKaCPpbYRNBPT5jeVqmd9Ntn09W10jWn8u1ECYGJ5L%2FJgOIFGFqlgLECW5n43faFWNlqdOrnxPTC4OUGBupElWT2YhLR16HbYIANJVsBYPS9yPJPM9qNzasNT02ova6OLpaGnZyWPTPdLhLOpoI0smGlJUB4%2BlIVZ1sH4CUN6JjTNMdcTUiv6DygmCgdc%2BpcqodIwwiQ9wHvrABendM65sfJjwunPc4qDj3Qr6W%2FptPODt6Q1Gvh7Dorm6im9pSegyZyHRvGyYWRTjZTxHcsXZk7QwPx7tF88vaWjMUI65TQrpai7geAlVbhMFeg%2Fw71%2BKTZkdfqLnMWTMUP4vEeRo%2BXWeP2AviC8VNcSySuDDIp5PYBjqkAcj1m%2FAJl3kbHrcGVMcTn%2Fi5Amg1dduK5x1jPJpSjfrfHF0JpCEidTznzRY67zXalfGbpS%2B9dz3sgLETLRu2xaVt%2BPLeH89iazXcOJbofe36dp0%2BW1d%2FK92VkaC%2BPQmA%2Bw48RfmURKCMriRjLdAtE3RNSINv1VuYAli3LaeZQ6wSo7ZNS3dEIgOryPgun9%2FTI5XP8EK1S%2FIg3MGPvqHf3sRysidH&X-Amz-Signature=0809c16187eb778a943059d0053aaa3cced77cbac875f296748b3a1736a61c76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675CDB4PI%2F20261124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261124T001234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4%2Bzq6Lk%2FnlF0OUPqncLenM8jWMf%2FPhv1meBI3sCPhNgIhAMmRvj45%2FfCld%2BBEHXnXxznxn3Mj7H%2B7vHwnIckgXP9oKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzdexCkpQPQPSDverAq3AMiYp3mNKJqIIr%2BlXu3RzW6TpRgVDSmF9IF1LZTBF6jH0tGWyCr8S5CUBJzAynZ6Bx3B9fmFdwGbj0jOAn%2FyV9yupHT6eh%2FT%2FRQSVXZSNRQ%2FEvqcGCIrD7hNAPUJy7viOITwRbYCN4P1r4WsbJ8En%2BhK0Fk8pFqNp3Sq%2Fzg1WQSuuQMflb0kd9CmZP92THVbJ1gV%2BapnnPlM3trkPqV1nEBDgifGK0uROjuhZ43U2IF5BmlzolrvFGz7qf1crKLJFlfdY84Gjp6Pz8IwIjUoRKaCPpbYRNBPT5jeVqmd9Ntn09W10jWn8u1ECYGJ5L%2FJgOIFGFqlgLECW5n43faFWNlqdOrnxPTC4OUGBupElWT2YhLR16HbYIANJVsBYPS9yPJPM9qNzasNT02ova6OLpaGnZyWPTPdLhLOpoI0smGlJUB4%2BlIVZ1sH4CUN6JjTNMdcTUiv6DygmCgdc%2BpcqodIwwiQ9wHvrABendM65sfJjwunPc4qDj3Qr6W%2FptPODt6Q1Gvh7Dorm6im9pSegyZyHRvGyYWRTjZTxHcsXZk7QwPx7tF88vaWjMUI65TQrpai7geAlVbhMFeg%2Fw71%2BKTZkdfqLnMWTMUP4vEeRo%2BXWeP2AviC8VNcSySuDDIp5PYBjqkAcj1m%2FAJl3kbHrcGVMcTn%2Fi5Amg1dduK5x1jPJpSjfrfHF0JpCEidTznzRY67zXalfGbpS%2B9dz3sgLETLRu2xaVt%2BPLeH89iazXcOJbofe36dp0%2BW1d%2FK92VkaC%2BPQmA%2Bw48RfmURKCMriRjLdAtE3RNSINv1VuYAli3LaeZQ6wSo7ZNS3dEIgOryPgun9%2FTI5XP8EK1S%2FIg3MGPvqHf3sRysidH&X-Amz-Signature=65fa0dbd8a0da49ade8a3aadcb43f41894c635cc81413336a752c5da60b866e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







