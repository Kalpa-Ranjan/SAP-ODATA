



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCYZMZFI%2F20260829%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260829T201810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDIaHpML2wQ9Xhamhj5TfwmA2h1zrRBXbkqJsMqDgK8NgIhANX0RgFQlukbk%2F8TOJ4SBQqFiXb8qDiVeAGLltJZpAr2Kv8DCG0QABoMNjM3NDIzMTgzODA1Igwlfq7RIKrW3VDOrj4q3AOStfEChdEqz4zm%2B%2F6wFVautaSzvFVi1HZOdOaFFdVOmgoZ7ud4UHpgtAuUC1H4GJfST3o4sUbasjWQCRQn3j71GeSqjDV0F9AbIhM1DVNOBoXepuymIbRfdxtkt%2FGp26EIEY8sbdv3mmBFEcfsvD%2FaXNozL7NA5DbRqvVCV5RPrXaKnTLbsf4ygGOWCTiwgI3lBASpzfwFsW9ZelDrmIuKg2Zby7VYAB4R0x8rSa2zZnXZ17fw9CWof6SxvhaAvFsnXecKhaxXJ2YMcfZoC3AehjyY02Lj3jd3COC8WeHO6PoT%2BB4xWoHEaMzfCBrBaNipsXzNSUjcbAYeP%2FBmiAdQqCb6TPDcjXUDiOlR4w5gp5pXJwEwXRqvppwt9oTZ2UEZIM%2BZhqZCYD6sabqJEIpUO%2BkSBhtIAmPwhfMVkXUnAqx4eH24kxjoghN7E4jpnCKzD2gZqW7Ot4arRx6FYDCxwb5fK%2BZVCJy5H9pASFOzd00ecXPZW%2FPwasBL9KHe0WAB6nRrw0cSc1bVfnWQ3kCl81coeA97ZfJPtHc%2Fd5PLfBHP10bo%2BUExFHbi8AJLnvKWJWRPTSbsZ8kMhZ4oAOS%2Fy6dJU8jdJ6Yxg6EtdVP71XpTDgQRt67NZS34pjC9%2B8zUBjqkAQS8OS2arsItqJ7Fn%2BJ394ZoFIhJJffII2hGEi7u%2BuJNlhbpye5975RLK0fNV8ILeIJ%2B5e8qD2kqvUlhkJmUSPL7ax6H%2BiCAYx5dU3Y%2BIuM4i9LALvGRoCQgAVWTIeYKp5y03UxteohK365%2Fd3nP77sFyhP9QnlU%2BFsgbKyOCmEEqyal1yXmPOBR6bB4djtlpzFVvAY1XY6gUu4JR7LmXfPVgEI0&X-Amz-Signature=9fb08d5b4486a53578a46f031c20d13a895670c2152e870f0e613b480fb1791e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCYZMZFI%2F20260829%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260829T201810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDIaHpML2wQ9Xhamhj5TfwmA2h1zrRBXbkqJsMqDgK8NgIhANX0RgFQlukbk%2F8TOJ4SBQqFiXb8qDiVeAGLltJZpAr2Kv8DCG0QABoMNjM3NDIzMTgzODA1Igwlfq7RIKrW3VDOrj4q3AOStfEChdEqz4zm%2B%2F6wFVautaSzvFVi1HZOdOaFFdVOmgoZ7ud4UHpgtAuUC1H4GJfST3o4sUbasjWQCRQn3j71GeSqjDV0F9AbIhM1DVNOBoXepuymIbRfdxtkt%2FGp26EIEY8sbdv3mmBFEcfsvD%2FaXNozL7NA5DbRqvVCV5RPrXaKnTLbsf4ygGOWCTiwgI3lBASpzfwFsW9ZelDrmIuKg2Zby7VYAB4R0x8rSa2zZnXZ17fw9CWof6SxvhaAvFsnXecKhaxXJ2YMcfZoC3AehjyY02Lj3jd3COC8WeHO6PoT%2BB4xWoHEaMzfCBrBaNipsXzNSUjcbAYeP%2FBmiAdQqCb6TPDcjXUDiOlR4w5gp5pXJwEwXRqvppwt9oTZ2UEZIM%2BZhqZCYD6sabqJEIpUO%2BkSBhtIAmPwhfMVkXUnAqx4eH24kxjoghN7E4jpnCKzD2gZqW7Ot4arRx6FYDCxwb5fK%2BZVCJy5H9pASFOzd00ecXPZW%2FPwasBL9KHe0WAB6nRrw0cSc1bVfnWQ3kCl81coeA97ZfJPtHc%2Fd5PLfBHP10bo%2BUExFHbi8AJLnvKWJWRPTSbsZ8kMhZ4oAOS%2Fy6dJU8jdJ6Yxg6EtdVP71XpTDgQRt67NZS34pjC9%2B8zUBjqkAQS8OS2arsItqJ7Fn%2BJ394ZoFIhJJffII2hGEi7u%2BuJNlhbpye5975RLK0fNV8ILeIJ%2B5e8qD2kqvUlhkJmUSPL7ax6H%2BiCAYx5dU3Y%2BIuM4i9LALvGRoCQgAVWTIeYKp5y03UxteohK365%2Fd3nP77sFyhP9QnlU%2BFsgbKyOCmEEqyal1yXmPOBR6bB4djtlpzFVvAY1XY6gUu4JR7LmXfPVgEI0&X-Amz-Signature=af9da58164a083a623638b09fd42902c498dde8650049c43164a43aeed4b9d3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







