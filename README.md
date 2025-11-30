



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MC7MAHP%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T182048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJIMEYCIQDDl6I10tzvO%2Bu%2FXBQe9Rpy0aN0ynqRckeQRGlnORTdMgIhALBbjls5tsCpYBFCRpirjRBNsRcZH%2FPrLGWlcNKgIdVAKogECOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwAYvEUi1mZMDaNjmMq3AM2WJC3xQ8Vm12fpac621MmGoxtFXkE76mG3g0VBZZ6aoT6zIJSLRt3z8MnZyfZLsVogskbIVVjb3d52DTwO852gUJ3gTahy8DmPr3iEKtTeZaU0hKBGJ%2FGt1AQJCudHku9eirpcbjUyjU6u%2BKX5E40QNQ%2FdKnhaHRCA8Kezq6EGmhKP3XbNVCa6djcKra02g36I4m7OgHQPdOSjpEcQLeeVtMJNwSTkZg%2BQpC%2BPQaCHATU6XDsg6VX221xP4Fju%2B6UTNwBZ38yKE89ibTCLNkQ63Z8Kg21GeQumcqAcNnPNH7dKyBYugWt4sEIWRAEltQsJS1K841edzty4fD9ayoP7%2BdJf14c%2B3%2Fs3V9ipfEB%2B73Ihz9W6i0qLrFLUjcORX6bZbfkY1dOHv2Kle42ioxoV1X%2BFsjxJkGjk%2BXOrlGe4r%2FTN91H1lUEjfmFFUkA9iw7DCtAhgdEea8O50WlZckow2XFYob3%2FENZkyrltimqB4jrh1MPB4AE39vFmh5pUlBIBkLNd01FvvZm2%2B0RHltPJhTcmSCEI20LrszNVu%2Fp8%2B42PhjcE8NDqDk740GCnw%2FXSdhPqBSvzq6MtK658G%2BNgzs5%2Fkf1mQXafD9z5c2QowxKAF9neZUktrs69TCP5bHJBjqkAVyaj8rcUgR44iUvScAEljn%2Bi4LNe0DUo2EqY5dKlSWgL49DFaCPRttgQH%2F4Gd7EBtaR92HGV0U6xXZ6DIB%2B81%2F3Mq0NMuMNP7JayFYMpPrRls8%2Fm9pHkcFpoeZsI%2BKtKb5V1VYdEPehVyauu5tTtDf1uGB8JSEHgA0cHzOF6%2FHNMqS6FshZ0Pf8wU4MO5BUAiAXYlZBZG%2BnWy24xONASvwwm8q9&X-Amz-Signature=1253c69d3d4be4d3746d227f3b8bbb274accb61a432e7fae9f9fba059729da41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MC7MAHP%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T182048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJIMEYCIQDDl6I10tzvO%2Bu%2FXBQe9Rpy0aN0ynqRckeQRGlnORTdMgIhALBbjls5tsCpYBFCRpirjRBNsRcZH%2FPrLGWlcNKgIdVAKogECOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwAYvEUi1mZMDaNjmMq3AM2WJC3xQ8Vm12fpac621MmGoxtFXkE76mG3g0VBZZ6aoT6zIJSLRt3z8MnZyfZLsVogskbIVVjb3d52DTwO852gUJ3gTahy8DmPr3iEKtTeZaU0hKBGJ%2FGt1AQJCudHku9eirpcbjUyjU6u%2BKX5E40QNQ%2FdKnhaHRCA8Kezq6EGmhKP3XbNVCa6djcKra02g36I4m7OgHQPdOSjpEcQLeeVtMJNwSTkZg%2BQpC%2BPQaCHATU6XDsg6VX221xP4Fju%2B6UTNwBZ38yKE89ibTCLNkQ63Z8Kg21GeQumcqAcNnPNH7dKyBYugWt4sEIWRAEltQsJS1K841edzty4fD9ayoP7%2BdJf14c%2B3%2Fs3V9ipfEB%2B73Ihz9W6i0qLrFLUjcORX6bZbfkY1dOHv2Kle42ioxoV1X%2BFsjxJkGjk%2BXOrlGe4r%2FTN91H1lUEjfmFFUkA9iw7DCtAhgdEea8O50WlZckow2XFYob3%2FENZkyrltimqB4jrh1MPB4AE39vFmh5pUlBIBkLNd01FvvZm2%2B0RHltPJhTcmSCEI20LrszNVu%2Fp8%2B42PhjcE8NDqDk740GCnw%2FXSdhPqBSvzq6MtK658G%2BNgzs5%2Fkf1mQXafD9z5c2QowxKAF9neZUktrs69TCP5bHJBjqkAVyaj8rcUgR44iUvScAEljn%2Bi4LNe0DUo2EqY5dKlSWgL49DFaCPRttgQH%2F4Gd7EBtaR92HGV0U6xXZ6DIB%2B81%2F3Mq0NMuMNP7JayFYMpPrRls8%2Fm9pHkcFpoeZsI%2BKtKb5V1VYdEPehVyauu5tTtDf1uGB8JSEHgA0cHzOF6%2FHNMqS6FshZ0Pf8wU4MO5BUAiAXYlZBZG%2BnWy24xONASvwwm8q9&X-Amz-Signature=853f6a93c6ad9857c0ef16ab9464572d28ae36d58e2621b5aa1e49b75e506ee7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







