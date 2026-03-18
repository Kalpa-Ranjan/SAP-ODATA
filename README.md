



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OPZ6NYA%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T065618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDYaCXVzLXdlc3QtMiJHMEUCIQDniqktfStfFb074oXIzDjvGI%2BVfMGZlrgEOSrx5nIyDAIgOJnUVgRBTD0Fkk2OscGcgovk%2F8eIC7%2Fmm5e4eYo0dDYqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA48k1v2R9ELYB5f8SrcA808LVhHZvzuh46W9YXOmnFcTyginFennCYUVKJooGjh2k1SWXDRRxNJ75awymW6o8VNgTSx0%2B%2Fjd4TTVUeV2wPyZe4hPwa%2BoaKIdzrAr6dlQ2ECymF5vUQSTpNi9RjMOeiJ9BHAcJGoNHHgfdHz8b8NUP0tAr0rdpS1WlQzimbAVmhKhR3zP%2FPVQAtFvdrhpttsxLxIorXGL21%2F6LQtZMvGuGE%2F4OwVKpM9fif7n9EWxBRrRXHfHvwT4n9mawhmL93mKp6oOCBINpNQz%2Fn9SDE0eQ1ntDY788soK3vu3sjyPtioGbNk6Uh%2Ftji7OfMot0wuL47O%2BbntMpVu2RZyTeS1Yl4QrbaY6K%2FwKq1ukuzwm%2F7f%2BdsP%2B5QEtXpJH%2BrlN1FYOM4qiJU8i5bZ5eUmtGsrELwFrx2EuGVyIabwbn8X6Zf3Kyx2RgoGVOHco%2BeQf6F4EtBNVof1drJfmXFFZ5GRqTZPCejAoe%2B2NsrBlo2f%2FJjCoM9iFDsjL6JlYw7WrMto9wDjJniSB6IMCmOmxcZIVrIQ7VgR6uTQtZKkp%2FPWKW9LwRS2qydKZOBuvemwQIhh9GX%2BXUIyZnMBkyT6wL%2BluSwNA%2FP8W9xZ8XQ8BuYVvCo%2B%2Bk5IpPFnhd7CMLD26M0GOqUBfM%2BRg2cHGXYcRfTUGEOcEZ78odChILGH2OGh5zzrPtQp7YKR39HufLtR7dYwFuFLqqqExYSnLazWx4XB3EJQ01BwTGP68SJ0vk0U97Ve8nmJ2K47PaJGSs%2Bz6anbVUcOkzb8TR5TLr6J%2BrLhygfbLUqNoWaeMbreXnp%2BsIuiux7Mn05T%2BVvzNJITqGk6cyDGebCfc2obBW%2Bel9WdNliQ7dWijw2J&X-Amz-Signature=c35ff8c430733e837b1d5b651f837deb102cc6277ba8a768bb54228d1e93702f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OPZ6NYA%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T065618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDYaCXVzLXdlc3QtMiJHMEUCIQDniqktfStfFb074oXIzDjvGI%2BVfMGZlrgEOSrx5nIyDAIgOJnUVgRBTD0Fkk2OscGcgovk%2F8eIC7%2Fmm5e4eYo0dDYqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA48k1v2R9ELYB5f8SrcA808LVhHZvzuh46W9YXOmnFcTyginFennCYUVKJooGjh2k1SWXDRRxNJ75awymW6o8VNgTSx0%2B%2Fjd4TTVUeV2wPyZe4hPwa%2BoaKIdzrAr6dlQ2ECymF5vUQSTpNi9RjMOeiJ9BHAcJGoNHHgfdHz8b8NUP0tAr0rdpS1WlQzimbAVmhKhR3zP%2FPVQAtFvdrhpttsxLxIorXGL21%2F6LQtZMvGuGE%2F4OwVKpM9fif7n9EWxBRrRXHfHvwT4n9mawhmL93mKp6oOCBINpNQz%2Fn9SDE0eQ1ntDY788soK3vu3sjyPtioGbNk6Uh%2Ftji7OfMot0wuL47O%2BbntMpVu2RZyTeS1Yl4QrbaY6K%2FwKq1ukuzwm%2F7f%2BdsP%2B5QEtXpJH%2BrlN1FYOM4qiJU8i5bZ5eUmtGsrELwFrx2EuGVyIabwbn8X6Zf3Kyx2RgoGVOHco%2BeQf6F4EtBNVof1drJfmXFFZ5GRqTZPCejAoe%2B2NsrBlo2f%2FJjCoM9iFDsjL6JlYw7WrMto9wDjJniSB6IMCmOmxcZIVrIQ7VgR6uTQtZKkp%2FPWKW9LwRS2qydKZOBuvemwQIhh9GX%2BXUIyZnMBkyT6wL%2BluSwNA%2FP8W9xZ8XQ8BuYVvCo%2B%2Bk5IpPFnhd7CMLD26M0GOqUBfM%2BRg2cHGXYcRfTUGEOcEZ78odChILGH2OGh5zzrPtQp7YKR39HufLtR7dYwFuFLqqqExYSnLazWx4XB3EJQ01BwTGP68SJ0vk0U97Ve8nmJ2K47PaJGSs%2Bz6anbVUcOkzb8TR5TLr6J%2BrLhygfbLUqNoWaeMbreXnp%2BsIuiux7Mn05T%2BVvzNJITqGk6cyDGebCfc2obBW%2Bel9WdNliQ7dWijw2J&X-Amz-Signature=921bdca8dd8a9bb5de94d495260fbad69f3e4ba34e75af60114c0f37ddc8da93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







