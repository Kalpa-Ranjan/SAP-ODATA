



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKDTGCDL%2F20261114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261114T001228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIENONCiRGBf75blox9%2B21EkeTY7ZB%2FvYLyYCzVmzbmgtAiB4c%2BsVXSA0f0esu0RLuLdcLUtJKO8jxb94HXdUj17OmCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTqD%2FiEl%2BXfsoX3TlKtwD7JPh7XoAt6eFPr7wKPO8%2BxE2FEEgiIl73Xvzyz23k3L7VI5xiFezQEJHXMsQwBJu1L%2BoBu4vlKltDitda2ggcC0f2hWZR6edvERTZZAygxucPe88ImKPQdwbVBRhcRvrPZfM0JNXbL94Y3ztOjDYotfHELofwzohr%2FLSq9rhsbkolMzTwf6kPzfqlYFk2DniBtFYUcflMVUW85i4BX1gCjsydDGFum6sDcipYuV%2BxZ4dS4b%2BJTzSXfRsK6y5AZy2UogpFMKSZpLd2SoJmSwP3P5MzxB7YIoGf17uFidL8IQLsLwDpsbiTHyTzawF7ljefaxVoA3hE81NwO%2FMevGSm6%2BiftriaLpDoJLt7hH%2BhrbRmb4gNgQywEBSS1C4e1c%2FLGpY3ndpZ%2FqVIvDu%2FwMgdHzr2%2B7%2Fv%2BMq30ohaO%2F%2FSHFMOSepzV%2FcFtGsTzRP18jmJGnyczzRaHYDkODjxnDhXcLRiwytX5Sj%2FqQ0cMO%2BWHDapDYki2w9ogMrA%2BW8T9oO5xgFqembfU7SGPHkzgegvCJ%2BvJ7NgQgpxg4xHC9d%2BcqMjR2ApFDS4%2F9mjk9%2Be7kG4O%2FWdXW2jLrzvWWn%2FKaGQRILBJuWA%2BRT57w2RKx85h947rT1YT2JzCvW8L8wjrXd1wY6pgFdcjEmuqQ5Cp0YIaEXOoxJ%2B9WQKhYXwhk3w8U1GswXAJ%2BsewMI8eLA1j01tAij9J9zksChffjq9FLTWOEfS9Z2qvCLQIQ5%2BJqMJWiZpqX4CRKh95TueDBJ9S1X7nUbCPMwxTKR5Z63PcKFk6o17SFGp50wRsfamF2mHMVNAOwzDOyHKuChP4vPkXpuDB2Vt2jlxDpWWHpZaQz7zpFRDPPwltCPKNql&X-Amz-Signature=e5786f28d459df4f288ad1835b1a367cf46efbaea9950cafd3f8d6ae3221b5a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKDTGCDL%2F20261114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261114T001228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIENONCiRGBf75blox9%2B21EkeTY7ZB%2FvYLyYCzVmzbmgtAiB4c%2BsVXSA0f0esu0RLuLdcLUtJKO8jxb94HXdUj17OmCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTqD%2FiEl%2BXfsoX3TlKtwD7JPh7XoAt6eFPr7wKPO8%2BxE2FEEgiIl73Xvzyz23k3L7VI5xiFezQEJHXMsQwBJu1L%2BoBu4vlKltDitda2ggcC0f2hWZR6edvERTZZAygxucPe88ImKPQdwbVBRhcRvrPZfM0JNXbL94Y3ztOjDYotfHELofwzohr%2FLSq9rhsbkolMzTwf6kPzfqlYFk2DniBtFYUcflMVUW85i4BX1gCjsydDGFum6sDcipYuV%2BxZ4dS4b%2BJTzSXfRsK6y5AZy2UogpFMKSZpLd2SoJmSwP3P5MzxB7YIoGf17uFidL8IQLsLwDpsbiTHyTzawF7ljefaxVoA3hE81NwO%2FMevGSm6%2BiftriaLpDoJLt7hH%2BhrbRmb4gNgQywEBSS1C4e1c%2FLGpY3ndpZ%2FqVIvDu%2FwMgdHzr2%2B7%2Fv%2BMq30ohaO%2F%2FSHFMOSepzV%2FcFtGsTzRP18jmJGnyczzRaHYDkODjxnDhXcLRiwytX5Sj%2FqQ0cMO%2BWHDapDYki2w9ogMrA%2BW8T9oO5xgFqembfU7SGPHkzgegvCJ%2BvJ7NgQgpxg4xHC9d%2BcqMjR2ApFDS4%2F9mjk9%2Be7kG4O%2FWdXW2jLrzvWWn%2FKaGQRILBJuWA%2BRT57w2RKx85h947rT1YT2JzCvW8L8wjrXd1wY6pgFdcjEmuqQ5Cp0YIaEXOoxJ%2B9WQKhYXwhk3w8U1GswXAJ%2BsewMI8eLA1j01tAij9J9zksChffjq9FLTWOEfS9Z2qvCLQIQ5%2BJqMJWiZpqX4CRKh95TueDBJ9S1X7nUbCPMwxTKR5Z63PcKFk6o17SFGp50wRsfamF2mHMVNAOwzDOyHKuChP4vPkXpuDB2Vt2jlxDpWWHpZaQz7zpFRDPPwltCPKNql&X-Amz-Signature=1b6d12172b608e58cde340021a2608e24bc87926cef539d3794652d87ca896b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







