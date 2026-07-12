



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EYUVESF%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T185754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJHMEUCIHkizoFXScpC%2B0vkNUu9zz4e0BOoCsd24E1OCbxqEHYzAiEAlkhMjTRH2KWjENtMoEoi2uh5qWkD7nA4UIA%2BkohDOz8qiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMlodbEsI052pxxZ%2BCrcA4LToNHYUP1C3Sqp6FPUTe74iNa4%2FNH6c%2BbCIGvpusI6aLH5p%2B%2BJOra%2BGRS2TVfRvUnW9VAppoHh7EPNnrznAbxR%2FQ%2B1sMPOxwNVNiOy5gCP2mQC%2FkEfAIFTS%2B3O6pefaplfuBgBsYvnTmFO%2BXaM4LgrHEYqvvWgDGNMsaHU60YEIXR1Rtk7W5oHw8jnmwxTRz04ocrZf9TjsqvapLC9rdXKb1J%2B91mvAhw1l9ycVwEVDjbmJ%2Bqdp8vTA9VGv2hPZ%2FY39jz6XC4tDzwrwmPFfFApQLIFlaV8vDqyJPsrfvP%2BhjKMLrMQiva%2FYdikR%2BZW%2B30q46ZP1oWtoiNbP0lU2N%2FVGmmOW7Fdp8jwUupcmDSnE0FcX15V%2BxhGUiaADE%2Fcx7ksFwBodBGPuiPGlaL0PET35hJTI6gdq3aXMN0kmC2Z7uYGhSEuWd8VYcgms%2F46jxLuI1KIjcQsGxGmA6iXO%2FkBmg2UNduwCFmgqONyzQzV3gQEj2sXOKor%2FbREE8O1%2BSv4mZP29kLbUs6%2BwepGP30rr5dQozOKAbMm2zSSD94WZkj3zRV0Ive2CB%2FEfvQQKX9Elwu9v7lEbD8rwbSO6m%2Fc%2BGRU%2FJpwSiOrjkynqCDmbaniaTJ%2BIxlt8Q%2BaMISPz9IGOqUBHbVnAicskcSsn%2BLoLngURYaQH31avAIXz2MpHGsgiPxxtdCvmQuYuMiPi3XYBjAijv24RsBsw1oexwR9UTvKVdkKhgFhSdY4YAEAIh6HCTuB3LeoPpmSI00wAxKvYJNvZk3rnJn9U8rgG8O5GMBVWPYDqsEeM%2BjmlvOzR1IjnAN6izB1OS9IiMD2Eg1Jy0sWFTlEh%2BpQ2BTxbKAKcLR3IBul%2FiW0&X-Amz-Signature=dbcbec2bdf6dbc394fe9a7243e13c721a5e09b0c6203cd10defcf898d06d986e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EYUVESF%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T185754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJHMEUCIHkizoFXScpC%2B0vkNUu9zz4e0BOoCsd24E1OCbxqEHYzAiEAlkhMjTRH2KWjENtMoEoi2uh5qWkD7nA4UIA%2BkohDOz8qiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMlodbEsI052pxxZ%2BCrcA4LToNHYUP1C3Sqp6FPUTe74iNa4%2FNH6c%2BbCIGvpusI6aLH5p%2B%2BJOra%2BGRS2TVfRvUnW9VAppoHh7EPNnrznAbxR%2FQ%2B1sMPOxwNVNiOy5gCP2mQC%2FkEfAIFTS%2B3O6pefaplfuBgBsYvnTmFO%2BXaM4LgrHEYqvvWgDGNMsaHU60YEIXR1Rtk7W5oHw8jnmwxTRz04ocrZf9TjsqvapLC9rdXKb1J%2B91mvAhw1l9ycVwEVDjbmJ%2Bqdp8vTA9VGv2hPZ%2FY39jz6XC4tDzwrwmPFfFApQLIFlaV8vDqyJPsrfvP%2BhjKMLrMQiva%2FYdikR%2BZW%2B30q46ZP1oWtoiNbP0lU2N%2FVGmmOW7Fdp8jwUupcmDSnE0FcX15V%2BxhGUiaADE%2Fcx7ksFwBodBGPuiPGlaL0PET35hJTI6gdq3aXMN0kmC2Z7uYGhSEuWd8VYcgms%2F46jxLuI1KIjcQsGxGmA6iXO%2FkBmg2UNduwCFmgqONyzQzV3gQEj2sXOKor%2FbREE8O1%2BSv4mZP29kLbUs6%2BwepGP30rr5dQozOKAbMm2zSSD94WZkj3zRV0Ive2CB%2FEfvQQKX9Elwu9v7lEbD8rwbSO6m%2Fc%2BGRU%2FJpwSiOrjkynqCDmbaniaTJ%2BIxlt8Q%2BaMISPz9IGOqUBHbVnAicskcSsn%2BLoLngURYaQH31avAIXz2MpHGsgiPxxtdCvmQuYuMiPi3XYBjAijv24RsBsw1oexwR9UTvKVdkKhgFhSdY4YAEAIh6HCTuB3LeoPpmSI00wAxKvYJNvZk3rnJn9U8rgG8O5GMBVWPYDqsEeM%2BjmlvOzR1IjnAN6izB1OS9IiMD2Eg1Jy0sWFTlEh%2BpQ2BTxbKAKcLR3IBul%2FiW0&X-Amz-Signature=53e2ee1145bae3ceae825cac835bca490c9e9a00edd4137cb8fc143603a31fd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







